#!/usr/bin/env python3

class Ponto:
    def __init__(self, x=0, y=0):
        '''
        Inicializa um ponto no plano cartesiano.
        O ponto é representado por suas coordenadas x e y,
        que são inicialmente definidas como 0.

        :param self: Referência ao objeto atual da classe Ponto
        :return:none
        '''

        self.x = x # Atributop de instância que representa a coordenada x do ponto.
        self.y = y # Atributop de instância que representa a coordenada y do ponto.
        return
    
    def __str__(self):
        '''
        Retorna uma representação em string do ponto no formato [x,y].
        :param self: Referência ao objeto atual da classe Ponto
        :return: Uma string representando o ponto no formato [x,y]
        '''
        return f'[{self.x},{self.y}]'

    def __eq__(self, outro):
        '''
        Compara o ponto atual com outro ponto para verificar se são iguais.
        Dois pontos são considerados iguais se suas coordenadas x e y forem iguais.

        :param self: Referência ao objeto atual da classe Ponto
        :param outro: Outro objeto da classe Ponto a ser comparado
        :return: True se os pontos forem iguais, False caso contrário
        '''
        return self.x == outro.x and self.y == outro.y
    
'''
Setor de testes
'''
def main():
    p1 = Ponto()
    p2 = Ponto(3,4)
    p3 = Ponto(5)
    p4 = Ponto(y=6)
    print(f'Ponto 1: ({p1.x},{p1.y})')
    print(f'Ponto 2: ({p2.x},{p2.y})')
    print(f'Ponto 1: {p1}')
    print(f'Ponto 3: {p3}')
    print(f'Ponto 4: {p4}')

    if p1 == p2:
        print('Pontos p1 e p2 são iguais')
    else:        
        print('Pontos p1 e p2 são diferentes')
    
           
    return

if __name__ == "__main__":
    main() 