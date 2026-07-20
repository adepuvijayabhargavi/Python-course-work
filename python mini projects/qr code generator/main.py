import qrcode

print("====== QR Code Generator ======")

data = input("Enter the data to encode in the QR code: ")

filename = input("Enter the filename to save the QR code (without .png): ")

img = qrcode.make(data)

img.save(filename + ".png")

print(f"QR Code saved successfully as {filename}.png")