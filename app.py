import os
import sys
import traceback
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from backend_ucb_model import UCBTrainer
from python_question_bank import question_bank
import re
import random

# Configure error logging
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Configure Gemini API (if available)
try:
    import google.generativeai as genai

    # Suppress verbose logging
    os.environ['GRPC_PYTHON_LOG_LEVEL'] = 'ERROR'
    os.environ['GLOG_minloglevel'] = '2'

    # Initialize Gemini (use your API key here)
    load_dotenv()
    # Now you can access the API key
    API_KEY = os.getenv('API_KEY')
    if (API_KEY):
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        GEMINI_AVAILABLE = True
        logger.info("Gemini AI is available for answer checking")
    else:
        GEMINI_AVAILABLE = False
        logger.warning("API_KEY not found in environment variables. Gemini AI will not be available.")
except (ImportError, Exception) as e:
    GEMINI_AVAILABLE = False
    logger.warning(f"Gemini AI not available: {e}")
    logger.info("Falling back to standard answer checking")

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Add error handlers to prevent the app from shutting down
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Uncaught exception: {e}")
    logger.error(traceback.format_exc())
    return jsonify({
        "error": "Internal server error",
        "message": str(e)
    }), 500

# Initialize the question system as a global variable
question_system = None

def normalize_code(code):
    """
    Normalize code by trimming whitespace from each line and keeping only non-empty lines.
    This allows comparison of code regardless of indentation differences.
    """
    # Remove any special characters or color codes
    code = re.sub(r'\x1b\[[0-9;]*[mGKH]', '', code)

    # Process each line: trim whitespace and keep only non-empty lines
    lines = []
    for line in code.split('\n'):
        trimmed = line.strip()
        if trimmed:  # Only include non-empty lines
            lines.append(trimmed)

    return lines  # Return array of trimmed lines

def gemini_check_answer(user_answer, correct_answer, question_text):
    """
    Use Gemini AI to check if the user's answer is correct.
    This provides more flexibility than exact string matching.
    """
    if not GEMINI_AVAILABLE:
        return None

    try:
        # Format the query for Gemini
        prompt = f"""
As a programming teacher, evaluate if the student's answer fixes the code problem.

PROBLEM:
{question_text}

CORRECT ANSWER:
{correct_answer}

STUDENT'S ANSWER:
{user_answer}

Does the student's answer correctly fix the issue? Reply with ONLY 'Yes' or 'No'.
"""
        # Get response from Gemini
        response = model.generate_content(prompt)
        result = response.text.strip().lower()

        # Parse response (looking for yes/no)
        if 'yes' in result:
            return True
        elif 'no' in result:
            return False
        else:
            print(f"Unclear Gemini response: {result}")
            return None
    except Exception as e:
        print(f"Error using Gemini: {e}")
        return None

