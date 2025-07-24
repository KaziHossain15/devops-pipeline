# will use flask to create basic web app in python
from flask import Flask

app = Flask(__name__) # object name; tells Flask if you are running a file or importing it

@app.route('/') # use a decorator that associates a function with a URL
def home(): # the home function that is called when the root URL is accessed
    return "Hello from DevOps world!"

if __name__ == "__main__": # this means that this will run if the file is executed directly (not imported)
    app.run(debug=True) # gives error message which is useful for dev