import qrcode
from PIL import Image

def generate_qr_with_logo(url, qr_color, bg_color, output_file="qr-code.png"):
    # Настройки QR-кода для размера 300x300
    qr = qrcode.QRCode(
        version=1,  # Минимальный размер модуля
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Высокая коррекция ошибок (30%)
        box_size=10,  # Каждый "квадрат" = 10 пикселей
        border=4  # Рамка 4 модуля (4 * 10 * 2 + 21 * 10 = 290, с учетом погрешности ~300)
    )
    
    # Добавляем ссылку
    qr.add_data(url)
    qr.make(fit=True)
    
    # Создаем QR-код с указанными цветами
    qr_img = qr.make_image(fill_color=qr_color, back_color=bg_color).convert('RGB')
    
    # Принудительно устанавливаем размер 300x300
    qr_img = qr_img.resize((300, 300), Image.LANCZOS)
    
    # Открываем логотип
    # logo = Image.open(logo_path)
    
    # Масштабируем логотип (~25% от 300 = 75x75 пикселей)
    # logo_size = 75
    # logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    
    # # Центрируем логотип
    # logo_pos = ((300 - logo_size) // 2, (300 - logo_size) // 2)
    # qr_img.paste(logo, logo_pos, logo if logo.mode == 'RGBA' else None)  # Учитываем прозрачность PNG
    
    # Сохраняем результат
    qr_img.save(output_file)
    print(f"QR-код сохранен как {output_file}")

# Параметры
url = "https://drive.google.com/file/d/1xpeZxtJj3Nm41M1hrgheb6tk-S6VuFPy/view?usp=sharing"  # Замени на свою ссылку
# logo_path = r"C:/Users/Admin/Desktop/Презентации для Куралай — копия — копия/ГРУНТ ЭПОКСИДНЫЙ ЭКОНОМ/img/Floortec Logo.5 знак.png"#flortec logo
# logo_path=r"C:/Users/Admin/Desktop/Презентации для Куралай — копия — копия/Nomad Top/img/conteria-white.png" #conteria logo
# qr_color = (79, 209, 197)  # Цвет #4fd1c5 в RGB бирюзовый
qr_color=(0, 0, 0) # Цвет #ff121e в RGB красный
bg_color = "white"  # Фон белый
output_file = "qr-code.png"

generate_qr_with_logo(url, qr_color, bg_color, output_file)