print ("programacion poo")
# definicion de clase
class perro:
    #funciones dentro de la clase
    def morder(self):
        print("el perro me mordio")
    def Datos_perro(self,nombre, edad):
        print(f"Nombre : {nombre} edad: {edad}")


# zona de creacion de objetos
pitbull= perro()


#zona de objetos 
pitbull.Datos_perro("body",4)
pitbull.morder()