# Generated by Django 3.0.4 on 2020-03-15 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kudo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('awarded', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kudos_given', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kudos_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-awarded'],
            },
        ),
    ]
