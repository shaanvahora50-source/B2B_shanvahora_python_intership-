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
9
for index,name in enumerate(names,start=1):

    Certificate_template = Image.open('Certificate_template.png')

    draw= ImageDraw.Draw(Certificate_template)

    font = ImageFont.truetype("DancingScript-Regular.ttf",100)

    text_position = (569,601)

    draw.text(text_position,name,fill="black",font=font)

    safe_filename = f"{name}.png"

    output_path = os.path.join("Certificates",safe_filename)


    Certificate_template.save(output_path)

    print(f'{index}, Certificate Generator for the name {name} is created successfully!')

