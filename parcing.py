import requests
from telethon.sync import TelegramClient, utils
from telethon import events
import sqlite3
api_id = 12345678
api_hash = 'your_api_hash'
phone = '+375446666666'


def data():
    connect = sqlite3.connect('database.db', timeout=10)
    cursor = connect.cursor()
    cursor.execute("select name from list;")
    c = cursor.fetchall()

    result = " ".join(str(x) for x in c)
    result = result.replace('(', "")
    result = result.replace(')', "")
    result = result.replace(',', "")
    result = result.replace("'", "")
    result = result.split(' ')
    return result


def telegram_parser(send_message_func=None, loop=None):
    client = TelegramClient(phone, api_id, api_hash, loop=loop)
    client.start()

    @client.on(events.NewMessage(chats=(data())))
    async def handler(event):

        if send_message_func is None:
            chat = await client.get_entity(event.chat_id)
            chat_from = event.chat if event.chat else (await event.get_chat())
            chat_title = utils.get_display_name(chat_from)
            if event.raw_text:
                headers = {'Content-type': 'application/json', }
                json_data = {
                    'unfurl_links': True,
                    "unfurl_media": True,
                    'text': f':love_letter: New message: \n:mega: Name of the channel: *{chat_title}*\n :speech_balloon: Text: {event.raw_text} \n :link: Link: <https://t.me/{chat.username}/{event.id}>', }
                requests.post(
                    'https://hooks.slack.com/services/your_hook', headers=headers, json=json_data,)
                print(f'New message in channel: {chat_title}\n')
        else:
            await send_message_func(f'@your_link\n{event.raw_text}')

    return client


if __name__ == "__main__":
    client = telegram_parser()
    client.run_until_disconnected()
