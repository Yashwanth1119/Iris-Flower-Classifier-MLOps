import pickle
from sklearn.metrics import classification_report
from src.train import train_model

def evaluate():
    clf, X_test, y_test = train_model()
    y_pred = clf.predict(X_test)
    print("Model Evaluation:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluate()
