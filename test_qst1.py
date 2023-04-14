from qst1 import *

def teste_nome1():
    assert ler_nome('Carlos Souza Silva') == 'css'
    assert gerar_email('css') == 'css@empresa.com.br'

def teste_nome_minusculo():
    assert ler_nome('carlos souza silva') == ''

def teste_numeros():
    assert ler_nome('12345') == ''