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
print(Mun.getNom())
print(Mun.info())
#print(Mun.getcve())
#print(Mun.getpobTot())
#print(Mun.getalt())
#print(Mun.getsup())
    