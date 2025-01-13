from flask import Flask, jsonify
import json

app = Flask(__name__)

# Função para carregar os dados do arquivo JSON
def load_data():
    with open('data/moedas_24hr_info.json', 'r') as file:
        return json.load(file)

# Rota /api/cryptos para retornar todos os dados das criptomoedas
@app.route('/api/cryptos', methods=['GET'])
def get_cryptos():
    dados = load_data()  # Carrega os dados do arquivo JSON
    return jsonify(dados)  # Retorna os dados no formato JSON

if __name__ == '__main__':
    app.run(debug=True)
