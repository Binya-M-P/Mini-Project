# Generated by Django 4.2.5 on 2023-11-04 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0009_remove_menutbl_cidf_menutbl_cn_alter_menutbl_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menutbl',
            name='cn',
        ),
        migrations.AlterField(
            model_name='menutbl',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scname', models.CharField(max_length=200)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page1.category')),
            ],
        ),
        migrations.AddField(
            model_name='menutbl',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page1.subcategory'),
        ),
    ]
