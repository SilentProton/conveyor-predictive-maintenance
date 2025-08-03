from flask import Flask, request, send_file
from flask_cors import CORS
from ultralytics import YOLO
import io
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)

model = YOLO("conveyor.pt") 

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return {"error": "No image uploaded"}, 400
    
    file = request.files["image"]

    # Convert FileStorage → PIL Image
    pil_img = Image.open(file.stream).convert("RGB")

    # Convert PIL Image → NumPy (YOLO accepts NumPy arrays)
    img_array = np.array(pil_img)

    # Run YOLO prediction
    results = model.predict(source=img_array, conf=0.1)

    # Get annotated image (NumPy BGR)
    annotated_img = results[0].plot()

    # Convert back to PIL (RGB)
    annotated_pil = Image.fromarray(annotated_img[..., ::-1])

    # Store in memory
    img_io = io.BytesIO()
    annotated_pil.save(img_io, format="JPEG")
    img_io.seek(0)

    # Send to frontend
    return send_file(img_io, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)
