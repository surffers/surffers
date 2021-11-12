from django.forms import ModelForm

from .models import Category, Bookmark

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
     


class BookmarkForm(ModelForm):

    class Meta:
        model = Bookmark
        fields = ['title', 'url']

    def __init__(self, *args, **kwargs):
        super(BookmarkForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['title'].widget.attrs.update({
                "placeholder": "Bookmark title",
                'class': "input"
        })
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['url'].widget.attrs.update({
                "placeholder": "Url address",
                'class': "input",
                "autocomplete": "off"
        })



       
      








