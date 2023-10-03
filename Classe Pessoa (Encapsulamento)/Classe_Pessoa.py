class pessoa():
    def __init__(self,nome,idade, peso, altura, sexo, estado='vivo', esta_civil='solteiro', conjuge=None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = esta_civil
        self.__conjuge = conjuge

    def envelhecer(self):
        self.__idade += 1
        self.crescer()
        print(f'{self.__nome} esta com {self.__idade} anos e {self.__altura}cm de altura')

    def engodar(self, valor):
        self.__peso += valor

    def emagrecer(self,valor):
        self.__peso -= valor

    def crescer(self, valor=5):
        if self.__idade <= 21:
            self.__altura += valor
        else:
            print(f'{self.__nome} não pode mais crescer pois está com 21 anos ou mais')
    

    def casar(self, pessoa):
        if self.__estado_civil != 'casado(a)' and self.__nome != pessoa.__nome:
            if self.__idade >= 18 and pessoa.__idade >= 18:
                self.__estado_civil = 'casado(a)'
                self.__conjuge = pessoa
                print(f'{self.__nome} está casado com {self.__conjuge.__nome}')
            else:
                print('meno de idade')
        else:
            print('nao pode casar')

    def morrer(self, op=True):
        self.__estado = 'morto'
        print(f'{self.__nome} morreu')


maria = pessoa('maria', 5, 20, 100, 'F')
joão = pessoa('joão', 12, 40, 140, 'M')
pedro = pessoa('pedro', 22, 65, 170, 'M')
bia = pessoa('bia', 18, 55, 160, 'F')
julia = pessoa('julia', 30, 65, 170, 'F')
carlos = pessoa('carlos', 2, 11, 80, 'M')
jonas = pessoa('jonas', 34, 70, 180, 'M')


maria.__idade = 10
maria.envelhecer()
pedro.crescer(2)
bia.casar(carlos)
pedro.casar(maria)
pedro.casar(julia)
pedro.casar(bia)
maria.morrer()
pedro.morrer()
jonas.casar(julia)
pedro.casar(bia)
#
joão.__idade = 50
