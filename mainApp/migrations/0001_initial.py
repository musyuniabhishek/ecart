# Generated by Django 4.2 on 2023-05-01 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Maincategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('baseprice', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('finalprice', models.IntegerField()),
                ('stock', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('pic1', models.ImageField(upload_to='products')),
                ('pic2', models.ImageField(blank=True, default=None, null=True, upload_to='products')),
                ('pic3', models.ImageField(blank=True, default=None, null=True, upload_to='products')),
                ('pic4', models.ImageField(blank=True, default=None, null=True, upload_to='products')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.brand')),
                ('maincategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.maincategory')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory')),
            ],
        ),
    ]
