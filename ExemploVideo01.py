import cv2

# Carrega o classificador em cascata treinado
cascade = cv2.CascadeClassifier('data/cascade.xml')

# Carrega a imagem a ser detectada
img = cv2.imread('mask.jpg')

# Converte a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecta objetos na imagem
objects = cascade.detectMultiScale(gray, scaleFactor=1.5, minSize=(150, 150))

# Desenha retângulos ao redor dos objetos detectados
for (x, y, w, h) in objects:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostra a imagem com os objetos detectados
cv2.imshow('detector', img)
cv2.waitKey(0)
cv2.destroyAllWindows()