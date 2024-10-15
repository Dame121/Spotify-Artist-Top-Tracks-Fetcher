from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    if not client_id or not client_secret:
        raise ValueError("CLIENT_ID or CLIENT_SECRET environment variables not set.")

    # Prepare the authorization string and encode it to base64
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    try:
        # Send POST request to obtain the token
        result = post(url, headers=headers, data=data)
        result.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response JSON
        json_result = result.json()
        token = json_result["access_token"]
        return token
    except Exception as e:
        # Print the response text and status code for debugging
        print(f"An error occurred: {e}")
        if result is not None:
            print(f"Response Status Code: {result.status_code}")
            print(f"Response Content: {result.text}")
        return None

def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=1"
    query_url = f"{url}?{query}"

    try:
        result = get(query_url, headers=headers)
        result.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response JSON
        json_result = result.json()

        # Extract the artist's name and ID
        artists = json_result.get("artists", {}).get("items", [])
        if artists:
            artist = artists[0]
            artist_name = artist.get("name", "No artist name found")
            artist_id = artist.get("id", None)
            
            print(f"Artist Name: {artist_name}")
            
            if artist_id:
                # Fetch top tracks for the artist
                fetch_top_tracks(token, artist_id)
            else:
                print("Artist ID not found.")
        else:
            print("No artist found.")
    except Exception as e:
        # Print the response text and status code for debugging
        print(f"An error occurred: {e}")
        if result is not None:
            print(f"Response Status Code: {result.status_code}")
            print(f"Response Content: {result.text}")

def fetch_top_tracks(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = get_auth_header(token)
    params = {"market": "US"}

    try:
        result = get(url, headers=headers, params=params)
        result.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response JSON
        json_result = result.json()

        # Extract and print the top 10 tracks
        tracks = json_result.get("tracks", [])
        if tracks:
            print("Top 10 Tracks:")
            for i, track in enumerate(tracks[:10], start=1):
                track_name = track.get("name", "No track name found")
                print(f"{i}. {track_name}")
        else:
            print("No tracks found.")
    except Exception as e:
        # Print the response text and status code for debugging
        print(f"An error occurred: {e}")
        if result is not None:
            print(f"Response Status Code: {result.status_code}")
            print(f"Response Content: {result.text}")

# Get the token and search for an artist
token = get_token()
if token:
    a=input("Enter the artist you want to see the top 10 songs::")
    search_for_artist(token, a)
else:
    print("Failed to retrieve the access token.")
