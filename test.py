from pytube.contrib.playlist import Playlist
from aiogram.types.input_media import InputMediaAudio
# print(my_playlist, '\n', playlist_url, '\n', Owner, '\n', Length, '\n', video_urls, '\n', videos, '\n')
async def download_playlist(url):
    videos = Playlist(url).videos
    files = []
    media_group = []
    for yt in videos:
        try:
            output_path = 'media/playlist'
            filename = f'{yt.title}.mp3'
            yt.streams.get_audio_only().download(output_path=output_path, filename=filename)
            file_path = f'{output_path}/{filename}'
            files.append(file_path)
            # input_file = InputMediaAudio(media=open(file_path, 'wb'))
            # media_group.append(input_file)
        except Exception as ex:
            print(ex)
    return files


