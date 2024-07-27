import json
import slack
import os
from flask import Flask, jsonify
from slackeventsapi import SlackEventAdapter

# configuring flask application
app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(
    os.environ["SIGNING_SECRET"], "/slack/events", app
)

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])
BOT_ID = client.api_call("auth.test")["user_id"]

client.chat_postMessage(channel="#watson-research", text="Backend is up! CE test")


@app.route("/health", methods=["GET"])
def health_check():
    # Additional health check logic can be added here
    return jsonify(status="healthy"), 200


@slack_event_adapter.on("message")
def message(payload):
    event = payload.get("event", {})
    user_id = event.get("user")
    text = event.get("text")

    if BOT_ID != user_id:
        client.chat_postMessage(channel="#watson-research", text=text)


if __name__ == "__main__":
    app.run(debug=True)
