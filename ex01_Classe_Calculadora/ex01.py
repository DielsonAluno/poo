from calculadora import*

def main():
    print('-=-'*7,'Calculadora', '-=-'*7)
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    op = str(input('Qual é a operação '))
    c1 = calculadora(n1, n2, op)
    res = c1.calcula()
    
    print(f'Resultado:{res}')





if __name__=='__main__':
    main()