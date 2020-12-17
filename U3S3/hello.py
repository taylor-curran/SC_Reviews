from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Type Into Terminal to Run this Flask App

# -- FOR MAC --
# 1. export FLASK_APP=hello.py
# 2. flask run

# -- FOR WINDOWS COMMAND PROMPT --
# C:\path\to\app>set FLASK_APP=hello.py

# -- FOR POWERSHELL --
# PS C:\path\to\app> $env:FLASK_APP = "hello.py"