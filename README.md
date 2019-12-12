# game-review-app

To use this app follow these steps:

1. Install the dependancies
pip install -r requirements.txt

2. Sign up for a free YouTube API Key and set the environment variable matching below
YOUTUBE_API_KEY = "Your YouTube API key"

3. Set up the database
python manage.py makemigrations
python manage.py migrate

4. Run a local server
python manage.py runserver

5. Create an account using the "Sign Up" button

6. Create your own video game review using the "Make Reviews" button
