from gtts import gTTS

texto = """
Procedimiento de inicio de máquina:
Paso uno: colocarse los elementos de protección personal.
Paso dos: verificar que no haya objetos en el área.
Paso tres: encender el interruptor principal.
Paso cuatro: avisar al supervisor ante cualquier falla.
"""

tts = gTTS(text=texto, lang="es")
tts.save("procedimiento.mp3")

print("Audio generado correctamente")