import factory
from models.category import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = factory.Faker('name')
    color = factory.Faker('color')
    symbol = factory.Faker('symbol')
