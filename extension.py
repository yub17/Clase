class Municipio:
    #se declaran atributos de la clase
    nom = ""
    cve = ""
    __pobTot = 0 #doble guión bajo son atributos privados
    _alt = 0 # un guión bajo son atributos 
    sup = 0
    #definir constructor
    def __init__(self, nombre, clave, pobTotal, altitud, superficie):
        self.nom = nombre
        self.cve = clave
        self.__pobTot = pobTotal
        self._alt = altitud
        self.sup = superficie
    #A todo atributo que sea privado o protegido se le deberá asignar un método GET y SET
    def getNom(self):
        return self.nom
    def setNom(self, nombre):
        try:
            nom = str(nombre)
            self.nom = nombre
        except:
            print("Introduce un Municipio")

    def getcve(self):
        return self.cve
    def setcve(self, clave):
        try:
            cve = str(clave)
            self.cve = clave
        except:
            print("Introduce la clave de un municipio")
            
    def getpobTot(self):
        return self.__pobTot
    def setpobTot(self, pobTotal):
        try:
            __pobTot = str(pobTotal)
            self.__pobTot = pobTotal
        except:
            print("Introduce la poblacon total de un municipio")
            
    def getalt(self):
        return self._alt
    def setalt(self, altitud):
        try:
            _alt = str(altitud)
            self._alt = altitud
        except:
            print("Introduce la altura de un municipio")
            
    def getsup(self):
        return self.sup
    def setsup(self, superficie):
        try:
            sup = str(superficie)
            self.sup = superficie
        except:
            print("Introduce la superficie de un municipio")
    def info(self):
        print("El nombre del municipio es ", self.nom, " y su clave de inegi es ", self.cve, " y tiene una superficie de ", self.sup)
        
    def supKm(self, valor):
        if valor > 10000:
            print("Es un municipio grande ")
        else:
            print("Es un municipio pequeño ")
            
            

Mun = Municipio("Toluca", "106", 783682 , 4700, 876322)
print(Mun.getNom())
Mun.setNom("Metepec")
Mun.setcve("103")
print(Mun.getNom())
print(Mun.info())
print()

class colonia(Municipio):
    ah = 0
    #Definición de un constructor
    def __init__(self, areaH, nombre, clave, pobTotal, altitud, superficie):
        super().__init__(nombre, clave, pobTotal, altitud, superficie)
        self.ah = areaH
    #Métodos de la clase GET y SET
    def getAH(self):
        return self.ah
    def setAH(self, ah):
        self.ah = ah
    #Métodos alternativos
    def infoAH(self, value):
        self.ah = self.ah + value
        self.info()
        print (self.nom, "cuenta con ", self.ah, " áreas homogéneas") # self.nom es un atributo de la clase Municipio
col = colonia(5, "Toluca", "106", 783682 , 4700, 876322)
print (col.infoAH(3))
print (col.getNom()) #La clase Colonia no tiene el método getNom() pero es accesible mediante la herencia de la clase Municipio


class extension(Municipio, colonia):
    x1 = 0
    x2 = 0
    y1 = 0
    x2 = 0
    NomMun = ""
    ancho = 0
    largo = 0
    area = 0
    
    def __init__(self, x1, x2, y1, y2, NomMun, ancho, largo, area):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.NomMun = nombre
        self.ancho = ancho
        self.largo = largo
        self.area = area
    def getx1(self):
        return self.x1
    def setx1(self, x1):
        try:
            __x1 = (x1)
            self.__x1 = x1
        except:
            print("Introduce la coordenada de x1")
            
    def getx2(self):
        return self.x2
    def setx2(self, x2):
        try:
            __x2 = (x2)
            self.__x2 = x2
        except:
            print("Introduce la coordenada de x2")
    
    def gety1(self):
        return self.y1
    def sety1(self, y1):
        try:
            __y1 = (y1)
            self.__y1 = y1
        except:
            print("Introduce la coordenada de y1")
            
    def gety2(self):
        return self.y2
    def sety2(self, y2):
        try:
            __y2 = (y2)
            self.__y2 = y2
        except:
            print("Introduce la coordenada y2")
        
    def getancho(self):
        return self.ancho
    def setancho(self, ancho):
        try:
            ancho = (ancho)
            self.ancho = ancho
        except:
            print("Introduce el ancho del municipio")
    
    def getlargo(self):
        return self.largo
    def setlargo(self, largo):
        try:
            largo = (largo)
            self.largo = largo
        except:
            print("Introduce el largo del municipio")
        
    def getarea(self):
        return self.area
    def setarea(self, area):
        try:
            area = (area)
            self.area = area
        except:
            print("Introduce el area del municipio")
            
ext = extension (2243872.5560, 542329.6763, 2031290.0410, 330117.8247, "Tepotzotlan")
area = ar (ancho * largo)

NomMun = input()
print ("Introduce el municipio", NomMun)
x1 = input()
print("La coordenada x1 es: ", x1)
x2 = input()
print("La coordenada x2 es: ", x2)
y1 = input()
print("La coordenada y1 es: ", y1)
y2 = input()
print("La coordenada y2 es: ", x2)


                
            

            
