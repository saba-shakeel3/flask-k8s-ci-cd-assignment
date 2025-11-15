# test_app.py

from app import create_message


def test_create_message_output():
    """
    Tests the output of the simple function to meet the unit test requirement.
    """
    # Define the expected output from the function in app.py
    expected_message = "Hello, World! Welcome to the Flask-K8s CI/CD Assignment."
    
    # Assert that the function's actual output matches the expected output
    assert create_message() == expected_message
    
    # Add a second basic assertion to ensure the test is robust
    assert isinstance(create_message(), str)
