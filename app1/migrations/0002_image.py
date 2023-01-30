# Generated by Django 4.1.4 on 2023-01-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
