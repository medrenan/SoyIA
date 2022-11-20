import json
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

resultJson = json.load(open("out/sampleResults/data/Model-364580-Results.json"))
realDet=(resultJson["Dados reais x Detectados"])
i=0
for i in range(30):
    search="Imagem: "
    search+=str(i)
    imagemN=(realDet[search])
    print("JSON: ",imagemN)
    
    array = [[imagemN['graosReais'],imagemN['graosDetectados']],[imagemN['vagensReais'],imagemN['vagensDetectadas']]]
    print(array)
    df_cm = pd.DataFrame(array, index = ['Vagens','Grãos'],columns = ['Reais','Detectados'])
    plt.figure(figsize = (2,2))
    plt.ticklabel_format(style='plain', useOffset=False)
    sn.heatmap(df_cm, annot=True, fmt='g')
    plt.show()