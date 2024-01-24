from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Suponha que você tenha um DataFrame chamado 'data'
X = data[['X']]
y = data['y']

# Divida os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crie e treine o modelo
model = LinearRegression()
model.fit(X_train, y_train)
