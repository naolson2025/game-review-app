from django.test import TestCase
from unittest.mock import patch, call
from .youtube_api import clean_json
import unittest

class TestYouTubeAPI(TestCase):

    # This is an example api response with only 1 youtube video returned
    # The clean_json method should return the 1 video id gQ_1zX-F_No
    # @patch('youtube_api.api')
    @patch('youtube_api.py')
    def test_response(self, mock_video_id_list):
        mock_video_id_list = ['gQ_1zX-F_No']
        example_api_response = {
            "kind": "youtube#searchListResponse",
            "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/L-gjb5oFk5FEbSTZcRP4LWKAmo0\"",
            "nextPageToken": "CAEQAA",
            "regionCode": "US",
            "pageInfo": {
            "totalResults": 1000000,
            "resultsPerPage": 1
            },
            "items": [
            {
            "kind": "youtube#searchResult",
            "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/IUPje0AHo3kVWZPuaOELZDozfa0\"",
            "id": {
                "kind": "youtube#video",
                "videoId": "gQ_1zX-F_No"
            },
            "snippet": {
                "publishedAt": "2019-12-05T19:00:10.000Z",
                "channelId": "UCo_q6aOlvPH7M-j_XGWVgXg",
                "title": "SURFING HAWAII’S BEST WAVE WITH MY GIRLFRIEND (PIPELINE)",
                "description": "SOME FUN BARRELS IN THE MORNING TO SOME LONG BOARDING, RAFTING, AND BOARD TRANSFERS IN THE AFTERNOON! NEW STAY PSYCHED ...",
                "thumbnails": {
                "default": {
                "url": "https://i.ytimg.com/vi/gQ_1zX-F_No/default.jpg",
                "width": 120,
                "height": 90
                },
                "medium": {
                "url": "https://i.ytimg.com/vi/gQ_1zX-F_No/mqdefault.jpg",
                "width": 320,
                "height": 180
                },
                "high": {
                "url": "https://i.ytimg.com/vi/gQ_1zX-F_No/hqdefault.jpg",
                "width": 480,
                "height": 360
                }
                },
                "channelTitle": "Jamie O'Brien",
                "liveBroadcastContent": "none"
            }
            }
            ]
        }
        # mock_video_id.side_effect = [example_api_response]
        video_id_list = clean_json(example_api_response)
        self.assertEqual(mock_video_id_list, video_id_list)

if __name__ == '__main__':
    unittest.main()

