import qrcode

URL_PAGINA = "https://francisco-ne.github.io/fabrica-qr/"

qr = qrcode.make(URL_PAGINA)
qr.save("qr_maquina.png")

print("✅ QR generado. Listo para imprimir.")