# Generated by Django 4.0 on 2021-12-28 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_delete_language_alter_author_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
