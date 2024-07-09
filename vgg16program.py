import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np

# VGG16 modelini yükle
model_path = 'models-weights/vgg16/VGG16 Finetuned Model1.h5'
model = tf.keras.models.load_model(model_path)

# Resmi işleme ve tahmin yapma fonksiyonu
def predict_cataract(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Tahmin yap
    predictions = model.predict(img_array)
    if predictions[0][0] > predictions[0][1]:
        return "Normal"
    else:
        return "Katarakt"

# Test için kullanılacak resim dosyasının yolu
img_path = 'dataset/validation/cataract/2207_right.jpg'  # Burayı kendi resminizin yoluna göre güncelleyin

# Tahmin yap
result = predict_cataract(img_path)
print(f"Bu resim: {result}")
