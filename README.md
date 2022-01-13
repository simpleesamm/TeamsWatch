# TeamsWatch
Autoclick Teams to stay online &amp; watch the teams chat for changes forwarding messages as images to your Telegram via a bot. Reply to the bot to a specific chat (1,2 or 3) and the message will be forwarded to Teams.

## Features
1. Autoclick Teams at **user specified position** to **stay Available** at all times,
2. Watch Teams (or any other app) for **new messages** (via pixel matching)
  - Watch any user specified region
  - Clicks on the latest chat or user specified position
3. Sends screenshots of new message directly to your **telegram** via a bot (needs some setup)
  - https://www.geeksforgeeks.org/send-message-to-telegram-user-using-python/ follow this link to setup your telegram bot

## See demo: 
https://drive.google.com/file/d/1EBRhvVPC4b4MBBB6vNn1Mr6YMUgh7AtJ/view?usp=sharing - watching teams and auto clicker
https://drive.google.com/file/d/1ZQOvVkRdY0Z6_toBMuHu3Hl7y4D33lIC/view?usp=sharing - replying to the telegram bot and it will forward the message to your specified chat

## Usage guidelines:
1. Once everything is setup (Bot, pip installs) run the code.
2. Click over to your teams or anything you want to watch for changes. (You have one click - Semi primitive but your clicks after that one click will be tracked and used)
3. Select the region to watch 
  - Top Left of the region
  - Bottom Right of the region
4. Select chat 1
6. Select chat 2
7. Select chat 3
8. Select the area where you want your autoclicker to move to and click on constantly to keep Available or stop your computer from sleeping.
9. **Scroll** to stop the mouse tracker. 
10. Leave your mouse cursor in the region where you speicifed in step 3 and let the code do the watching :)

_Replying to a Person_
To select chat 1 -> "**#1:** Your message" 
To select chat 2 -> "**#2:** Your message"
If you dont use the "#1:" message will just be defaulted to the first chat

In total you should have 7 clicks including the one to click over to teams or any app.

### Current days spent on this project: 2
Currently using multi threading to watch both the telegram bot and the teams chat at the same time.
