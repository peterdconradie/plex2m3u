"""
Plex Playlist Export Script

This script connects to a Plex Media Server and allows users to export audio playlists
to M3U files. The playlists can be customized to include album and artist information 
and are moved to a specified target directory. Non-ASCII characters can be converted 
to ASCII if desired.

Original Code Attribution:
This script is based on the original work by evolve700, which is available at:
https://github.com/evolve700/PlexPlaylistExport/tree/main
The original code is licensed under the GPL-3.0 license.

Enhancements and modifications have been made to simplify usage, support file replacement, 
and improve compatibility for specific setups.
"""




import os
import argparse
import shutil
import requests
from plexapi.server import PlexServer
from unidecode import unidecode
from config import (
    HOST, TOKEN, PLEX_MUSIC_ROOT, REPLACE_WITH_DIR, ASCIIFY,
    WRITE_ALBUM, WRITE_ALBUM_ARTIST, TARGET_DIR
)

# Rest of your script remains unchanged
 


def do_asciify(input_string):
    """Converts a string to its ASCII representation."""
    if input_string is None:
        return None
    replaced = input_string.replace('Ä', 'Ae').replace('ä', 'ae')
    replaced = replaced.replace('Ö', 'Oe').replace('ö', 'oe')
    replaced = replaced.replace('Ü', 'Ue').replace('ü', 'ue')
    return unidecode(replaced)

def list_playlists():
    """List all audio playlists available on the Plex server."""
    try:
        print("Connecting to Plex...", end="")
        plex = PlexServer(HOST, TOKEN)
        print(" done.")
        playlists = plex.playlists()
        print("\nAvailable Playlists:")
        audio_playlists = [p.title for p in playlists if p.playlistType == "audio"]
        for idx, title in enumerate(audio_playlists, start=1):
            print(f"{idx}. {title}")
        return audio_playlists
    except Exception as e:
        print(f"Failed to connect or retrieve playlists. Error: {e}")
        return []

def export_playlist(playlist_name):
    """Export a selected playlist as an M3U file."""
    try:
        print(f"Connecting to Plex to export '{playlist_name}'...", end="")
        plex = PlexServer(HOST, TOKEN)
        playlist = plex.playlist(playlist_name)
        print(" done.")
        
        playlist_title = do_asciify(playlist.title) if ASCIIFY else playlist.title
        extension = "m3u"
        encoding = "ascii" if ASCIIFY else "utf-8"
        file_path = f"{playlist_title}.{extension}"
        with open(file_path, 'w', encoding=encoding) as m3u:
            m3u.write("#EXTM3U\n")
            m3u.write(f"#PLAYLIST:{playlist_title}\n\n")
            for item in playlist.items():
                seconds = int(item.duration / 1000)
                title = do_asciify(item.title) if ASCIIFY else item.title
                album = do_asciify(item.parentTitle) if ASCIIFY else item.parentTitle
                artist = do_asciify(item.grandparentTitle) if ASCIIFY else item.grandparentTitle
                if WRITE_ALBUM:
                    m3u.write(f"#EXTALB:{album}\n")
                if WRITE_ALBUM_ARTIST:
                    m3u.write(f"#EXTART:{artist}\n")
                for part in item.media[0].parts:
                    m3u.write(f"#EXTINF:{seconds},{artist} - {title}\n")
                    m3u.write(f"{part.file.replace(PLEX_MUSIC_ROOT, REPLACE_WITH_DIR)}\n\n")
        print(f"Playlist '{playlist_title}' exported to {file_path}.")

        # Move the file to the target directory, replacing if it exists
        destination = os.path.join(TARGET_DIR, file_path)
        if os.path.exists(destination):
            os.remove(destination)  # Remove the existing file
        shutil.move(file_path, TARGET_DIR)
        print(f"Moved {file_path} to {TARGET_DIR} (existing file replaced).")

    except Exception as e:
        print(f"Failed to export playlist. Error: {e}")


def export_all_playlists():
    """Export all audio playlists as M3U files."""
    try:
        print("Connecting to Plex to export all playlists...", end="")
        plex = PlexServer(HOST, TOKEN)
        print(" done.")
        
        playlists = [p for p in plex.playlists() if p.playlistType == "audio"]
        if not playlists:
            print("No audio playlists found.")
            return

        for playlist in playlists:
            print(f"Exporting playlist: {playlist.title}")
            export_playlist(playlist.title)
        print("All playlists have been exported.")
    except Exception as e:
        print(f"Failed to export all playlists. Error: {e}")

def main():
    playlists = list_playlists()
    if not playlists:
        return
    while True:
        try:
            print("\nOptions:")
            print("0. Export all playlists (CAUTION: depending on playlist size and amount, could be very slow)")
            for idx, title in enumerate(playlists, start=1):
                print(f"{idx}. {title}")
            choice = input("\nEnter the number of the playlist to export (or type 'exit' to exit): ")
            if choice.lower() == "exit":
                print("Exiting...")
                break
            if choice == "0":
                export_all_playlists()
                break
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(playlists):
                print("Invalid choice. Please enter a valid number.")
                continue
            selected_playlist = playlists[int(choice) - 1]
            export_playlist(selected_playlist)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
if __name__ == "__main__":
    main()