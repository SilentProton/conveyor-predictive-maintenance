# 🚀 YOLOv8 Training Guide

This guide explains how to train a YOLOv8 model using the provided `train.ipynb` notebook inside a Python virtual environment.

---

## 📌 1. Create and Activate a Virtual Environment

### **Windows**
```bash
    python -m venv venv
    venv\Scripts\activate
```

### **Linux / Mac**
```bash
    python3 -m venv venv
    source venv/bin/activate
```

## 📌 4. Train the Model

Inside the notebook, run the YOLOv8 training cell:

```bash
!yolo task=detect mode=train data=data/dataset/data.yaml model=yolov8s.pt epochs=50 imgsz=640
```

## 🔍 Parameter Details

- **`data.yaml`** → Path to dataset configuration  
- **`model`** → Pre-trained YOLOv8 model (`yolov8s.pt`, `yolov8m.pt`, etc.)  
- **`epochs`** → Number of training epochs  
- **`imgsz`** → Image size for training (e.g., `640`)
