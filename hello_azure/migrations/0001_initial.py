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
       
            name='ProjectContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectContractId', models.CharField(max_length=255)),
                ('ProjectContractName', models.CharField(max_length=255, null=True)),
                ('ContractStartDate', models.CharField(max_length=255, null=True)),
                ('ContractEndDate', models.CharField(max_length=255, null=True)),
                ('UpdatedAt', models.DateTimeField()),
                ('GrantApplicationId', models.CharField(max_length=255, null=True)),
            ],
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TestId', models.CharField(max_length=255)),
                ('TestName', models.CharField(max_length=255, null=True)),
                ('TestStartDate', models.CharField(max_length=255, null=True)),
                ('TestendDate', models.CharField(max_length=55, null=True)),
                ('TestApplicationId', models.CharField(max_length=55, null=True)),
            ]
        )
    ],
    