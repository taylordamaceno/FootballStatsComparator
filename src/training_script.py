import tensorflow as tf
from data_loader import load_data
from data_preprocessor import preprocess_data

def build_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model

def main():
    data = load_data()
    preprocessed_data = preprocess_data(data)
    
    # Supondo que preprocessed_data já esteja dividido em X_train, y_train, X_test, y_test
    X_train, y_train, X_test, y_test = preprocessed_data  # Simplificação
    
    model = build_model(input_shape=X_train.shape[1])
    model.fit(X_train, y_train, epochs=5, validation_split=0.2)
    model.evaluate(X_test, y_test)

if __name__ == "__main__":
    main()

