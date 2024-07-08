from PIL import Image
import os

# Kaynak klasör yolu
source_folder_path = '/Users/selmanorhan/Documents/GitHub/My-Cataract-Detection/dataset/2_cataract'

# Hedef klasör yolu
target_folder_path = '/Users/selmanorhan/Documents/GitHub/My-Cataract-Detection/taget'

# Hedef klasör yoksa oluştur
os.makedirs(target_folder_path, exist_ok=True)

# Yeni boyutlar
new_size = (299, 299)

# Kaynak klasördeki tüm dosyalar üzerinde döngü
for filename in os.listdir(source_folder_path):
    # Dosya yolunu oluştur
    file_path = os.path.join(source_folder_path, filename)
    
    # Sadece resim dosyalarını işlemek için kontrol et
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Resmi aç
        with Image.open(file_path) as img:
            # Resmi yeniden boyutlandır
            img_resized = img.resize(new_size)
            
            # Yeni dosya adını oluştur, aynı dosya adıyla hedef klasöre kaydet
            new_file_path = os.path.join(target_folder_path, filename)
            
            # Yeniden boyutlandırılmış resmi kaydet
            img_resized.save(new_file_path)

print("Tüm resimler başarıyla yeniden boyutlandırıldı ve hedef klasöre kaydedildi.")
