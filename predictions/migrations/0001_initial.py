from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('team', models.CharField(max_length=10, null=True, verbose_name='Team')),
                ('position', models.CharField(max_length=10, null=True, verbose_name='Position')),
                ('gp', models.IntegerField(verbose_name='Games Played')),
                ('pre_ranking', models.IntegerField(verbose_name='Pre-Ranking')),
                ('points', models.FloatField(verbose_name='Points')),
                ('owners', models.FloatField(verbose_name='Owners')),
                ('actual_ranking', models.IntegerField(verbose_name='Actual Ranking')),
                ('passyds', models.IntegerField(verbose_name='Passing Yards')),
                ('passtd', models.IntegerField(verbose_name='Passing Touchdowns')),
                ('passint', models.IntegerField(verbose_name='Passing Interceptions')),
                ('rushyds', models.IntegerField(verbose_name='Rushing Yards')),
                ('rushtd', models.IntegerField(verbose_name='Rushing Touchdowns')),
                ('recepts', models.IntegerField(verbose_name='Receiving Interceptions')),
                ('recyds', models.IntegerField(verbose_name='Receiving Yards')),
                ('rectd', models.IntegerField(verbose_name='Receiving Touchdowns')),
                ('returntd', models.IntegerField(verbose_name='Returning Touchdowns')),
                ('two_pt', models.IntegerField(verbose_name='2-point Plays')),
                ('fumble', models.IntegerField(verbose_name='Fumbles')),
                ('pos_QB', models.IntegerField(verbose_name='QB')),
                ('pos_RB', models.IntegerField(verbose_name='RB')),
                ('pos_TE', models.IntegerField(verbose_name='TE')),
                ('pos_WR', models.IntegerField(verbose_name='WR')),
                ('pos_WR_RB', models.IntegerField(verbose_name='Wide Receiver, Runningback')),
                ('pos_WR_TE', models.IntegerField(verbose_name='Wide Receiver, Tight End')),
                ('prediction', models.FloatField(verbose_name='prediction')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('backgroundImage', models.CharField(max_length=200)),
            ],
        ),
    ]