# Generated by Django 4.0.5 on 2022-08-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=20)),
                ('company_code', models.CharField(max_length=20)),
                ('strength', models.IntegerField()),
                ('website', models.CharField(max_length=30)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]