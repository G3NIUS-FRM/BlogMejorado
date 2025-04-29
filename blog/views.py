from django.shortcuts import render, redirect,get_object_or_404
from articles.models import *
from allauth.socialaccount.models import SocialAccount
from User.models import *
from .forms import *

# Create your views here.
def home(request):
    user=request.user
    articulos=Articles.objects.all().order_by('-created_at')
    if user.is_authenticated:
        usuario=CustomUser.objects.get(username=request.user)
        return render(request, 'home.html',{"user":user,'articulos':articulos,"usuarioCompleto":usuario})
    return render(request, 'home.html',{"user":user,'articulos':articulos})



    
    
def crear_articulo(request):
    if request.method == "POST":
        form=ArticleForm(request.POST)
        if form.is_valid():
            articulo=form.save(commit=False)
            articulo.autor=request.user
            articulo.save()
        return redirect('/')
    else:
    
       form=ArticleForm()
       return render(request, 'crud-articulo.html',{"form":form})
   
   
   
def editar_articulo(request, article_id):
    articulo=Articles.objects.get(id=article_id)
    if request.method == "POST":
        form=ArticleForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ArticleForm(instance=articulo)
        return render(request, 'crud-articulo.html',{'form':form, 'edit':True, 'arti_id':article_id})
    
    
    
def eliminar_articulo(request, article_id):
    articulo=get_object_or_404(Articles, id=article_id)
    if articulo:
        articulo.delete()
        return redirect('/')
    
    
    
def articulo_view(request, article_id):
    articulo = get_object_or_404(Articles, id=article_id)
    
    # Comentarios
    arti_comments = Comments.objects.filter(commented=article_id)
    
    # Likes
    arti_likes = Likes.objects.filter(liked=article_id)
    likes = len(arti_likes)
    
    your_like = False  # Por defecto, no ha dado likef
    
    if request.user.is_authenticated:
        try:
            like = Likes.objects.get(liker=request.user, liked=articulo)
            your_like = True
        except Likes.DoesNotExist:
            your_like = False
    
    return render(request, 'articulo-view.html', {
        "arti_id": article_id,
        "articulo": articulo,
        "comentario": arti_comments,
        "likes": likes,
        "your_like": your_like,
        "num_comentarios": len(arti_comments)
    })
    
def likear(request, article_id):
    try:
       user=CustomUser.objects.get(username=request.user)
    except CustomUser.DoesNotExist:
        return redirect('/')
    articulo=Articles.objects.get(id=article_id)
    try:
       like=Likes.objects.filter(liked=articulo, liker=user).get()
       print("Fafa")
    except Likes.DoesNotExist:
        like=None
    if like:
        like_el=get_object_or_404(Likes, id=like.id)
        like_el.delete()
    else:
        like=Likes(liked=articulo, liker=user)
        like.save()
    
    return redirect('articulo_view',article_id)

def comentar(request,article_id):
    articulo=Articles.objects.get(id=article_id)
    try:
        user=CustomUser.objects.get(username=request.user)
    except CustomUser.DoesNotExist:
        return redirect('/')
    if request.method == "POST":
        comentario=request.POST.get("comentario")
        if comentario:
            comen=Comments(content=comentario, commented=articulo, autor=request.user)
            comen.save()
            return redirect('articulo_view',article_id)
        else:
            return redirect('/')

def profile_view(request):
    usuario=SocialAccount.objects.filter(user=request.user).get()
    if usuario:
        datos=usuario.extra_data
        print(datos)
        user=CustomUser.objects.get(username=request.user)

        print(user.description)
        form=InformacionForm(instance=user)
        articulos_del_usuario=Articles.objects.filter(autor=request.user)

        
    return render(request, "profile.html",
                  {
                    "datos":datos, 
                    "user":user, 
                    "articulos":articulos_del_usuario,
                    'form':form
                    })


def crearDescription(request):
    user=CustomUser.objects.get(username=request.user)
    description=request.POST.get("description")
    print(description)
    user.description=description
    user.save()
    return redirect('profile_view')

def actualizar_infoUser(request):
    user=CustomUser.objects.get(username=request.user)
    if request.method == "POST":
        form=InformacionForm(request.POST,request.FILES, instance=user)
        if form.is_valid:
            form.save()
            return redirect('profile_view')

    return redirect('/')
    