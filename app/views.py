import os
import cv2
import imutils
from PIL import Image
from flask import Blueprint, request, render_template, current_app
from werkzeug.utils import secure_filename
from skimage.metrics import structural_similarity as ssim

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")

    # POST request
    if "file_upload" not in request.files:
        return "No file part"

    file_upload = request.files["file_upload"]

    if file_upload.filename == "":
        return "No file selected"

    filename = secure_filename(file_upload.filename)

    # Paths
    upload_dir = current_app.config["UPLOADS"]
    original_path = os.path.join(
        current_app.root_path, "static", "original", "original.jpg"
    )
    generated_dir = os.path.join(
        current_app.root_path, "static", "generated"
    )

    os.makedirs(upload_dir, exist_ok=True)
    os.makedirs(generated_dir, exist_ok=True)

    upload_path = os.path.join(upload_dir, "uploaded.jpg")

    # Save uploaded image
    uploaded_image = Image.open(file_upload).resize((250, 160))
    uploaded_image.save(upload_path)

    # Load original image (must exist!)
    original_image = Image.open(original_path).resize((250, 160))
    original_image.save(original_path)

    # Read with OpenCV
    original_cv = cv2.imread(original_path)
    uploaded_cv = cv2.imread(upload_path)

    # Convert to grayscale
    original_gray = cv2.cvtColor(original_cv, cv2.COLOR_BGR2GRAY)
    uploaded_gray = cv2.cvtColor(uploaded_cv, cv2.COLOR_BGR2GRAY)

    # SSIM
    score, diff = ssim(original_gray, uploaded_gray, full=True)
    diff = (diff * 255).astype("uint8")

    # Threshold + contours
    thresh = cv2.threshold(
        diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
    )[1]

    cnts = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(original_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(uploaded_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Save outputs
    cv2.imwrite(os.path.join(generated_dir, "original_marked.jpg"), original_cv)
    cv2.imwrite(os.path.join(generated_dir, "uploaded_marked.jpg"), uploaded_cv)
    cv2.imwrite(os.path.join(generated_dir, "diff.jpg"), diff)
    cv2.imwrite(os.path.join(generated_dir, "thresh.jpg"), thresh)

    return render_template(
        "index.html",
        pred=f"{round(score * 100, 2)}% correct"
    )
