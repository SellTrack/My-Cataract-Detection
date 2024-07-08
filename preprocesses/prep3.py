# a tool for transform png images to jpg image.

from PIL import Image
import os

#
# Kaynak klasörü ve hedef klasörü belirtin
source_folder = '/Users/selmanorhan/Documents/Intern/Dataset/source_folder'
target_folder = '/Users/selmanorhan/Documents/Intern/Dataset/target_folder'

# Hedef klasörü oluşturun (varsa, yeniden oluşturmayın)
os.makedirs(target_folder, exist_ok=True)

# Kaynak klasördeki tüm dosyaları listele
files = os.listdir(source_folder)

# Her bir PNG dosyasını JPG formatına dönüştürüp hedef klasöre kaydet
for file_name in files:
    if file_name.lower().endswith('.png'):  # Sadece PNG dosyalarını işle
        try:
            # Resmi aç
            img = Image.open(os.path.join(source_folder, file_name))
            
            # JPG formatına dönüştür
            rgb_img = img.convert('RGB')
            
            # Hedef dosya yolunu oluştur
            target_file_name = os.path.splitext(file_name)[0] + '.jpg'
            target_file_path = os.path.join(target_folder, target_file_name)
            
            # JPG olarak kaydet
            rgb_img.save(target_file_path, format='JPEG')

            print(f"{file_name} JPG formatına dönüştürüldü ve kaydedildi.")
        except Exception as e:
            print(f"Hata: {file_name} işlenirken bir hata oluştu - {e}")

print("İşlem tamamlandı.")
