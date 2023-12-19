from flask import Flask

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World! to flask '
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
