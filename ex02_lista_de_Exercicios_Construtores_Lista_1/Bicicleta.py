class Bicicleta():
    
    def __init__(self, veloc_atual, altura_cela, calibragem_pneus):
        self.veloc_atual = veloc_atual
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus
        self.veloc_max = 80
        self.veloc_min = 0
        self.altura_max = 40
        self.altura_min = 0
        self.calibragem_max = 35
        self.calibragem_min = 0

    def regular_cela(self, cela):
        if self.veloc_atual == 0 and self.altura_min < cela <= self.altura_max:
            self.altura_cela = cela
        else:
            print('ocorre um erro')
    
    def calibrar_pneus(self, pneus):
            if self.veloc_atual == 0 and self.calibragem_min < pneus <= self.calibragem_max:
                self.calibragem_pneus = pneus
            else:
                print('ocorre um erro')

            
    
bike = Bicicleta(10, 24, 30)

bike.regular_cela(14)
bike.veloc_atual = 0
bike.regular_cela(14)
bike.calibrar_pneus(36)
bike.calibrar_pneus(34)

print(bike.veloc_atual)
print(bike.altura_cela)
print(bike.calibragem_pneus)
