# Crear clase y atributos, constructor, y método de clasificación
# Autor: Fernando Manzo Virgen
# Fecha: 20/02/2019

class Persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def clasificacion(self):
        imc = self.peso / (self.altura**2)
        if imc < 18.5:
            return "Bajo peso"
        elif imc >= 18.5 and imc <= 24.9:
            return "Peso normal"
        elif imc >= 25 and imc <= 29.9:
            return "Sobrepeso"
        elif imc >= 30 and imc <= 34.9:
            return "Obesidad grado I"
        elif imc >= 35 and imc <= 39.9:
            return "Obesidad grado II"
        else:
            return "Obesidad grado III"


persona1 = Persona("David", 19, "Hombre", 62, 1.76)


if __name__ == "__main__":
    print(persona1.clasificacion())