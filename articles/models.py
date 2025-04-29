from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    autor=models.ForeignKey("User.CustomUser",related_name="autor", on_delete=models.CASCADE)
    tipo=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)

    
class Likes(models.Model):
    liked=models.ForeignKey("Articles", related_name="articulo", on_delete=models.CASCADE)
    liker=models.ForeignKey("User.CustomUser", related_name="liker", on_delete=models.CASCADE)

class Comments(models.Model):
    content=models.TextField()
    autor=models.ForeignKey("User.CustomUser", on_delete=models.CASCADE)
    commented=models.ForeignKey("Articles", related_name="comentado",on_delete=models.CASCADE)
