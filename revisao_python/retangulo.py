#!/usr/bin/env python3
import ponto
from ponto import Ponto 

class Retangulo:
    def __init__(self, a = Ponto(), b = Ponto(1,1)):
        '''
        Inicializa um retângulo definido por dois pontos opostos (p1 e p2).
        O retângulo é representado por seus vértices p1 e p2, que são objetos da classe Ponto.

        :param self: Referência ao objeto atual da classe Retangulo
        :param p1: Um objeto da classe Ponto representando um vértice do retângulo
        :param p2: Um objeto da classe Ponto representando o vértice oposto do retângulo
        :return:none
        '''
        p1 = a 
        p3 = b
        p2 = Ponto(p1.x, p3.y)
        p4 = Ponto(p3.x, p1.y)
        self.p1 = p1 # Atributo de instância que representa o vértice p1 do retângulo.
        self.p2 = p2 # Atributo de instância que representa o vértice p2 do retângulo.
        self.p3 = p3 # Atributo de instância que representa o vértice p3 do retângulo.
        self.p4 = p4 # Atributo de instância que representa o vértice p4 do retângulo.
        return

    def __str__(self):
        '''
        Retorna uma representação em string do retângulo, mostrando os vértices p1, p2, p3 e p4.
        :param self: Referência ao objeto atual da classe Retangulo
        :return: Uma string representando o retângulo com seus vértices
        '''
        return f'[{self.p1}, {self.p2}, {self.p3}, {self.p4}]'    
    
def main():
    r1 = Retangulo()
    r2 = Retangulo(Ponto(3,4), Ponto(5,6))
    print(f'Retângulo 1: {r1}')
    print(dir(r1))
    print(f'Retângulo 2: {r2}')
    return

if __name__ == "__main__":
    main()