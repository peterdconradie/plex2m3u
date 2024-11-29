
# Plex2m3u

A Python script to export audio playlists from Plex Media Server as `.m3u` files. Playlists are saved to a target directory and optionally adjusted for compatibility with your local music folder structure.

## Features

- Export Plex audio playlists as `.m3u` files.
- Include album and artist information in playlists.
- Optionally convert non-ASCII characters to ASCII.
- Automatically move playlists to a specified directory, replacing existing files.

## Requirements

- Python 3.x
- Plex Media Server
- Plex API Token ([How to find your Plex token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/))

## Installation

Clone this repository:
   ```bash
   git clone https://github.com/peterdconradie/Plex2M3U.git
   cd Plex2M3U 
   ```
## Screenshot
![Screenshot of terminal](terminal_screenshot)


## Configuration

Before running the script, adjust the configuration section in `plex2m3u.py`:

```python
# Configuration
HOST = "http://<your-plex-server-address>:32400"  # URL of your Plex Media Server.
TOKEN = "<your-plex-token>"  # Plex token for authentication (replace with your actual token).
# Learn how to find your token here: https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
PLEX_MUSIC_ROOT = '/Volumes/media/'  # Base directory for music files on the Plex server. Update for your server
# Note: This should exclude the specific music folder (e.g., use '/drive/plex' instead of '/drive/plex/music').
REPLACE_WITH_DIR = '../'  # Path prefix to replace PLEX_MUSIC_ROOT in the exported playlist.
# Keep it as '../' if your playlists will be stored in the root folder of your music directory (as is the case for the TARGET_DIR).
ASCIIFY = False  # Set to True to convert non-ASCII characters to ASCII (e.g., ä -> ae).
WRITE_ALBUM = True  # If True, include album information in the playlist file.
WRITE_ALBUM_ARTIST = True  # If True, include album artist information in the playlist file.
TARGET_DIR = "/Volumes/media/music/"  # Destination directory for the exported playlists. Update for your server

```

## Usage

Navigate to the plex2m3u folder in your terminal and run the script with:
```bash
python3 plex2m3u.py
```
Or write 
```bash
python3
```
in the terminal and drag the plex2m3u.py file into the terminal to find the exact location and subsequebtly run the file. 

Follow the prompts to select and export playlists. Exported `.m3u` files will be moved to the specified target directory.

## Acknowledgment

This script was adapted from the original work by [evolve700](https://github.com/evolve700/PlexPlaylistExport/tree/main), made available under the GPL-3.0 license.

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for details.
