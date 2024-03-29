# Generated by Django 2.2.3 on 2020-05-25 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Spec',
                'verbose_name_plural': 'Specs',
            },
        ),
        migrations.CreateModel(
            name='SpecContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec_contrnt', to='Product.Product', verbose_name='Product')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spen_content', to='Product.Spec', verbose_name='Spec')),
            ],
            options={
                'verbose_name': 'SpecContent',
                'verbose_name_plural': 'SpecContents',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='spec',
            field=models.ManyToManyField(related_name='category', to='Product.Spec', verbose_name='Spec'),
        ),
    ]
