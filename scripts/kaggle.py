# Download do dataset do Kaggle
# Após o download, mover a pasta /garbage-dataset/ para o diretório root do projeto

import kagglehub

path = kagglehub.dataset_download("sumn2u/garbage-classification-v2")

print("Path to dataset files:", path)
