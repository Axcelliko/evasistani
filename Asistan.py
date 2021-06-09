import speech_recognition as sr
from ConsoleCommands import *
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import os
import pywhatkit
cls()
import wikipedia
import time
import random
import feedparser
from currency_converter import CurrencyConverter
from Variables import *
from googletrans import Translator
from math import sqrt, factorial
import trnlp
import re
import _thread
import tkinter as tk
from tkinter.ttk import *
from tkinter import * 

current_text = ""
duyulan = ""
hatırlatma_text = ""

wikipedia.set_lang("tr")
IS_SPEAKING = False


def konuş(text_input):
	global current_text
	tts = gTTS(text = text_input, lang = "tr", slow = False)
	print(text_input)
	current_text = text_input
	tts.save("mtts.mp3")
	playsound("mtts.mp3")
	os.remove("mtts.mp3")

def konuş_dil(text_input, lng):
	global current_text
	tts = gTTS(text = text_input, lang = lng, slow = False)
	print(text_input)
	current_text = text_input
	tts.save("mtts.mp3")
	playsound("mtts.mp3")
	os.remove("mtts.mp3")

def yazmadan_konuş(text_input):
	tts2 = gTTS(text = text_input, lang = "tr", slow = False)
	tts2.save("mtts2.mp3")
	playsound("mtts2.mp3")
	os.remove("mtts2.mp3")

def dinle():
	global current_text
	global duyulan
	while 1:
		r = sr.Recognizer()
		mic = sr.Microphone()

		with mic as source:
			print("Dinleniyor...")
			current_text = "Dinleniyor..."
			duyulan = ""
			#r.adjust_for_ambient_noise(source)
			try:
				audio = r.listen(source, timeout=6, phrase_time_limit=10)
			except sr.WaitTimeoutError:
				pass
			try:
				speech = r.recognize_google(audio, language = "tr-TR")
			except Exception as e:
				print("Dediğiniz anlaşılmadı...")
			else:
				break
	return speech.lower().replace("̇","")


def dinle_custom(text = " "):
	global current_text
	global duyulan
	while 1:
		r = sr.Recognizer()
		mic = sr.Microphone()

		with mic as source:
			print(text)
			current_text = text
			duyulan = ""
			#r.adjust_for_ambient_noise(source)
			try:
				audio = r.listen(source, timeout=6, phrase_time_limit=10)
			except sr.WaitTimeoutError:
				pass
			try:
				speech = r.recognize_google(audio, language = "tr-TR")
			except Exception as e:
				print("Dediğiniz anlaşılmadı...")
			else:
				break
	return speech.lower().replace("̇","")

def hatırlatma_kontrol():
	global hatırlatma_text
	while 1:
		time.sleep(0.5)
		now = datetime.now()
		current_time = now.strftime("%H:%M")
		f = open("reminders.txt" , "r+", encoding='utf8')
		for i in f:
			if i.strip("\n").split('-|-')[0] == f"[{current_time}]":
				print(f"Bir hatırlatmanız var -> {i.split('-|-')[1]}")
				hatırlatma_text = f"Bir hatırlatmanız var -> {i.split('-|-')[1]}"
				while 1:
					try:
						yazmadan_konuş(f"Bir hatırlatmanız var, {i.split('-|-')[1]}")
						break
					except:
						pass
				lines = f.readlines()
				f.seek(0)
				for j in lines:
					if j != i:
						f.write(j)
				f.truncate()
				hatırlatma_text = ""
def hatırlatma_kur(text, time):
	f = open("reminders.txt", "a", encoding = "utf-8")
	f.write(f"[{time}]-|-{text}\n")

#Bu kısım asistanın bir ismi olması istendiği durumda kullanılır.
İSİM = None

