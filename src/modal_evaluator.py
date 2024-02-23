import numpy as np

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = np.mean(np.argmax(predictions, axis=1) == y_test)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    return accuracy

