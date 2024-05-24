# Generated by Django 4.2.11 on 2024-05-21 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_dislike_article_alter_like_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='article',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='core.article'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='comment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='core.comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.article'),
        ),
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.comment'),
        ),
    ]