#importar rede
from darkflow.net.build import TFNet
#opções do treino
options = {"model": "cfg/yolo-new.cfg", 
           "load": "bin/yolo.weights",
           "batch": 2,
           "epoch": 500,
           "gpu": 1.0,
           "train": True,
           "annotation": "./annotations/",
           "dataset": "./images/"}
#configurando a rede com as opções
tfnet = TFNet(options)
#treino
tfnet.train()