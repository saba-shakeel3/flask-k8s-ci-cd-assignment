# app.py

from flask import Flask

# Helper function to be tested by pytest
def create_message():
    """Returns the message for the main route."""
    # This message is tested by the unit test (test_app.py)
    return "Hello, World! Welcome to the Flask-K8s CI/CD Assignment."

# Initialize the Flask application
app = Flask(__name__)


@app.route("/")
def hello_world():
    """Main route that returns a greeting message."""
    return create_message()


if __name__ == "__main__":
    # In a real app, do not run with debug=True in production.
    # We use 0.0.0.0 for Docker compatibility.
    # Note: Removed debug=True for cleaner production example, though not required to pass CI.
    app.run(host='0.0.0.0', port=5000)
