from flask import Flask, jsonify
from flask_cors import CORS
from pybcv import PyBCV  # Importación directa y limpia gracias a Pip
import os

app = Flask(__name__)
CORS(app)  # Permite que tu HTML o Flutter consulten la API sin bloqueos

@app.route('/api', methods=['GET'])
def obtener_tasas():
    try:
        # Inicializa la librería oficial instalada por Pip
        bcv = PyBCV()
        
        # Extracción de tasas
        dolar_bcv = bcv.get_rate(currency_code='USD')
        euro_bcv = bcv.get_rate(currency_code='EUR')
        
        return jsonify({
            "status": "success",
            "dolar": dolar_bcv,
            "euro": euro_bcv
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Fallo en el servidor con pybcv oficial: {str(e)}"
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)