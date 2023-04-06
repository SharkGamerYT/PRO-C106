import cv2


# Crear nuestro clasificador de cuerpos
body_classifer = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Inicializar la captura de video para nuestro archivo de video
cap = cv2.VideoCapture('walking.avi')

# Comenzar el bucle una vez que el video esté cargado exitosamente
while True:
    
    # Leer el primer cuadro
    ret, frame = cap.read()

    # Convertir cada cuadro a escala de grises
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pasar el cuadro a nuestro clasificador de cuerpos
    bodies = body_classifer.detectMultiScale(gray, 1.2, 3)
    
    # Extraer las cajas envolventes para cualquier cuerpo identificado
    cv2.imshow() 

    if cv2.waitKey(1) == 32: #32 es la barra espaciadora
        break

cap.release()
cv2.destroyAllWindows()
