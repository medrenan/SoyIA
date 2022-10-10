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
sys.path.append('/scripts/processamento-imagem')

from scripts.imageProcessingScripts import preProcessing

image_path = "images/1a444f61-6811-4c8b-adfc-f47f15c76c7e_1_jpg.rf.3cd7a0a5f219bec6297d1be85288ff39.jpg"

#opções para carregar o modelo
options = {"model": "cfg/yolo-new.cfg",
           "load": -1,
           "gpu": 1.0}
#configura a rede com as opções
tfnet2 = TFNet(options)
#carrega a rede
tfnet2.load_from_ckpt()

#Le a imagem realizando os pré-processamentos necessários
#original_img = preProcessing(image_path)
original_img = cv2.imread("sample_img/3.jpg")

#Reconhece objetos na imagem
#results = tfnet2.return_predict(original_img)
results = tfnet2.return_predict(original_img)

confi = 0
soyTotal = 0
beans = 0

if results:
        print("\nResults---------------------------------------------------")
        #Para cada objeto reconhecido printa o nome e com qual confiança
        for y in range(0, len(results)):
            print("Label:%s\tConfidence:%f"%(results[y]['label'], results[y]['confidence']* 100))
            diferencax = results[y]['bottomright']['x'] - results[y]['topleft']['x']
            diferencay = results[y]['bottomright']['y'] - results[y]['topleft']['y']
            print("Diferença: %f" %diferencax)
            if results[y]['confidence'] * 100 >= 25:
                soyTotal = soyTotal + 1
                confi = confi + results[y]['confidence'] * 100
                if diferencax >= 15 or diferencay >= 26:
                    beans += 3
                elif diferencax < 15 and diferencax >= 8 and diferencay >= 18 or diferencay < 26 and diferencax >= 8 and diferencay >= 18:
                    beans += 2
                else:
                    beans += 1
            
        print('Media de confiança: ', confi/soyTotal)
        print('Total de soja: ', beans)
        print('Total de vagens: ', soyTotal)


#função para criar o retangulo 
def boxing(original_img , predictions):
    newImage = np.copy(original_img)
    #cria um box pra cada objeto detectado
    for result in predictions:
        top_x = result['topleft']['x']
        top_y = result['topleft']['y']

        btm_x = result['bottomright']['x']
        btm_y = result['bottomright']['y']

        confidence = result['confidence'] * 100
        label = result['label']

        diferencax = result['bottomright']['x'] - result['topleft']['x']
        diferencay = result['bottomright']['y'] - result['topleft']['y']
        #se for maior que 10% mostra
        if confidence > 30:
            if diferencax >= 15 or diferencay >= 26:
                newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (0, 0, 255), 1)
                newImage = cv2.putText(newImage, '3', (top_x+2, top_y+8), cv2.FONT_HERSHEY_PLAIN , 0.7, (0, 0, 255), 1)
            elif diferencax < 15 and diferencax >= 8 and diferencay >= 18 or diferencay < 26 and diferencax >= 8 and diferencay >= 18:
                newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (0, 255, 255), 1)
                newImage = cv2.putText(newImage, '2', (top_x+2, top_y+8), cv2.FONT_HERSHEY_PLAIN , 0.7, (0, 255, 255), 1)
            else:
                newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255, 0, 0), 1)
                newImage = cv2.putText(newImage, '1', (top_x+2, top_y+8), cv2.FONT_HERSHEY_PLAIN , 0.7, (255, 0, 0), 1)
        
    return newImage

#mostra imagem
cv2.imshow('image', boxing(original_img, results))
cv2.waitKey(0)
cv2.destroyAllWindows()

