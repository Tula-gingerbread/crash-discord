# crash-discord
## For educational purposes only!
## I'm not calling for anything!!

Just crash discord.
1. On [DDP](https://discord.com/developers/applications) create bot
2. Enable all `Privileged Gateway Intents` in `Bot` tab
3. OAuth2 tab -> OAuth2 URL Generator: `Scopes: bot`, `Bot permissions: Administrator`
4. Using this link add bot to server
5. In `Bot` tab reset and copy token
6. Set up config.py. To get UserID enable developer mode in your Discord client
7. Create env: `$ python -m venv env`
8. Change source to env: `$ source env/bin/activate`
9. Install libs: `$ pip install -r requirements.txt`
10. Run script: `$ python3 main.py`
11. Ready! In Discord client run slash command `/bot_info` to crash server. In console you see crash ETA.
