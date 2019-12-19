from django.test import TestCase
from unittest.mock import patch, call
from .youtube_api import clean_json
import unittest
from django.urls import reverse
from .models import Review
from django.contrib.auth.models import User

class TestYouTubeAPI(TestCase):

    # This is an example api response with only 1 youtube video returned
    # The clean_json method should return the 1 video id gQ_1zX-F_No
    # @patch('youtube_api.api')
    @patch('webApp.youtube_api')
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



class TestMakeReviewPageIsEmpty(TestCase):

    fixtures = ['test_user']

    def setUp(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)

    def test_make_review_page_is_empty(self):
        # Call the url
        response = self.client.get(reverse('blank_new_review'))
        # Make sure the template is correct
        self.assertTemplateUsed(response, 'webApp/make_review.html')
        # Make sure that the page displays "No videos were returned"
        self.assertContains(response, 'No videos were returned')


# Test passes!
class TestAllReviews(TestCase):
    # Created a json file that has a review in it
    fixtures = ['test_user','test_reviews']

    def test_contains_reviews(self):
        # Call the all_reviews url
        response = self.client.get(reverse('all_reviews'))
        # Make sure the url renders the correct template
        self.assertTemplateUsed(response, 'webApp/all_reviews.html')
        # Check the info in the test_reviews.json file
        self.assertContains(response, 'Super Wizard')
        self.assertContains(response, 'picture')
        self.assertContains(response, 'RPG')
        self.assertContains(response, 'great game')
        self.assertContains(response, '10')
        self.assertContains(response, '1x2x3x4x5x6')
        self.assertNotContains(response, 'Lame game')



# Test passes!
class TestAllReviewsBlank(TestCase):

    def test_all_reviews_defaults_to_blank(self):
        response = self.client.get(reverse('all_reviews'))
        self.assertTemplateUsed(response, 'webApp/all_reviews.html')
        # Test that when the all_reviews.html page displays with no data the message below is shown
        self.assertContains(response, 'There are no reviews in the database.')

# Test if a blank form is submitted for making a review.

# Test passes!
class TestMyReviews(TestCase):
    # Created a json file that has a review in it
    fixtures = ['test_user', 'test_reviews']

    def setUp(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)

    def test_contains_reviews(self):
        # Call the my_reviews url
        response = self.client.get(reverse('my_reviews'))
        # Make sure the url renders the correct template
        self.assertTemplateUsed(response, 'webApp/my_reviews.html')
        # Check the info in the test_reviews.json file
        self.assertContains(response, 'Super Wizard')
        self.assertContains(response, 'picture')
        self.assertContains(response, 'RPG')
        self.assertContains(response, '10')
        self.assertNotContains(response, 'Lame game')
        self.assertNotContains(response, '5')


# Test passes!
class TestMyReviewsBlank(TestCase):

    fixtures = ['test_user']

    def setUp(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)

    def test_my_reviews_defaults_to_blank(self):
        response = self.client.get(reverse('my_reviews'))
        self.assertTemplateUsed(response, 'webApp/my_reviews.html')
        # Test that when the all_reviews.html page displays with no data the message below is shown
        self.assertContains(response, 'You have not made any reviews.')


# Test passes!
class TestAddNewReview(TestCase):

    fixtures = ['test_user']

    def setUp(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)

    def test_add_new_review(self):
        response = self.client.post(reverse('make_review'), \
        {'game_name': 'Doom', 'game_summary': 'Defeat demons', 'reviewers_opinion': 'good game', 'rating': 10, 'photo': 'picture', 'video_id': '1x2x3x4x5x6'}, \
        follow=True)
        self.assertTemplateUsed(response, 'webApp/my_reviews.html')
        response_reviews = response.context['my_reviews']
        # There is one review in the POST above so the below should = 1
        self.assertEqual(len(response_reviews), 1)
        # The game name in the POST above is Doom
        game_name = response_reviews[0]
        # Test the game name is in the database
        doom_in_database = Review.objects.get(game_name='Doom')
        # make sure the game name matches the pull from the database
        self.assertEqual(game_name, doom_in_database)
