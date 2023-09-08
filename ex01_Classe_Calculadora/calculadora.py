class calculadora:
    #atributos
    num1 = None
    num2 = None
    op= '+'
    def __init__(self,num1, num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
    
    #metodos
    def somar(self):
        return self.num1 + self.num2
    
    def menos(self):
        return self.num1 - self.num2
    
    def multiplicacao(self):
        return self.num1 * self.num2    
    
    def divisao(self):
        return self.num1 / self.num2
    
    def operacao(self):
        if self.op == '+':
            res = self.somar()
        
        elif self.op == '-':
            res = self.menos()
        elif self.op == '*':
            res = self.multiplicacao()
        else:
            res = self.divisao()

        return res

    def calcula(self):
        res = self.operacao()
        return res