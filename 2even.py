from telethon.sync import TelegramClient
from telethon import events
import time
import asyncio
from telethon.tl.functions.messages import SearchRequest 
from telethon.tl.types import InputMessagesFilterEmpty

api_id = 952378
api_hash='376ed6a57831aca11be812ff628eb53a'
phone = '+5355451278'
client = TelegramClient(phone, api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ('/fight' in event.raw_text):
        await client.send_message ("chtwrsbot", event.raw_text)


@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ('/fight' in event.raw_text):
        await client.send_message("Elder of Assassin Creed", event.raw_text)

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ('/fight' in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message("Amigos Chat", event.raw_text)

@client.on(events.NewMessage(chats=("Amigos Chat")))
async def handler(event):
    if ('HIGHNEST' in event.raw_text):
        await client.send_message('chtwrsbot', '🦅')

@client.on(events.NewMessage(chats=("Amigos Chat")))
async def handler(event):
    if ('MOONLIGHT' in event.raw_text):
        await client.send_message('chtwrsbot', '🌑')

@client.on(events.NewMessage(chats=("Amigos Chat")))
async def handler(event):
    if ('DEERHORN' in event.raw_text):
        await client.send_message('chtwrsbot', '🦌')

@client.on(events.NewMessage(chats=("Amigos Chat")))
async def handler(event):
    if ('WOLFPACK' in event.raw_text):
        await client.send_message('chtwrsbot', '🐺')

@client.on(events.NewMessage(chats=("Amigos Chat")))
async def handler(event):
    if ('POTATO' in event.raw_text):
        await client.send_message('chtwrsbot', '🥔')

@client.on(events.NewMessage(chats=("Amigos Chat")))
async def handler(event):
    if ('SHARKTEETH' in event.raw_text):
        await client.send_message('chtwrsbot', '🦈')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("You'll be back in 3 minutes" in event.raw_text):
        await asyncio.sleep(200) 
        await client.send_message('chtwrsbot', '🗺Quests')
     
@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("You'll be back in 4 minutes" in event.raw_text):
        await asyncio.sleep(260) 
        await client.send_message('chtwrsbot', '🗺Quests')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("You'll be back in 5 minutes" in event.raw_text):
        await asyncio.sleep(320) 
        await client.send_message('chtwrsbot', '🗺Quests')



@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("You'll be back in 6 minutes" in event.raw_text):
        await asyncio.sleep(380) 
        await client.send_message('chtwrsbot', '🗺Quests')
        
@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ('Leaderboard of fighters are updated:' in event.raw_text):
        await client.send_message('chtwrsbot', '▶️Fast fight')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ('You successfully defeated' in event.raw_text):
        await asyncio.sleep(60)
        await client.send_message('chtwrsbot', '/myshop_open')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ('Stamina restored. You are ready for more adventures!' in event.raw_text):
        await asyncio.sleep(2)
        await client.send_message('chtwrsbot', '🗺Quests')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ('Battle is coming. You have no time for games.' in event.raw_text):
        await asyncio.sleep(2)
        await client.send_message('chtwrsbot', '🛡Defend')

@client.on(events.NewMessage(chats=('@chtwrsbot')))
async def handler(event):
    if ('Who knows what is lurking in mud.' in event.raw_text):
        await asyncio.sleep(2)
        await event.click(text='🌲Forest')


@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ('/promo' in event.raw_text):
        await asyncio.sleep(2)
        await client.send_message('chtwrsbot', '/myshop_open')

@client.on(events.NewMessage(chats=('🐉Dragonscale Castle Chat')))
async def handler(event):
    if ('🏰 Welcome' in event.raw_text):
        await client.send_message('Amigos Chat', 'Radio for all 🔊')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ('/f_report' in event.raw_text):
        await client.send_message('chtwrsbot', '/f_report')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ('Encounter:' in event.raw_text):
        await asyncio.sleep(2)
        await client.send_message('chtwrsbot', '/whois')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("You should heal up a bit first." in event.raw_text):
        await asyncio.sleep(1800) 
        await client.send_message('chtwrsbot', '🗺Quests')




@client.on(events.NewMessage(chats=("Squad's Creed")))
async def handler(event):
    if ('Your result on the battlefield:' in event.raw_text):
        await client.send_message ('@ACreedGBot', event.raw_text) 

@client.on(events.NewMessage(chats=("@ACreedGBot")))
async def handler(event):
    if ('Your result on the battlefield:' in event.raw_text):
        await client.send_message ('@ForwardInfoBot', event.raw_text)

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("You need to heal your wounds and recover" in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '🗺Quests') 

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("Not enough gold to pay the entrance fee." in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '🗺Quests')

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("🗺Quests" in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '🗺Quests')

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("▶️Fast fight" in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '▶️Fast fight')

@client.on(events.NewMessage(chats=('⚔️ Orange Dragons')))
async def handler(event):
    if ('⚔️🦅Highnest @chtwrsbot' in event.raw_text):
        await client.send_message("Squads's Creed Orders", '⚔️🦅HIGHNEST')

@client.on(events.NewMessage(chats=('⚔️ Orange Dragons')))
async def handler(event):
    if ('⚔️🐺Wolfpack @chtwrsbot' in event.raw_text):
        await client.send_message("Squads's Creed Orders", '⚔️🐺WOLFPACK')

@client.on(events.NewMessage(chats=('⚔️ Orange Dragons')))
async def handler(event):
    if ('⚔️🌑Moonlight @chtwrsbot' in event.raw_text):
        await client.send_message("Squads's Creed Orders", '⚔️🌑MOONLIGHT')

@client.on(events.NewMessage(chats=('⚔️ Orange Dragons')))
async def handler(event):
    if ('⚔️🥔Potato @chtwrsbot' in event.raw_text):
        await client.send_message("Squads's Creed Orders", '⚔️🥔POTATO')

@client.on(events.NewMessage(chats=('⚔️ Orange Dragons')))
async def handler(event):
    if ('⚔️🦌Deerhorn @chtwrsbot' in event.raw_text):
        await client.send_message("Squads's Creed Orders", '⚔️🦌DEERHORN')

@client.on(events.NewMessage(chats=('⚔️ Orange Dragons')))
async def handler(event):
    if ('⚔️🦈Sharkteeth @chtwrsbot' in event.raw_text):
        await client.send_message("Squads's Creed Orders", '⚔️🦈SHARKTEETH')

@client.on(events.NewMessage(chats=('@chtwrsbot')))
async def handler(event):
    if ('You were strolling around on your horse' in event.raw_text):
        await asyncio.sleep(1)
        await event.click(text='🧹Intervene')

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("⬅Back" in event.raw_text):
        await client.send_message('chtwrsbot', '⬅Back')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("Battle of the seven castles in" in event.raw_text):
        await client.send_message('Amigos Chat', event.raw_text) 

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("⚖Exchange" in event.raw_text):
        await client.send_message('chtwrsbot', event.raw_text) 

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("Here you can buy and sell some items." in event.raw_text):
        await client.send_message('Amigos Chat', event.raw_text) 

#@client.on(events.NewMessage(chats=('Amigos Chat')))
#async def handler(event):
    #if ("/1" in event.raw_text):
        #await client.send_message('chtwrsbot', '/t_01') 

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("Thread offers now:" in event.raw_text):
        await client.send_message('Amigos Chat', event.raw_text) 

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/c1" in event.raw_text):
        await client.send_message('chtwrsbot', '/wtb_01') 

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("You don't even have enough" in event.raw_text):
        await client.send_message('Amigos Chat', event.raw_text) 

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/start" in event.raw_text):
        await client.send_message('chtwrsbot', '⚔Attack') 

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/help" in event.raw_text):
        await client.send_message('chtwrsbot', '🛡Defend') 

#@client.on(events.NewMessage(chats=('Amigos Chat')))
#async def handler(event):
    #if ("/wts_01" in event.raw_text):
        #await client.send_message('chtwrsbot', event.raw_text)

#@client.on(events.NewMessage(chats=('chtwrsbot')))
#async def handler(event):
    #if ("You don't have these items" in event.raw_text):
        #await client.send_message('Amigos Chat', event.raw_text) 

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/arena" in event.raw_text):
        await client.send_message('chtwrsbot', event.raw_text)

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("Dirty air is soaked with the thick" in event.raw_text):
        await client.send_message('Amigos Chat', event.raw_text)



@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/report" in event.raw_text):
        await client.send_message('chtwrsbot', event.raw_text)

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("Your result on the battlefield:" in event.raw_text):
        await client.send_message('Amigos Chat', event.raw_text)




@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("🛎Auction" in event.raw_text):
        await client.send_message('chtwrsbot', event.raw_text)

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("🛎Welcome to auction!" in event.raw_text):
        await client.send_message('Amigos Chat', event.raw_text)

@client.on(events.NewMessage(chats=('@CWGuildButlerBot')))
async def handler(event):
    if ('Stock difference since last update' in event.raw_text):
        await asyncio.sleep(1)
        await client.send_message('chtwrsbot', '🛡Defend')

@client.on(events.NewMessage(chats=('@CWGuildButlerBot')))
async def handler(event):
    if ('Differences from war' in event.raw_text):
        await asyncio.sleep(1)
        await client.send_message('chtwrsbot', '/myshop_open')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("You should heal up" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('chtwrsbot', '/myshop_open')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("You joined the defensive formations" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('chtwrsbot', '⚔Attack')

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/info" in event.raw_text):
        await client.send_message('@CW_Kazna_EU_bot', '/gearinfo_update')

@client.on(events.NewMessage(chats=('@CW_Kazna_EU_bot')))
async def handler(event):
    if ("/gearinfo_update" in event.raw_text):
        await client.send_message('Amigos Chat', '/info')

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("has ordered" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('Elder of Assassin', event.raw_text)


@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("has ordered" in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '/time')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/g_withdraw" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('chtwrsbot', event.raw_text)

@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if ("/g_receive" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('Amigos Chat', event.raw_text)
              
        
#@client.on(events.NewMessage(chats=('chtwrsbot')))
#async def handler(event):
    #if ("/g_withdraw" in event.raw_text):
        #await asyncio.sleep(1) 
        #await client.send_message('Amigos Chat', event.raw_text)
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_murky" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('chtwrsbot', '/use_tw1')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_murky" in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '/use_tw2')        

@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_murky" in event.raw_text):
        await asyncio.sleep(3) 
        await client.send_message('chtwrsbot', '/use_tw3')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_health" in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '/use_p22')
                
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_health" in event.raw_text):
        await asyncio.sleep(3) 
        await client.send_message('chtwrsbot', '/use_p23')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_health" in event.raw_text):
        await asyncio.sleep(4) 
        await client.send_message('chtwrsbot', '/use_p24')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_greed" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('chtwrsbot', '/use_p08')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_twilight" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('chtwrsbot', '/use_p16')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_nature" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('chtwrsbot', '/use_p10')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_nature" in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '/use_p11')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_nature" in event.raw_text):
        await asyncio.sleep(3) 
        await client.send_message('chtwrsbot', '/use_p12')
                        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_peace" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('chtwrsbot', '/use_p04')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_peace" in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '/use_p05')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_peace" in event.raw_text):
        await asyncio.sleep(3) 
        await client.send_message('chtwrsbot', '/use_p06')
        
                      
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_rage" in event.raw_text):
        await asyncio.sleep(1) 
        await client.send_message('chtwrsbot', '/use_p01')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_rage" in event.raw_text):
        await asyncio.sleep(2) 
        await client.send_message('chtwrsbot', '/use_p02')
        
@client.on(events.NewMessage(chats=('Amigos Chat')))
async def handler(event):
    if ("/use_rage" in event.raw_text):
        await asyncio.sleep(3) 
        await client.send_message('chtwrsbot', '/use_p03')        
                        
             
        
        
print('even...')
client.run_until_disconnected()