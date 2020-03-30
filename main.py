import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

''' DogeClick Bot Channel from dogeclick.com
Options:
1. Dogecoin_click_bot
2. Litecoin_click_bot
3. BCH_clickbot
4. Zcash_click_bot
5. Bitcoinclick_bot
# '''
dogeclick_channel = 'Dogecoin_click_bot'
ltcclick_channel = 'Litecoin_click_bot'
bchclick_channel = 'BCH_clickbot'
zcclick_channel = 'Zcash_click_bot'

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')
	
def get_response(url, method='GET'):
	response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=250)
	text_response = response.text
	status_code = response.status_code
	return[status_code, text_response]
def logResponse(i):
  for x in range(0,i+1):
   sys.stdout.write(Fore.YELLOW+'[%s] Waiting %s seconds! %d\r'%(datetime.now().strftime("%H:%M:%S"),i,x))
   time.sleep(1)

async def main():
	print(Fore.BLUE + ' ====================================================================  \n' + Fore.RESET)
	print(Fore.GREEN + ' Created By Hedwar NewBie Project Anak Minang Padang Kota Tercinta  -   \n' + Fore.RESET)
	print(Fore.GREEN + ' Ndak Bisa Jadi Hacker Script Python Pun Bisa Diakalin Brader -   \n' + Fore.RESET)
	print(Fore.GREEN + ' EARNING CRYPTO BotClick Telegram PASTI LANDING masuk WALLET  -   \n' + Fore.RESET)
	print(Fore.BLUE + ' ====================================================================  \n' + Fore.RESET)
  
	if len(sys.argv) < 2:
		print('Cara: python main.py no-Hp')
		print('Contoh : python main.py +62852xxxxx)\n')
		e = input(Fore.Red+'Tekan Enter Untuk Keluar ...')
		exit(1)
		
	phone_number = sys.argv[1]
		if not os.path.exists("session"):
	    os.mkdir("session")
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
f'NAMA AKUN : {me.first_name}({me.username})')
 
  #ZCASH_click_bot_VISIT
	# Start command /visit
	await client.send_message(zcclick_channel, '/visit')
	
	# Start visiting the ads
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def visit_ads(event):
	
	
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				#url = event.message.reply_markup.rows[0].buttons[0].url
			
				if url is not None:
					print_msg_time('SEDANG MASUK KE WEBSITE...')

					# Parse the html of url
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					
					# Captcha detected
					if captcha is not None:
						print_msg_time(Fore.RED + 'CAPTCHA TERDETEKSI !!!'+ Fore.RED +' SKIP CAPTCHA...')
									
						# Clicks the skip
						await client(GetBotCallbackAnswerRequest(
							peer=zcclick_channel,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[0].buttons[1].data
						))		
		
	# Print earned money
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + f'{message}'+ Fore.RESET)
			# No more ads
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print_msg_time(Fore.RED + 'MAAF, IKLAN SUDAH HABIS !!!' + Fore.RESET)
		
		exit(0)
			
	await client.run_until_disconnected()
	
	
asyncio.get_event_loop().run_until_complete(main())
