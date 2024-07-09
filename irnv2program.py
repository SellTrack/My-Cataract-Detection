import tensorflow as tf
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2
from tensorflow.keras.preprocessing import image
import numpy as np

model = InceptionResNetV2(weights=None, input_shape=(299, 299, 3), classes=2)
model.load_weights('weights/secondweight.keras')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalizasyon
    return img_array

img_path = 'dataset/validation/cataract/cataract_098.jpg'
img_array = preprocess_image(img_path)



predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)

# Sınıf adlarını belirleyin (örneğin, 0: Normal, 1: Katarakt)
class_names = ['Normal', 'Katarakt']
print(f"Bu resim: {class_names[predicted_class[0]]}")
