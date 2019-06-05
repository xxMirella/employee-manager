# Generated by Django 2.2.1 on 2019-06-05 04:04

from django.db import migrations


def populate_country(apps, schema_editor):
    country = apps.get_model('core', 'Country')
    country.objects.create(name='Brasil')


def populate_state(apps, schema_editor):
    state = apps.get_model('core', 'State')
    countrys = apps.get_model('core', 'Country')
    country = countrys.objects.first()
    state.objects.create(name='São Paulo', country=country)
    state.objects.create(name='Rio de Janeiro', country=country)


def populate_city(apps, schema_editor):
    city = apps.get_model('core', 'City')
    states = apps.get_model('core', 'State')
    state = states.object.get(name='São Paulo')
    city.objects.create(name='São Paulo', state=state)
    city.objects.create(name='Guarulhos', state=state)
    city.objects.create(name='Santos', state=state)


def populate_address(apps, schema_editor):
    address = apps.get_model('core', 'Address')
    cities = apps.get_model('core', 'City')
    for city in cities.objects.all():
        address.objects.create(
            street='Rua 1', number=40, neighborhood='Vila Jardim Terra', zip_code=14528774, city=city
        )
        address.objects.create(
            street='Rua 2', number=90, neighborhood='Vila Jardim Céu', zip_code=24563887, city=city
        )
        address.objects.create(
            street='Rua 1', number=140, neighborhood='Vila Jardim Vento', zip_code=87965224, city=city
        )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_country),
        migrations.RunPython(populate_state),
    ]
