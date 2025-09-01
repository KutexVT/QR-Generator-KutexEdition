import qrcode
from PIL import Image, ImageDraw
import random

# URL para el QR
url = "https://guns.lol/kutex"

# Crear QR básico
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Generar imagen QR en blanco y negro
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# Crear fondo decorado (azul oscuro)
size = qr_img.size[0] + 80
bg = Image.new("RGBA", (size, size), (10, 20, 60, 255))
draw = ImageDraw.Draw(bg)

star_color = (255, 215, 0, 255)  # Amarillo dorado

# Generar estrellas aleatorias
for _ in range(50):  # cantidad de estrellas
    x = random.randint(0, size)
    y = random.randint(0, size)
    star_size = random.randint(5, 15)  # tamaños variados
    draw.regular_polygon(((x, y), star_size), n_sides=5, fill=star_color)

# Algunas estrellas grandes y brillantes
for _ in range(5):
    x = random.randint(0, size)
    y = random.randint(0, size)
    star_size = random.randint(20, 30)
    draw.regular_polygon(((x, y), star_size), n_sides=5, fill=star_color)

# Pegar QR en el centro
bg.paste(qr_img, ((size-qr_img.size[0])//2, (size-qr_img.size[1])//2), qr_img)

# Guardar imagen
output_path = "C:/Users/mikel/Desktop/qr_kutex.png"
bg.save(output_path)
output_path
