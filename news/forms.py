from django import forms
from django.forms.fields import ChoiceField

from .models import News

PAGE_CHOICES = (
    ('10', '10'),
    ('20', '20'),
    ('50', '50'),
)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            'title',
            'text',
            'image',
        )


class PageForm(forms.Form):
    news_on_page = forms.ChoiceField(choices=PAGE_CHOICES, label='Новостей на странице')
