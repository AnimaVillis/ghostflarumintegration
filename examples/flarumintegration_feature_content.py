import requests
import json
from datetime import datetime, timedelta
import html2text

# Api keys
ghost_api_key = ''
flarum_api_key = ''
discord_webhook_url = ''  

# Api Endpoints
ghost_api_url = 'https://ghostdomain.pl/ghost/api/content/posts/?key=' + ghost_api_key
flarum_api_url = 'https://flarum_forum-link.com/api/discussions'

# Tags Flarum
flarum_tags = ["56"]

# JSON file to store post IDs
database_file = 'post_database.json'

def check_ghost_config():
    response = requests.get(ghost_api_url)
    if response.status_code != 200:
        raise Exception(f'Ghost API configuration error. Error code: {response.status_code}')

def get_ghost_posts():
    check_ghost_config()  # Dodaj to sprawdzenie przed próbą pobrania postów
    response = requests.get(ghost_api_url)
    posts = response.json()['posts']
    return posts

def load_post_database():
    try:
        with open(database_file, 'r') as file:
            post_database = json.load(file)
    except FileNotFoundError:
        post_database = []
    return post_database

def save_post_id(post_id):
    post_database = load_post_database()
    post_database.append(post_id)
    with open(database_file, 'w') as file:
        json.dump(post_database, file)

def is_post_added(post_id):
    post_database = load_post_database()
    return post_id in post_database

def send_discord_message(content, success=True):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'content': content,
        'username': 'Flarum Bot',
        'avatar_url': 'https://example.com/avatar.png'  # Replace with the appropriate avatar URL
    }
    if not success:
        data['content'] = f'❌ Error updating on Flarum forum:\n{content}'

    response = requests.post(discord_webhook_url, headers=headers, data=json.dumps(data))
    return response

def check_flarum_config():
    response = requests.get(flarum_api_url)
    if response.status_code != 200:
        raise Exception(f'Flarum API configuration error. Error Code: {response.status_code}')

def create_flarum_post(title, created_at, tags, feature_image, content):
    check_flarum_config()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {flarum_api_key}'
    }

    title = title[:80]

    # Convert HTML to Markdown using html2text
    markdown_content = html2text.html2text(content)

    # Add [img] tag to feature_image
    feature_image = f'[img]{feature_image}[/img]'

    data = {
        'data': {
            'type': 'discussions',
            'attributes': {
                'title': title,
                'content': f'{title}\n{feature_image}\n{markdown_content}',
                'createdAt': created_at.isoformat()
            },
            'relationships': {
                'tags': {
                    'data': [{'type': 'tags', 'id': tag_id} for tag_id in tags]
                }
            }
        }
    }

    response = requests.post(flarum_api_url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    ghost_posts = get_ghost_posts()
    post_database = load_post_database()

    for post in ghost_posts:
        post_id = post['id']

        # Check if the post has already been added
        print(f"Checking post {post_id}...")
        if is_post_added(post_id):
            print(f"Post {post_id} has already been added.")
            continue
        print(f"Post {post_id} is not yet added. Adding...")

        title = post['title']

        feature_image = post['feature_image']

        content = post['html']
        
        # Process the date in Ghost format
        created_at = datetime.fromisoformat(post['created_at'][:-6])

        # Adjust the time zone if necessary
        created_at += timedelta(hours=1)

        original_url = post['url']

        try:
            # Create a topic on the Flarum forum with tags
            response = create_flarum_post(title, created_at, flarum_tags, feature_image, content)

            # Save the post ID to the database
            save_post_id(post_id)

            # Log the Flarum response
            print(response)

            # Send a message to Discord after a successful update
            send_discord_message(f'✅ Post on the Flarum forum has been successfully updated!\n', success=True)

        except Exception as e:
            # Send a message to Discord after an unsuccessful update
            send_discord_message(f'❌ Error updating on the Flarum forum:\n{str(e)}', success=False)

            # Save the post ID to the database even after an error to avoid sending the same error multiple times
            save_post_id(post_id)
