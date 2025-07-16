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
