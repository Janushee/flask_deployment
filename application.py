from flask import Flask

application=Flask(__name__)
app=application


@application.route('/')
def hello_world():
    return 'Hello :)'



if __name__=='__main__': 
    application.run() 
