# Generated by Django 4.2.3 on 2023-08-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(
                related_name="get_posts", to="blog.category", verbose_name="Categorias"
            ),
        ),
    ]
