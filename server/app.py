from flask import Flask, jsonify
#initialize flask application
app = Flask(__name__)
#list of car models "fleet"
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

#default route
@app.route('/')
def index():
    return "Welcome to Flatiron Cars"
# route to list all existing "fleet"
@app.get("/existing_models")
def existing_models_index():
    return jsonify(existing_models)
#route check if model exists
@app.get("/<model>")
def model_show(model):
    exists = model.lower() in (m.lower() for m in existing_models)
    if exists:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog", 404

