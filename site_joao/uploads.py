from datetime import datetime
from datetime import date
import os


data = date.today()
hora = datetime.now().strftime('%H-%M-%S')
dia = str(data)[8:10]

def handle_uploaded_file(arquivo, nome, titulo=None):
    if titulo:
        titulo = titulo.replace(' ', '_')
        caminho = 'www/_arquivos/'  + titulo
        if not os.path.exists('static/'+caminho):
            os.makedirs('static/'+caminho)
    
    nome = caminho+'/'+nome
    destination = open('static/'+nome, 'wb+')
    for chunk in arquivo.chunks():
        destination.write(chunk)
    destination.close()
    return nome