class DebugQuestionSystem:
    def __init__(self):
        self.trainer = UCBTrainer()
        for difficulty, questions in question_bank.items():
            for q in questions:
                self.trainer.add_question(q["id"], q["text"], q["answer"], difficulty)
        self.current_question = None
        self.current_difficulty = 0  # Start with Easy
        self.consecutive_correct = 0
        self.consecutive_wrong = 0
        # Add a counter for wrong attempts on the current question
        self.current_question_wrong_attempts = 0

        # Track used question IDs
        self.used_questions = set()

        # Create copies of question lists for each difficulty level to ensure no repetition
        self.available_questions = {
            0: list(self.trainer.questions[0]),  # Easy
            1: list(self.trainer.questions[1]),  # Medium
            2: list(self.trainer.questions[2]),  # Hard
        }

    def get_next_question(self):
        # Select question for current difficulty
        difficulty = self.current_difficulty

        # If all questions at current difficulty have been used, reset questions for this level
        if not self.available_questions[difficulty]:
            print(
                f"\nAll {['Easy', 'Medium', 'Hard'][difficulty]} level questions have been used. Resetting question bank...")
            self.available_questions[difficulty] = list(self.trainer.questions[difficulty])

        # Randomly select an unused question from current difficulty
        question = random.choice(self.available_questions[difficulty])

        # Remove from available questions list
        self.available_questions[difficulty].remove(question)

        # Record current question
        self.current_question = question

        # Add to used questions set
        self.used_questions.add(question.id)

        # Reset wrong attempts counter when getting a new question
        self.current_question_wrong_attempts = 0

        return self.format_question(question)

    def format_question(self, question):
        difficulty_names = ["Easy", "Medium", "Hard"]

        # Extract hints from question bank
        question_data = None
        for difficulty, questions in question_bank.items():
            for q in questions:
                if q["id"] == question.id:
                    question_data = q
                    break
            if question_data:
                break

        # Include hints if available
        hints = []
        if question_data and "hints" in question_data:
            if isinstance(question_data["hints"], dict):
                # If hints are stored as a dictionary with levels
                hints = [
                    question_data["hints"].get("level1", ""),
                    question_data["hints"].get("level2", ""),
                    question_data["hints"].get("level3", "")
                ]
            elif isinstance(question_data["hints"], list):
                # If hints are stored as a list
                hints = question_data["hints"]

        return {
            "difficulty": difficulty_names[question.difficulty],
            "id": question.id,
            "text": question.text,
            "hints": hints  # Add hints to the response
        }

    def check_answer(self, user_answer):
        if not self.current_question:
            return False, False

        # First try Gemini-based checking if available
        if GEMINI_AVAILABLE:
            print("\nUsing AI to check your answer...")
            gemini_result = gemini_check_answer(
                user_answer,
                self.current_question.answer,
                self.current_question.text
            )

            if gemini_result is not None:
                is_correct = gemini_result
                print(f"AI assessment: {'Correct' if is_correct else 'Incorrect'}")
            else:
                # Fall back to traditional checking if Gemini fails
                print("AI check failed, falling back to standard checking")
                is_correct = self.traditional_check(user_answer)
        else:
            # Use traditional checking
            is_correct = self.traditional_check(user_answer)

        # Update model based on result
        if is_correct:
            self.consecutive_correct += 1
            self.consecutive_wrong = 0
            # Reset wrong attempts counter on correct answer
            self.current_question_wrong_attempts = 0
            # Update UCB model state
            self.trainer.agent.update(self.current_difficulty, 1.0)

            # Upgrade difficulty after two consecutive correct answers
            if self.consecutive_correct >= 2 and self.current_difficulty < 2:
                self.current_difficulty += 1
                self.consecutive_correct = 0  # Reset consecutive counter after upgrade
                print(
                    f"\nCongratulations! You've answered two questions correctly in a row. Difficulty upgraded to {['Easy', 'Medium', 'Hard'][self.current_difficulty]}!")
        else:
            self.consecutive_wrong += 1
            self.consecutive_correct = 0
            # Increment wrong attempts counter
            self.current_question_wrong_attempts += 1
            # Update UCB model state
            self.trainer.agent.update(self.current_difficulty, 0.0)

            # Downgrade difficulty immediately after wrong answer (if not at lowest difficulty)
            if self.current_difficulty > 0:
                old_difficulty = self.current_difficulty
                self.current_difficulty -= 1
                print(
                    f"\nDifficulty downgraded from {['Easy', 'Medium', 'Hard'][old_difficulty]} to {['Easy', 'Medium', 'Hard'][self.current_difficulty]}")

            # Check if wrong attempts threshold is reached
            if self.current_question_wrong_attempts >= 3:
                print("\nYou've attempted this question 3 times without success. Moving to the next question...")
                # Return a flag to indicate we should move to the next question
                return is_correct, True

        # Default return with the correct/incorrect status and no question change flag
        return is_correct, False

    def traditional_check(self, user_answer):
        """Traditional string-based answer checking as fallback"""
        # Get normalized lines from both answers (strips whitespace, removes empty lines)
        user_lines = normalize_code(user_answer)
        correct_lines = normalize_code(self.current_question.answer)

        # For debugging
        debug_info = {
            "user_lines": user_lines,
            "correct_lines": correct_lines
        }
        print("\nUser answer normalized lines:", user_lines)
        print("\nCorrect answer normalized lines:", correct_lines)

        # Try different matching strategies
        # 1. Check if all lines in correct answer exist in user's answer
        all_lines_present = all(line in user_lines for line in correct_lines)

        # 2. Check if correct lines appear in sequence somewhere in user's answer
        def check_sequence():
            for i in range(len(user_lines) - len(correct_lines) + 1):
                if all(user_lines[i + j] == correct_lines[j] for j in range(len(correct_lines))):
                    return True
            return False
        sequence_match = len(correct_lines) <= len(user_lines) and check_sequence()

        # 3. Check if the answer contains the key line(s) that fix the problem
        key_line_match = any(line in user_lines for line in correct_lines)

        # Consider it correct if any of the strategies finds a match
        is_correct = all_lines_present or sequence_match or key_line_match
        print(f"\nMatch details - All lines present: {all_lines_present}, Sequence match: {sequence_match}, Key line match: {key_line_match}")
        print(f"\nString match result: {'Correct' if is_correct else 'Incorrect'}")
        return is_correct

    def get_next_difficulty(self):
        """Return the difficulty level for the next question"""
        return self.current_difficulty

    def get_stats(self):
        """Return statistics about the current session"""
        difficulty_names = ["Easy", "Medium", "Hard"]
        return {
            "current_difficulty": difficulty_names[self.current_difficulty],
            "consecutive_correct": self.consecutive_correct,
            "consecutive_wrong": self.consecutive_wrong,
            "questions_used": len(self.used_questions)
        }

