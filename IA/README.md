Utiliza o algoritmo Yolo com Tensorflow, Keras e Opencv para detecção de vagens de soja em imagens.

Requisitos: 
Python 3.6.8

Para utilzar com GPU Nvidia:
CUDA Development kit 10.0
Cudnn 7.6.5.32

pip:
protobuf==3.11.0
tensorflow==1.15      (apenas para CPU)
tensorflow-gpu==1.15  (versao com suporte a GPU)
pytest
requests
opencv-python
numpy
Cython
codecov
pytest-cov

# Compilar:
```sh
py setup.py build_ext --inplace
```

# Treinar:
```sh
py treino.py
```

# Executar IA treinada:
```sh
py imagem.py
```

Para testar em uma imagem, coloque ela na pasta sample_img e no arquivo imagem.py em 'original_img = cv2.imread("sample_img/teste5.jpg")' mude o "teste5.jpg" para o nome da imagem a ser testada.
