# Generated by Django 5.0.6 on 2024-08-16 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_livro"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livro",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="livro",
            name="site",
        ),
        migrations.AddField(
            model_name="livro",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.categoria",
            ),
        ),
        migrations.AddField(
            model_name="livro",
            name="editora",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.editora",
            ),
        ),
        migrations.AddField(
            model_name="livro",
            name="isbn",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="preco",
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="quantidade",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="titulo",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
