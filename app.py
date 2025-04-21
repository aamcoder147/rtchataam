import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get Supabase credentials from environment variables
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase URL and Key must be set in the .env file")

@app.route('/')
def index():
    """Serves the main HTML page."""
    # Pass Supabase credentials to the template
    return render_template(
        'index.html',
        supabase_url=SUPABASE_URL,
        supabase_key=SUPABASE_KEY
    )

if __name__ == '__main__':
    # Use debug=True for development (auto-reloads)
    # Use host='0.0.0.0' to make it accessible on your network
    app.run(debug=True, host='0.0.0.0', port=5000)