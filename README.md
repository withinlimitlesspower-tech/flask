# Click Counter App

A simple Flask web application that demonstrates AJAX-based counter incrementation with a modern dark theme and toast notifications.

## Features

- Click a button to increment a counter
- Counter updates via AJAX without page reload
- Dark theme CSS
- Toast notifications on success and error
- `/health` endpoint for health checks
- Logging and error handling

## Setup

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser to `http://localhost:5000`.

## Environment Variables

- `PORT`: Port to run the server (default: 5000).
- `SECRET_KEY`: Flask secret key (optional, defaults to 'dev-secret-key').

## Endpoints

- `GET /`: Main page with the click button.
- `POST /increment`: Increment counter, returns JSON with count.
- `GET /health`: Health check, returns JSON with status and current count.
