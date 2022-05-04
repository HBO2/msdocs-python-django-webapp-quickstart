from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GrantId', models.CharField(max_length=255)),
                ('GrantName', models.CharField(max_length=255, null=True)),
                ('CrantStartDate', models.CharField(max_length=255, null=True)),
                ('GrantendDate', models.CharField(max_length=255, null=True)),
                ('UpdatedAt', models.DateTimeField()),
                ('GContractApplicationId', models.CharField(max_length=55, null=True)),
            ],          
        ),
    ],
    