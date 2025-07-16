# 🤖 Community Scheduler Bot

A simple Discord bot that automatically sends scheduled reminders to your community — perfect for organizing meetups, events, or study groups.  

Built with:
- **discord.py** for Discord interactions
- **APScheduler** for scheduling messages
- **dotenv** for easy environment variable management

---

## 🚀 Features

- Sends automated reminders to a specific channel on a weekly schedule.
- Customizable messages and times using `APScheduler`.
- Simple command `!check` to verify that the bot is online.
- Status updates when the bot is online.

---

## 🗓️ Default reminders

The bot is pre-configured to send the following reminders:

- **Tuesday at 18:30** — "🔔 Reminder: Be ready! Our IT meetup is tomorrow at 18:30!"
- **Wednesday at 13:30** — "💻 Get ready! Our IT meetup starts in 5 hours at 18:30! See you there!"
- **Wednesday at 17:30** — "⏰ Almost time! Our IT meetup starts in 1 hour at 18:30!"
- **Tuesday at 22:00** — "🌙 Tuesday 22:00 reminder! Don't forget to rest! Tomorrow meet-up!"

---

## ⚙️ Setup

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/community-scheduler-bot.git
cd community-scheduler-bot
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Dependencies include:

discord.py

apscheduler

python-dotenv

3️⃣ Create a .env file
env
Copy
Edit
DISCORD_TOKEN=your_discord_bot_token_here
💡 Note: You can get your Discord bot token from the Discord Developer Portal.

4️⃣ Configure channel ID
Update the CHANNEL_ID variable in main.py to the ID of your target channel:

python
Copy
Edit
CHANNEL_ID = 1277521890608681001
✅ Usage
Start the bot
bash
Copy
Edit
python main.py
When started, it will:

Log in to Discord

Start the scheduler

Begin sending reminders automatically

Available commands
diff
Copy
Edit
!check
Replies with ✅ Bot works!

🛡️ Permissions
Make sure your bot has:

Permission to read and send messages in the target channel.

The Message Content Intent enabled in the Developer Portal.

💬 Contributing
Pull requests and improvements are welcome!
Feel free to suggest new features or improve existing ones.

⚡ License
MIT License.
