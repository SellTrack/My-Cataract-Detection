# a tool for resize images

from PIL import Image
import os


# Kaynak klasörü ve hedef klasörü belirtin
source_folder = '/Users/selmanorhan/Documents/Intern/Dataset/source_folder'
target_folder = '/Users/selmanorhan/Documents/Intern/Dataset/target_folder'

# Hedef boyut
target_size = (512, 512)

# Hedef klasörü oluşturun (varsa, yeniden oluşturmayın)
os.makedirs(target_folder, exist_ok=True)

# Kaynak klasördeki tüm dosyaları listele
files = os.listdir(source_folder)

# Her bir dosyayı yeniden boyutlandırıp hedef klasöre kaydet
for file_name in files:
    if file_name.endswith('.jpg') or file_name.endswith('.png'):  # Sadece JPEG veya PNG dosyalarını işle
        try:
            # Resmi aç
            img = Image.open(os.path.join(source_folder, file_name))
            
            # Resmi thumbnail olarak yeniden boyutlandır (orijinal oranı korur)
            img.thumbnail(target_size, Image.LANCZOS)

            # Yeniden boyutlandırılmış resmi hedef klasöre kaydet
            background = Image.new('RGB', target_size, (0, 0, 0))  # Siyah arka plan oluştur
            bg_w, bg_h = background.size
            img_w, img_h = img.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
            background.paste(img, offset)
            
            target_file_path = os.path.join(target_folder, file_name)
            background.save(target_file_path)

            print(f"{file_name} yeniden boyutlandırıldı ve kaydedildi.")
        except Exception as e:
            print(f"Hata: {file_name} işlenirken bir hata oluştu - {e}")

print("İşlem tamamlandı.")
