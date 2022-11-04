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

def IAprocess(imageStr,test):
    image= ""
    samples = list()
    idTemp = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    if test == False:
        #Converte a string em uma imagem 
        imageStr = imageStr.encode('utf-8')
        decoded_data=base64.b64decode((imageStr))
    
        img_file = open(f'../IA/out/imageOUT-{idTemp}.jpg', 'wb')
        img_file.write(decoded_data)
        img_file.close() 
        image = f'../IA/out/imageOUT-{idTemp}.jpg'

    elif test == True and imageStr == 'test':
        for _, _, arquivo in os.walk('../IA/sample_img'):
         samples = arquivo
        image = '../IA/sample_img/'+samples[7]
    else:
        print(imageStr)
        image = '../IA/sample_img/' + imageStr

    #opções para carregar o modelo
    options = {"model": "../IA/cfg/yolo-new.cfg",
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
                if results[y]['confidence'] * 100 >= 40:
                    soyTotal = soyTotal + 1
                    confi = confi + results[y]['confidence'] * 100
                    if diferencax >= 17 or diferencay >= 17:
                        beans += 3
                    elif diferencax < 17 and diferencax >= 10 and diferencay < 17 and diferencay >= 10:
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
    cv2.imwrite(f"../IA/out/ImageOUT2-{idTemp2}.jpg", boxing(original_img, results))
    with open(f"../IA/out/ImageOUT2-{idTemp2}.jpg", "rb") as image2string: 
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
    # with open(f"../IA/out/{date}.json", "w") as outfile: 
    #     outfile.write(json_info) 

    #mostra imagem (opcional para testes, pode ser comentado)
    # cv2.imshow('image',boxing(original_img, results))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #Exclui as imagens geradas (comentar para deixa-las salvas)
    if os.path.isfile(f"../IA/out/ImageOUT2-{idTemp2}.jpg"):
        os.remove(f"../IA/out/ImageOUT2-{idTemp2}.jpg")
    if os.path.isfile(f"../IA/out/imageOUT-{idTemp}.jpg"):
        os.remove(f"../IA/out/imageOUT-{idTemp}.jpg")
    
    #retorna o JSON para o endpoint
    return dictionary

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

        #se for maior que 40% mostra
        if confidence > 40:
            if diferencax >= 17 or diferencay >= 17:
                newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (0, 0, 255), 1)
                newImage = cv2.putText(newImage, '3', (top_x+2, top_y+8), cv2.FONT_HERSHEY_PLAIN , 0.7, (0, 0, 255), 1)
            elif diferencax < 17 and diferencax >= 10 and diferencay < 17 and diferencay >= 10:
                newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (0, 255, 255), 1)
                newImage = cv2.putText(newImage, '2', (top_x+2, top_y+8), cv2.FONT_HERSHEY_PLAIN , 0.7, (0, 255, 255), 1)
            else:
                newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255, 0, 0), 1)
                newImage = cv2.putText(newImage, '1', (top_x+2, top_y+8), cv2.FONT_HERSHEY_PLAIN , 0.7, (255, 0, 0), 1)

    return newImage

#Gerar dados de 28 imagens de teste para medir a precisão do modelo
def IATest():
    with open('../IA/sampleInfos.json') as json_file:
        data = json.load(json_file)

    samples = []
    for _, _, arquivo in os.walk('../IA/sample_img'):
        samples = arquivo

    graos = []
    vagens = []
    confiancaMedia = []
    detects = {}

    for i in range(0, len(samples)):
        img = IAprocess(samples[i], True)
        graos.append(img['graos'])
        vagens.append(img['vagens'])
        confiancaMedia.append(img['confianca'])

    graosReal = 0
    vagensReal = 0

    graosTotal = 0
    vagensTotal = 0
    confiancaMediaTotal = 0

    for i in range(0, len(data["n_graos"])):
        graosTotal += graos[i]
        vagensTotal += vagens[i]
        confiancaMediaTotal += confiancaMedia[i]

        graosReal += data["n_graos"][i]
        vagensReal += data["n_vagens"][i]

        detects[samples[i]] = {'graosReais': data["n_graos"][i], 'vagensReais': data["n_vagens"][i], 'graosDetectados': graos[i], 'vagensDetectadas': vagens[i], 'confiancaMedia': confiancaMedia[i]}

    print('Graos: ', graosTotal, 'Vagens: ', vagensTotal, 'VagensReal: ', vagensReal, 'GraosReal: ', graosReal)
    PorcentagemVagens = (vagensTotal * 100) / vagensReal
    PorcentagemGraos = (graosTotal * 100) / graosReal
    PorcentagemConfianca = confiancaMediaTotal / len(samples)

    for _, _, arquivo in os.walk('../IA/ckpt'):
        id = arquivo[4].split('.')[0]

    dados = {
        "model": id,
        "PorcentagemVagens": PorcentagemVagens,
        "PorcentagemGraos": PorcentagemGraos,
        "PorcentagemConfianca": PorcentagemConfianca,
        "Dados reais x Detectados": detects
    }
    json_info = json.dumps(dados, indent = 4) 
    with open(f"../IA/out/sampleResults/{id}.json", "w") as outfile: 
     outfile.write(json_info) 
        

#Chamada do metodo para testar leitura do json (apenas para testes)
# with open('./out/2022-10-10-23-35.json', 'r') as openfile: 
#     json_object = json.load(openfile) 
# imagestr = json_object['image']
# IAprocess(imagestr)

#Chamada do metodo para testar sem leitura do json (apenas para testes)
#IAprocess('test')


