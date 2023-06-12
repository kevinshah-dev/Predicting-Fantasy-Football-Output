from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentstat',
            name='head_shot',
            field=models.CharField(default='https://toppng.com/uploads/preview/erreur-404-11550708744oo95egrxlp.png', max_length=500),
            preserve_default=False,
        ),
    ]