import pickle
from sklearn.ensemble import RandomForestClassifier
from src.data_loader import load_data
from src.preprocess import preprocess

def train_model():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess(df)
    
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    with open('model/iris_model.pkl', 'wb') as f:
        pickle.dump(clf, f)
    
    return clf, X_test, y_test

if __name__ == "__main__":
    train_model()