def main():
	global current_text
	global duyulan
	while 1:
		while 1:
			komut_işlendi = False
			k2 = dinle()
			if İSİM != None:
				if f'{İSİM} ' in k2:
					k = k2.replace(f'{İSİM} ', '')
					break
				if f' {İSİM}' in k2:
					k = k2.replace(f' {İSİM}', '')
					break
			else:
				k = k2.lower()
				break
		print(f"Duyulan: {k}")
		duyulan = f"Duyulan: {k}"


		islemkomut = ["artı", "topla", "eksi", "çıkar", "böl", "çarp", "kere", "üssü", "üzeri", "faktöriyel", "kök", "+", "-", "/", "x"]
		for i in islemkomut:
			if i in k:
				k = k.replace(",", ".")
				islem = i
				sy2 = None
				try:
					sy1 = float(re.findall('[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', k)[0])
					sy2 = float(re.findall('[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', k)[1])
				except:
					pass
				try:
					if (islem == "+") or (islem == "topla"):
						sonuc = sy1 + sy2
					elif (islem == "-") or (islem == "çıkar"):
						sonuc = sy1 - sy2
					elif (islem == "/") or (islem == "böl"):
						sonuc = sy1 / sy2
					elif (islem == "x") or (islem == "çarp") or (islem == "kere"):
						sonuc = sy1 * sy2
					elif (islem == "üssü") or (islem == "üzeri"):
						sonuc = sy1 ** sy2
					elif islem == "faktöriyel":
						sonuc = factorial(sy1)
					elif islem == "kök":
						sonuc = sqrt(sy1)
						if str(sonuc).split(".")[1] == "0":
							sonuc = int(sonuc)
					if ((type(sy1) is float) and (type(sy2) is None)) or ((type(sy1) is float) and (type(sy2) is float)):
						if str(sonuc).split(".")[1] == "0":
							sonuc = int(sonuc)

					konuş(f"Sonuç: {round(sonuc, 4)}")
					sy1 = None
					sy2 = None
					komut_işlendi = True
				except Exception as e:
					sy1 = None
					sy2 = None
					pass


		selamkomut = ["selam", "merhaba"]
		for i in k.split():
			if i in selamkomut:
				selamla = random.choice(["Merhaba!", "Selam!"])
				konuş(selamla)
				komut_işlendi = True


		komutlar = ["neler yapabilirsin", "komutlar neler", "ne yapabilirsin", "ne yapabiliyorsun", "neler yapabiliyorsun"]
		for i in komutlar:
			if i in k:
				yardım = """Bana sorabileceklerin:

	Saat
	Wikipedia'da araştırabileceğim herhangi bir konu
	Tanınmış bir kişinin doğum günü
	Youtubedan dinlemek istediğin bir müzik ("'müzik ismi' çal" demen yeterli)
	Google'dan aratabileceğim bir konu ("'konu' arat" demen yeterli)
	Herhangi bir şehir veya ilçenin hava durumu
	Bir cümlenin başka bir dile çevrilmiş hali
	Para kurlarını çevirme
	Yapabileceklerim şimdilik bu kadar..."""

				print(yardım)
				tts = gTTS(text = "Yapabileceklerimi listeledim", lang = "tr", slow = False)
				tts.save("mtts.mp3")
				playsound("mtts.mp3")
				os.remove("mtts.mp3")
				time.sleep(6)
				komut_işlendi = True

		nslkomut = ["nasılsın", "naber", "ne haber", "iyi misin"]
		for i in nslkomut:
			if i in k:
				nslcevap = ["İyiyim teşekkür ederim...", "Çok iyiyim..."]
				cvp = random.choice(nslcevap)
				konuş(cvp)
				komut_işlendi = True

		havakomut = ["hava"]
		for i in havakomut:
			if i in k:
				try:
					if "'" in k:
						şehir = asciify(k.split("'")[0])
					else:
						şehir = asciify(k.split()[0])
					parse = feedparser.parse(f"http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|00000|{şehir}|")
					parse = parse["entries"][0]["summary"]
					parse = parse.split()
					if parse[2] == "additional":
						konuş("Bulunamadı")
					else:
						hava = (f"{trnlp.deascii(parse[2])} {parse[4]} {parse[5]}")
						konuş(hava)
				except Exception: #UnicodeError
					pass
				komut_işlendi = True

		#Şimdilik sadece dolar, euro ve tl sorulabilir.
		kurkomut = ["kaç"]
		for i in k.split():
			if i in kurkomut:
				if "€" in k:
					eur_miktar = k.split("€")[1]
					k1 = k.replace("€", "")
					k = k1.replace(" ", " euro ", 1)
				if "bir" in k:
					k = k.replace("bir", "1")
				if "türk lirası" in k:
					k = k.replace("türk lirası", "tl")
				if en_az_iki(k.split(), kurlar):
					c = CurrencyConverter()
					miktar = k.split()[0]
					if "kaç" in k:
						try:
							çevrilen = kurdict[k.split()[(k.split().index("kaç")) - 1]]
							kur = kurdict[k.split()[(k.split().index("kaç")) + 1]]
							sonuc = round(c.convert(miktar, çevrilen, kur), 2)
							konuş(f"{miktar} {çevrilen}, {sonuc} {kur}")
						except Exception:
							konuş("Anlaşılmadı")
						komut_işlendi = True

		wikikomut = ["kim", "nedir", "kimdir"]
		for i in k.split():
			if i in wikikomut:
				if komut_işlendi == False:
					konu = k.replace(i, "")
					if len(konu.split()) > 3:
						break
					konuş(f"Wikipedia'da {konu} aratılıyor...")
					try:
						print(wikipedia.summary(konu, 2))
						current_text = wikipedia.summary(konu, 2)
						yazmadan_konuş("Bunu buldum. Okumamı ister misin?")
						eh = dinle_custom("Evet/hayır")
						if "evet" in eh:
							current_text = wikipedia.summary(konu, 2)
							yazmadan_konuş(wikipedia.summary(konu, 2))
						elif "hayır" in eh:
							yazmadan_konuş("Tamam.")
						komut_işlendi = True
					except Exception:
						konuş("Konu bulunamadı...")
						komut_işlendi = True

		if "çevir" in k:
			if komut_işlendi == False:
				if "ingilizce'ye" in k:
					k = k.replace("ingilizce'ye", "ingilizceye")
				for i in diller:
					if dil_algıla(i) in k:
						t = Translator()
						said = False
						try:
							dil = dildict[re.search(dil_regex[0][0], k).group()]
						except AttributeError:
							konuş("Anlaşılmadı")
							said = True
						text = k.replace("çevir", "")
						text = text.replace(dil_algıla(k), "")
						try:
							konuş_dil((t.translate(text, src = "tr", dest = dil).text), dil)
						except Exception:
							if said == False: konuş("Anlaşılmadı")
						komut_işlendi = True
						break

		if "liste" in k:
			with open("reminders.txt" , "r+", encoding='utf8') as f:
				konuş("Listeliyorum")
				text = ""
				for line in f:
					line = line.strip("\n")
					line.replace("-|-", "->")
					text = text + f"{line}\n"
				current_text = text
				time.sleep(5)
				komut_işlendi = True

		if "hatırlat" in k:
			if komut_işlendi == False:
				saat_duzen = ('(\d{1,2}:\d{1,2})|(\d{1,2}.\d{1,2})|(\d{1,2} \d{1,2})|(\d{1,4})')
				saat1 = re.findall(saat_duzen, k)
				saat = []
				konuş("Ne hatırlatmamı istersin?")
				hatırlatma = dinle()
				if len(saat1) != 0:
					for i in saat1[0]:
						if i == "":
							pass
						else:
							saat.append(i) 
					print(f'Duyulan: "{hatırlatma}" Saat: {saat[0]}')
				else:
					print(f"Duyulan: {hatırlatma}")
					konuş("Ne zaman hatırlatmamı istersin?")
					zaman = dinle()
					saat1 = re.findall(saat_duzen, zaman)
					for i in saat1[0]:
						if i == "":
							pass
						else:
							saat.append(i) 
					print(f"Duyulan: {zaman}")
				while 1:
					saat = saat[0]
					if "." in saat:
						saat = saat.replace(".", ":")
						if len(saat.split(":")[0]) == 1:
							saat = "0" + saat 
						if len(saat.split(":")[1]) == 1:
							saat = saat[:3] + "0" + saat[-1]
						break
					elif " " in saat:
						saat = saat.replace(" ", ":")
						if len(saat.split(":")[0]) == 1:
							saat = "0" + saat 
						if len(saat.split(":")[1]) == 1:
							saat = saat[:3] + "0" + saat[-1]
						break
					elif ":" in saat:
						if len(saat.split(":")[0]) == 1:
							saat = "0" + saat 
						if len(saat.split(":")[1]) == 1:
							saat = saat[:3] + "0" + saat[-1]
						break
					elif ":" not in saat:
						try:
							saat = saat[:-2] + ":" + saat[-2] + saat[-1]
							if len(saat.split(":")[0]) == 1:
								saat = "0" + saat 
							if len(saat.split(":")[1]) == 1:
								saat = saat[:3] + "0" + saat[-1]
							break
						except Exception:
							konuş("Geçersiz zaman")
					else:
						konuş("Geçersiz zaman")


				hatırlatma_kur(hatırlatma, saat)

				konuş(f"Saat {saat} için hatırlatıcı kuruldu.")
				komut_işlendi = True

		elif "saat" in k:
			now = datetime.now()
			current_time = now.strftime("%H:%M")
			konuş(f"Şuan saat {current_time}")
			komut_işlendi = True


		elif "çal" in k:
			t = k.replace("çal", "")
			konuş(f"Youtube'dan {t} adlı konu aratılıyor...")
			pywhatkit.playonyt(t)
			komut_işlendi = True

		

		elif "ne zaman doğdu" in k:
			kişi = k.replace("ne zaman doğdu", "") 
			try:
				tarih = ((((wikipedia.summary(kişi, 2)).split("("))[1]).split(")"))[0]
				konuş(tarih)
				komut_işlendi = True
			except Exception:
				konuş("Bulunamadı...")
				komut_işlendi = True



		elif "arat" in k:
			if komut_işlendi == False:
				konu = k.replace("arat", "")
				konuş(f"{konu}aratılıyor...")
				pywhatkit.search(konu)
				komut_işlendi = True

		elif ("kuşdili") in k or ("kuş dili") in k:
			sesli = {"a":"aga", "e":"ege", "i":"igi", "ı":"ıgı", "o":"ogo", "ö":"ögö", "u":"ugu", "ü":"ügü", "b":"b", "c":"c", "ç":"ç", "d":"d", "f":"f", "g":"g", "ğ":"ğ", "h":"h", "j":"j", "k":"k", "l":"l", "m":"m", "n":"n", "p":"p", "r":"r", "s":"s", "ş":"ş", "t":"t", "v":"v", "y":"y", "z":"z"}
			çeviri = ""
			yazı = k.replace("kuşdili", "")
			for i in yazı:
				try:
					if not i == " ":
						çeviri += sesli[i]
					else:
						çeviri += " "
				except KeyError:
					pass
			konuş(çeviri)
			komut_işlendi = True



		elif komut_işlendi == False:
			print("Dediğiniz anlaşılmadı veya nasıl yanıt verileceğini henüz bilmiyorum.")
			current_text = "Dediğiniz anlaşılmadı veya nasıl yanıt verileceğini henüz bilmiyorum."
			yazmadan_konuş("Anlaşılmadı")
 


