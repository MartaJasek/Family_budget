# Generated by Django 3.1 on 2020-09-27 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_auto_20200926_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_login', models.CharField(max_length=50, unique=True)),
                ('owner_email', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.owner'),
        ),
    ]
