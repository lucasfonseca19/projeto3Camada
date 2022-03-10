import random as rd
import numpy as np

def sorteador(numerodecomandos,bytedeseparacao):
    """
        Essa funcao ira retornar uma lista contendo os bytes dos comandos.cada sequencia de bytes de cada comando 
        vai estar separada pelo byte de separacao
    """

    commands=[b'\x00\xFF\x00\xFF',b'\x00\xFF\xFF\x00',b'\xFF',b'\x00',b'\xFF\x00',b'\x00\xFF']
    res=b""
    numerodebytes=0
    for i in range(numerodecomandos):
        sorteado=rd.randint(0,5)
        res+=commands[sorteado]
        res+=bytedeseparacao
    
    return res,len(res)


