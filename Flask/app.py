from flask import Flask
### WSGI Application:- it is a standard used for intreacting b/w server and web application
app=Flask(__name__)

@app.route('/')
def welcome():
  return "welcome to my youtube channel"

@app.route('/')
def member():
  return "welcome to my application"


if __name__=="__main__":
  app.run(debug = True)