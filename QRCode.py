import cv2
from pyzbar import pyzbar

# Cargar la imagen
imagen = cv2.imread("codigo.png")

# Encontrar y decodificar los códigos de barras y QR en la imagen
codigos = pyzbar.decode(imagen)

# Mostrar la información de los códigos encontrados
for codigo in codigos:
    # Obtener las coordenadas del código
    (x, y, w, h) = codigo.rect

    # Dibujar un rectángulo alrededor del código
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Mostrar la información del código
    tipo_codigo = codigo.type
    datos_codigo = codigo.data.decode("utf-8")
    texto = f"{datos_codigo} ({tipo_codigo})"
    cv2.putText(imagen, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Mostrar la imagen resultante
cv2.imshow("Imagen", imagen)
cv2.waitKey(0)
