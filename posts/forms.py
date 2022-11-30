from django import forms
from posts.models import Category

CATEGORY_CHOICES = (
    (category.id, category.title) for category in Category.objects.all()
)


class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=150, min_length=10)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    rate = forms.FloatField()
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)


class CommentCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Введите отзыв', max_length=255)
