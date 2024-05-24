# Generated by Django 4.2.11 on 2024-05-17 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_like_dislike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='article',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dislike', to='core.article'),
        ),
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like', to='core.article'),
        ),
    ]