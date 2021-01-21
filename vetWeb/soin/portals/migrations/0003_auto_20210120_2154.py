# Generated by Django 3.1.3 on 2021-01-20 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0002_auto_20210119_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Death_Approach_Form',
            fields=[
                ('vet_form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portals.vet_forms')),
                ('species_dead', models.CharField(choices=[('0', 'cattle'), ('1', 'sheep'), ('2', 'goat'), ('3', 'donkey'), ('4', 'dog'), ('5', 'horse'), ('6', 'poultry'), ('7', 'others')], default='0', max_length=20)),
                ('num_of_species_dead', models.IntegerField(default=1)),
                ('case_history', models.CharField(default='', max_length=100)),
                ('mortality_rate', models.CharField(default='', max_length=100)),
                ('death_time', models.DateTimeField()),
                ('signs_of_cadever_on_the_ground', models.CharField(max_length=200)),
                ('carcass_opened_for_the_pm', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='0', max_length=5)),
                ('if_yes_pathological_signs', models.CharField(blank=True, max_length=100, null=True)),
                ('if_no_reason', models.CharField(blank=True, max_length=100, null=True)),
                ('sample_sent_lab', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='0', max_length=5)),
                ('if_yes_lab_report', models.CharField(blank=True, max_length=100, null=True)),
                ('death_cause_notifiable', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='0', max_length=5)),
                ('if_yes_message_to_relevant_body', models.CharField(blank=True, max_length=100, null=True)),
                ('intervention_regards_to_death', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='sick_approach_form',
            name='species_affected',
            field=models.CharField(choices=[('0', 'cattle'), ('1', 'sheep'), ('2', 'goat'), ('3', 'donkey'), ('4', 'dog'), ('5', 'horse'), ('6', 'poultry'), ('7', 'others')], default='0', max_length=20),
        ),
    ]