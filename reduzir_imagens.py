import os
from PIL import Image
from image_transform import image_transform

from PIL import PngImagePlugin
LARGE_ENOUGH_NUMBER = 100
PngImagePlugin.MAX_TEXT_CHUNK = LARGE_ENOUGH_NUMBER * (1024**2)

def verificaExtensao(nomeArquivo):
    if nomeArquivo.endswith('png') or nomeArquivo.endswith('jpg'):
        return True
    return False

def renomearImagens(input_dir, output_dir ,ext='.jpg'):
    listarArquivos = [nome for nome in os.listdir(input_dir) if verificaExtensao(nome)]
    for nome in listarArquivos:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
        processada = imagem.resize((300,300))
        nomeSemExtensao = os.path.splitext(nome)[0]
        processada.save(os.path.join(output_dir, nomeSemExtensao+ext))
        os.remove(os.path.join(input_dir, nome))
        #print(listarArquivos)

if __name__ == "__main__":
    diretorio = "/Users/franklin.campos/Desktop/imagens"
    processadas = "/Users/franklin.campos/Desktop/imagens/processadas"

    renomearImagens(diretorio, processadas)

