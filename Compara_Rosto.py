import cv2
import mediapipe as mp
import numpy as np

webcam = cv2.VideoCapture(0)

reconhecimento_rosto = mp.solutions.face_detection
desenho = mp.solutions.drawing_utils
reconhecedor_rosto = reconhecimento_rosto.FaceDetection()

# Carrega a imagem de referência, tem que criar um Array para ter mais de uma referencia.
imagem_referencia = cv2.imread('FotoRodrigo.png')

while webcam.isOpened():
    validacao, frame = webcam.read()
    if not validacao:
        break
    imagem = frame
    lista_rostos = reconhecedor_rosto.process(imagem)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(imagem, rosto)

            # Extrai a região do rosto da imagem atual
            x, y, w, h = int(rosto.location_data.relative_bounding_box.xmin * imagem.shape[1]), \
                         int(rosto.location_data.relative_bounding_box.ymin * imagem.shape[0]), \
                         int(rosto.location_data.relative_bounding_box.width * imagem.shape[1]), \
                         int(rosto.location_data.relative_bounding_box.height * imagem.shape[0])

            rosto_atual = frame[y:y + h, x:x + w]

            # Realiza a comparação com a imagem de referência
            resultado_comparacao = cv2.matchTemplate(imagem_referencia, rosto_atual, cv2.TM_CCOEFF_NORMED)

            # Define um limite de similaridade (ajuste conforme necessário)
            limite_similaridade = 0.7

            # Encontra as correspondências acima do limite
            loc = np.where(resultado_comparacao >= limite_similaridade)

            if loc[0].size > 0:
                print("Rosto correspondente encontrado!")
            else:
                print("Rosto NÃO encontrado!")

    cv2.imshow("Rostos na sua webcam", imagem)
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
