

from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('jscode', __name__, url_prefix='/jscode')

@bp.route('/', methods=('GET',"POST"))
def add():
    if request.method == 'POST':
        a_val = request.form.get('a')
        b_val = request.form.get('b')

        operacion = request.form.get('operacion')
        if not a_val or not b_val:
            return jsonify(error="Faltan ingresar valores numéricos"), 400
        
        a = float(a_val)
        b = float(b_val)

        if operacion == "suma":
            resultado = a + b
        elif operacion == "resta":
            resultado = a - b
        elif operacion == "multiplicacion":
            resultado = a * b
        elif operacion == "division":
            if b == 0:
                return jsonify(error="Error: División por cero"), 400
            resultado = a / b
        else:
            return jsonify(error="Operación no válida"), 400
        
        if resultado.is_integer():
            resultado = int(resultado)

        return jsonify(result=resultado)
    return render_template('fetch.html')