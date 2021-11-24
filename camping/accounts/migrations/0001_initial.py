# Generated by Django 3.2.8 on 2021-11-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampingPlace',
            fields=[
                ('label', models.IntegerField(db_column='LABEL', primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, db_column='TYPE', max_length=20, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=200, null=True)),
                ('phone', models.CharField(blank=True, db_column='PHONE', max_length=50, null=True)),
                ('url', models.CharField(blank=True, db_column='URL', max_length=200, null=True)),
                ('info1', models.CharField(blank=True, max_length=200, null=True)),
                ('avg', models.FloatField(blank=True, db_column='AVG', null=True)),
                ('info2', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'CAMPING_PLACE',
                'managed': False,
            },
        ),
    ]
