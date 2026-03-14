import cv2
import numpy as np
import os

# Pega o diretório onde o script está sendo executado
base_dir = os.path.dirname(__file__)
filter_path = os.path.join(base_dir, 'anon.png')

# 1. Configurações Iniciais
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carregar com -1 para garantir a leitura do canal de transparência (Alpha)
img_filter = cv2.imread(filter_path, cv2.IMREAD_UNCHANGED)

# Checagem de segurança (Se a imagem carregou)
if img_filter is None:
    print(f"Erro: Não foi possível encontrar a imagem em: {filter_path}")
    exit()

# Iniciar captura
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # Aumentamos a largura em 30% e a altura em 60% para cobrir tudo
        nw, nh = int(w * 1.3), int(h * 1.6)
        nx, ny = int(x - 0.15 * w), int(y - 0.35 * h)
        
        # Impede que a máscara tente ser desenhada fora da janela (evita erro de matriz)
        ny, nx = max(0, ny), max(0, nx)
        if ny + nh > frame.shape[0] or nx + nw > frame.shape[1]:
            continue

        # Redimensionar a máscara para o tamanho do rosto detectado
        face_mask = cv2.resize(img_filter, (nw, nh))

        # --- A MÁGICA DA TRANSPARÊNCIA ---
        # Se a imagem tem 4 canais (BGRA)
        if face_mask.shape[2] == 4:
            # Separar os pixels de cor (RGB) e os pixels de transparência (Alpha)
            overlay_colors = face_mask[:, :, :3]
            alpha_channel = face_mask[:, :, 3] / 255.0  # Normaliza de 0 a 1

            # Recorte da webcam onde a máscara será aplicada
            roi = frame[ny:ny+nh, nx:nx+nw]

            # Mistura os pixels: (Máscara * Transparência) + (Webcam * Inverso da Transparência)
            for c in range(3):
                roi[:, :, c] = (alpha_channel * overlay_colors[:, :, c] + 
                                (1.0 - alpha_channel) * roi[:, :, c])
            
            frame[ny:ny+nh, nx:nx+nw] = roi
        else:
            # Se cair aqui, seu PNG não tem transparência real no arquivo
            # Apenas desenha o retângulo padrão para não dar erro
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, "PNG sem Canal Alfa", (x, y-10), 1, 1, (0,0,255), 2)

    cv2.imshow('Filtro Expert - Masks', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()