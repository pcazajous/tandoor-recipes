from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0243_auto_20261018_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='step_recipe_factor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=16),
        ),
    ]
