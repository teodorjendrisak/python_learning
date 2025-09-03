import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="0a2e5c6d5e824ba7bf48d95e1b4886a6",
                                               client_secret="ab72bbe16cf949bfa2937aad49a7e712",
                                               redirect_uri="https://localhost:8888/callback",
                                               scope="user-library-read"))

