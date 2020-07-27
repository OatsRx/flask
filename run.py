# This module provides a portable way of using operating system dependent functionality
import os

# importing the Flask class
from flask import Flask, render_template

# creating an instance of Flask and assigning it to to the variable "app"
# the first argument of the Flask class is the name of the applications module or package
# __name__ is a built in python variable used when using a single module like we are here
# Flask needs this to know where to look for templates and static files
app = Flask(__name__)

# a decorator in Python is any callable Python object that is used to modify a function or a class
# decorators are a way of wrapping functions
# use the route() decorator to tell Flask what URL should trigger our function
# The forward-slash ( / ) is just the root level of a website. 
# Let's say you go to www.google.com (the url can usually end with  www.google.com/ )
@app.route("/")
def index():
    return render_template("index.html")


# __main__ is the name of the default module in python
if __name__ == "__main__":
# app.run template - run(host=None, port=None, debug=None, load_dotenv=True, **options)
    app.run(
# we are using the os module from the standard library to get the IP environment variable if it exists and setting 0.0.0.0 as the default
        host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)
            # debug=True should never be used in a production applicationor submitting a project