# Crear clase y atributos, constructor, y método de clasificación

class persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
    
    def clasificacion(self):
        imc = self.peso / (self.altura ** 2)
        if imc < 18.5:
            return "Bajo peso"
        elif imc >= 18.5 and imc < 25:
            return "Peso normal"
        elif imc >= 25 and imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"
        

yo = persona("David", 19, "Hombre", 64, 1.76)

print(yo.clasificacion())