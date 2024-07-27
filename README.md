# Watson Integration for SAP Enablement(WISE) on PowerVS

## Steps to create a slack app
1. Navigate to https://api.slack.com/ 
2. Click on 'Your Apps' button on top right corner
3. Click on 'Create New App' -> 'From scratch' -> provide the app name and the respective workspace -> click on 'Create App'
4. The above steps will land on a dashboard and 'Basic Information' page will be shown. Scroll down and click on 'Bots'
5. Step 4 will take you to 'App Home' page. We need to provide the slack bot the permissions to perform actions on a slack channel. Click on 'Review Scopes to Add' to proceed. 
6. Once the 'OAuth & Permissions' page is opened,
7. Event subscription - turn 'Enable Events' on
8. Subscribe to bot events
9. Reinstall your app to take these changes to take effect.

## Setup
```bash
pip3 install slackclient
pip3 install flask
pip3 install slackeventsapi
```