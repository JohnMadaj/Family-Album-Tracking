import reader
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

def spotipy_find_album(album_name):
    # Set up the parameters for the Spotify API request

    # Set up the Spotify API client with user authentication
    client_id = "0433e614f46845fca89d48326848ec31"
    client_secret = "27edb312cf614a039bc511e14255dcf2"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri="http://localhost:8080"))
    # Search for the album
    results = sp.search(q=album_name, type='album', market='US')
    print(results)

    # Check if there are any albums in the search results
    if not results['albums']['items']:
        print("No albums were found for the search query.")
    else:
        # Extract the total streams for the first album in the search results
        album_id = results['albums']['items'][0]['id']
        print(album_id)
        tracks = sp.album_tracks(album_id)
        # print(tracks)
        # print(tracks)
        for track in tracks["items"]:
            print(track["name"])
            for key, val in track.items():
                print(key, val)
            # print(track["name"], track["popularity"])

        # # Print the total streams
        # total_streams = sum([track['popularity'] for track in tracks['items']])
        # print("The album '{}' has a total of {} streams on Spotify.".format(album_name, total_streams))

if __name__ == '__main__':
    reader.file_reader("family_album_tracking.tsv")

    # for num, album in reader.justin_dict.items():
    #     print("\n", album)
    #     spotipy_find_album(album)
    a = reader.justin_dict["1"][1]
    print(reader.justin_dict["1"])
    spotipy_find_album(a)
