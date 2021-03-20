# Generated by Django 3.1.7 on 2021-03-20 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favo4', '0002_favorite4_posttwi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=25, verbose_name='サブクラス')),
                ('sub_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='サブクラス画像')),
            ],
            options={
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='copyright',
            field=models.CharField(default='設定されてません', max_length=100, verbose_name='権利表記'),
        ),
        migrations.AddField(
            model_name='content',
            name='hashtag',
            field=models.CharField(default='#F4', max_length=20, verbose_name='ハッシュタグ'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=15, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='content',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
        migrations.AddField(
            model_name='chara',
            name='subclass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='favo4.subclass', verbose_name='サブクラス'),
        ),
    ]
