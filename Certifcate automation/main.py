from PIL import Image,ImageDraw,ImageFont
import os

names = [
    "Vahora M.faaiz M.safi",
    "Vahora M.saad Asifbhai",
    "Vahora M.zaid Salimbhai",
    "Vahora M.ayan Samir bhai",
    "Vahora M.aayan Sohelbhai",
    "Vahora M.abaan Farukbhai",
    "Vahora M.saed Anasbhai",
    "Vahora Rehan Javedbhai",
    "Vahora Huzaifa Aarifbhai",
    "Vahora M.shan Majidbhai"
]

os.makedirs('Certificates',exist_ok=True)

for index,name in enumerate(names,start=1):

    Certificate_template = Image.open('Certificate_template.png')

    draw= ImageDraw.Draw(Certificate_template)

    font = ImageFont.truetype("DancingScript-Regular.ttf",100)

    text_position = (569,601)

    draw.text(text_position,name,fill="black",font=font)

    pdf_path = os.path.join("Certificates", f"{name}.pdf")


    rgb_image = Certificate_template.convert('RGB')
    rgb_image.save(pdf_path, format="PDF", resolution=100.0)

    print(f'{index}, Certificate Generator for the name {name} is created successfully!')