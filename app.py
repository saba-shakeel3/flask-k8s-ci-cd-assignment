# app.py

from flask import Flask


# Helper function to be tested by pytest
def create_message():
    """Returns the message for the main route."""
    # This function is kept simple to pass the unit test requirement
    return "Hello, World! Welcome to the Flask-K8s CI/CD Assignment."


# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def hello_world():
    """Main route that returns a greeting message."""
    return create_message()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
