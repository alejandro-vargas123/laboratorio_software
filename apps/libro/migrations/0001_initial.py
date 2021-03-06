# Generated by Django 3.1.3 on 2020-11-29 02:19

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id_autor', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=20, null=True, unique=True, verbose_name='Cedula')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=220)),
                ('nacimiento', models.DateField(null=True, verbose_name='Fecha de nacimiento')),
                ('ciudad', models.CharField(choices=[('Armenia', 'Armenia'), ('Barranquilla', 'Barranquilla'), ('Bello', 'Bello'), ('Bogotá', 'Bogotá'), ('Bucaramanga', 'Bucaramanga'), ('Cali', 'Cali'), ('Cartagena', 'Cartagena'), ('Cúcuta', 'Cúcuta'), ('Ibagué', 'Ibagué'), ('Manizales', 'Manizales'), ('Medellín', 'Medellín'), ('Montería', 'Montería'), ('Neiva', 'Neiva'), ('Cartagena', 'Cartagena'), ('Pasto', 'Pasto'), ('Pereira', 'Pereira'), ('Santa Marta', 'Santa Marta'), ('Soacha', 'Soacha'), ('Soledad', 'Soledad'), ('Valledupar', 'Valledupar'), ('Villavicencio', 'Villavicencio')], default='1', max_length=200, verbose_name='Ciudad de residencia')),
                ('genero', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino'), ('Otro', 'Otro')], max_length=15, null=True, verbose_name='Genero')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='Correo Electrónico')),
                ('temas_preferidos', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Historia y Geografía', 'Historia y Geografía'), ('Narrativa', 'Narrativa'), ('Juvenil', 'Juvenil'), ('Ciencias físicas', 'Ciencias físicas'), ('Infantil', 'Infantil'), ('Ciencias Sociales y política', 'Ciencias Sociales y política'), ('Medicina y salud', 'Medicina y salud'), ('Filosofía', 'Filosofía'), ('Arquitectura', 'Arquitectura'), ('Arte', 'Arte'), ('Gastronomía', 'Gastronomía'), ('Varios', 'Varios')], max_length=157, null=True, verbose_name='Temas de preferencia')),
                ('usuario', models.CharField(max_length=100, null=True, unique=True, verbose_name='Nombre de usuario')),
                ('contrasena', models.CharField(max_length=30, null=True, verbose_name='Contrasena')),
                ('suscripcion', models.BooleanField(blank=True, default=False, null=True, verbose_name='Suscribirme a noticias')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='tarjeta',
            fields=[
                ('id_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, null=True, verbose_name='Nombre de la tarjeta')),
                ('caducidad', models.DateField(null=True, verbose_name='Fecha de caducidad')),
                ('tipo_tarjeta', models.CharField(choices=[('Debito', 'Debito'), ('Credito', 'Credito')], default='Credito', max_length=30, verbose_name='Tipo de tarjeta')),
                ('saldo', models.IntegerField(null=True, verbose_name='Saldo')),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.autor')),
            ],
            options={
                'verbose_name': 'Tarjeta',
                'verbose_name_plural': 'Tarjetas',
            },
        ),
        migrations.CreateModel(
            name='libro',
            fields=[
                ('issn', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255, null=True, verbose_name='Titulo')),
                ('paginas', models.IntegerField(null=True, verbose_name='Paginas')),
                ('editorial', models.CharField(choices=[('Norma', 'Norma'), ('Planeta', 'Planeta'), ('Alfaomega', 'Alfaomega'), ('Mundo libro', 'Mundo libro'), ('Penguin', 'Penguin'), ('Kinesis', 'Kinesis'), ('Andina', 'Andina'), ('Deusto', 'Deusto'), ('Maeva', 'Maeva'), ('Ariel', 'Ariel'), ('Critica', 'Critica'), ('Salamandra', 'Salamandra')], default=None, max_length=200, verbose_name='Editorial')),
                ('idioma', models.CharField(choices=[('Espanol', 'Espanol'), ('Ingles', 'Ingles')], default='Espanol', max_length=20, verbose_name='Idioma')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha publicacion')),
                ('es_nuevo', models.BooleanField(default=True, verbose_name='Nuevo')),
                ('precio', models.IntegerField(null=True, verbose_name='Precio del libro')),
                ('cantidad', models.IntegerField(null=True, verbose_name='Cantidad de ejemplares')),
                ('agotado', models.BooleanField(default=False, verbose_name='Agotado')),
                ('genero', models.CharField(choices=[('Historia y Geografía', 'Historia y Geografía'), ('Narrativa', 'Narrativa'), ('Juvenil', 'Juvenil'), ('Ciencias físicas', 'Ciencias físicas'), ('Infantil', 'Infantil'), ('Ciencias Sociales y política', 'Ciencias Sociales y política'), ('Medicina y salud', 'Medicina y salud'), ('Filosofía', 'Filosofía'), ('Arquitectura', 'Arquitectura'), ('Arte', 'Arte'), ('Gastronomía', 'Gastronomía'), ('Varios', 'Varios')], default=None, max_length=50, verbose_name='Generos')),
                ('autor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
