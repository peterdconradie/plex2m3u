# config.py
HOST = "http://192.168.xxx.xxx:32400"  # URL of your Plex Media Server, replace with your own address
TOKEN = "xxxxxxxxxxxxxxxxxxxx"  # Plex token for authentication.
PLEX_MUSIC_ROOT = '/plex/media/'  # Base directory for music files on the Plex server but excludes the music folder (see TARGET_DIR below)
REPLACE_WITH_DIR = '../'  # Path prefix to replace PLEX_MUSIC_ROOT.
ASCIIFY = False  # Convert non-ASCII characters to ASCII.
WRITE_ALBUM = True  # Include album information in the playlist file.
WRITE_ALBUM_ARTIST = True  # Include album artist information.
TARGET_DIR = "/plex/media/music/"  # Destination for exported playlists.
