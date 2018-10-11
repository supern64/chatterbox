-- Instructions on how to set up Chatterbox for your own --
(This version is heavily customizable. If you have trouble setting this up and is fine with uncustomizable options, use the default version (http://chanonlim.pythonanywhere.com/static/chatterbox.rar))

Prerequisites:
Python (3.7.0 and some other versions (>3.5.4) should work) (https://www.python.org/downloads/)
discord.py rewrite and chatterbot 0.8.7 
(To install these, after installing Python, open a command line in the chatterbox directory and type "pip3 install -r requirements.txt")

These are the files you should get when downloading and extracting Chatterbox:
1. README.txt - Guide to installation
2. chatterbox.py - Chatterbox bot itself
3. requirements.txt - Prerequisites for Python
4. config.json - Configuration file for bot
5. db.sqlite3 - English word database for Chatterbot module

1. Create a bot account (skip if you already have one)
- Go to https://discordapp.com/developers
- Login with your Discord account
- Click "Create an app"
- Set the name and avatar for your application. This will be the name shown when you invite the bot on the authorization page.
- On the left, click on "Bots"
- Click "Create a Bot", then click "Yes"
- Set the name and profile picture for your bot. This will be the actual name of the bot when you see it in a server.
- Set public bot to "on" if you want, but do NOT enable "requires oauth2 code grant".
*Don't forget to click "Save Changes" on the bottom of the screen after setting the name and avatar for both Application and bot!
- On the "Bot" menu in the "Token" section, click "Copy" (This is NOT the client secret!!!)

2. Set up Chatterbox
***PLEASE TAKE A LOOK AT THE JSON FORMAT BELOW!!!
- Open up config.json in any text editor
*DONT FORGET QUOTES HERE AND DONT DELETE ANYTHING!!!
- Paste the token you copied earlier after "token": "[your token here]"
- Type in the prefix after "prefix": "[your prefix here]"
- Type in the playing status after "status": "[your game name here]", leave it if you don't want status
- In this version, you can add custom responses and custom "I don't understand" message.
- Type in the name after "name": [your name here] to locate the name of the bot.
- Type in a list of responses if the bot does not understand the question after "not_understand_responses"
- Type in a list of custom responses as a list in the dictionary after "custom_responses"
- Don't edit the corpus if you want to use English. If you wish to use another language, edit it here.
***TOKEN, STATUS, PREFIX, NAME, NOT_UNDERSTAND_RESPONSES AND CORPUS ARE REQUIRED TO BE PRESENT!!!
- Save the file

3. Start the bot
- Open a command line window in the Chatterbox directory
- Type "py -3 chatterbox.py" into the command line
- The bot should start. If you are getting an error about JSON, look at the error part of this instruction.
- If it says "[your bot name] is ready!", that means you have successfully started up the bot. 

4. Getting the invite link
- If you haven't been getting any errors so far, you have successfully set up the bot.
- Now it's time to make an invite link.
- Go back to your Discord Developers page.
- Go to your application and click on "General Information"
- Copy the client ID, and put it in the form here:
https://discordapp.com/oauth2/authorize?client_id=[your client ID]&scope=bot&permissions=0
- Go to this link and invite it to your respective server.
- To use it, mention it or type [your prefix]chat [message to ask] or mention it with your question, and it should respond
- To retrain the bot, type [your prefix]train (It should take a while.)
Congratulations! You have successfully set up the bot! Use it to your enjoyment!

5. Maintainance
- To reset the bot's word database in case it gets messed up, download the original file from here:
https://chanonlim.pythonanywhere.com/static/db.sqlite3
- Then replace the db.sqlite3 in the Chatterbox folder with the one from the link (DO NOT CHANGE THE FILE NAME!!!)

Errors:
JSON error:
If you are getting a JSON error, it means the config.json failed to load.
Here is an example of a valid config.json (and no, this token is not valid):
{
    "token": "QiPdkDMfOPDmsuNfOfmFO-FVIVmbPfj_FfjFIFm.FydvkOV.FifKkfDIFkOFLVVF",
    "status": "with my boy",
    "prefix": "box",
    "bot_settings": {
        "name": "Jwindish",
        "not_understand_responses": ["Umm... Sorry but I don't really understand...",
                                    "I don't know what you mean."],
        "custom_responses": [
            {"Knock Knock!": "Who's that?"},
            {"THE DOOR": "I know it's an asdfmovie joke"}
        ],
        "corpus": "chatterbot.corpus.english"
    }
}
Double-check EVERYTHING.
Here is a list of common mistakes:
Use single-quotes instead of double-quotes. ONLY USE DOUBLE-QUOTES
Forgot the ",". DONT FORGET ","s.
You can try and use a JSON validator online (e.g. https://jsonformatter.org/).
If you have trouble with these errors or any other errors, please contact me on Discord, SuperNiintendo#3700



