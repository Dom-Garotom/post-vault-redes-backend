# Generated by Django 5.2.4 on 2025-07-22 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post_delete_tarefa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='descricao',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
    ]
