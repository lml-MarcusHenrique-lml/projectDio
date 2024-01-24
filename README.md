# projectDio
Repositorio criado para armazenar e entregar projetos relacionado ao curso da  dio

# Projeto de Análise de Dados

Este é um projeto de análise de dados usando regressão linear.

## Objetivo

O objetivo deste projeto é criar um modelo de regressão linear para prever Y com base na variável X.

## Configuração do Ambiente

Certifique-se de ter Python e as bibliotecas necessárias instaladas. Você pode instalar as dependências usando o seguinte comando:

```bash
pip install -r requirements.txt

Clone deste repositorio:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Baixe o conjunto de dados dados.csv e coloque-o na raiz do projeto.

Execute o script Python:
python projeto.py

O script treinará um modelo de regressão linear e imprimirá o erro quadrático médio (MSE).

Detalhes do Código
1. Importar Bibliotecas

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

Avaliar Desempenho

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

Esta seção calcula o erro quadrático médio (MSE) para avaliar o desempenho do modelo.


Lembre-se de substituir "seu-usuario" e "seu-repositorio" pelos seus detalhes específicos. Além disso, você pode adicionar mais detalhes conforme necessário para explicar seu projeto da melhor maneira possível.
