def ler_arquivo(caminho):
    """Esta função lê os nomes inseridos num arquivo de texto e retorna as iniciais desses nomes"""
    nomes = open(caminho, 'r')
    lista_letras = []
    lista_nomes = []
    
    for nome in nomes.readlines():
        letras = ''
        for letra in nome:
            if letra.isupper():
                letras = letras + letra
        letras_min = letras.lower()
        if lista_letras:
            for i in range(len(lista_letras)):
                if letras_min == lista_letras[i]:
                    letras_min = letras_min + '2'
        lista_letras.append(letras_min)
        lista_nomes.append(nome.replace('\n', ''))

    
    nomes.close()
    lista_nomes.sort()
    lista_letras.sort()
    return lista_letras, lista_nomes

def gerar_email(lista_inicias):
    """Esta função recebe uma lista com grupos de letras e gera os e-mails"""
    emails = []

    for iniciais in lista_inicias:
        email = iniciais + '@empresa.com.br'
        emails.append(email)

    return emails

def gerar_arquivo(emails, nomes):
    """Esta função recebe os emails e os nomes e os adiciona a um novo arquivo txt"""
    with open('qst2saida.txt', 'w') as f:
        f.write('NOME' + '\t' + 'E-MAIL' + '\n')
        for i in range(len(emails)):
            f.write(nomes[i] + '\t' + emails[i] + '\n')
        
    f.close()

if __name__ == '__main__':
    lista_inicias, lista_nomes = ler_arquivo('qst2entrada.txt')
    emails = gerar_email(lista_inicias)
    gerar_arquivo(emails, lista_nomes)

    help(ler_arquivo)
    help(gerar_email)
    help(gerar_arquivo)