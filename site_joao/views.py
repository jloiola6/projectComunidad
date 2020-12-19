from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from site_joao.uploads import handle_uploaded_file
from site_joao.models import *
from site_joao.form import *
from django.shortcuts import render, get_object_or_404



# Create your views here.

def main(request):
    if verification(request):
        user = True
        try:
            superAdm = Usuario.objects.get(id= request.session['id'], superAdm= 'S')
            adm = True
        except:
            pass

        try:
            moderador = Usuario.objects.get(id= request.session['id'], moderador= 'S')
            moderador = True
        except:
            pass
    
    mainCarrosel = Conteudo.objects.filter(status= 'S').order_by('-id')[0]
    carrosel = Conteudo.objects.filter(status= 'S').order_by('-id')[1:3]
    mainCard = Conteudo.objects.filter(status= 'S').order_by('-id')[3:7]
    card = Conteudo.objects.filter(status= 'S').order_by('-id')[7:11]
    conteudo = Conteudo.objects.filter(status= 'S').order_by('-id')[11:]

    buscar = request.GET.get('pesquisa')
    if buscar:
        conteudo = Conteudo.objects.filter(titulo__icontains= buscar, status= 'S')
        return TemplateResponse(request, 'aprovar.html', locals())
    
    return TemplateResponse(request, 'home.html', locals())

def deletarConteudo(request):
    if verification(request):
        try:
            superAdm = Usuario.objects.get(id= request.session['id'], superAdm= 'S')
            id = request.GET.get('id')
            conteudo = Conteudo.objects.get(id=id)
            conteudo.delete()
            return HttpResponseRedirect('/aprovar')
        except:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def aprovarConteudo(request):
    if verification(request):
        try:
            superAdm = Usuario.objects.get(id= request.session['id'], superAdm= 'S')
            id = request.GET.get('id')
            conteudo = Conteudo.objects.get(id=id)
            conteudo.status = 'S'
            conteudo.save()
            return HttpResponseRedirect('/aprovar')
        except:
            return HttpResponseRedirect('/aprovar')
    else:
        return HttpResponseRedirect('/')

def conteudo(request):
    if verification(request):
        user = True
        try:
            superAdm = Usuario.objects.get(id= request.session['id'], superAdm= 'S')
            adm = True
        except:
            pass

        try:
            moderador = Usuario.objects.get(id= request.session['id'], moderador= 'S')
            moderador = True
        except:
            pass
    
    buscar = request.GET.get('pesquisa')
    if buscar:
        conteudo = Conteudo.objects.filter(titulo__icontains= buscar, status= 'S')
        return TemplateResponse(request, 'aprovar.html', locals())

    nome = request.GET.get('nome')
    conteudo = Conteudo.objects.get(titulo= nome)
    if conteudo.status == 'N':
        status = True
    if conteudo.legenda == 'S':
        legenda = 'Contém legenda'

    link = conteudo.linkYoutube.split('watch?v=')
    try:
        link = link[0]+'embed/'+link[1]
    except IndexError:
        link = ''

    return TemplateResponse(request, 'conteudo.html', locals())

def moderadores(request):
    if verification(request):
        user = True
        try:
            superAdm = Usuario.objects.get(id= request.session['id'], superAdm= 'S')
            adm = True
        except:
            pass

        try:
            moderador = Usuario.objects.get(id= request.session['id'], moderador= 'S')
            moderador = True
        except:
            return HttpResponseRedirect('/')
        
        usuarios = Usuario.objects.all()
        buscar = request.GET.get('pesquisa')
        if buscar:
            usuarios = Usuario.objects.filter(nome__icontains= buscar)
            if not usuarios:
                usuarios = Usuario.objects.filter(login__icontains= buscar)

            return TemplateResponse(request, 'moderadores.html', locals())

    else:
        return HttpResponseRedirect('/')
    
    return TemplateResponse(request, 'moderadores.html', locals())

def tornarAdm(request):
    if verification(request):
        try:
            id = request.GET.get('id')
            usuario = Usuario.objects.get(id=id)
            usuario.superAdm = 'S'
            usuario.save()
            return HttpResponseRedirect('/moderadores')
        except:
            return HttpResponseRedirect('/moderadores')
    else:
        return HttpResponseRedirect('/')

