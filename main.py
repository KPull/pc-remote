import asyncio

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


def create_server():
    application = FastAPI()

    @application.get("/twitch")
    async def twitch(channel: str):
        await asyncio.create_subprocess_shell(F"streamlink -p mpv https://www.twitch.tv/{channel} best")
        return {"status": "OK"}

    @application.get("/shutdown")
    async def shutdown():
        await asyncio.create_subprocess_shell(F"shutdown now")
        return {"status": "OK"}

    return application


server = create_server()