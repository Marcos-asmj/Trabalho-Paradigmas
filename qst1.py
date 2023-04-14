def ler_nome(nome):
    """Esta função pega o nome que recebe como parâmetro e retorna suas iniciais"""
    letras = ''
    
    for letra in nome:
        if letra.isupper():
            letras = letras + letra    
    
    letras = letras.lower()
    return letras

def gerar_email(letras):
    """Esta função recebe letras e gera os e-mails"""
    email = letras + '@empresa.com.br'

    return email

if __name__ == '__main__':
    iniciais = ler_nome('Carlos Souza Silva')
    email = gerar_email(iniciais)
    print(email)

    help(ler_nome)
    help(gerar_email)