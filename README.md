# **GHOST API + FLARUM API INTEGRATION**

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

5. **Install by pip**
   - 'pip install html2text' for convert html to bbcode
   - 'pip install requests' for requests from api.

## **Configuration**

- **`ghost_api_key`:** API key for the Ghost blog.
- **`flarum_api_key`:** API key for the Flarum forum.
- **`discord_webhook_url`:** Webhook URL for Discord notifications.
- **`ghost_api_url`:** URL for Ghost blog API.
- **`flarum_api_url`:** URL for Flarum forum API.
- **`flarum_tags`:** List of tag IDs for Flarum posts.
- **`database_file`:** JSON file to store post IDs.

## **Crontab Configuration**

### Crontab Header

Add the following crontab header at the beginning of the file:

```bash
# Sample crontab header for the Flarum Forum Updater
# ---------------------------
# M  H  D  M  W  COMMAND
# ---------------------------
```

### Configuration Steps
1. **Open crontab file:**

```bash
crontab -e
```

2. **Add crontab task:**
```bash
M H D M W COMMAND
```

M: Minute (0 - 59)

H: Hour (0 - 23)

D: Day of the month (1 - 31)

M: Month (1 - 12)

W: Day of the week (0 - 6) (0 is Sunday)

COMMAND: Command to be executed

3. **Save and close the crontab file.**

### Sample Crontab Configurations

1. **Run every hour:**
   ```bash
   0 * * * * /path/to/script.py
   ```
2. **Run daily at 3:30 AM:**
   ```bash
   30 3 * * * /path/to/script.py
   ```
3. **Run twice a day at 8 AM and 8 PM:**
   ```bash
   0 8,20 * * * /path/to/script.py
   ```

Feel free to customize the crontab configurations based on your specific scheduling needs.