# Add a health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    try:
        # More comprehensive health check
        env_vars = {
            "API_KEY_SET": bool(os.getenv('API_KEY')),
            "PORT": os.getenv('PORT', 'default:5000'),
            "ENVIRONMENT": os.getenv('ENVIRONMENT', 'development'),
        }
        return jsonify({
            'status': 'healthy',
            'environment': env_vars,
            'gemini_available': GEMINI_AVAILABLE,
            'question_system_initialized': question_system is not None
        }), 200
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return jsonify({'status': 'degraded', 'error': str(e)}), 500

# API Routes
@app.route('/api/init', methods=['GET'])
def initialize_system():
    try:
        global question_system
        question_system = DebugQuestionSystem()
        # Get total number of questions for each difficulty level
        total_counts = {
            "Easy": len(question_system.trainer.questions[0]),
            "Medium": len(question_system.trainer.questions[1]),
            "Hard": len(question_system.trainer.questions[2])
        }
        logger.info(f"System initialized with {sum(total_counts.values())} total questions")
        return jsonify({
            "status": "initialized",
            "question_counts": total_counts
        })
    except Exception as e:
        logger.error(f"System initialization failed: {e}")
        logger.error(traceback.format_exc())
        return jsonify({"error": f"Failed to initialize system: {str(e)}"}), 500

@app.route('/api/question', methods=['GET'])
def get_next_question():
    if not question_system:
        return jsonify({"error": "System not initialized"}), 400
    question_data = question_system.get_next_question()
    return jsonify(question_data)

@app.route('/api/check', methods=['POST'])
def check_answer():
    if not question_system:
        return jsonify({"error": "System not initialized"}), 400

    data = request.json
    if not data or 'answer' not in data:
        return jsonify({"error": "Answer missing"}), 400

    user_answer = data['answer']

    # Debug log to see what's being submitted
    print(f"\n--- Answer submission ---\nUser answer: {user_answer}\n")

    # Get both the correctness result and the auto-next flag
    is_correct, should_next_question = question_system.check_answer(user_answer)

    # Debug log to confirm the result
    print(f"Is correct: {is_correct} (type: {type(is_correct)})")

    next_difficulty = question_system.get_next_difficulty()
    difficulty_names = ["Easy", "Medium", "Hard"]

    return jsonify({
        "correct": is_correct,
        "consecutive_correct": question_system.consecutive_correct,
        "consecutive_wrong": question_system.consecutive_wrong,
        "next_difficulty": difficulty_names[next_difficulty],
        "stats": question_system.get_stats(),
        # Add a new field to indicate if the frontend should automatically fetch a new question
        "auto_next": should_next_question
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    if not question_system:
        return jsonify({"error": "System not initialized"}), 400

    return jsonify(question_system.get_stats())

# Make sure the question system persists across sessions
@app.before_request
def ensure_question_system():
    try:
        global question_system
        if question_system is None:
            question_system = DebugQuestionSystem()
            logger.info("Question system initialized before request")
    except Exception as e:
        logger.error(f"Failed to initialize question system: {e}")
        # Don't raise an exception here to allow the request to continue

# This signal handler helps with graceful shutdowns
def sigterm_handler(signal, frame):
    logger.info("SIGTERM received, shutting down gracefully")
    # Cleanup code if needed
    sys.exit(0)

# Register the signal handler if in production
if os.environ.get('ENVIRONMENT') == 'production':
    import signal
    signal.signal(signal.SIGTERM, sigterm_handler)

# Make sure your app listens on the port provided by Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=os.environ.get('ENVIRONMENT') != 'production',
            host='0.0.0.0',
            port=port)
