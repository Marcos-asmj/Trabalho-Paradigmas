from qst2 import *

def teste1():
    assert ler_arquivo('qst2entrada.txt') == (['asc', 'css', 'css2', 'msc'],['Antonio dos Santos Cardoso', 'Carlos Souza Silva', 'Cassio Silva dos Santos', 'Maria da Silva Castro'])
    assert gerar_email(['asc', 'css', 'css2', 'msc']) == (['asc@empresa.com.br', 'css@empresa.com.br', 'css2@empresa.com.br', 'msc@empresa.com.br'])