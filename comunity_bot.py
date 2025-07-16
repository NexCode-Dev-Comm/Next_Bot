import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers import SchedulerAlreadyRunningError
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1277521890608681001

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
scheduler = AsyncIOScheduler(timezone="Europe/Bucharest")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await bot.change_presence(status=discord.Status.online)
    try:
        scheduler.start()
        print("✅ Scheduler started")
    except SchedulerAlreadyRunningError:
        print("⚠️ Scheduler already running — skip starting again")

    schedule_reminders()

async def send_reminder(message):
    try:
        channel = await bot.fetch_channel(CHANNEL_ID)
        await channel.send(message)
    except Exception as e:
        print(f"⚠️ Error sending reminder: {e}")

def schedule_reminders():
    loop = asyncio.get_event_loop()

    scheduler.add_job(
        lambda: asyncio.run_coroutine_threadsafe(
            send_reminder("🔔 Reminder: Be ready! Our IT meetup is tomorrow at 18:30! "), loop
        ),
        'cron',
        day_of_week='tue',
        hour=18,
        minute=30,
    )

    scheduler.add_job(
        lambda: asyncio.run_coroutine_threadsafe(
            send_reminder("💻 Get ready! Our IT meetup starts in 5 hours at 18:30! See you there!"), loop
        ),
        'cron',
        day_of_week='wed',
        hour=13,
        minute=30,
    )

    scheduler.add_job(
        lambda: asyncio.run_coroutine_threadsafe(
            send_reminder("⏰ Almost time! Our IT meetup starts in 1 hour at 18:30! "), loop
        ),
        'cron',
        day_of_week='wed',
        hour=17,
        minute=30,
    )

    scheduler.add_job(
        lambda: asyncio.run_coroutine_threadsafe(
            send_reminder("🌙 Tuesday 22:00 reminder! Don't forget to rest! Tomorrow meet-up!"), loop
        ),
        'cron',
        day_of_week='tue',
        hour=22,
        minute=0,
    )

@bot.command()
async def check(ctx):
    await ctx.send("✅ Bot works!")

bot.run(TOKEN)
