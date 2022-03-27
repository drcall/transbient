from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('long_name', models.CharField(max_length=35)),
                ('short_name', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('call_name', models.CharField(max_length=20)),
                ('long', models.IntegerField()),
                ('lat', models.IntegerField()),
                ('service_status', models.CharField(max_length=12)),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transit.route')),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('long', models.IntegerField()),
                ('lat', models.IntegerField()),
                ('code', models.IntegerField()),
                ('routes', models.ManyToManyField(to='transit.route')),
                ]
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('start', models.IntegerField(default=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
