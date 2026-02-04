import qrcode

URL_PAGINA = "https://fabrica-qr.vercel.app/"

qr = qrcode.make(URL_PAGINA)
qr.save("qr_maquina.png")

print("✅ QR generado. Listo para imprimir.")