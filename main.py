import qrcode


def generar_codigo_qr(enlace):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(enlace)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("codigo_qr.png")


# Ejemplo de uso
enlace = "https://www.instagram.com/fablabuv/"
generar_codigo_qr(enlace)
