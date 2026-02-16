# create flask app for sam3
import base64
import os
from flask import Flask
from flask import Flask, jsonify, request
from urllib.request import urlopen

## import torch
# from transformers import Sam3Processor, Sam3Model
# from PIL import Image

# load environment variables
from dotenv import load_dotenv
load_dotenv()

HuggingFace_token = os.getenv("HuggingFace_token")
 
# login to huggingface via token
from huggingface_hub import login
login(token=HuggingFace_token)


# # loadmodel function
# def loadModel():
#   global model, processor, device # Declare global inside the function
#   device = "cuda" if torch.cuda.is_available() else "cpu"
#   print(f"Using device: {device}")

#   # Load model
#   model = Sam3Model.from_pretrained("facebook/sam3").to(device)
#   processor = Sam3Processor.from_pretrained("facebook/sam3")
#   print("✓ Model loaded successfully!")


# # getBoundingBoxAndMask
# def getBoundingBoxAndMask(path):
#   # Load your image
#   image = Image.open(path)
#   prompt = ["window"]

#   # Run inference with text prompt
#   inputs = processor(
#       images=image,
#       text=prompt,
#       return_tensors="pt"
#   ).to(device)

#   with torch.no_grad():
#       outputs = model(**inputs)

#   # Post-process to get bounding boxes
#   results = processor.post_process_instance_segmentation(
#       outputs,
#       threshold=0.5,
#       mask_threshold=0.5,
#       target_sizes=inputs.get("original_sizes").tolist()
#   )[0]
#   return results

# function to convert image to base64 string
def b64_encode_image(path):
    """Convert an image (from URL or local path) to base64-encoded string."""
    
    # Check if it's a URL
    if path.startswith('http://') or path.startswith('https://'):
        # Use urllib instead of requests - no installation needed!
        with urlopen(path) as response:
            image_data = response.read()
        encoded_string = base64.b64encode(image_data).decode('utf-8')
    else:
        # Local file path
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    return encoded_string









app = Flask(__name__)



# # call loadModel
# loadModel()



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

    # Extract the image path from the request
    image_path = data.get('image_path')

    # convert image to base64 string
    image_b64 = b64_encode_image(image_path)

    # # call getboundingboxes and mask function
    # results = getBoundingBoxAndMask(image_path)

    # just return "okay" as response
    return jsonify({

        'image_b64': image_b64
        # 'results': results
    })




if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8001)