from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    login = models.CharField('Login', max_length=15, unique=True)
    senha = models.CharField('Senha', max_length=15)
    email = models.CharField('email', max_length=35)
    sexo = models.CharField('Sexo', max_length=1, choices=(('M','Masculino'),('F','Feminino')), default='Masculino')
    superAdm = models.CharField(max_length=1)
    moderador = models.CharField(max_length=1, null= True)

class Conteudo(models.Model):
    titulo = models.CharField('Titulo', max_length=60)
    descricao = models.TextField('Texto')
    linkYoutube = models.CharField('Link youtube', max_length=60)
    imagem = models.FileField()
    tamanho = models.CharField('Tamanho', max_length=10)
    lancamento = models.CharField('Lançamento', max_length=5)
    audio = models.CharField('Áudio', max_length=50)
    legenda = models.CharField('Legenda', max_length=1)
    formato = models.CharField('formato', max_length=6)
    duracao = models.CharField('Duração', max_length=6)
    qualidadeAudio = models.CharField('Qualidade de Áudio', max_length=2)
    qualidadeVideo = models.CharField('Qualidade de Vídeo', max_length=2)
    linkArquivo = models.TextField('Link magnético')
    status = models.CharField(max_length=1, null= True)

    @property
    def path_arquivo(self):
        return str(self.arquivo).replace('..projectComunidad','')

    @property
    def path_image(self):
        print('-'*80)
        print(self.imagem)
        print('-'*80)
        return str(self.imagem).replace('../projectComunidad','')

class Genero(models.Model):
    genero = models.CharField('Gênero', max_length=25)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE, blank= True, null=True)
    
class Log(models.Model):
    data = models.DateTimeField()
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)



