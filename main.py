import requests
import time

# Telegram API key and channel information
telegram_token = 'TELEGRAM_BOT_API_TOKEN'
telegram_channel = '@YourChannelUsername'

# Discord Webhook URL
discord_webhook_url = 'DISCORD_WEBHOOK_URL'

# To store the ID of the last checked message
last_message_id = None


def delete_telegram_webhook():
    url = f'https://api.telegram.org/bot{telegram_token}/deleteWebhook'
    response = requests.get(url)
    data = response.json()
    print("Delete webhook response:", data)
    return data['ok']


def get_telegram_messages():
    global last_message_id
    url = f'https://api.telegram.org/bot{telegram_token}/getUpdates?offset={last_message_id + 1 if last_message_id else 0}'
    response = requests.get(url)
    data = response.json()
    print("Telegram response:", data)

    if data['ok']:
        messages = data['result']
        new_messages = []
        for message in messages:
            if 'channel_post' in message:
                post = message['channel_post']
                if last_message_id is None or post['message_id'] > last_message_id:
                    new_messages.append(post)
                    last_message_id = post['message_id']
        return new_messages
    return []


def format_telegram_message(message):
    text = message.get('text', '')
    entities = message.get('entities', [])

    # Parse entities to format embedded links correctly for Discord
    if entities:
        entities.sort(key=lambda x: x['offset'], reverse=True)  # Reverse sorting by offset
        for entity in entities:
            if entity['type'] == 'text_link':
                url = entity['url']
                offset = entity['offset']
                length = entity['length']
                link_text = text[offset:offset + length]
                formatted_link = f"[{link_text}](<{url}>)"
                text = text[:offset] + formatted_link + text[offset + length:]
            elif entity['type'] == 'url':
                offset = entity['offset']
                length = entity['length']
                url = text[offset:offset + length]
                formatted_link = f"<{url}>"
                text = text[:offset] + formatted_link + text[offset + length:]

    return text


def send_to_discord(content):
    data = {
        "content": content
    }
    response = requests.post(discord_webhook_url, json=data)
    print("Discord response status:", response.status_code)
    print("Discord response content:", response.text)
    return response.status_code == 204


def main():
    if delete_telegram_webhook():
        while True:
            messages = get_telegram_messages()
            for message in messages:
                text = format_telegram_message(message)
                if text:
                    print("Sending to Discord:", text)
                    send_to_discord(text)
            time.sleep(10)  # Wait 10 seconds and check again
    else:
        print("Failed to delete existing webhook.")


if __name__ == '__main__':
    main()
