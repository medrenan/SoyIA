#importar biblioteca numpy
from tkinter import image_types
from matplotlib import image
import numpy as np
from scipy.fftpack import sc_diff
#importa biblioteca da rede
from darkflow.net.build import TFNet
#importar opencv
import cv2

import sys
# sys.path.append('/scripts/processamento-imagem')
# from imageProcessingScripts import preProcessing

# image_path = "images/1a444f61-6811-4c8b-adfc-f47f15c76c7e_1_jpg.rf.3cd7a0a5f219bec6297d1be85288ff39.jpg"

#opções para carregar o modelo
options = {"model": "cfg/yolo-new.cfg",
           "load": -1,
           "gpu": 1.0}
#configura a rede com as opções
tfnet2 = TFNet(options)
#carrega a rede
tfnet2.load_from_ckpt()

#Le a imagem realizando os pré-processamentos necessários
# original_img = preProcessing(image_path)
original_img = cv2.imread("sample_img/teste.jpg")

#Reconhece objetos na imagem
# results = tfnet2.return_predict(original_img)
results = tfnet2.return_predict(original_img)

if results:
        print("\nResults---------------------------------------------------")
        #Para cada objeto reconhecido printa o nome e com qual confiança
        for y in range(0, len(results)):
            print("Label:%s\tConfidence:%f"%(results[y]['label'], results[y]['confidence']))


#função para criar o retangulo 
def boxing(original_img , predictions):
    newImage = np.copy(original_img)
    #cria um box pra cada objeto detectado
    for result in predictions:
        top_x = result['topleft']['x']
        top_y = result['topleft']['y']

        btm_x = result['bottomright']['x']
        btm_y = result['bottomright']['y']

        confidence = result['confidence']
        label = result['label']
        #se for maior que 10% mostra
        if confidence > 0.1:
            #desenha o retangulo
            newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255,0,0), 2)
            #escreve o texto
            newImage = cv2.putText(newImage, label, (top_x, top_y-5), cv2.FONT_HERSHEY_PLAIN , 1, (255,0,0), 1)
        
    return newImage

#mostra imagem
cv2.imshow('image', boxing(original_img, results))
cv2.waitKey(0)
cv2.destroyAllWindows()

