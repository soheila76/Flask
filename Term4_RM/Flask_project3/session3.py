from flask import Flask
app=Flask(__name__)

@app.route("/")
def get_news():
    return "hello this is a test"


# @app.route("/soheila/")
# def say_soheila():
#    return '''
#     <html>
#         <head>
#         <title>soheila</title>
#         <style>
#         body{
#         background-color:pink;
#         }
#         </style>
#         </head>
#         <body>
#             <p>this is soheila's page</p>
#         </body>
#     </html>
#     '''

# @app.route("/poulstar/<name>/")
# def show_student(name):
#     return f"this is a poulstar's student: {name}"

# @app.route("/poulstar/<int:age>/")
# def show_age_student(age):
#     return f"age: {age}"

@app.route("/<name>/<lastname>/<int:age>/")
def show_age_student(name,lastname,age):
    a=f"name: {name}<br>lastname: {lastname}<br>age: {int(age)}"
    return a



app.run(port=5000,debug=True)