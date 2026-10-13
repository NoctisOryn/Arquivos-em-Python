import os
valor: int = 0
dir: str = ''
arq: str = ''

def mult(vlr, tab):
    res: int = 0
    res = vlr * tab
    return res

def grava(c, rslt):
    global dir
    global arq
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''

    dir = '/tmp/exercicios'
    arq = 'ex34.txt'
    linha = str(rslt) + '\n'
    enc = 'utf-8'

    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    
    if os.path.exists(dir) and os.path.isdir(dir):
        if os.path.isfile(os.path.join(dir, arq)) and c > 0:
            tipo = 'a'
        else:
            tipo = 'w'

        with open(os.path.join(dir, arq), tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print("Diretório inválido")


def main():
    global valor
    tab: int = 0
    result: int = 0

    valor = int(input("Digite um número:"))
    while (valor < 1 or valor > 10):
        valor = int(input(f"O número {valor} é inválido! Digite outro número entre 1 e 10."))

    for tab in range (10): 
        result = mult(valor, tab + 1)
        grava(tab,result)

if __name__ == '__main__':
    main()
