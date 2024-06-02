import qrcode 
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H ,
                 box_size=10,border=4,)

qr.add_data("https://www.youtube.com/watch?v=OKuiyX5k6zg&list=LL&index=6&t=29599s")
qr.make(fit=True)
img=qr.make_image(fill_color="black" , back_color="blue")
img.save("100dayscode.png")
