import speech_recognition as sr
from ConsoleCommands import *
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import os
import pywhatkit
import wikipedia
import time
import random


wikipedia.set_lang("tr")


def konuş(text_input):
	tts = gTTS(text = text_input, lang = "tr", slow = False)
	print(text_input)
	tts.save("mtts.mp3")
	playsound("mtts.mp3")
	os.remove("mtts.mp3")

def yazmadan_konuş(text_input):
	tts = gTTS(text = text_input, lang = "tr", slow = False)
	tts.save("mtts.mp3")
	playsound("mtts.mp3")
	os.remove("mtts.mp3")

def dinle():
	while 1:
		r = sr.Recognizer()
		mic = sr.Microphone()

		with mic as source:
			#Konsol ekranını temizler.
			cls()
			print("Dinleniyor...")
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			try:
				speech = r.recognize_google(audio, language = "tr-TR")
			except Exception as e:
				print("Dediğiniz anlaşılmadı...")
			else:
				break
	return speech.lower()


def dinle_custom(text = " "):
	while 1:
		r = sr.Recognizer()
		mic = sr.Microphone()

		with mic as source:
			print(text)
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			try:
				speech = r.recognize_google(audio, language = "tr-TR")
			except Exception as e:
				print("Dediğiniz anlaşılmadı...")
			else:
				break
	return speech.lower()



def main():
	while 1:
		komut_işlendi = False
		k = dinle()
		break
		#Bu kısım asistanın bir ismi olması istendiği durumda kullanılır.

		# if 'isim ' in k2:
		# 	k = k2.replace('isim ', '')
		# 	break
		# if ' isim' in k2:
		# 	k = k2.replace(' isim', '')
		# 	break

	print(f"Duyulan: {k}")



	wikikomut = ["kim", "nedir", "kimdir"]
	for i in k.split():
		if i in wikikomut:
			konu = k.replace(i, "")
			konuş(f"Wikipedia'da {konu}aratılıyor...")
			try:
				print(wikipedia.summary(konu, 2))
				yazmadan_konuş("Bunu buldum. Okumamı ister misin?")
				eh = dinle_custom("Evet/hayır")
				if "evet" in eh:
					yazmadan_konuş(wikipedia.summary(konu, 2))
				elif "hayır" in eh:
					yazmadan_konuş("Tamam.")
				komut_işlendi = True
			except Exception:
				konuş("Konu bulunamadı...")
				komut_işlendi = True


	selamkomut = ["selam", "merhaba"]
	for i in k.split():
		if i in selamkomut:
			selamla = random.choice(["Merhaba!", "Selam!"])
			konuş(selamla)
			komut_işlendi = True


	komutlar = ["neler yapabilirsin", "komutlar neler", "ne yapabilirsin", "ne yapabiliyorsun"]
	for i in komutlar:
		if i in k:
			yardım = """Bana sorabileceklerin:

Saat
Wikipedia'da araştırabileceğim herhangi bir konu
Tanınmış bir kişinin doğum günü
Youtubedan dinlemek istediğin bir müzik ("'müzik ismi' çal" demen yeterli)
Google'dan aratabileceğim bir konu ("'konu' arat" demen yeterli)
Yapabileceklerim şimdilik bu kadar..."""

			print(yardım)
			tts = gTTS(text = "Yapabileceklerimi listeledim", lang = "tr", slow = False)
			tts.save("mtts.mp3")
			playsound(".\mtts.mp3")
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



	if "saat" in k:
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
		konu = k.replace("arat", "")
		konuş(f"{konu}aratılıyor...")
		pywhatkit.search(konu)
		komut_işlendi = True

	elif "kuş diline çevir" in k:
		sesli = {"a":"aga", "e":"ege", "i":"igi", "ı":"ıgı", "o":"ogo", "ö":"ögö", "u":"ugu", "ü":"ügü", "b":"b", "c":"c", "ç":"ç", "d":"d", "f":"f", "g":"g", "ğ":"ğ", "h":"h", "j":"j", "k":"k", "l":"l", "m":"m", "n":"n", "p":"p", "r":"r", "s":"s", "ş":"ş", "t":"t", "v":"v", "y":"y", "z":"z"}
		çeviri = ""
		yazı = k.replace("kuş diline çevir", "")
		for i in yazı:
			try:
				if not i == " ":
					çeviri += sesli[i]
				else:
					çeviri += " "
			except KeyError:
				pass
		konuş(çeviri[1:])
		komut_işlendi = True



	elif komut_işlendi == False:
		pass #konuş("Dediğiniz anlaşılmadı veya nasıl yanıt verileceğini henüz bilmiyorum.")
 

if __name__ == "__main__":
	while 1:
		cls()
		main()