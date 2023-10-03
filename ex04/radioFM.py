estacoes ={89.5:'Cocais', 91.5: 'Mix', 94.1:'Boa', 99.1:'Clube'}
class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.volume_min=0
        self.volume_max=vol_max
        self.freq_min=88
        self.freq_max=108
        self.estacoes = estacoes
        self.volume=None
        self.ligado=False
        self.estacao_atual=None
        self.frequencia_atual=None
        self.antena_habilitada=False

    def ligar(self):
        self.ligado=True
        self.volume= self.volume_min
        if self.antena_habilitada == True:
            for i, j in enumerate(self.estacoes):
                self.estacao_atual=j
                self.frequencia_atual=i
                break
        
    def desligar(self):
        self.estacoes = False
        self.volume=None
        self.frequencia_atual=None

    def aumentar_volume(self,avolume=1):
        if self.volume + avolume <= self.volume_max:
            self.volume+=avolume
        else:
            print('Volume acima do pemitido')

    def diminuir_volume(self,dvolume=1):
        if self.volume - dvolume <= self.volume_min:
            self.volume-=dvolume
        else:
            print('Volume abaixo do pemitido')
    def mudar_frequencia(self, mud_fre=0):
        pass

