# Generated by Django 2.2.21 on 2021-10-09 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Book title', max_length=256)),
                ('auther_name', models.CharField(help_text='Auther name', max_length=256)),
                ('isbn_number', models.CharField(help_text='Book ISBN Number', max_length=256)),
                ('genre', models.CharField(blank=True, help_text='Book genre', max_length=256, null=True)),
                ('discription', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libraries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Library Name here', max_length=256)),
                ('city', models.CharField(help_text='Enter Library City Here', max_length=256)),
                ('state', models.CharField(help_text='Enter Library State Here', max_length=256)),
                ('postal_code', models.CharField(help_text='Enter Library Postal code Here', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('BOOK_IN', 'in'), ('BOOK_OUT', 'out')], default='BOOK_IN', max_length=256)),
                ('checked_out', models.DateTimeField()),
                ('checked_in', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LibraryBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ManyToManyField(blank=True, null=True, related_name='books', to='libraryApp.Books', verbose_name='Books library have')),
                ('last_library_activity', models.ManyToManyField(related_name='last_activity', to='libraryApp.LibraryActivity')),
                ('library', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='library', to='libraryApp.Libraries', verbose_name='Lirary-book pool')),
            ],
        ),
        migrations.AddField(
            model_name='libraryactivity',
            name='library_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryApp.LibraryBooks'),
        ),
        migrations.AddField(
            model_name='libraryactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
