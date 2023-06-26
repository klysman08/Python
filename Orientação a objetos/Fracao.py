# Atributos
# 1. numerador; 2. denominador

# Metodos
# somar; subtrair; multiplicar; inverter

class Fracao:
    # self; ponto de referência na memoria onde o objeto será instanciado
    def __init__(self, num, den):
        self.numerador = num

        if den == 0:
            self.denominador = 1
        else:
            self.denominador = den

    def somar(self, outra):
        if self.denominador == outra.denominador:
            num = self.numerador + outra.numerador
            den = self.denominador
            return Fracao(num, den)
        num = self.numerador * outra.denominador + outra.numerador*self.denominador
        den = self.denominador*outra.denominador
        return Fracao(num, den)

    def subtrair(self, outra):
        return self.somar(self, outra.negar())

    def multiplicar(self, outra):
        num = self.numerador * outra.numerador
        den = self.denominador * outra.denominador

        return num * den

    def dividir(self, outra):
        return self.multiplicar(outra.inverter())

    def inverter(self):
        return Fracao(self.denominador, self.numerador)

    def negar(self):
        return Fracao(-self.numerador, -self.denominador)

    def __str__(self):
        representation = "{}/{}".format(self.numerador, self.denominador)
        return representation

    def __repr__(self):
        representation = "Fracao({}, {})".format(
            self.numerador, self.denominador)
        return representation


print("*"*30)

primeira = Fracao(5, 7)
print(primeira)

lista = [2, ' teste ', primeira]
print(lista)
