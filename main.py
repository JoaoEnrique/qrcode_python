import qrcode
text = input("Texto para QR Code: ")

imagem = qrcode.make(text)
imagem.save(f"{text}.jpg")

print("QR Code gerado")