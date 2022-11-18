import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix

resultJson = json.load(open("out/sampleResults/data/Model-364580-Results.json"))
realDet=(resultJson["Dados reais x Detectados"])
i=0
for i in range(30):
    search="Imagem: "
    search+=str(i)
    imagemN=(realDet[search])
    
    realGrao = pd.Series(imagemN["graosReais"], name='Graos Reais')
    detecGrao = pd.Series(imagemN["graosDetectados"], name='Graos Detectados')
    realVagem = pd.Series(imagemN["graosReais"], name='Vagens Reais')
    detecVagem = pd.Series(imagemN["graosDetectados"], name='Vagens Detectadas')

    plot_confusion_matrix(realGrao, detecGrao, realVagem,detecVagem) 