# Generated by Django 3.1.3 on 2020-11-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_auto_20201126_0457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='id_libro',
            new_name='issn',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='libro',
            name='agotado',
            field=models.BooleanField(default=False, verbose_name='Estado si esta agotado'),
        ),
        migrations.AddField(
            model_name='libro',
            name='cantidad',
            field=models.IntegerField(null=True, verbose_name='Cantidad de ejemplares'),
        ),
        migrations.AddField(
            model_name='libro',
            name='editorial',
            field=models.CharField(choices=[('Norma', 'Norma'), ('Planeta', 'Planeta'), ('Alfaomega', 'Alfaomega'), ('Mundo libro', 'Mundo libro'), ('Penguin', 'Penguin'), ('Kinesis', 'Kinesis'), ('Andina', 'Andina'), ('Deusto', 'Deusto'), ('Maeva', 'Maeva'), ('Ariel', 'Ariel'), ('Critica', 'Critica'), ('Salamandra', 'Salamandra')], default=None, max_length=200, verbose_name='Editorial'),
        ),
        migrations.AddField(
            model_name='libro',
            name='es_nuevo',
            field=models.BooleanField(default=True, verbose_name='Nuevo o usado'),
        ),
        migrations.AddField(
            model_name='libro',
            name='genero',
            field=models.CharField(choices=[('Historia y Geografía', 'Historia y Geografía'), ('Narrativa', 'Narrativa'), ('Juvenil', 'Juvenil'), ('Ciencias físicas', 'Ciencias físicas'), ('Infantil', 'Infantil'), ('Ciencias Sociales y política', 'Ciencias Sociales y política'), ('Medicina y salud', 'Medicina y salud'), ('Filosofía', 'Filosofía'), ('Arquitectura', 'Arquitectura'), ('Arte', 'Arte'), ('Gastronomía', 'Gastronomía'), ('Varios', 'Varios')], default=None, max_length=50, verbose_name='Generos'),
        ),
        migrations.AddField(
            model_name='libro',
            name='idioma',
            field=models.CharField(choices=[('Espanol', 'Espanol'), ('Ingles', 'Ingles')], default='Espanol', max_length=20, verbose_name='Idioma'),
        ),
        migrations.AddField(
            model_name='libro',
            name='paginas',
            field=models.IntegerField(null=True, verbose_name='Paginas'),
        ),
        migrations.AddField(
            model_name='libro',
            name='precio',
            field=models.IntegerField(null=True, verbose_name='Precio del libro'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=255, null=True, verbose_name='Titulo'),
        ),
    ]
