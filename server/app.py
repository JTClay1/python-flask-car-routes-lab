from flask import Flask

# Create the Flask app instance
# Tests import `app` directly, so the variable name matters
app = Flask(__name__)

# These are the car models our company actually carries
# The route below checks against this list
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


# Default route
# Just a simple landing message to confirm the app is running
@app.get("/")
def index():
    return "Welcome to Flatiron Cars"


# Dynamic route that takes a model name from the URL
# Example: /Crossroads or /M2
@app.get("/<model>")
def show_model(model):
    # If the model exists in our catalog, return a success message
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    
    # Otherwise, let the user know the model doesn't exist
    return f"No models called {model} exists in our catalog"
