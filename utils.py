import os
import shutil

categorias = {
    'Imagens' : ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos' : ['.pdf', '.docx', '.txt'],
    'Compactos' : ['.zip', '.rar']
}


def organizar_pasta(caminho):
    itens = os.listdir(caminho)
    for item in itens:
        print(item)
        nome ,extensao = os.path.splitext(item)
        extensao = extensao.lower()
        print(extensao)
        for categoria, lista_extensoes in categorias.items():
            if extensao in lista_extensoes:
                pasta_destino = os.path.join(caminho, categoria)
                os.makedirs(pasta_destino, exist_ok=True)
                caminho_arquivo = os.path.join(caminho, item)
                shutil.move(caminho_arquivo, pasta_destino)
                print(f'Movido: {item} -> {categoria}')
                break


