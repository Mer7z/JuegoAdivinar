import math
import random
import time

class Juego():
    
    def seleccionarOpcion(self):
        try:
            opcion = int(input("1. Jugar\n0. Salir\n-> "))
            return opcion
        except ValueError as e:
            print("Error de valor... Selecciona un número entero válido.")
            return self.seleccionarOpcion()
    
    def obtenerRango(self):
        try:
            rango = int(input("Seleccione el máximo rango: "))
            return rango
        except ValueError as e:
            print("Error de valor... El rango debe ser un número entero. Intente de nuevo.")
            return self.obtenerRango()

    def obtenerNumeroAleatoreo(self, inicio, rango):
        try:
            numeroAleatoreo = random.randrange(inicio, rango)
            return numeroAleatoreo
        except ValueError as e:
            print("Error. El rango debe ser mayor que 1")
            rango = self.obtenerRango()
            return self.obtenerNumeroAleatoreo(inicio, rango)
    
    def iniciarIntentos(self):
        print(f"Tienes {self.numeroAdivinar} intentos restantes...")
        if self.numeroAdivinar == 0:
            print(f"¡Se acabaron los Intentos!\nEl número era: {self.numeroAleatoreo}\nFin del Juego...\n")
            return
        
        try:
            numero = int(input("Ingresa el número que pienses: "))
            print(self.vector[numero - 1])
            if self.vector[numero - 1] == "acertó":
                print(f"¡Bien Hecho! ¡El número {numero} es correcto!\n")
            else:
                self.numeroAdivinar -= 1
                if self.numeroAdivinar > 0:
                    if self.numeroAleatoreo < numero:
                        print("Pista: el número que elegiste es mayor al número por adivinar...")
                    elif self.numeroAleatoreo > numero:
                        print("Pista: el número que elegiste es menor al número por adivinar...")
                self.iniciarIntentos()
        except ValueError as e:
            print("Error de valor... Debes ingresar un número entero.")
            self.numeroAdivinar -= 1
            self.iniciarIntentos()
        except IndexError as e:
            print("Error... ¡El número que ingresaste está fuera del rango!")
            self.numeroAdivinar -= 1
            self.iniciarIntentos()

 
    def __init__(self):
        print("##### Adivina el Número #####")
        print("¡Bienvenido!\nSelecciona una opción:")
        opcion = 99
        while opcion != 0:
            opcion = self.seleccionarOpcion()
            if opcion == 0:
                print("Hastá pronto!")
                break
            elif opcion != 1:
                print("Opción no válida. Intente de nuevo.")
                continue
            rango = self.obtenerRango()
            self.numeroAdivinar = math.ceil(rango / 20)
            self.numeroAleatoreo = self.obtenerNumeroAleatoreo(1, rango)
            self.vector = []
            for i in range(rango):
                if i == self.numeroAleatoreo - 1:
                    self.vector.append("acertó")
                else:
                    self.vector.append("falló")
                    
            self.iniciarIntentos()