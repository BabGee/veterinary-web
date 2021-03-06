# Generated by Django 3.1.3 on 2021-01-21 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0003_auto_20210120_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surgical_Approach_Form',
            fields=[
                ('vet_form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portals.vet_forms')),
                ('species_operated_on', models.CharField(choices=[('0', 'cattle'), ('1', 'sheep'), ('2', 'goat'), ('3', 'donkey'), ('4', 'dog'), ('5', 'horse'), ('6', 'poultry'), ('7', 'others')], default='0', max_length=20)),
                ('num_of_animals_operated_on', models.IntegerField(default=1)),
                ('operation_nature', models.CharField(choices=[('C', 'c_section'), ('I', 'interstinal_torsion'), ('T', 'tumor_extraction'), ('C', 'canine_spaying'), ('H', 'hernia'), ('W', 'Warts_etraction'), ('C', 'castration'), ('S', 'skin_injuries'), ('F', 'fructure'), ('R', 'rumenatomy'), ('O', 'other')], default='0', max_length=20)),
                ('if_other_specify', models.CharField(blank=True, max_length=100, null=True)),
                ('operation_date', models.DateTimeField()),
                ('post_operation_management', models.CharField(default='', max_length=100)),
                ('prognosis', models.CharField(default='', max_length=100)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
