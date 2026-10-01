inventario = [
	{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"},
	{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
	{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
	{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"}
]
print("###################")
#Imprimir todos los hostnames
print("Inventario:")
for name in inventario:
	print(name["hostname"])
print("\n###################\n")
#Imprimir todas las ip
print ("IP's de los host:")
for ip in inventario:
	print(ip["ip"])
print("\n###################\n")
#Imprimir todos los que esten en down
print("Inventario en status 'down':")
for d in inventario:
	if d["status"] == "down":
		print(d["hostname"])
print("###################\n")