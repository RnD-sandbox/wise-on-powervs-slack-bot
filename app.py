import json
import slack
import os
from pathlib import Path
from flask import Flask
from slackeventsapi import SlackEventAdapter

# configuring flask application
app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(
    os.environ["SIGNING_SECRET"], "/slack/events", app
)

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])
BOT_ID = client.api_call("auth.test")["user_id"]


@slack_event_adapter.on("message")
def message(payload):
    event = payload.get("event", {})
    user_id = event.get("user")
    text = event.get("text")

    if BOT_ID != user_id:
        client.chat_postMessage(channel="#watson-research", text=text)


if __name__ == "__main__":
    app.run(debug=True)
