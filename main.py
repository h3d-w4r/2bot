import asyncio,logging,re,time,os,json;import sys,requests,random
from time import sleep;from bs4 import BeautifulSoup
from datetime import datetime;import colorama
reset = "\033[0m";abu = "\033[1;30m";merah = "\033[1;31m"
hijau = "\033[92m";kuning = "\033[1;33m";biru = "\033[1;34m"
pink = "\033[1;35m";cyan = "\033[1;36m";g = "\033[2;04m"
logging.basicConfig(level=logging.ERROR)
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from bs4 import BeautifulSoup
os.system('cls' if os.name=='nt' else 'clear')
doge = '@Dogecoin_click_bot';ltc = 'Litecoin_click_bot'
bch = 'BCH_clickbot';zec = 'Zcash_click_bot'

api_id = 1096441;api_hash = 'fa5a67d7e150c639d876724ec406868d'

def ketik(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random() * 0.18)

def menunggu(i):
	for x in range(0,i+1):
		sys.stdout.write("\r")
		sys.stdout.write("\033[1;92m[%s] Waiting %s %d\r"%(datetime.now().strftime("%H:%M:%S"),i,x))
		sys.stdout.flush()
		time.sleep(1)
def get_response(url, method='GET'):
	response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=15)
	text_response = response.text
	status_code = response.status_code
	return[status_code, text_response]

async def main():
	print(g+abu+' ══════════'+kuning+'๑۩۩๑'+abu+'══════════'+kuning+'๑۩۩๑'+abu+'══════════'+kuning+'๑۩۩๑'+abu+'══════════'+reset)
	print(hijau+'	╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗ ╦ ╦╔═╗╔═╗╦═╗ '+reset)
	print(pink+'	║║║║╣ ║  ║  ║ ║║║║║╣  ║ ║╚═╗║╣ ║   '+reset)
	print(hijau+'	╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝ ╚═╝╚═╝╚═╝╩   '+reset)
	print(g+abu+' ═════════════════════════════════════════════════════'+reset)
	ketik(cyan+f"   [Author : Hedwar]"+hijau+"✯[Project Anak Minang]✯"+pink+"[Padang]")
	print(g+abu+' ═════════════════════════════════════════════════════'+reset)

	if len(sys.argv) < 2:
		ketik(cyan+'Cara Pakai ==>> '+kuning+' python main.py +62812345678xxx'+reset)
		e = input('Press any key to exit...')
		exit(1)

	phone_number = sys.argv[1]
	if not os.path.exists("session"):
		os.mkdir("session")
	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()

	ketik(hijau+'		Welcome Back		')
	ketik(cyan+'	Username : '+kuning+f' {me.first_name}({me.username}')
	print(cyan+'	Nomor	 : '+kuning+f' {phone_number} \n'+reset)
#doge
	await client.send_message(doge, '/visit')
	@client.on(events.NewMessage(chats=doge, incoming=True))
	async def visit_ads(event):
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				if url is not None:
					print(kuning+'['+hijau+'BotDoge'+kuning+']'+cyan+f' Sedang Klik Link .....')
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					tt=parse_data.find('div',{'id':'headbar'})
					if captcha is not None:
						ketik(kuning+'['+hijau+'BotDoge'+kuning+']'+cyan+f' Ada Captcha ==>>'+merah+' Skip CAPTCHA...')
						await client(GetBotCallbackAnswerRequest(
							peer=doge,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[1].buttons[1].data
						))
					elif status_code==200 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						menunggu(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True)
					elif status_code==307 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						menunggu(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True)

	@client.on(events.NewMessage(chats=doge, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:
			ketik(kuning+'['+hijau+'BotDoge'+kuning+']'+cyan+f' {message}'+reset)
			sleep(2)
	@client.on(events.NewMessage(chats=doge, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print(merah+' Maaf, Iklan Visit Habis '+reset)
			time.sleep(2)

#ltc

	await client.send_message(ltc, '/visit')
	@client.on(events.NewMessage(chats=ltc, incoming=True))
	async def visit_ads(event):
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				if url is not None:
					print(kuning+'['+abu+'BotLtc'+kuning+']'+cyan+f' Sedang Klik Link .....')
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					tt=parse_data.find('div',{'id':'headbar'})
					if captcha is not None:
						ketik(kuning+'['+abu+'BotLtc'+kuning+']'+cyan+f' Ada Captcha ==>>'+merah+' Skip CAPTCHA...')
						await client(GetBotCallbackAnswerRequest(
							peer=ltc,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[1].buttons[1].data
						))
					elif status_code==200 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						menunggu(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True)
					elif status_code==307 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						menunggu(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True)

	@client.on(events.NewMessage(chats=ltc, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:
			ketik(kuning+'['+abu+'BotLtc'+kuning+']'+cyan+f' {message}'+reset)
			sleep(2)
	@client.on(events.NewMessage(chats=ltc, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print(merah+' Maaf, Iklan Visit Habis '+reset)
			sleep(2)

#zec

	await client.send_message(zec, '/visit')
	@client.on(events.NewMessage(chats=zec, incoming=True))
	async def visit_ads(event):
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				if url is not None:
					print(kuning+'['+pink+'BotZec'+kuning+']'+cyan+f' Sedang Klik Link .....')
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					tt=parse_data.find('div',{'id':'headbar'})
					if captcha is not None:
						ketik(kuning+'['+hijau+'BotZec'+kuning+']'+cyan+f' Ada Captcha ==>>'+merah+' Skip CAPTCHA...')
						await client(GetBotCallbackAnswerRequest(
							peer=zec,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[1].buttons[1].data
						))
					elif status_code==200 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						menunggu(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True)
					elif status_code==307 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						menunggu(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True)

	@client.on(events.NewMessage(chats=zec, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:
			ketik(kuning+'['+hijau+'BotZec'+kuning+']'+cyan+f' {message}'+reset)
			sleep(2)
	@client.on(events.NewMessage(chats=doge, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print(merah+' Maaf, Iklan Visit Habis '+reset)
			time.sleep(2)

#bch

	await client.send_message(doge, '/visit')
	@client.on(events.NewMessage(chats=bch, incoming=True))
	async def visit_ads(event):
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				if url is not None:
					ketik(kuning+f'['+reset+'BotBch'+kuning+']'+cyan+f' Sedang Klik Link .....')
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					tt=parse_data.find('div',{'id':'headbar'})
					if captcha is not None:
						ketik(kuning+'['+hijau+'BotBch'+kuning+']'+cyan+f' Ada Captcha ==>>'+merah+' Skip CAPTCHA...')
						await client(GetBotCallbackAnswerRequest(
							peer=bch,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[1].buttons[1].data
						))
					elif status_code==200 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						menunggu(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True)
					elif status_code==307 and captcha is None and tt is not None:
						setPhoneNumber=tt.get('data-code')
						data_timer=tt.get('data-timer')
						data_token=tt.get('data-token')
						menunggu(int(data_timer))
						requests.post('http://dogeclick.com/reward/',data={'code':setPhoneNumber,'token':data_token}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} ,allow_redirects=True)

	@client.on(events.NewMessage(chats=bch, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:
			ketik(kuning+'['+reset+'BotBch'+kuning+']'+cyan+f' {message}'+reset)
			sleep(2)
	@client.on(events.NewMessage(chats=bch, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print(kuning+'['+reset+'BotBch'+kuning+']'+cyan+f' Maaf, Iklan Visit Habis '+reset)
			time.sleep(2)



	await client.run_until_disconnected()
asyncio.get_event_loop().run_until_complete(main())