def visual():
	def on_closing():
		_thread.interrupt_main()

	global current_text
	global duyulan
	root = Tk()

	root.geometry('500x300')
	root.configure(background='#7AC5CD')
	root.title('Asistan')

	label1 = Label(root, text=current_text, bg='#7AC5CD', font=('arial', 14, 'normal'), wraplength = 490)
	label1.place(x=250, y=140, anchor="center")

	label2 = Label(root, text=duyulan, bg='#7AC5CD', font=('arial', 12, 'normal'), wraplength = 490)
	label2.place(x=250, y=30, anchor="center")

	label3 = Label(root, text=hatırlatma_text, bg='#7AC5CD', font=('arial', 12, 'normal'), wraplength = 490)
	label3.place(x=250, y=255, anchor="center")

	def update():
		global current_text
		global duyulan
		global hatırlatma_text
		label1["text"] = current_text
		label2["text"] = duyulan
		label3["text"] = hatırlatma_text
		root.after(100, update)

	root.after(100, update)
	root.protocol("WM_DELETE_WINDOW", on_closing)
	root.mainloop()


if __name__ == "__main__":
	_thread.start_new_thread(main, ())
	_thread.start_new_thread(hatırlatma_kontrol, ())
	_thread.start_new_thread(visual, ())

	while 1: 
		pass
