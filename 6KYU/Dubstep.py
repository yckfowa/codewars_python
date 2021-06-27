def song_decoder(song):
    song = song.split('WUB')
    initial_song = []
    for i in song:
        if i != '':
            initial_song.append(i)
    return ' '.join(initial_song)
