# Chat Bot Application

https://github.com/user-attachments/assets/249359c7-03de-4569-ad04-9550d062effd

A Flask-based chatbot application using Google's Gemini API.

## Deployment to Render

1. Fork this repository to your GitHub account
2. Sign up or log in to [Render](https://render.com)
3. Click "New+" and select "Web Service"
4. Connect your GitHub repository
5. Set the following:
   - Name: chat-bot (or any name you prefer)
   - Region: (Choose the one closest to you)
   - Branch: main (or your default branch)
   - Root Directory: Leave empty
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
6. Add environment variables:
   - `GOOGLE_API_KEY` = your actual Google API key
   - `PORT` = 10000 (Render's default port)
7. Click "Create Web Service"
8. Wait for deployment to complete

## Local Development

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

4. Run the application:
   ```
   python main.py
   ```

5. Visit `http://localhost:5000` in your browser

## API Endpoints

- `GET /` - Serve the chat interface
- `POST /data` - Process chat messages
- `GET /health` - Health check endpoint

## Requirements

- Python 3.9+
- Google Gemini API key

## Getting a Google API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Create an API key
4. Copy the API key for use in your environment variables
