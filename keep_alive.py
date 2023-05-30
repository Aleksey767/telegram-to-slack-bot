from flask import Flask, request, Response
from threading import Thread
import slack_sdk as slack
import json
import subprocess
import os
import signal
import sqlite3
import time
from threading import Thread

pid = 0


def start_listening_msg():
    global pid
    pid = subprocess.Popen(['python', 'parcing.py']).pid


def stop_listening_msg():
    global pid
    os.kill((pid), signal.CTRL_C_EVENT)


start_listening_msg()


def start_join():
    subprocess.Popen(['python', 'join_channel.py'])


def start_leave():
    subprocess.Popen(['python', 'leave_channel.py'])


def add_channel_from_bd(channel_link):
    connect = sqlite3.connect('database.db', timeout=10)
    cursor = connect.cursor()
    sqlite_insert_query = f"""insert into list (name) values('{channel_link}');"""
    cursor.execute(sqlite_insert_query)
    connect.commit()
    cursor.close()
    return print('Add to database: 🧑‍💻 ' + channel_link)


client = slack.WebClient(
    token='your_token')


app = Flask('')


@app.route('/', methods=['GET'])
def test_server():
    return Response("Server are working"), 200


@app.route('/activity', methods=['POST', 'GET'])
def activity():
    data = request.form
    trigger_id = data.get('payload')
    new_data = json.loads(trigger_id)
    try:
        if new_data['type'] == 'view_submission' and new_data['view']['title']['text'] == "Add new chat":
            block_id = new_data['view']['blocks'][0]['block_id']
            value = new_data['view']['state']['values'][f'{block_id}']['title']['value']
            stop_listening_msg()
            add_channel_from_bd(value)
            start_join()
            time.sleep(2)
            start_listening_msg()

    except Exception as err:
        print(err)

    try:
        if new_data['type'] == 'view_submission' and new_data['view']['title']['text'] == "Delete chat":
            block_id = new_data['view']['blocks'][0]['block_id']
            value = new_data['view']['state']['values'][f'{block_id}']['title']['value']
            stop_listening_msg()
            add_channel_from_bd(value)
            start_leave()
            time.sleep(2)
            start_listening_msg()
    except Exception as err:
        print(err)

    if new_data['type'] == 'shortcut' and new_data['callback_id'] == 'add':
        print('The request to add was triggered')
        client.views_open(trigger_id=new_data["trigger_id"],
                          view={
            "title": {
                "type": "plain_text",
                "text": "Add new chat"
            },
            "submit": {
                "type": "plain_text",
                "text": "Send"
            },
            "blocks": [{
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "title",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "For example - https://t.me/any_channel"
                    }
                },
                "label": {
                    "type": "plain_text",
                    "text": "Input link"
                }
            }],
            "type":
            "modal"
        })

    elif new_data['type'] == 'shortcut' and new_data['callback_id'] == 'delete':
        print('The request to delete was triggered')
        client.views_open(trigger_id=new_data["trigger_id"],
                          view={
            "title": {
                "type": "plain_text",
                "text": "Delete chat"
            },
            "submit": {
                "type": "plain_text",
                "text": "Send"
            },
            "blocks": [{
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "title",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "For example - https://t.me/any_channel"
                    }
                },
                "label": {
                    "type": "plain_text",
                    "text": "Input link"
                }
            }],
            "type":
            "modal"
        })
    return Response(), 200


def run():
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)


def keep_alive():
    t = Thread(target=run)
    t.start()
