# Generated by Django 5.1.2 on 2024-11-30 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTop100Django', '0006_alter_cancion_estilo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_votos', models.IntegerField(default=0)),
                ('cancion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='votos', to='appTop100Django.cancion')),
            ],
        ),
    ]
