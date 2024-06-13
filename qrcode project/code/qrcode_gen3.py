import os
import qrcode
from PIL import Image
import qrcode.constants

# basic code

# qr = qrcode.QRCode()
# qr.add_data('https://chatgpt.com/c/8e0c7016-79fd-43e6-af2c-e574b7c726fa')
# qr.make(fit=True)

# img = qr.make_image(fill='black' , back_color='white')
# img.show()


# Creating a QR code with custom size and border



# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('https://www.example.com')
# qr.make(fit=True)

# img = qr.make_image(fill='black', back_color='white')
# img.show()



# text image qr code


# qr = qrcode.QRCode()
# qr.add_data('Hello , World!')
# qr.make(fit = True)
# img = qr.make_image(fill='black' , back_color='white')
# # img.show()
# directory = "/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/qrcode project/images"
# file_name = "helloworld.png"

# file_path = os.path.join(directory , file_name)
# img.save(file_path)


qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

qr.add_data("Sam Altman")
qr.make(fit=True)

img = qr.make_image(fill = 'black' , back_color = 'white')
logo = Image.open('/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/qrcode project/images/google.png')
logo = logo.resize((90, 90))
pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)

img.show()
# img.show()