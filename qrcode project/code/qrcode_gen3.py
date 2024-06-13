import os
import qrcode

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
qr = qrcode.QRCode()
qr.add_data('Hello , World!')
qr.make(fit = True)
img = qr.make_image(fill='black' , back_color='white')
# img.show()
directory = "/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/PythonPlayground/qrcode project/images"
file_name = "helloworld.png"

file_path = os.path.join(directory , file_name)
img.save(file_path)