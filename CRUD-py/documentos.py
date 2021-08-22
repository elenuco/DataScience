import pymongo
from colecciones import colecciones
def menu():
	print("Bienvenido  al registro d centros escolares")
	while(True):
		print("""
			1) Registrar un nuevo Centro Escolar
        2) Visualizar los Centros Escolares registrados
        3) Actualizar un registro de un Centro Escolar
        4) Eliminar registro de un Centro Escolar
        5) Salir del sistema
        """)
        option=input()
        if option=="1"
           Id=int(input("Digite el codigo del centro escolar(solo escriba numeros)"))
           Nombre=input("Ingrese el nombre del centro escolar")
           Departamento=input("Ingrese el departamento al que pertenece")
           Muncipio=input("Ingrese el Muncipioal que esta inscrito")
           insertarRegistro=insrtarColeccione(colecciones)
           print("Registro realizado con exito")
        elif option=="2":
        	verCE()
        elif option=="3":
        	Id = int(input("Ingrese el codigo del centro escolar a actualizar"))
        	Nombre= input("Ingrese el nombre a actualizar")
        	Departamento= input("Nombre SEL DEPARTAMENTO")
        	Muncipio=input("Ingrese el minicio a a actualizar")
        	registroActualizado=actualizar_colecciones(Id, Nombre, Departamento, Muncipio)
        	print("Registro actualizado:", registroActualizado)
        elif option=="4":
        	Id = int(input("Digite el codigo del centro escolar a suprimir"))
        	registroEliminado=borrarCE(Id)
        elif option=="5":
        	break
        else:
        	print("Opcion no valida, vuelva a intentar")
#Conexion con Mongo 
def get_db():
	try:
		client = pymongo.MongoClient("mongodb+srv://Ellen:mxiyd4msRmmEIG26@evaluacion01.1gzai.mongodb.net/tests")
		db=client["Evaluacion01"]
		colec=db["CE"]
	except ConnectionError:
		print("Error de conexion")
	return db 
#opcion 1
def VisualizarCE():
	db=get_db()
	escuela=db.CE.find().limit(10)
	print("{:<30}{:<20} {:30} {:<20}".fromat(escuela["Id"], escuela["Nombre"],
		escuela["Departamento"], escuela["Muncipio"]))
	#opcion 2
def insertarCE(CE):
		db=get_db()
		resultado=db.CE.insert_one(CE.toCollection())
		return resultado.inserted_id
	#opcion 3 
def actualizarCE(Id, Nombre, Departamento, Muncipio):
	db=get_db()
	resultado=db.CE.update_one({
		"Id":int(Id)
		},
		{
		"$set":{"Nombre":Nombre, "Departamento": Departamento, "Municipio":Municipio}
		})
		    return resultado.modified_count
		    #opcion 4
def borrarCE(Id):
	db=get_db()
	resultado=db.CE.deleted_count
##main
menu()