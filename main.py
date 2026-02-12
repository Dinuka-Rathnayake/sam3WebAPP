Name = "Dinuka"
print(f"Hello, {Name}!")

# create flask app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, {Name}!'

if __name__ == '__main__':
    app.run(debug=True)