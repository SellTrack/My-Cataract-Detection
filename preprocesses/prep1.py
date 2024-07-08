# a tool for extract specific files from a folder to another by checking excel sheet

import os
import shutil
import pandas as pd

# Klasör yolunu ve hedef klasör yolunu belirtin
source_folder = '/Users/selmanorhan/Downloads/Ocular Disease Recognition/preprocessed_images'
target_folder = '/Users/selmanorhan/Documents/extracted dataset'

# Dosya isimlerini içeren tabloyu okuyun (örneğin CSV dosyası olarak)
file_names_file = '/Users/selmanorhan/Downloads/Untitled spreadsheet page1.csv'
df = pd.read_csv(file_names_file)

# 0. sütunu seçmek için
file_names_to_move = df.iloc[:, 0].tolist()

# Klasördeki dosyaları listele
files_in_folder = os.listdir(source_folder)

# Hedef klasörü oluşturun (varsa, yeniden oluşturmayın)
os.makedirs(target_folder, exist_ok=True)

# Belirtilen dosya isimlerini hedef klasöre kopyala
for file_name in file_names_to_move:
    if file_name in files_in_folder:
        source_file_path = os.path.join(source_folder, file_name)
        target_file_path = os.path.join(target_folder, file_name)
        shutil.copy(source_file_path, target_file_path)
        print(f"{file_name} kopyalandı.")
    else:
        print(f"{file_name} klasörde bulunamadı.")

print("İşlem tamamlandı.")
