from flask import Flask, jsonify
from calculo_inicial import Calculo

app = Flask(__name__)

@app.route('/')
def api():
    calc = Calculo()
    return jsonify({
        "status": "API rodando",
        "teste_soma": str(calc.add(10, 5))
    })

if __name__ == "__main__":
    app.run(debug=True)