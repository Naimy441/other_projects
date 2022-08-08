import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


scopes = ['https://www.googleapis.com/auth/youtube.readonly']

def main():
    # Setup
    api_service_name = 'youtube'
    api_version = 'v3'
    client_secrets_file = 'client_secret.json'

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )

    credentials = flow.run_console()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )

    # Get playlists
    request = youtube.playlists().list(
        part='snippet',
        mine=True
    )

    response = request.execute()

    playlists = {}
    for playlist in response['items']:
        title = playlist['snippet']['title']
        id = playlist['id']
        playlists[title] = id

    # Get videos in each playlist
    for title, id in playlists.items():
        request = youtube.playlistItems().list(
            part='snippet',
            maxResults = 50,
            playlistId=id
        )

        response = request.execute()

        print(f'{title} : {id}')
        for video in response['items']:
            video_title = video['snippet']['title']
            print(f'  - {video_title}')
        print()

if __name__ == '__main__':
    main()
