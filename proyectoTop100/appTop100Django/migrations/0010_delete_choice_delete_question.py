# Generated by Django 5.1.2 on 2024-12-03 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTop100Django', '0009_question_choice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
