# Generated by Django 4.0.4 on 2022-06-20 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_calling', '0004_roommember_delete_videoconferenceroommember'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RoomMember',
            new_name='VideoConferenceRoomMember',
        ),
        migrations.RenameField(
            model_name='videoconferenceroommember',
            old_name='insession',
            new_name='in_session',
        ),
    ]