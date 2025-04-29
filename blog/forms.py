from django import forms
from articles.models import Articles
from User.models import CustomUser
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Articles
        fields=['title','description']
class InformacionForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','description','phone_number','picture']
        help_texts={
            'username':''
        }