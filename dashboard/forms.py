from django.forms import ModelForm
from .models import Todo
from django import forms

class TodoForm(ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"text",
        "name":"title",
        "placeholder":"Title"
    }),label="Title")

    memo = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control",
        "type":"text",
        "name":"memo",
        "placeholder":"Memo",
        "maxlength":"140",
        "rows":"4"
    }),label="Memo")

    # important = forms.BooleanField(widget=forms.CheckboxInput(attrs={
    #     "class":"custom-control-input",
    #     "type":"checkbox",
    #     "name":"important",
    #     "placeholder":""
    # }),label="Important")

    class Meta:
        model = Todo
        fields = ['title','memo']
