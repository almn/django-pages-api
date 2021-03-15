# Generated by Django 3.1.7 on 2021-03-15 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('counter', models.IntegerField(default=0)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_app.contentitem_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ContentItemOnPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_by', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contentitem')),
            ],
            options={
                'ordering': ('sort_by',),
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('contentitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.contentitem')),
                ('bitrate', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.contentitem',),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('contentitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.contentitem')),
                ('content', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.contentitem',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('contentitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.contentitem')),
                ('video_file', models.CharField(max_length=250)),
                ('srt_file', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.contentitem',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('items', models.ManyToManyField(related_name='related_items', through='app.ContentItemOnPage', to='app.ContentItem')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='contentitemonpage',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.page'),
        ),
    ]