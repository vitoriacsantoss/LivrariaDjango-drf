# Generated by Django 5.0.6 on 2024-09-10 17:53

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_alter_user_passage_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="passage_id",
            field=models.CharField(
                default=uuid.UUID("28e01e63-b072-40e8-92ce-2cfbbf5e94cd"),
                help_text="Passage ID",
                max_length=255,
                unique=True,
                verbose_name="passage_id",
            ),
        ),
        migrations.CreateModel(
            name="Compra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Carrinho"), (2, "Realizado"), (3, "Pago"), (4, "Entregue")], default=1
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="compras", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
