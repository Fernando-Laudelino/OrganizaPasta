                            # Projeto para organiza diretorio com varios aquirvos com extenções diferentes diferente como diretorio Dowload
import os

de="../../../../Downloads/a"      # Caminho para Diretorio que quer organizar. Salvei em uma variavel (Opcional)

os.chdir(de)                      # Entrando no Diretorio usando a variavel com endereço

def dir(arquivo):                 # A função para criar diretorio se não existir, se exitir só enviar os arquivos para dentro do diretorio.
    try:                          # O diretorio vai ser criado com o nome que colocar dentro dos parentes (Melhor colocar igual da extençãoOrgani)
        os.mkdir(arquivo)
        os.rename(f,arquivo+"/"+f)
    except FileExistsError:
        os.rename(f,arquivo+"/"+f)


for f in os.listdir("."):         # Lisatar os Arquivos e salvar na variavel F um por um.
    if f.endswith(".pdf"):        # Se o Arquivo salvo em F tiver o final do nome "Igual pedi"
        dir("PDF")                # Ultilizo a função criada. Já com o nome da pasta a ser criada
    elif f.endswith(".mp4"):
        dir("MP4")
    elif f.endswith(".jpg"):
        dir("JPG")
