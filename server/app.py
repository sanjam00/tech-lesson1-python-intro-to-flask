#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Remember: decorators are functions that take functions as arguments and return them decorated with new features.
@app.route('/')
def index():
  return "<h1>Welcome to my page!</h1>"

@app.route('/<string:username>')
def user(username):
  return f'<h1>Profile for {username}</h1>'


"""
Set up our app to trigger flask run after running the app (using python app.py).
This can let us control useful features such as an auto-re-run. 
By using the debug line, we can set our app up so that it will cause the server to restart when we save, whereas previously, when testing, 
if we wanted to see a change we made apply to our server, we would need to restart the server by exiting and rerunning Flask.
  Now when we reload the webpage after saving, the changes will be reflected right away, just like a React server.
"""
if __name__ == '__main__':
  app.run(port=5555, debug=True)