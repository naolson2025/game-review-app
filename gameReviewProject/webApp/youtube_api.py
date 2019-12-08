# Used Google documentation on how to use their YouTube API
import requests
import os
import googleapiclient.discovery
from .models import Search


def main():
    # Get the user's last search
    user_search = Search.objects.latest('video_search')
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ.get('YOUTUBE_API_KEY')

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        eventType="completed",
        maxResults=5,
        order="viewCount",
        q=f'{user_search}',
        type="video",
        videoEmbeddable="true"
    )
    response = request.execute()

    video_ids = clean_json(response)

    return video_ids



def clean_json(youtube_json):
    # When a video search is conducted 5 videos will be returned. Loop through the json 5 times to get all 5 video ids
    # put those 5 ids into a list and return that list to main()
    # The list of video ids will then be sent to views.py where they will be embedded into make_review.html
    # The user will then be able to pick which video they want to associate with their video game review
    video_id_list = []
    id = 0
    while id < 5:
        video_id_list.append(youtube_json['items'][id]['id']['videoId'])
        id += 1

    return video_id_list



if __name__ == "__main__":
    main()
