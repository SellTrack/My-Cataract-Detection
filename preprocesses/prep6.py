import os
import shutil
import random

# Klasör yolları
original_dataset_dir_normal = 'dataset/1_normal'
original_dataset_dir_cataract = 'dataset/2_cataract'
base_dir = 'dataset'

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

train_normal_dir = os.path.join(train_dir, 'normal')
train_cataract_dir = os.path.join(train_dir, 'cataract')
validation_normal_dir = os.path.join(validation_dir, 'normal')
validation_cataract_dir = os.path.join(validation_dir, 'cataract')

# Klasörleri oluştur
os.makedirs(train_normal_dir, exist_ok=True)
os.makedirs(train_cataract_dir, exist_ok=True)
os.makedirs(validation_normal_dir, exist_ok=True)
os.makedirs(validation_cataract_dir, exist_ok=True)

# Normal göz görüntülerini ayır
normal_images = os.listdir(original_dataset_dir_normal)
random.shuffle(normal_images)
split_point = int(0.8 * len(normal_images))

train_normal_images = normal_images[:split_point]
validation_normal_images = normal_images[split_point:]

for fname in train_normal_images:
    src = os.path.join(original_dataset_dir_normal, fname)
    dst = os.path.join(train_normal_dir, fname)
    shutil.copyfile(src, dst)

for fname in validation_normal_images:
    src = os.path.join(original_dataset_dir_normal, fname)
    dst = os.path.join(validation_normal_dir, fname)
    shutil.copyfile(src, dst)

# Katarakt göz görüntülerini ayır
cataract_images = os.listdir(original_dataset_dir_cataract)
random.shuffle(cataract_images)
split_point = int(0.8 * len(cataract_images))

train_cataract_images = cataract_images[:split_point]
validation_cataract_images = cataract_images[split_point:]

for fname in train_cataract_images:
    src = os.path.join(original_dataset_dir_cataract, fname)
    dst = os.path.join(train_cataract_dir, fname)
    shutil.copyfile(src, dst)

for fname in validation_cataract_images:
    src = os.path.join(original_dataset_dir_cataract, fname)
    dst = os.path.join(validation_cataract_dir, fname)
    shutil.copyfile(src, dst)
