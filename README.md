# 🚦 Traffic Sign Detector with Deep Learning and MLOps

A deep learning project that detects traffic signs using Keras and integrates a full MLOps workflow with GitHub Actions, Docker, Kubernetes, ArgoCD, MLflow, and a Streamlit demo interface.

---

## 💡 Project Features

- Deep Learning (Keras + TensorFlow)
- Model Evaluation & Visualization
- Model Registry with MLflow
- Dockerized Training Pipeline
- CI/CD with GitHub Actions
- GitOps Deployment using ArgoCD
- Kubernetes-ready Inference
- Streamlit UI for Predictions

---

## 🧠 Model Training

The CNN model is trained on the GTSRB dataset (or CIFAR-10 for demo). `train.py` includes preprocessing and saving the model (`.h5` format).

## 📊 Model Evaluation

Model performance is visualized using a Streamlit dashboard in `streamlit_app/app.py`.

## 🚀 Deployment Workflow

1. **CI/CD (GitHub Actions)**
2. **Docker Image Build & Push**
3. **ArgoCD syncs Kubernetes manifests**
4. **Kubernetes Deployment (YAML files)**
5. **Streamlit UI for live predictions**

---

## 📁 Project Structure

```
traffic-sign-detector/
├── data/                      # Training data (not included)
├── notebooks/                 # Jupyter exploration
├── src/                       # Python scripts
│   ├── train.py
│   ├── model.py
│   └── predict.py
├── streamlit_app/             # Streamlit dashboard
│   └── app.py
├── k8s/                       # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
├── .github/workflows/         # GitHub Actions
│   └── ci-cd.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone and Install Dependencies
```bash
git clone https://github.com/Max-Ola/Detect-Traffic-Signs-with-Deep-Learning-using-Keras)
cd traffic-sign-detector
pip install -r requirements.txt
```

### 2. Train Model
```bash
python src/train.py
```

### 3. Run Streamlit Dashboard
```bash
streamlit run streamlit_app/app.py
```

---

## ☸️ Kubernetes Deployment

### Apply resources:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

## 🔁 ArgoCD GitOps

Point ArgoCD to this GitHub repo or sync manually:
```bash
argocd app create traffic-detector \
  --repo https://github.com/yourusername/traffic-sign-detector.git \
  --path k8s \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default

argocd app sync traffic-detector
```

---

## 📦 MLflow Tracking

Run MLflow locally:
```bash
mlflow ui
```

It will log metrics and save your model in the `mlruns/` directory.

---

## 🧪 CI/CD with GitHub Actions

The pipeline:
- Builds + tests
- Pushes Docker image
- Triggers ArgoCD sync

---

## 🎨 Streamlit UI

Interactive dashboard for predictions. Upload a traffic sign image and get predicted output with confidence score.

---

