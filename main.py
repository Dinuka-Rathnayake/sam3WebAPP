# create flask app
from flask import Flask
from flask import Flask, jsonify, request


# load model function
def loadModel():
  print("Loading model...")

# getBoundingBoxAndMask function
def getBoundingBoxAndMask(path):
  print(f"Processing image at {path}...")

  print("this is results...")

app = Flask(__name__)

# call loadModel
loadModel()

# create a route for health check
@app.route('/')
def hello_world():
    return f'Health check successful!'

# creat route for predict
@app.route('/predict', methods=["POST"])
def boundingBox():
    """get SAM2 ready bounding boxes for given image.

    Expected JSON body:
    {
      
      "bboxes": [[x1, y1, x2, y2]]
    }
    """

    from werkzeug.exceptions import BadRequest

    # Get the JSON data from the POST request
    data = request.get_json()

    # get image path
     # Extract the image path from the request
    image_path = data.get('image_path')

    getBoundingBoxAndMask(image_path)

    # just return "okay" as response
    return jsonify({
        'status': 'okay',
        'received_path': image_path
    })




if __name__ == '__main__':
    app.run(debug=True)