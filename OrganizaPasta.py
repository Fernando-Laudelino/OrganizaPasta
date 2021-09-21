                            # Projeto para organiza diretorio com varios aquirvos com extenções diferentes diferente como diretorio Dowload
import os


de="../../../../Downloads"                  # Caminho para Diretorio que quer organizar. Salvei em uma variavel (Opcional)

os.chdir(de)                                # Entrando no Diretorio usando a variavel com endereço

def dir(nome):                              # A função para criar diretorio se não existir, se exitir só enviar os arquivos para dentro do diretorio.
    try:                                    # O diretorio vai ser criado com o nome que colocar dentro dos parentes (Melhor colocar igual da extençãoOrgani)
        os.mkdir(nome)
        os.rename(f,nome+"/"+f)
    except FileExistsError:
        os.rename(f,nome+"/"+f)


for f in os.listdir("."):                   # Lisatar os Arquivos e salvar na variavel F um por um.
    if f.lower().endswith(".pdf"):          # Se o Arquivo salvo em F tiver o final do nome "Igual pedi"
        dir("PDF")                          # Ultilizo a função criada. Já com o nome da pasta a ser criada
    elif f.lower().endswith(".mp4"):
        dir("MP4")
    elif f.lower().endswith(".jpg") or f.lower().endswith(".png") or f.lower().endswith(".jpeg"):
        dir("JPG")
    elif f.lower().endswith(".docx") or f.lower().endswith("doc"):
        dir("DOCX")
    elif f.lower().endswith(".exe"):
        dir("EXE")
    elif f.lower().endswith(".zip") or f.lower().endswith(".gz") or f.lower().endswith(".bz2"):
        dir("ZIP")
    elif f.lower().endswith(".deb"):
        dir("DEB")
    elif f.lower().endswith(".torrent"):
        dir("TORRENTE")

