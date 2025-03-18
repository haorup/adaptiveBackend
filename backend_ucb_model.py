import numpy as np
from math import log, sqrt
import json
import random


class Question:
    """Question class representing a single debugging problem"""

    def __init__(self, id, text, answer, difficulty):
        self.id = id
        self.text = text  # Question content
        self.answer = answer  # Correct answer
        self.difficulty = difficulty  # Difficulty level: 0=Easy, 1=Medium, 2=Hard


class UCBDifficultyAgent:
    """UCB algorithm agent for selecting question difficulty with adaptive progression"""

    def __init__(self, n_difficulties=3, exploration_param=sqrt(2)):
        self.n_difficulties = n_difficulties
        self.exploration_param = exploration_param

        # Initialize statistics
        self.counts = np.zeros(n_difficulties)  # Attempt counts per difficulty
        self.rewards = np.zeros(n_difficulties)  # Cumulative rewards per difficulty
        self.values = np.zeros(n_difficulties)  # Average rewards per difficulty
        self.total_count = 0  # Total attempts

        # History records
        self.history = {
            'difficulties': [],  # Historical selected difficulties
            'rewards': [],  # Historical rewards
            'ucb_values': []  # Historical UCB values
        }

        # Track consecutive correct answers (overall, not per difficulty)
        self.consecutive_correct_count = 0

    def select_difficulty(self):
        """Select difficulty based on UCB and force upgrade after two consecutive correct answers"""
        # Force difficulty upgrade after two consecutive correct answers
        if self.consecutive_correct_count >= 2:
            current_difficulty = self.history['difficulties'][-1] if self.history['difficulties'] else 0
            if current_difficulty < self.n_difficulties - 1:
                # Reset consecutive counter and move up
                self.consecutive_correct_count = 0  # Reset after upgrade
                return current_difficulty + 1

        # If player is struggling at current difficulty (multiple wrong answers),
        # consider moving down a level
        if (self.history['difficulties'] and
                len(self.history['rewards']) >= 3 and
                sum(self.history['rewards'][-3:]) == 0):  # 3 consecutive wrong answers
            current_difficulty = self.history['difficulties'][-1]
            if current_difficulty > 0:
                return current_difficulty - 1

        # Standard UCB calculation as fallback
        ucb_values = []
        for d in range(self.n_difficulties):
            if self.counts[d] == 0:
                # If a difficulty has never been tried, prioritize it
                ucb_values.append(float('inf'))
            else:
                # Exploitation term: average reward
                exploitation = self.values[d]

                # Exploration term
                exploration = self.exploration_param * sqrt(log(self.total_count) / self.counts[d])

                # UCB value
                ucb = exploitation + exploration
                ucb_values.append(ucb)

        # Record UCB values
        self.history['ucb_values'].append(ucb_values.copy())

        # Return difficulty with highest UCB
        return np.argmax(ucb_values)

    def update(self, difficulty, reward):
        """Update model statistics and track consecutive correct answers"""
        # Update counts
        self.counts[difficulty] += 1
        self.total_count += 1

        # Update cumulative rewards
        self.rewards[difficulty] += reward

        # Update average rewards
        self.values[difficulty] = self.rewards[difficulty] / self.counts[difficulty]

        # Record history
        self.history['difficulties'].append(difficulty)
        self.history['rewards'].append(reward)

        # Update consecutive correct answers tracking (overall, not per difficulty)
        if reward == 1.0:  # Correct answer
            self.consecutive_correct_count += 1
        else:  # Wrong answer
            self.consecutive_correct_count = 0

    def get_stats(self):
        """Get current statistics"""
        return {
            'counts': self.counts.tolist(),
            'values': self.values.tolist(),
            'total_count': self.total_count,
            'consecutive_correct_count': self.consecutive_correct_count,
            'history': self.history
        }

    def save_model(self, filename):
        """Save model to file"""
        model_data = {
            'n_difficulties': self.n_difficulties,
            'exploration_param': self.exploration_param,
            'counts': self.counts.tolist(),
            'rewards': self.rewards.tolist(),
            'values': self.values.tolist(),
            'total_count': self.total_count,
            'consecutive_correct_count': self.consecutive_correct_count,
            'history': self.history
        }

        with open(filename, 'w') as f:
            json.dump(model_data, f, indent=4)

    @classmethod
    def load_model(cls, filename):
        """Load model from file"""
        with open(filename, 'r') as f:
            model_data = json.load(f)

        agent = cls(
            n_difficulties=model_data['n_difficulties'],
            exploration_param=model_data['exploration_param']
        )

        agent.counts = np.array(model_data['counts'])
        agent.rewards = np.array(model_data['rewards'])
        agent.values = np.array(model_data['values'])
        agent.total_count = model_data['total_count']
        agent.history = model_data['history']

        # Handle backward compatibility
        if 'consecutive_correct_count' in model_data:
            agent.consecutive_correct_count = model_data['consecutive_correct_count']
        else:
            agent.consecutive_correct_count = 0

        return agent

    def get_optimal_difficulty(self):
        """Get current optimal difficulty"""
        if self.total_count == 0:
            return 0  # Default to Easy

        # Find difficulty with highest average reward among tried ones
        valid_difficulties = [d for d in range(self.n_difficulties) if self.counts[d] > 0]
        if not valid_difficulties:
            return 0

        return max(valid_difficulties, key=lambda d: self.values[d])


class UCBTrainer:
    """UCB model trainer"""

    def __init__(self):
        self.questions = {
            0: [],  # Easy questions
            1: [],  # Medium questions
            2: []  # Hard questions
        }
        self.agent = UCBDifficultyAgent(n_difficulties=3)
        self.results = []

    def add_question(self, id, text, answer, difficulty):
        """Add question to bank"""
        question = Question(id, text, answer, difficulty)
        self.questions[difficulty].append(question)

    def train_step(self, correct_prob=None):
        """Perform one training step (simulate one answer)"""
        # Select difficulty
        difficulty = self.agent.select_difficulty()

        # Ensure questions exist for the selected difficulty
        if len(self.questions[difficulty]) == 0:
            # Try other difficulties
            available_difficulties = [d for d, qs in self.questions.items() if len(qs) > 0]
            if not available_difficulties:
                raise ValueError("No available questions")
            difficulty = random.choice(available_difficulties)

        # Randomly select a question from the difficulty
        question = random.choice(self.questions[difficulty])

        # Simulate answering
        if correct_prob is None:
            # Default correctness: Easy=0.8, Medium=0.5, Hard=0.3
            default_probs = [0.8, 0.5, 0.3]
            is_correct = random.random() < default_probs[difficulty]
        else:
            # Use specified correctness probability
            if isinstance(correct_prob, list):
                is_correct = random.random() < correct_prob[difficulty]
            else:
                is_correct = random.random() < correct_prob

        # Calculate reward
        reward = 1.0 if is_correct else 0.0

        # Update model
        self.agent.update(difficulty, reward)

        # Record result
        result = {
            'question_id': question.id,
            'difficulty': difficulty,
            'is_correct': is_correct,
            'reward': reward,
            'consecutive_correct': self.agent.consecutive_correct_count
        }
        self.results.append(result)

        return result

    def get_stats(self):
        """Get training statistics"""
        return self.agent.get_stats()

    def save_model(self, filename):
        """Save model"""
        self.agent.save_model(filename)