#importar rede
from darkflow.net.build import TFNet
#opções do treino
options = {"model": "cfg/yolo-new.cfg", 
           "load": -1,
           "batch": 2,
           "epoch": 10000,
           "save": 9300,
           "gpu": 1.0,
           "train": True,
           "annotation": "./annotations/",
           "dataset": "./images/"}
#configurando a rede com as opções
tfnet = TFNet(options)
#treino
tfnet.train()