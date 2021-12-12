from django.forms import ModelForm
from django import forms
from .models import Category, Bookmark, Comment


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['title'].widget.attrs.update({
                "placeholder": "Category title",
                'class': "input"
        })
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['body'].widget.attrs.update({
                "placeholder": "Short description",
                'class': "textarea"
        })
     

class BookmarkForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea is-medium'}), required=False)
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'body', 'tags']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['body'].widget.attrs.update({
                "placeholder": "What do you think about it?",
                'class': "textarea",
                'title': "Write a comment"
            })








