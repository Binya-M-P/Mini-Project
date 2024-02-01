# Generated by Django 4.2.5 on 2023-11-02 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0008_menutbl_cidf_alter_menutbl_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menutbl',
            name='cidf',
        ),
        migrations.AddField(
            model_name='menutbl',
            name='cn',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='menutbl',
            name='cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page1.category'),
        ),
    ]
