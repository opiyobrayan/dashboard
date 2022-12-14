# Generated by Django 4.1.1 on 2022-09-26 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Database', '0008_alter_addparticipant_total_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thematic', models.CharField(choices=[('SRHR', 'SRHR'), ('HIV/TB', 'HIV/TB'), ('WLPR', 'WLPR'), ('SILU', 'SILU'), ('H&G', 'H&G')], max_length=100, verbose_name='Choose Thematic')),
                ('activity', models.CharField(max_length=100, verbose_name='Activity')),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=100, verbose_name='Options')),
                ('option_count', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main_Database.question')),
            ],
        ),
    ]
