# import qrcode 
# from PIL import Image
# import qrcode.constants

# qr=qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H ,
#     box_size=10,
#     border=4,
# )

# qr.add_data("https://www.youtube.com/watch?v=OKuiyX5k6zg&list=LL&index=6&t=29599s")
# qr.make(fit=True)
# img=qr.make_image(fill_color="black" , back_color="blue")
# img.save("100dayscode.png")

# import qrcode
# from PIL import Image
# # import qrcode.constants

# qr=qrcode.QRCode(
#     version=1 ,
#     # error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=5,
# )

# qr.add_data("https://www.youtube.com/watch?v=OKuiyX5k6zg&list=LL&index=6&t=29599s")
# qr.make(fit=True)
# img=qr.make_image(fill_color="purple")
# img.save("google.png")


# import qrcode
# from PIL import Image
# import qrcode.constants

# while True:
#     qr=qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_H,
#         box_size=20,
#         border=5,
#     )
#     qr.add_data("https://www.youtube.com/watch?v=OKuiyX5k6zg&list=LL&index=6&t=29599s")
#     qr.make(fit=True)
#     encolor = input("enter the color you want to get print - ")
#     img=qr.make_image(fill_color=encolor)
#     # file_name= f"qrcode_{encolor}.png"
#     # img.save(file_name)
#     img.save("google.png")
#     # print(encolor)
    
    
    
    # quit_input = input("enter quit to end or c to continue! ")
    # if quit_input=="quit":
    #     break
    # elif quit_input=="c":
    #     continue
    
import os
import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode (
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=30,
    border=8,
)

qr.add_data("https://chatgpt.com/c/f74c954a-d289-4b2f-8e9c-1cf17e00a92a")
qr.make(fit=True)
img=qr.make_image(fill_color="red" , back_color="green")

directory = "/Users/shiveshrichhariya/Desktop/GITHUB/Python Projects/images"
file_name = "googlee.png"

file_path = os.path.join(directory , file_name)
img.save(file_path)
# img.save("google.png")