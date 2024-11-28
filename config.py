# Configuration
HOST = "http://<your-plex-server-address>:32400"  # URL of your Plex Media Server.
TOKEN = "<your-plex-token>"  # Plex token for authentication (replace with your actual token).
# Learn how to find your token here: https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
PLEX_MUSIC_ROOT = '/Volumes/media/'  # Base directory for music files on the Plex server.
# Note: This should exclude the specific music folder (e.g., use '/drive/plex' instead of '/drive/plex/music').
REPLACE_WITH_DIR = '../'  # Path prefix to replace PLEX_MUSIC_ROOT in the exported playlist.
# Keep it as '../' if your playlists will be stored in the root folder of your music directory (as is the case for the TARGET_DIR).
ASCIIFY = False  # Set to True to convert non-ASCII characters to ASCII (e.g., ä -> ae).
WRITE_ALBUM = True  # If True, include album information in the playlist file.
WRITE_ALBUM_ARTIST = True  # If True, include album artist information in the playlist file.
TARGET_DIR = "/drive/plex/music/"  # Destination directory for the exported playlists.