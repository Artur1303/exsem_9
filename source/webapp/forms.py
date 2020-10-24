from django import forms


from webapp.models import Photo


class ProductForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = []