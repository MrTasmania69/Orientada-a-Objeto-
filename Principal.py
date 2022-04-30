from Electrodomesticos import Electrodomesticos
from os import system
import os

class Principal:
    __op = 0
    __cod = 0 
    __nom = ""
    __mar = 0
    __pre = 0
    __fab = ""
    __ele = Electrodomesticos()
    __lista = []
    
    def __init__(self):
        pass

    def menu(self):
        try:
            system("cls")
            print("--- MENU ---")
            print("1. Agregar.")
            print("2. Listar Todos.")
            print("3. Listar Solo Fensa.")
            print("4. Listar Solo Mademsa.")
            print("5. Estadistica.")
            print("6. Salir Del Programa.")
            op = int(input("Introduzca Una Opcion : "))
            if op ==1:
                self.agregar()
            elif op == 2:
                self.listarTodos()
            elif op == 3:
                self.listarSoloFensa()
            elif op == 4:
                self.listarSoloMademsa() 
            elif op == 5:
                self.estadistica()
            elif op == 6:
                self.salir() 
                os._exit(1) 
            else:
                self.errorOpcion()                     
        except:
            print("\n--- Error Al Intentar Ejecutar La Opcion!!!---")
            system("pause")
            self.menu()
        
    
    def agregar(self):
        while True:
            try:
                system("cls")
                cod = int(input("Digite El Codigo Del Producto ("+str(len(self.__lista)+1)+") : "))
                if cod<1 or cod>99999:
                    print("\n--- El Codigo Debe Tener Hasta 5 Digitos!!! ---")
                    system("pause")
                else:
                    res = False 
                    for x in self.__lista:
                        if cod==x.getCodigo():
                            res = True
                    
                    if res==True:
                        print("\n--- El Codigo ",cod," Ya Existe!! ---")
                        system("pause")  
                    else:
                        break            
            except:
                print("\n--- Error Al Intentar Ejecutar La Opcion!!!---")
                system("pause")
        
        while True:
            try:
                system("cls")
                nom = input("Digite El Nombre Del Producto ("+str(len(self.__lista)+1)+") : ")
                if len(nom.strip())<1 or len(nom.strip())>20:
                    print("\n--- El Nombre Debe Tener Entre 1 y 20 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre!! ---")
                system("pause")
        
        while True:
            try:
                system("cls")
                print("1. Fensa.")
                print("2. Mademsa.")
                mar = int(input("Digite La Marca Del Producto ("+str(len(self.__lista)+1)+") : "))
                if mar!=1 and mar!=2:
                    print("\n--- Error De Opcion De Marca!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar Almacenar La Marca!! ---")
                system("pause")
            
        while True:
            try:
                system("cls")
                pre = int(input("Digite El Precio Del Producto ("+str(len(self.__lista)+1)+") : "))
                if pre<10000 or pre>500000:
                    print("\n--- El Precio Debe Estar Entre $10000 y $500000!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Precio!! ---")
                system("pause")
            
        while True:
            try:
                system("cls")
                fab = input("Digite Nombre Del Fabricante ("+str(len(self.__lista)+1)+") : ")
                if len(fab.strip())<1 or len(fab.strip())>30:
                    print("\n--- El Nombre Debe Tener Entre 1 y 30 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre!! ---")
                system("pause")
        
        self.__ele = Electrodomesticos()
        self.__ele.setCodigo(cod)
        self.__ele.setNombre(nom)
        self.__ele.setMarca(mar)
        self.__ele.setPrecio(pre)
        self.__ele.setFabricante(fab)
        self.__lista.append(self.__ele)
        self.menu() 
                 
    def listarTodos(self):
        if len(self.__lista) == 0:
            system("cls")
            print("----------------------------------------------------")
            print("--- No Hay Registros De Productos Para Listar!!! ---")
            print("----------------------------------------------------")
            system("pause")
            self.menu()
        else:
            system("cls")
            print("---------------")
            print("--- Listado ---")
            print("---------------")   
            for x in self.__lista:
                print("Codigo : ",x.getCodigo())
                print("Nombre : ",x.getNombre())
                if x.getMarca()==1:
                    print("Marca  :  Fensa")
                elif x.getMarca()==2:
                    print("Marca  :  Mademsa")    
                print("Precio :  $",x.getPrecio())
                print("Fabricante : ",x.getFabricante(), end="\n\n")
            system("pause")
            self.menu()     
    
    def listarSoloFensa(self):
        if len(self.__lista) == 0:
           system("cls")
           print("----------------------------------------------------")
           print("--- No Hay Registros De Productos Para Solo Fensa!!! ---")
           print("----------------------------------------------------")
           system("pause")
           self.menu()
        else:             
            try:
                system("cls")
                cod = int(input("Digite El Codigo Del Producto Deseado : "))
                res = False
                for x in self.__lista:
                    if cod==x.getCodigo():
                        res = True
                        system("cls")
                        print("---------------")
                        print("--- Producto Encontrado ---")
                        print("---------------") 
                        print("Codigo : ",x.getCodigo())
                        print("Nombre : ",x.getNombre())
                        if x.getMarca()==1:
                            print("Marca  :  Fensa")
                        elif x.getMarca()==2:
                            print("Marca  :  Mademsa")       
                        print("Precio :  $",x.getPrecio())
                        print("Fabricante : ",x.getFabricante(), end="\n\n")
                        system("pause")
                        self.menu()
                    
                    if res== False:
                        print("--- El Codigo Buscado No Existe!!! ---")
                    system("pause")
                    self.menu()       
            except:
                    print("\n--- Error Al Intentar Almacenar El Codigo Buscado!! ---")
                    system("pause")
                    self.menu()
                     
    
    def listarSoloMademsa(self):
            if len(self.__lista) == 0:
                system("cls")
                print("----------------------------------------------------")
                print("--- No Hay Registros De Productos Para Solo Fensa!!! ---")
                print("----------------------------------------------------")
                system("pause")
                self.menu()
            else:             
                 try:
                    system("cls")
                    cod = int(input("Digite El Codigo Del Producto Deseado : "))
                    res = False
                    for x in self.__lista:
                        if cod==x.getCodigo():
                            res = True
                            system("cls")
                            print("---------------")
                            print("--- Producto Encontrado ---")
                            print("---------------") 
                            print("Codigo : ",x.getCodigo())
                            print("Nombre : ",x.getNombre())
                            if x.getMarca()==2:
                                print("Marca  :  Fensa")
                            elif x.getMarca()==1:
                                print("Marca  :  Mademsa")        
                            print("Precio :  $",x.getPrecio())
                            print("Fabricante : ",x.getFabricante(), end="\n\n")
                            system("pause")
                            self.menu()
                    
                        if res== False:
                         print("--- El Codigo Buscado6 No Existe!!! ---")
                        system("pause")
                        self.menu()       
                 except:
                     print("\n--- Error Al Intentar Almacenar El Codigo Buscado!! ---")
                     system("pause")
                     self.menu()
    
    def estadistica(self):
        if len(self.__lista) == 0:
            system("cls")
            print("------------------------------------------------------")
            print("--- No Hay Registros Para Generar La Estadistica!! ---")
            print("------------------------------------------------------")
            system("pause")
            self.menu()
        else:
            cfe=0; cma=0
            sfe=0; sma=0
            pfe=0; pma=0
            for x in self.__lista:
                if x.getMarca()==1:
                    cfe += 1
                    sfe += x.getPrecio()
                    pfe += sfe / cfe
                elif x.getMarca()==2:
                    cma += 1
                    sma += x.getPrecio() 
                    pma += sma / cma
            system("cls")
            print("-------------------")
            print("--- EStadistica ---")
            print("-------------------")
            print("Cantidad Segun Marcas")
            print("   Cantidad De Productos Fensa            :  ",cfe)
            print("   Cantidad De Productos Mademsa          :  ",cma)
            print("Suma Segun Marcas")
            print("   Suma. $ De Productos Fensa          : $",sfe)
            print("   Suma. $ De Productos Mademsa        : $",sma)
            print("Promedio Segun Marcas")
            print("   Promedio. $ De Productos Fensa          : $",sfe/cfe)
            print("   Promedio. $ De Productos Mademsa        : $",sma/cma)
            system("pause")
            self.menu()        
    
    def salir(self):
        try:
                system("cls")
                print ("---------------------")
                print ("--- ¿Desea Salir? ---")
                print ("--- 1.SI     2.NO ---")
                print ("---------------------")
                salir = int(input("Digite Su Opcion A Elegir: "))
                if salir!=1 and salir!=2:
                    system("cls")
                    print("----------------------------------------")
                    print("--- ¡¡ ERROR !!, Digite Una Opcion Valida ---")
                    print("----------------------------------------")
                    system("pause")
                    self.salir()
            
                elif salir == 1:
                     print ("-------------------")
                     print ("--- Hasta Luego ---")
                     print ("-------------------")
                     system("pause")
                elif salir == 2:
                    print("-------------------------")
                    print("--- Volviendo Al Menu ---")
                    print("-------------------------")
                    self.menu()
                 
        except:
            print("\n--- Error De Opcion!!! ---")
            system("pause") 
            self.salir()
          
                
    def errorOpcion(self):
        print ("\n--------------------------")
        print ("--- Error De Opcion!!! ---")
        print ("--------------------------")
        system("pause")
        self.menu()


p = Principal()
p.menu()  
