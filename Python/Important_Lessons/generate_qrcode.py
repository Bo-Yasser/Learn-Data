import qrcode
import os
# print(os.getcwd())
print("Qrcode Application")
qr_code = input("Write Any Thing To Generate It As Qrcode: ")
save_place = input("Write Absloute Pass With File Name: ")

image = qrcode.make(qr_code)
image.save(fr"{save_place}")
image.show()
# H:\Programing\Python\Photos