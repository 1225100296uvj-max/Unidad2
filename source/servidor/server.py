'''
Mi primer Servidor con Flask y Python
Autor: Uriel Villalobos Juárez
Fecha: 30 de Septiembre de 2026
'''
from flask import Flask
app = Flask(__name__)

inventario = [
		{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"},
		{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
		{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
		{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"}
		]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<nombre>")
def saludo(nombre):
	return f"Hola {nombre}"

@app.route("/dispositivo/<device>")
def buscar_dispositivo(device):
	for i in inventario:
		if device == i["hostname"]:
			return f"Informacion de dispositivo '{device}':\n{i}"
	return f"Dispositivo '{device}' no encontrado"

if __name__=="__main__":
	app.run(debug=True, port=5066)
