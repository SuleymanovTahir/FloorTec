import fitz  # PyMuPDF
import os

pdf_path = r"C:/Users/Админ/Desktop/Презентации для Куралай/Nomad Top мешок 35х60 в кривых/Nomad Top мешок 35х60 в кривых.pdf"
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)

doc = fitz.open(pdf_path)
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    pix = page.get_pixmap(dpi=300)
    output_path = os.path.join(
        output_folder,
        f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{page_num + 1}.png"
    )
    pix.save(output_path)

print("Готово!")
