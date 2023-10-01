from django import forms
from django.contrib.auth.models import User
class UserRegister(models.Model):
    username=forms.CharField(max_length=20)
    last_name =forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100)
    class Meta:
        models = User
        fields = ['username', 'email', 'first_name', 'last_name','password', 'password_confirmation']
class UserupdateForm(models.Model):
    email = forms.EmailField(max_length=100)
    class Meta:
        models = User
        fields = ['email','username']
class ProfileUpdateForm(models.Model):
    class Meta:
        model = Profile
        fields = ['profile_image']
class checkimage(models.Model):
    class Meta :
        model = CheckImage
        fields = ['image']
class CommentForm(models.Model):
    content = forms.CharField(max_length=300)
    class Meta:
        models = content
        fields= ['content']