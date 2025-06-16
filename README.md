# MLOps Iris Classifier Project

This project demonstrates a full MLOps pipeline with model training, evaluation, prediction, and REST API deployment using FastAPI and Docker.

## 🔧 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/mlops_iris_project.git
cd mlops_iris_project
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Train and Evalute
```bash
python src/train.py
python src/evaluate.py
```
### 4. Start API locally
```bash
uvicorn api.app:app --reload
```
### 5. Dockerize
```bash
docker build -t iris-mlops
docker run -p 8000:8000 iris-mlops
```
## API Endpoint
Post/predict
```bash
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
Returns:
```bash
json
{
    "prediction"=0
}
```
## Features
* Scikit-Learn ML Pipeline
* REST API with FastAPI
* Docker container
* Ready for CI/CD and Deployment

```bash

---

### ✅ To Host on GitHub
1. Create a GitHub repository (e.g., `mlops_iris_project`)
2. Initialize your local folder:
   ```bash
   git init
   git add .
   git commit -m "Initial MLOps project"
   git branch -M main
   git remote add origin https://github.com/yourusername/mlops_iris_project.git
   git push -u origin main

```

