from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados simulados para pintores
pintores = [
    {'id': 1, 'nome': 'Pintor 1', 'avaliacoes': [5, 4, 4]},
    {'id': 2, 'nome': 'Pintor 2', 'avaliacoes': [3, 3, 4]},
]

def calcular_media(avaliacoes):
    if avaliacoes:
        return sum(avaliacoes) / len(avaliacoes)
    return 0

@app.route('/avaliar', methods=['POST'])
def avaliar():
    data = request.json
    pintor_id = data.get('pintor_id')
    avaliacao = data.get('avaliacao')

    for pintor in pintores:
        if pintor['id'] == pintor_id:
            pintor['avaliacoes'].append(avaliacao)
            media = calcular_media(pintor['avaliacoes'])
            return jsonify({'message': 'Avaliação recebida!', 'media': media})

    return jsonify({'message': 'Pintor não encontrado!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
