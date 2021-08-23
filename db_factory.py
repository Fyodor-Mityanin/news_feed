import factory
import factory.django

from news.models import News


class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News

    title = factory.Faker('name')
    text = factory.Faker('text')
