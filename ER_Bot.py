import asyncio
import twitchio
from twitchio.ext import pubsub
from ER_CE_Integration import *

my_token = "[YOUR-TOKEN-HERE]"
users_channel_id = 0 # Your channel ID here
client = twitchio.Client(token=my_token)
client.pubsub = pubsub.PubSubPool(client)

@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
    if (event is None or event.reward.title is None):
        return
        
    print (event.reward.title)
    print (event.input)
    
    if (event.reward.title == "Set Character HP" and event.input.isnumeric()):
        SetHP(int(event.input))
    
    if (event.reward.title == "Set Character Runes" and event.input.isnumeric()):
        SetRunes(int(event.input))

async def main():
    topics = [
        pubsub.channel_points(my_token)[users_channel_id],
    ]
    
    print ("Running...")
    
    await client.pubsub.subscribe_topics(topics)
    await client.start()
    
client.loop.run_until_complete(main())