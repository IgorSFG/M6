import cv2

# Abre o arquivo de video
cap = cv2.VideoCapture('arsene.mp4')

# Checa se foi possivel abrir o arquivo
if not cap.isOpened():
    print("Error opening video file")
    exit(1)
    
# Definição do tamanho do video de saida
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Loop de leitura frame por frame
while True:
    # Leitura do frame
    ret, frame = cap.read()

    # Para se não conseguir ler o frame
    if not ret:
        break
    
    # Edição frame com um retangulo
    cv2.rectangle(
            img=frame,
            pt1=(100, 100),
            pt2=(300, 300),
            color=(0,0,255),
            thickness=5
        )

    # Exibe o frame
    cv2.imshow('Playback', frame)
    
    # Escreve o frame no output
    out.write(frame)

    # Se o usuario apertar q, encerra o playback
    # O valor utilizado no waiKey define o fps do playback
    if cv2.waitKey(24) & 0xFF == ord('q'):
        break
    
# Fecha tudo
cap.release()
cv2.destroyAllWindows()