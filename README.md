# Simple Discord Bot - README

This is a simple Discord bot that can perform the following actions: say hello, roll a die, add numbers, and divide numbers. The bot responds to specific keywords and modifiers in messages.

# Commands

To interact with the bot, use the following keywords:

1. `hello`: The bot responds with a friendly greeting.
2. `roll`: The bot rolls a six-sided dice and responds with the result (a random number from 1 to 6).
3. `add`: The bot adds any numbers included in the message and responds with the result.
4. `div`: The bot divides any numbers included in the message and responds with the result.
5. `mul`: The bot multiplies any numbers included in the message and responds with the result.
6. `sub`: The bot subtracts any numbers included in the message and responds with the result.

# How to Use

1. Add the bot to your Discord server.
2. Use the bots' commands by typing the desired keyword followed by any necessary parameters.

   For example: 
      
      To roll a die, send the message: `roll`
   
      To add numbers, send the message: `add 5 10 15`
   
      To divide numbers, send the message: `div 20 2`
   
      To multiply numbers, send the message: `mul 3 4`
   
      To subtract numbers, send the message: `sub 100 30`

3. If you want the bot to send the messages privately, prefix your message with a question mark `?`.   
   For example: `?hello`

The bot will respond with the appropriate message in the same channel where the command was issued or in a private message if the command is prefixed with `?`.

# Deployment

To deploy this bot, follow these steps:

note: the first ```"$"``` is just a line indicator, do not copy it
      Also, 

1. Create a new Discord application and bot on the [Discord Developer Portal.](https://discord.com/developers/applications)
2. Copy the bot token generated by Discord and save it.
3. Clone the GitHub Repository and cd into it.
   ```
   $ git clone https://github.com/TheSurlyGent/discordbot.git
   ```
   ```
   $ cd discordbot
   ```
4. Make and Activate the Python Virtual Environment.
   ```
   $ python3 -m venv venv
   ```
   On Windows:
   ```
   $ venv\Scripts\activate
   ```
   On Linux:
   ```
   $ source venv/bin/activate
   ```   
5. Install the required libraries by running the following command in your terminal or command prompt:
   ```
   $ pip install discord
   ```
6. Set the TOKEN from discord in the virtual environment. (Optional if your TOKEN is added directly to the code)

   Windows:
   ```
   $ $env:TOKEN="YOURTOKENHERE"
   ```
   Linux:
   ```
   $ export TOKEN="YOURTOKENHERE"
   ```

7. Run the bot by executing the following command in the terminal:

   ```
   $ python3 main.py
   ```
   

The bot should be up and running, and you can start interacting with it on your Discord server.

# Additional Information

For any additional help or to display the list of available commands, send the bot the message `help`. The bot will respond with the list of keywords and a brief explanation of each command.

Feel free to customize the bot and add more features as per your requirements. Happy coding!
