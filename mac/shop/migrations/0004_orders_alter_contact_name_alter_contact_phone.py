# Generated by Django 4.1 on 2022-12-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact_alter_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=70)),
                ('zip_code', models.CharField(max_length=5000)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
    ]