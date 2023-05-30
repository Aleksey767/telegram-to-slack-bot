from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import sqlite3
import asyncio


def get_last_channel():
    connect = sqlite3.connect('database.db', timeout=10)
    cursor = connect.cursor()
    cursor.execute("select name from list order by id  desc limit 1;")
    result = cursor.fetchone()
    cursor.close()
    return " ".join(result)


async def join_channel():
    api_id = 12345678
    api_hash = 'your_api_hash'
    phone = '+375446666666'
    channel_link = get_last_channel()
    client_tg = TelegramClient(phone, api_id, api_hash)
    await client_tg.start()
    entity = await client_tg.get_entity(channel_link)
    await client_tg(JoinChannelRequest(entity))
    print('Start follow 👀 ' + channel_link)
    client_tg.disconnect
    return 0


async def main():
    task = asyncio.create_task(join_channel())
    await task

asyncio.run(main(), debug=True)
