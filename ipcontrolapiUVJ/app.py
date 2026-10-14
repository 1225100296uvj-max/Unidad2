"""
IP-Control: API REST con Flask para el inventario de direccionamiento IP.
Actividad 2 - Desafío B

Ejecutar:  python app.py
Servidor:  http://127.0.0.1:7777
"""
from flask import Flask, jsonify

app = Flask(__name__)

direcciones = [
    {"id": 1, "direccion_ip": "192.168.10.1",   "dispositivo": "Router-Principal",  "subred": "192.168.10.0", "tipo_asignacion": "estática", "estado": "asignada"},
    {"id": 2, "direccion_ip": "192.168.10.10",  "dispositivo": "Servidor-Archivos", "subred": "192.168.10.0", "tipo_asignacion": "estática", "estado": "asignada"},
    {"id": 3, "direccion_ip": "192.168.10.20",  "dispositivo": "PC-Laboratorio-01", "subred": "192.168.10.0", "tipo_asignacion": "DHCP",     "estado": "asignada"},
    {"id": 4, "direccion_ip": "192.168.10.21",  "dispositivo": "Sin asignar",       "subred": "192.168.10.0", "tipo_asignacion": "DHCP",     "estado": "disponible"},
    {"id": 5, "direccion_ip": "192.168.20.1",   "dispositivo": "Switch-Capa3",      "subred": "192.168.20.0", "tipo_asignacion": "estática", "estado": "asignada"},
    {"id": 6, "direccion_ip": "192.168.20.15",  "dispositivo": "Impresora-Red",     "subred": "192.168.20.0", "tipo_asignacion": "estática", "estado": "asignada"},
    {"id": 7, "direccion_ip": "192.168.20.50",  "dispositivo": "Sin asignar",       "subred": "192.168.20.0", "tipo_asignacion": "DHCP",     "estado": "disponible"},
    {"id": 8, "direccion_ip": "10.0.0.5",       "dispositivo": "Access-Point-01",   "subred": "10.0.0.0",     "tipo_asignacion": "estática", "estado": "asignada"},
    {"id": 9, "direccion_ip": "10.0.0.100",     "dispositivo": "Sin asignar",       "subred": "10.0.0.0",     "tipo_asignacion": "DHCP",     "estado": "disponible"},
]

@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensaje": "API IP-Control funcionando correctamente",
        "version": "1.0",
        "endpoints": [
            "/direcciones",
            "/direcciones/<id>",
            "/direcciones/estado/<estado>",
            "/direcciones/subred/<subred>",
        ],
    })

@app.route("/direcciones", methods=["GET"])
def listar_direcciones():
    return jsonify({"total": len(direcciones), "direcciones": direcciones})

@app.route("/direcciones/<int:id_registro>", methods=["GET"])
def obtener_direccion(id_registro):
    for registro in direcciones:
        if registro["id"] == id_registro:
            return jsonify(registro)          
    return jsonify({
        "error": "Recurso no encontrado",
        "mensaje": f"No existe un registro con id {id_registro}",
        "codigo": 404,
    }), 404
@app.route("/direcciones/estado/<estado>", methods=["GET"])
def filtrar_por_estado(estado):
    resultado = [d for d in direcciones if d["estado"].lower() == estado.lower()]
    return jsonify({"estado": estado, "total": len(resultado), "direcciones": resultado})

@app.route("/direcciones/subred/<subred>", methods=["GET"])
def filtrar_por_subred(subred):
    resultado = [d for d in direcciones if d["subred"] == subred]
    return jsonify({"subred": subred, "total": len(resultado), "direcciones": resultado})

@app.errorhandler(404)
def no_encontrado(_error):
    return jsonify({
        "error": "Recurso no encontrado",
        "mensaje": "La ruta solicitada no existe en esta API",
        "codigo": 404,
    }), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7777, debug=True)