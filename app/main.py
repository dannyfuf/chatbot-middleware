import os
from typing import Union
from fastapi import FastAPI
from asyncio import create_task
from dotenv import load_dotenv
load_dotenv()

# custom modules
from routers.users import users
from discord.discord_bot import bot

app = FastAPI()

app.include_router(
    users,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@app.get("/")
def read_root():
    return {"description": "Farm Middleware"}

async def start_bot():
    await bot.start(os.getenv("DISCORD_TOKEN"))

create_task(start_bot())