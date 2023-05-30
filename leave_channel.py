from telethon.sync import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
import sqlite3
import asyncio


def get_last_channel():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("select name from list order by id  desc limit 1;")
    result = cursor.fetchone()
    cursor.close()
    return " ".join(result)


def del_channel_from_bd(channel_link):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    sqlite_insert_query = f"""delete from list where name = '{channel_link}';"""
    cursor.execute(sqlite_insert_query)
    connect.commit()
    cursor.close()
    return print('Deleted from database: 😈 ' + channel_link)


async def join_channel():
    api_id = 12345678
    api_hash = 'your_api_hash'
    phone = '+375446666666'
    channel_link = get_last_channel()
    client_tg = TelegramClient(phone, api_id, api_hash)
    await client_tg.start()
    entity = await client_tg.get_entity(channel_link)
    await client_tg(LeaveChannelRequest(entity))
    print('Unfollowed to channel 😤 ' + channel_link)
    del_channel_from_bd(channel_link)
    client_tg.disconnect
    return 0


async def main():
    task = asyncio.create_task(join_channel())
    await task

asyncio.run(main(), debug=True)
