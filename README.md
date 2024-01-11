# **Flarum Forum Updater**

## **Overview**

This script automates the process of updating your Flarum forum with posts from a Ghost blog. It fetches posts from the Ghost blog's API, creates corresponding topics on the Flarum forum, and sends update messages to a Discord channel. The script ensures that the same post is not updated multiple times.

## **Features**

- **Ghost Blog Integration:** Fetches posts from a Ghost blog using its API.
- **Flarum Forum Integration:** Creates topics on a Flarum forum with specified tags.
- **Discord Notifications:** Sends update messages to a Discord channel, indicating the success or failure of the forum update.
- **Post Tracking:** Prevents the same post from being updated on the forum multiple times.

## **Setup**

1. **API Keys:**
   - Obtain API keys for your Ghost blog, Flarum forum, and Discord webhook.
   - Replace the placeholder values in the script with your actual API keys.

2. **Flarum Tags:**
   - Specify the Flarum tag IDs you want to associate with the imported posts.

3. **Dependencies:**
   - Install the required Python packages using `pip install requests`.

4. **Run the Script:**
   - Execute the script to update your Flarum forum with the latest Ghost blog posts.

## **Configuration**

- **`ghost_api_key`:** API key for the Ghost blog.
- **`flarum_api_key`:** API key for the Flarum forum.
- **`discord_webhook_url`:** Webhook URL for Discord notifications.
- **`ghost_api_url`:** URL for Ghost blog API.
- **`flarum_api_url`:** URL for Flarum forum API.
- **`flarum_tags`:** List of tag IDs for Flarum posts.
- **`database_file`:** JSON file to store post IDs.

## **Usage**

1. Run the script using `python script_name.py`.
2. Monitor console logs for updates on post processing.
3. Check Discord for success or error notifications.

## **Important Note**

- The script adjusts the time zone of the post creation date to match your requirements.

## **Contributions**

Contributions are welcome! Feel free to open issues or submit pull requests.
