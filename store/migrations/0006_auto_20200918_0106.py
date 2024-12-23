# Generated by Django 3.0.8 on 2020-09-17 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0005_auto_20200917_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='purchased_item',
            name='user',
        ),
        migrations.AddField(
            model_name='purchased_item',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='purchased_item',
            name='address',
        ),
        migrations.AddField(
            model_name='purchased_item',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.ShippingAddress'),
        ),
        migrations.AlterField(
            model_name='purchased_item',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.Product'),
        ),
    ]
