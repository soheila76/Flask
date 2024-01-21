from flask import Flask
app=Flask(__name__)
@app.route("/")
def get_news():
    return "hello this is a test"
@app.route("/soheila/")
def say_soheila():
   return '''
    <html>
        <head>
        <title>soheila</title>
        <style>
        body{
        background-color:pink;
        }
        </style>
        </head>
        <body>
            <p>this is soheila's page</p>
        </body>
    </html>
    '''


app.run(port=5000,debug=True)