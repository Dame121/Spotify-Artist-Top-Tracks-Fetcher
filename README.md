# Spotify Artist Top Tracks Fetcher

This project uses the Spotify API to search for an artist by name and retrieve their top 10 tracks. It demonstrates how to authenticate with Spotify, search for artists, and fetch track details using Spotify's public API.

## Features

- Authenticate with Spotify's API using `client_credentials` flow.
- Search for artists by name.
- Retrieve and display the top 10 tracks of the artist.
- Handle errors gracefully with clear error messages.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.12 installed (or any compatible version of Python).
- A Spotify Developer Account to create an app and obtain `CLIENT_ID` and `CLIENT_SECRET`.
- An `.env` file with your Spotify credentials.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/spotify-top-tracks-fetcher.git
    cd spotify-top-tracks-fetcher
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root of the project and add your Spotify credentials:

    ```bash
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    ```

4. Run the script:

    ```bash
    python main.py
    ```

5. Enter the name of the artist when prompted, and the program will display their top 10 tracks.

## Usage

1. Run the script and input an artist's name.
2. The program will retrieve and display the artist's top 10 tracks.
   
## Example

```bash
Enter the artist you want to see the top 10 songs: Drake
Top 10 Tracks:
1. God's Plan
2. In My Feelings
3. Hotline Bling
...
```

## Dependencies

- `dotenv` for environment variable management.
- `requests` for sending HTTP requests.
- `base64` for encoding client credentials.

You can install the required dependencies with:

```bash
pip install python-dotenv requests
```

## License

This project is licensed under the MIT License.

---

**Repository Name**: `spotify-top-tracks-fetcher`
