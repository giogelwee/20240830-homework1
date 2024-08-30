import google.generativeai as palm
from flask import Flask, render_template, request

# Indicate API key used
api='AIzaSyDUP0SCxU19X8jclqd_ekU-lwp-mfc3Cus'
palm.configure(api_key=api)

# INdicate model used
model = palm.GenerativeModel('gemini-pro')

# Set up app
app = Flask(__name__)

# First page
@app.route("/", methods=["GET", "POST"])
def index_homework():
    return render_template("index_homework.html")

# Second page
# Access the joke_homework html + listens for GET requests
@app.route("/joke_homework", methods=["GET"])
# Function joke_homework is executed when joke_homework html is accessed
def joke_homework():
    q="Tell me a joke related to Singapore"
    try:
        # Use model to generate the content for question q 'Tell me a joke'
        joke_generated = model.generate_content(q).text
    except Exception as e:
        print(f"Error occurred: {e}")
        joke_generated = "An error occurred while generating a joke. Please try again."
    # Returns the 'joke' which will be displayed through the joke_homework html
    return render_template("joke_homework.html", joke=joke_generated)

# # Optional: Define the prediction route if needed
# @app.route("/prediction", methods=["POST"])
# def prediction():
#     # Logic for prediction can be added here
#     return "Prediction feature is under development."

if __name__ == "__main__":
    app.run()
