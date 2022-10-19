import numpy as np
#importa biblioteca da rede
from darkflow.net.build import TFNet
#importar opencv
import cv2
import json
from datetime import datetime
import base64 
import os
from random import randint

import sys
# sys.path.append('/scripts/processamento-imagem')

# from scripts.imageProcessingScripts import preProcessing

def IAprocess(imageStr):
    image= ""
    idTemp = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    if imageStr != 'test':
        #Converte a string em uma imagem 
        imageStr = imageStr.encode('utf-8')
        decoded_data=base64.b64decode((imageStr))
    
        img_file = open(f'./out/imageOUT-{idTemp}.jpg', 'wb')
        img_file.write(decoded_data)
        img_file.close() 
        image = f'./out/imageOUT-{idTemp}.jpg'
    else:
        image = './sample_img/10.jpg'

    #opções para carregar o modelo
    options = {"model": "cfg/yolo-new.cfg",
            "load": -1,
            "gpu": 1.0}
    #configura a rede com as opções
    tfnet2 = TFNet(options)
    #carrega a rede
    tfnet2.load_from_ckpt()

    #Le a imagem  
    #original_img = preProcessing(image)
    original_img = cv2.imread(image)

    #Reconhece objetos na imagem
    results = tfnet2.return_predict(original_img)
    confi = 0
    soyTotal = 0
    beans = 0
    mediaConfianca = 0
    if results:
            print("\nResults---------------------------------------------------")
            #Para cada objeto reconhecido printa o nome e com qual confiança
            for y in range(0, len(results)):
                print("Label:%s\tConfidence:%f"%(results[y]['label'], results[y]['confidence']* 100))
                diferencax = results[y]['bottomright']['x'] - results[y]['topleft']['x']
                diferencay = results[y]['bottomright']['y'] - results[y]['topleft']['y']
                if results[y]['confidence'] * 100 >= 25:
                    soyTotal = soyTotal + 1
                    confi = confi + results[y]['confidence'] * 100
                    if diferencax >= 15 or diferencay >= 26:
                        beans += 3
                    elif diferencax < 15 and diferencax >= 8 and diferencay >= 18 or diferencay < 26 and diferencax >= 8 and diferencay >= 18:
                        beans += 2
                    else:
                        beans += 1
            
            if soyTotal > 0:
                mediaConfianca = confi / soyTotal

            print('Media de confiança: ', mediaConfianca)
            print('Total de soja: ', beans)
            print('Total de vagens: ', soyTotal)

    
    #converte a imagem de saida em JSON
    imageString = "" 
    idTemp2 = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    cv2.imwrite(f"./out/ImageOUT2-{idTemp2}.jpg", boxing(original_img, results))
    with open(f"./out/ImageOUT2-{idTemp2}.jpg", "rb") as image2string: 
        imageString = str(base64.b64encode(image2string.read()), 'utf-8')

    #cria um JSON com a imagem e os resultados
    date = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    dictionary ={ 
        "imageName": image,
        "confianca" : mediaConfianca, 
        "graos" : beans, 
        "vagens" : soyTotal, 
        "image" : imageString
    } 
    #JSON com os resultados
    json_info = json.dumps(dictionary, indent = 5) 

    #salva o JSON (opcional para testes, pode ser comentado)
    with open(f"./out/{date}.json", "w") as outfile: 
        outfile.write(json_info) 

    #mostra imagem (opcional para testes, pode ser comentado)
    cv2.imshow('image',boxing(original_img, results))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if os.path.isfile(f"./out/ImageOUT2-{idTemp2}.jpg"):
        os.remove(f"./out/ImageOUT2-{idTemp2}.jpg")
    if os.path.isfile(f"./out/imageOUT-{idTemp}.jpg"):
        os.remove(f"./out/imageOUT-{idTemp}.jpg")
    
    #retorna o JSON para o endpoint
    return json_info

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
        if confidence > 25:
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


#Chamada do metodo para testar leitura do json (apenas para testes)
# with open('./out/2022-10-10-23-35.json', 'r') as openfile: 
#     json_object = json.load(openfile) 
# imagestr = json_object['image']
# IAprocess(imagestr)

#Chamada do metodo para testar sem leitura do json (apenas para testes)
IAprocess('test')


