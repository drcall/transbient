# Generated by Django 3.2.12 on 2022-03-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transit', '0003_auto_20220327_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='lat',
            field=models.DecimalField(decimal_places=17, max_digits=17),
        ),
        migrations.AlterField(
            model_name='stop',
            name='long',
            field=models.DecimalField(decimal_places=17, max_digits=17),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='lat',
            field=models.DecimalField(decimal_places=17, max_digits=17),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='long',
            field=models.DecimalField(decimal_places=17, max_digits=17),
        ),
    ]
