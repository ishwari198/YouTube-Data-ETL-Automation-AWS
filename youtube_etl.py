import os
import googleapiclient.discovery
import pandas as pd
import s3fs 

def run_youtube_etl():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ""

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    # Initialize an empty list to store video data
    videos_data = []

    # Initialize an empty string for the page token
    page_token = ""

    # Loop through pages of results
    while True:
        request = youtube.search().list(
            part="snippet",
            q="Elon Musk",
            maxResults=50,
            type="video",
            pageToken=page_token,
        )
        response = request.execute()

        # Extract video details and add to the list
        for item in response['items']:
            video_id = item['id']['videoId']
            video_request = youtube.videos().list(
                part="statistics",
                id=video_id
            )
            video_response = video_request.execute()
            video_item = video_response['items'][0]
            videos_data.append({
                'title': item['snippet']['title'],
                'video_id': video_id,
                'description': item['snippet']['description'],
                'like_count': video_item['statistics'].get('likeCount', 'N/A'),

                'comment_count': video_item['statistics'].get('commentCount', 'N/A')
            })

        # Check if there is a next page, if not, break the loop
        page_token = response.get('nextPageToken')
        if not page_token:
            break

    # Convert to DataFrame
    df = pd.DataFrame(videos_data)

    # Write DataFrame to CSV
    df.to_csv('s3://ishwari-airflow-youtube-bucket/elon_musk_videos.csv', index=False)
