from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0242_space_household_setup_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='step_recipe_factor',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=16),
        ),
    ]
