import os
from flask import Flask
app = Flask(__name__)

# Q) Explore the flask module and create a web server using Flask & Python


@app.route("/")
def hello_world():
    return '''
    <head>
        <title>Abdullah-Mehboob Flask</title>
    </head>
    <body>
        <h1>My name is abdullah mehboob</h1>
    </body>
    '''

if __name__ == "__main__" :
    app.run(debug=True)
