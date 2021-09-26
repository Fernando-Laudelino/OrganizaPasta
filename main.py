                                # Projeto para organiza diretorio com varios aquirvos com extenções diferentes diferente como diretorio Dowload.
import os                                                       #Importa o modulo OS para mover entre os diretorios.


def procura_dir(caminho):                                       # Função só colocar o caminho do diretorio que quer Organizar.
    os.chdir(caminho)                                           # Aqui entramos no Diretorio escolhido.
    for arquivo in os.listdir("."):                             # Lisatar os Arquivos e salvar na variavel $arquivo um por um.
        no_ar, ex_tensao=os.path.splitext(arquivo)              # Aqui pegamos variavel $arquivo e separamos em duas parte nome e extenção.
        nome=ex_tensao.upper().strip(".")                       # Salvei a extenção na variavel $nome toda em maiscula e sem o ponto.
        if ex_tensao.startswith("."):                           # Condição IF para ter certeza que vamos manipular só os arquivos do direteorio.
            try:
                os.mkdir(nome)                                  # Se for um arquivo vai criar uma pasta com o mesmo nome que o arquivo maiusculo sem o ponto.
                os.rename(arquivo, nome + "/" + arquivo)        # Vai jogar o arquivo para dentro da pasta.
            except FileExistsError:                             # Se  o diretorio já existir vai só jogar o arquivo para pasta.
                os.rename(arquivo, nome + "/" + arquivo)



#procura_dir("/home/fernando/Downloads")                         Função pronta já com o endereço do diretorio para organizar.









