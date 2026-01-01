# 🆔 PAN Card Tampering Detection using Flask & Computer Vision

A Flask-based web application that detects PAN card tampering by comparing an uploaded PAN card image with an original reference image using SSIM (Structural Similarity Index) and OpenCV.

This project demonstrates an end-to-end Computer Vision + Web Application workflow.

---

## 🚀 Features

- Upload PAN card image via web UI  
- Compare uploaded image with original PAN card  
- Detect tampered regions using SSIM  
- Highlight differences using bounding boxes  
- Generate:
  - Similarity score
  - Difference image
  - Threshold image
  - Marked original & uploaded images

---

## 🧠 Workflow

1. Upload PAN card image  
2. Resize and preprocess images  
3. Convert images to grayscale  
4. Compute SSIM score  
5. Extract differences  
6. Detect contours  
7. Highlight tampered regions  
8. Display results on UI  

---

## 📁 Project Structure

pan-card-tampering-detection/
│

├── app.py

├── config.py

├── requirements.txt

├── Procfile

├── README.md

├── .gitignore

│

├── app/

│   ├── __init__.py

│   ├── views.py

│   ├── templates/

│   │   └── index.html

│   └── static/

│       ├── css/

│       ├── js/

│       ├── uploads/

│       ├── original/

│       │   └── original.jpg

│       └── generated/

│

├── notebooks/

├── sample_data/

└── image/

---

## ⚙️ Technologies Used

- Python  
- Flask  
- OpenCV  
- scikit-image (SSIM)  
- Pillow (PIL)  
- HTML, CSS (Materialize)  

---

## 🛠️ Installation Steps

1) Clone Repository

git clone https://github.com/Musharraf-Bubere/pan-card-tampering-detection.git  
cd pan-card-tampering-detection

2) Create Environment (Recommended)

Conda:
conda create -n pctd_env python=3.10 -y  
conda activate pctd_env

OR venv:
python -m venv venv  
venv\Scripts\activate

3) Install Dependencies

pip install -r requirements.txt

4) Add Original PAN Image

Place the original PAN card image here:
app/static/original/original.jpg

Note: This file must exist before running the app.

5) Run Application

python app.py

Open browser:
http://127.0.0.1:5000/

---

## 📊 Output

- Similarity score (%)  
- Marked original image  
- Marked uploaded image  
- Difference image  
- Threshold image  

---

## 🔐 Security Notes

- Uploaded files are stored locally  
- Generated images are ignored in GitHub  
- Do NOT upload real PAN card images to public repositories  

---

## 🚀 Future Enhancements

- Tampered / Not Tampered classification  
- OCR-based PAN number validation  
- Database integration  
- Authentication system  
- Cloud deployment  

---

## 🎯 Learning Outcomes

- Flask Blueprints & config management  
- File upload handling  
- Image preprocessing  
- SSIM-based image comparison  
- Real-world Computer Vision integration in web apps  

---

## 👤 Author

Musharraf Bubere  
Aspiring Data Scientist & Machine Learning   
GitHub: https://github.com/Musharraf-Bubere  

---

## ⭐ Acknowledgements

- OpenCV  
- scikit-image  
- Flask Documentation  
- Computer Vision Community  
