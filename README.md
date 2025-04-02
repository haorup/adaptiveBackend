# Adaptive Backend

## Deployment on Render.com

1. Create a new Web Service on Render.com
2. Connect your GitHub repository
3. Set the following configuration:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Add the required environment variables:
   - `API_KEY`: Your Gemini API key
5. Deploy the application

The application will be available at the URL provided by Render once deployment is complete.

## Development

# ...existing code...