from EzCnc import CNC, better_disbot as disbot
import streamlit as st
import asyncio
import threading
import uvicorn
app = CNC(
    db_name="Database", name="EZCNC", debug=True, logs_path="EZCNC_logs"
)  # initiate the api
#app.generate_fake_clients(5)
api = app.api  # exporting the api class so that you can run   "uvicorn main:api"
Database = app.Database
TOKEN = "MTA4NTc0NjM0Nzg3OTE4MjM3Ng.GvOjde.nt4AmgrRi_dZYrVszef6h3uJ85dEp4lwjqaX1Q"

# Define a function to run the Discord bot
def run_discord_bot(db,guild__id:str):
    
    bot = disbot.BOT(db=db,guild_id=guild__id)
    bot.bot.run(TOKEN)


# Start the Discord bot in a separate thread
discord_thread = threading.Thread(target=run_discord_bot, args=(Database,"1085747808759455764"))
discord_thread.start()

# Start the API using uvicorn
if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)

