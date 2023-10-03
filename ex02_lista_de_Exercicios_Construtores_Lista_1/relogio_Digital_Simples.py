import time
class relogio_digital():

    def __init__(self, horas=0, minutos=0, segundos=0):
            self.horas = horas
            self.minutos = minutos
            self.segundos = segundos
          
    def ligar(self):
        for i in range(10):
            time.sleep(1)
            self.segundos += 1
            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1
                if self.minutos == 60:
                    self.minutos = 0
                    self.horas += 1
                    if self.horas == 24:
                        self.horas = 0
    
    def mostrar_horas(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"
    
    def troca_horas(self):
        self.horas = int(input())
        self.minutos = int(input())
        self.segundos = int(input())


r1 = relogio_digital()
r2 = relogio_digital(10, 25, 21)
r1.ligar()
print(r1.mostrar_horas())

