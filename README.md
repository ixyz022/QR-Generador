# Generador de Códigos QR en Python con la Biblioteca `qrcode`

## Introducción

Los códigos QR son una forma eficaz de compartir información de manera rápida y accesible. En Python, podemos generar fácilmente códigos QR utilizando la biblioteca `qrcode`. Este documento explica cómo instalar y usar esta biblioteca para crear códigos QR a partir de enlaces web.

## Instalación de `qrcode`

Primero, necesitas instalar la biblioteca `qrcode`. Esta biblioteca incluye todo lo necesario para generar códigos QR. Puedes instalarla mediante pip:

```bash
pip install qrcode[pil]
```

La parte `[pil]` asegura que también se instale Pillow, una biblioteca requerida para el manejo de imágenes.

## Uso de la Biblioteca `qrcode`

### Creación Básica de un Código QR

Para generar un código QR, sigue estos pasos en tu script de Python:

1. **Importa la biblioteca:**

   ```python
   import qrcode
   ```

2. **Define una función para generar el código QR:**

   ```python
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
   ```

   - `version`: Determina el tamaño del código QR.
   - `error_correction`: Define el nivel de corrección de errores.
   - `box_size`: Tamaño de cada caja del código QR.
   - `border`: Tamaño del borde alrededor del código QR.

3. **Genera un código QR con un enlace específico:**

   ```python
   enlace = "https://www.ejemplo.com"
   generar_codigo_qr(enlace)
   ```

   Esto creará un archivo de imagen llamado `codigo_qr.png` que contiene el código QR del enlace proporcionado.

### Personalización Adicional

La biblioteca `qrcode` ofrece varias opciones para personalizar tu código QR, como cambiar los colores, ajustar el tamaño y más. Consulta la [documentación oficial](https://pypi.org/project/qrcode/) para más detalles.

## Conclusión

Con la biblioteca `qrcode` en Python, generar códigos QR es un proceso sencillo y altamente personalizable. Esta herramienta es útil para compartir enlaces, información de contacto, o cualquier otro tipo de datos de manera rápida y eficiente en forma de códigos QR.