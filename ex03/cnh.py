class cnh():

    def __init__(self, nome, cpf, data_nasc, data_emis, tipo, obs='SEM OBESERVACAO'):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.data_emis = data_emis
        self.obs = obs
        self.tipo = tipo
    
    def valedar_data(self):
        pass