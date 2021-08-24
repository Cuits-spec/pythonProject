import qrcode
import image
# 只需将文本、链接或任何内容传递给QRcode 模块的“make”功能。
img = qrcode.make('http://www.baidu.com/')
img.save("11.jpg")



