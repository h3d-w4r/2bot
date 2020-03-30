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
	print(Fore.CYAN+'['+Fore.YELLOW+' Telegram '+Fore.CYAN+']'+Fore.BLUE+f'NAMA AKUN	: {me.first_name}({me.username})')
	print(Fore.CYAN+'['+Fore.YELLOW+' Telegram '+Fore.CYAN+']'+Fore.BLUE+f'NOMOR HP		: ({phone_number})\n'

	await client.send_message(zcclick_channel, '/join')
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'You must join' in message:	
			channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
			print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.GREEN + f' BERGABUNG KE @{channel_name}...' + Fore.RESET)
			await client(JoinChannelRequest(channel_name))
			print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.GREEN + f' Sedang Loading ...')
			time.sleep(2)
			await client(GetBotCallbackAnswerRequest(
				peer=zcclick_channel,
				msg_id=event.message.id,
				data=event.message.reply_markup.rows[0].buttons[1].data
			))
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You must stay' in message:	
			waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
			print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.GREEN + f' Sukses Join !!! tunggu {waiting_hours} Untuk rewards' + Fore.RESET)
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.GREEN + ' Maaf, Tidak Ada Iklan Sekarang !!!' + Fore.RESET)
			

	await client.send_message(zcclick_channel, '/bots')
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'Forward a message to' in message:	
			channel_msg = event.original_update.message.reply_markup.rows[0].buttons[0].url
			print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.GREEN + f' URL @{channel_msg}' + Fore.RESET)
			if '?' in channel_msg:
				channel_name = re.search(r't.me\/(.*?)\?', channel_msg).group(1)
			elif '?' not in channel_msg:
				channel_name = re.search(r't.me\/(.*?)', channel_msg).group(1)
	
			print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.GREEN + f' MessageBot @{channel_name}...' + Fore.RESET)
			await client.send_message(channel_name, '/start')
			
			@client.on(events.NewMessage(chats=channel_name, incoming=True))
			async def earned_amount(event):
				msg_id = event.message.id,
				await client.forward_messages(zcclick_channel, msg_id, channel_name)
	
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.GREEN + event.raw_text + Fore.RESET)
			# No more ads
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.RED + 'Maaf, Iklan Habis !!!' + Fore.RESET)

	await client.send_message(zcclick_channel, '/visit')
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def visit_ads(event):	
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				if url is not None:
					print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.GREEN +' Sedang Mengunjungi Iklan Web ...')
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					tt=parse_data.find('div',{'id':'headbar'})
					if captcha is not None:
						print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.RED + 'Warning .... Ada CAPTCHA !!!'+ Fore.RED +'Iklan Di SKIP CAPTCHA...')
						await client(GetBotCallbackAnswerRequest(
							peer=zcclick_channel,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[0].buttons[1].data
						))
					elif status_code==200 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						logResponse(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token},headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True) 
					elif status_code==307 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						logResponse(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token},headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True)
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def wait_second(event):
		message = event.raw_text
		if 'Please stay on' in message:
			sec = re.findall( r'([\d.]*\d+)', message)
			logResponse(int(sec[0]))
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.GREEN + f'{message}'+ Fore.RESET)
			# No more ads
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print_msg_time(print_msg_time(Fore.YELLOW+'['+Fore.MAGENTA+' Bot_Zec '+Fore.YELLOW+']'+Fore.RED + 'Maaf, Ads Sedang Habis !!!' + Fore.RESET)
		
		exit(0)
			
	await client.run_until_disconnected()
	
	
asyncio.get_event_loop().run_until_complete(main())
