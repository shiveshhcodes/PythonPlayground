import qrcode as qr
img = qr.make("https://chatgpt.com/c/f74c954a-d289-4b2f-8e9c-1cf17e00a92a")
img.save("chatgpt_100.png")