from PIL import Image
from PIL import PngImagePlugin
import os
import re

LARGE_ENOUGH_NUMBER = 100
PngImagePlugin.MAX_TEXT_CHUNK = LARGE_ENOUGH_NUMBER * (1024**2)

# INPUT_FOLDER = "input"
# OUTPUT_FOLDER = "output"
# BACKGROUND_FOLDER = "background"
def sobreporImagemSM(background, principal, centro):
    img1 = background
    img2 = principal.convert('RGBA')
    img1.paste(img2, (centro), mask=img2)
    imagem = img1.convert('RGB')
    processada = imagem.resize((500,500))
    return processada

def sobreporImagem(background, principal, centro):
    img1 = background
    img2 = principal.convert('RGBA')
    img1.paste(img2, (centro), mask=img2)
    imagem = img1.convert('RGB')
    processada = imagem.resize((300,300))
    return processada


def criaBg(root, file, bgImagem):
    #return os.path.join(INPUT_FOLDER, filename)
    image = Image.new("RGB", (bgImagem, bgImagem), (255, 255, 255))
    # print("tamanho final: ", bgImagem)
    # image.show()
    return image


def tamanhoImagem(root, file, ext=".jpg"):
    listaDeImagens = os.path.join(root, file)
    
    nomeArquivo = os.path.splitext(file)[0]
    
    meuNagumo = "/Users/franklin.campos/Desktop/meuNagumo"
    siteMercado = "/Users/franklin.campos/Desktop/siteMercado"
    # backup = "/Users/franklin.campos/Desktop/testeImagem/backup"
    
    pillow_img = Image.open(listaDeImagens)
    width, height = pillow_img.size

    
    # verifica qual eixo é maior
    if (width > height):
        bgImagem = width
    else:
        bgImagem = height
    
    # calcula as cordenadas do centro
    eixoX = (bgImagem - width) // 2
    eixoY = (bgImagem - height) // 2
    centro = (eixoX, eixoY)

    fundoBranco = criaBg(root, file, bgImagem)
    imagemPrincipal = pillow_img
    imagemFinal = sobreporImagem(fundoBranco, imagemPrincipal, centro)
    imagemFinal.save(os.path.join(meuNagumo, nomeArquivo+ext))
    imagemFinal2 = sobreporImagemSM(fundoBranco, imagemPrincipal, centro)
    imagemFinal2.save(os.path.join(siteMercado, nomeArquivo+ext))
    # shutil.move(pillow_img, backup)


def verificaImagem(extension):
    extension_lowercase = extension.lower()
    return bool(re.search(r'^\.(jpe?g|png)$', extension_lowercase))


def checarImagem(root, file):
    filename, extension = os.path.splitext(file)
    print ("processando imagem: ", filename)

    if not verificaImagem(extension):
        return

    tamanhoImagem(root = root, file = file)


def listaArquivos(root, files):

    for file in files:
        checarImagem(root, file)

def main(input_folder):
    for root, dirs, files in os.walk(input_folder):
        listaArquivos(root, files)


if __name__ == '__main__':
    diretorio = "/Users/franklin.campos/Desktop/testeImagem"
    
    main(diretorio)