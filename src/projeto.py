import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Suponha que você já tenha um DataFrame chamado 'data'
# Substitua 'seu_arquivo.csv' pelo nome real do seu arquivo
arquivo_csv = 'dados.csv'
data = pd.read_csv(arquivo_csv)

# Divida os dados em conjuntos de treino e teste
X = data[['X']]
y = data['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crie e treine o modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Faça previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avalie o desempenho usando o erro quadrático médio (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
