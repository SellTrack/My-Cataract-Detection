# a tool for taking center 1600 pixel square from image.

from PIL import Image
import os

# Kaynak klasörü ve hedef klasörü belirtin
source_folder = '/Users/selmanorhan/Documents/Intern/Dataset/source_folder'
target_folder = '/Users/selmanorhan/Documents/Intern/Dataset/target_folder'

# Hedef boyut
target_size = 1600

# Hedef klasörü oluşturun (varsa, yeniden oluşturmayın)
os.makedirs(target_folder, exist_ok=True)

# Kaynak klasördeki tüm dosyaları listele
files = os.listdir(source_folder)

# Her bir dosyayı işleyip hedef klasöre kaydet
for file_name in files:
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):  # Sadece JPEG, JPG veya PNG dosyalarını işle
        try:
            # Resmi aç
            img = Image.open(os.path.join(source_folder, file_name))
            
            # Görüntü boyutları
            width, height = img.size
            center_x, center_y = width // 2, height // 2
            
            # Kırpılacak bölgenin koordinatları
            left = max(center_x - target_size // 2, 0)
            upper = max(center_y - target_size // 2, 0)
            right = min(center_x + target_size // 2, width)
            lower = min(center_y + target_size // 2, height)
            
            # Resmi kırp
            cropped_img = img.crop((left, upper, right, lower))
            
            # Hedef dosya yolunu oluştur
            target_file_path = os.path.join(target_folder, file_name)
            
            # Kırpılmış resmi kaydet
            cropped_img.save(target_file_path)

            print(f"{file_name} işlenip kaydedildi.")
        except Exception as e:
            print(f"Hata: {file_name} işlenirken bir hata oluştu - {e}")

print("İşlem tamamlandı.")
