# Generated by Django 3.0.3 on 2020-04-05 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seznam_kontaktu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'permissions': [('can_see_contacts', 'Can see all contacts')]},
        ),
    ]