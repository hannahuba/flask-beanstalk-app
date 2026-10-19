from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from a6jp15cu Elastic Beanstalk CI-CD verification-2026101918105730498"