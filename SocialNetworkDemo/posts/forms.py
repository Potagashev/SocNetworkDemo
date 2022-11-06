from django import forms

from .models import Post


class CreatePostForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['category'].empty_label = 'категория не выбрана'
    #     # for changing some properties
    photo = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['text', 'photo']
        # widgets = {
        #     'photo': forms.FileInput(attrs={'required': 'false'})
        # }
