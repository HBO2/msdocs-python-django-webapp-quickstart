from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_azure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='GrantendDate',
            field=models.DateTimeField(),
        ),
    ]