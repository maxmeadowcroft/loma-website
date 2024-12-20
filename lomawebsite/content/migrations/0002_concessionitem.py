# Generated by Django 5.1.1 on 2024-12-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConcessionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('popcorn', 'Popcorn'), ('combo', 'Combo'), ('candy', 'Candy'), ('drink', 'Drink'), ('other', 'Other')], max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('extra_info', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
