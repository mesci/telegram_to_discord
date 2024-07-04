
# Telegram to Discord
This application instantly shares the content shared on your Telegram channel to your Discord channel via webhook.
## How to Use 

#### 1️⃣ Download the code and open it in your editor.
1.1 Create a bot with [@BotFather](https://t.me/BotFather) and get the token.

1.2 Get the handle of the Telegram channel you will use as the source channel. (Must be a public channel.)

1.3 Create a webhook for your Discord channel.

[> How to create webhook?](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
#### 2️⃣ Edit the following parts in the code.



```bash 
  telegram_token = 'TELEGRAM_BOT_API_TOKEN'
  telegram_channel = '@YourChannelUsername'
  discord_webhook_url = 'DISCORD_WEBHOOK_URL'
```

#### 3️⃣ Install the library.
```bash
  pip install requests
```
#### 4️⃣ Create virtual environment.
Navigate to the directory where you want to create the virtual environment.

Windows:
```bash
  python -m venv myenv
  myenv\Scripts\activate
```
Mac and Linux:
```bash
  python3 -m venv myenv
  source myenv/bin/activate
```
#### 5️⃣ Run the project.
```bash
  python main.py
```
## Feedback

📨 If you have any feedback, please reach out to:
```bash 
  mail(@)mesci.dev
```
