import tensorflow as tf
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
import datetime

# TensorBoard günlüklerinin kaydedileceği klasör
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# TensorBoard geri çağrısı
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Inception-ResNet-v2 modelini oluşturun (weights=None)
model = InceptionResNetV2(weights='weights/first weight.keras', input_shape=(299, 299, 3), classes=2)

# Modeli derleyin
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Eğitim ve doğrulama veri jeneratörlerini ayarlayın
train_datagen = ImageDataGenerator(
    rescale=1./255,             # Normalizasyon
    shear_range=0.2,            # Kesme işlemi
    zoom_range=0.2,             # Zoom işlemi
    horizontal_flip=True)       # Yatay çevirme

val_datagen = ImageDataGenerator(rescale=1./255)  # Sadece normalizasyon

# Eğitim veri jeneratörü
train_generator = train_datagen.flow_from_directory(
    'dataset/train',  # Eğitim veri yolu
    target_size=(299, 299),     # Resim boyutları
    batch_size=32,              # Batch boyutu
    class_mode='categorical')   # Sınıf modu

# Doğrulama veri jeneratörü
validation_generator = val_datagen.flow_from_directory(
    'dataset/validation',  # Doğrulama veri yolu
    target_size=(299, 299),     # Resim boyutları
    batch_size=32,              # Batch boyutu
    class_mode='categorical')   # Sınıf modu

# Modeli eğitin
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size,
    epochs=50,
    callbacks=[tensorboard_callback])  # TensorBoard geri çağrısını ekleyin

# Modeli Keras formatında kaydedin
model.save()
