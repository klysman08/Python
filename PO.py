# Atributos
# 1. numerador; 2. denominador

# Metodos
# somar; subtrair; multiplicar; inverter

class Fracao:
    def __init__(self, num, den):  # self; ponto de referência na memoria onde o objeto será instanciado
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

a = Fracao(5, 4)
b = Fracao(2, 2)

multiplicar = a.multiplicar(b)
dividir = a.dividir(b)

print(f'{multiplicar} e {dividir}')
