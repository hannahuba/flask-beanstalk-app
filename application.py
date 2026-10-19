from flask import Flask
 
application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from a6jp15cu Elastic Beanstalk CI-CD"