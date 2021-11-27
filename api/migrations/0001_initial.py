# Generated by Django 3.1.4 on 2021-11-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insuarance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_code', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('lab_name', models.CharField(max_length=50)),
                ('contact_info', models.CharField(max_length=10)),
                ('charges', models.IntegerField()),
                ('test_name', models.CharField(max_length=50)),
                ('testing_at', models.CharField(choices=[('PLACE', 'PLACE'), ('LAB', 'LAB')], default='LAB', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=10)),
                ('profile_pic', models.ImageField(default='default.ico', upload_to='transport/profile_image/')),
                ('address', models.CharField(max_length=50)),
                ('availability', models.CharField(max_length=50)),
            ],
        ),
    ]