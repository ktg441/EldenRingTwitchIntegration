import asyncio
import twitchio
from twitchio.ext import pubsub
from Handle_File_Data import *
from ER_CE_Integration import *

tokens = get_keys()

my_token = tokens["Access"] # Access token here
users_channel_id = int(tokens["ChannelID"]) # Your channel ID here
client = twitchio.Client(token=my_token)
client.pubsub = pubsub.PubSubPool(client)

@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
    if (event is None or event.reward.title is None):
        return
        
    print (event.reward.title)
    print (event.input)
    
    try:
        if (event.reward.title == "Set Character HP" and event.input.isnumeric()):
            SetHP(int(event.input))
        
        if (event.reward.title == "Set Character Runes" and event.input.isnumeric()):
            SetRunes(int(event.input))
    except:
        print ("Failed to change memory")

async def main():
    topics = [
        pubsub.channel_points(my_token)[users_channel_id],
    ]
    
    print ("Running...")
    
    await client.pubsub.subscribe_topics(topics)
    await client.start()
    
client.loop.run_until_complete(main())