def retirarAdm(request):
    if verification(request):
        try:
            id = request.GET.get('id')
            usuario = Usuario.objects.get(id=id)
            usuario.superAdm = 'N'
            usuario.save()
            return HttpResponseRedirect('/moderadores')
        except:
            return HttpResponseRedirect('/moderadores')
    else:
        return HttpResponseRedirect('/')

def verification(request):
    try:
       if request.session['id']:
           return True
    except KeyError:
        return False

def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponseRedirect('/')

def login(request):
    if verification(request):
        return HttpResponseRedirect('/')
    else:
        buscar = request.GET.get('pesquisa')
        if buscar:
            conteudo = Conteudo.objects.filter(titulo__icontains= buscar, status= 'S')
            return TemplateResponse(request, 'aprovar.html', locals())

        if request.method == 'POST':
            login = request.POST.get('Login')
            senha = request.POST.get('Senha')
            
            user = get_object_or_404(Usuario, login= login, senha= senha) 
            # user = Usuario.objects.get(login= login, senha= senha)
            if user:
                request.session['id'] = user.id
                return HttpResponseRedirect('/')
            else:
                msg = 'Usuário não Cadsatrado'

            if user:
                request.session['id'] = user.id
                return HttpResponseRedirect('/')
            
    return TemplateResponse(request, 'login.html', locals())

def register(request):
    buscar = request.GET.get('pesquisa')
    if buscar:
        conteudo = Conteudo.objects.filter(titulo__icontains= buscar, status= 'S')
        return TemplateResponse(request, 'aprovar.html', locals())

    form = Form_Register()
    if request.method == 'POST':
        form = Form_Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/entrar')
        else:
            msg = 'Usuário já Cadsatrado'
    return TemplateResponse(request, 'register.html', locals())

def aprovar(request):
    if verification(request):
        user = True

        buscar = request.GET.get('pesquisa')
        if buscar:
            conteudo = Conteudo.objects.filter(titulo__icontains= buscar, status= 'N')
            return TemplateResponse(request, 'aprovar.html', locals())

        try:
            superAdm = Usuario.objects.get(id= request.session['id'], superAdm= 'S')
            adm = True
            conteudo = Conteudo.objects.all().filter(status= 'N').order_by('-id')
        except:
            return HttpResponseRedirect('/')
        
        try:
            moderador = Usuario.objects.get(id= request.session['id'], moderador= 'S')
            moderador = True
        except:
            pass

    else:
        return HttpResponseRedirect('/')
    return TemplateResponse(request, 'aprovar.html', locals())

def adicionar(request):
    if verification(request):
        user = True

        buscar = request.GET.get('pesquisa')
        if buscar:
            conteudo = Conteudo.objects.filter(titulo__icontains= buscar, status= 'S')
            return TemplateResponse(request, 'aprovar.html', locals())

        try:
            superAdm = Usuario.objects.get(id= request.session['id'], superAdm= 'S')
            adm = True
        except:
            pass

        try:
            moderador = Usuario.objects.get(id= request.session['id'], moderador= 'S')
            moderador = True
        except:
            pass
        
        editar = False
        try:
            id = request.GET.get('id')
            conteudo_existente = Conteudo.objects.get(id=int(id))
            new = FormConteudo(instance=conteudo_existente)
            editar = True
        except:
            new = FormConteudo()
        if request.method == 'POST':
            if editar:
                new = FormConteudo(request.POST, request.FILES, instance=conteudo_existente)
            else:
                new = FormConteudo(request.POST, request.FILES)
            editarArquivo = False
            if request.FILES.get('myFile'):
                editarArquivo = True
                nomeImg = 'imagem.' + str(request.FILES.get('myFile')).split('.')[-1]
                if 'jpg' in nomeImg:
                    nomeImg = 'imagem.png'
            tituloArquivo = request.POST.get('titulo')

            if new.is_valid():
                conteudo = new.save()
                if editarArquivo:
                    upload_imagem = handle_uploaded_file(request.FILES['myFile'], nomeImg, tituloArquivo)
                    conteudo.imagem = upload_imagem
                conteudo.status = 'N'
                conteudo.save()
                return HttpResponseRedirect('/')
            else:
                print('Não salvou!!')
        return TemplateResponse(request, 'add.html', locals())
    else:
        return HttpResponseRedirect('/entrar')
