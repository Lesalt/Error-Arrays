import numpy as np

#matriz com elemento em sequencia, gera o erro
def MatrizError():
    tabela = np.array([[['0', '1'], '0'],
                       [None, '2'],
                       [None, None]], dtype=int)
    print(tabela)

#matriz com elementos unicos, roda perfeito
def MatrizSuccessful():
    tabela = np.array([['1', '2'],
                       ['3', '4'],
                       ['5', '6']], dtype=int)
    print(tabela)