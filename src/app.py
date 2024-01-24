from flask import Flask, request, jsonify

app = Flask(__name__)

# Ponto de extremidade para previsões
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Faça a previsão usando o modelo treinado
    input_data = data['input_data']
    prediction = model.predict([[input_data]])

    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
