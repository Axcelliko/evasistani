import re
import trnlp
şehirler = ['adana', 'adiyaman', 'afyon', 'agri', 'amasya', 'ankara', 'antalya', 'artvin', 'aydin', 'balikesir', 'bilecik', 'bingol', 'bitlis', 'bolu', 'burdur', 'bursa', 'çanakkale', 'çankiri', 'çorum', 'denizli', 'diyarbakir', 'edirne', 'elazig', 'erzincan', 'erzurum', 'eskisehir', 'gaziantep', 'giresun', 'gumushane', 'hakkari', 'hatay', 'isparta', 'mersin', 'i̇stanbul', 'i̇zmir', 'kars', 'kastamonu', 'kayseri', 'kirklareli', 'kirsehir', 'kocaeli', 'konya', 'kutahya', 'malatya', 'manisa', 'kahramanmaras', 'mardin', 'mugla', 'mus', 'nevsehir', 'nigde', 'ordu', 'rize', 'sakarya', 'samsun', 'siirt', 'sinop', 'sivas', 'tekirdag', 'tokat', 'trabzon', 'tunceli', 'sanliurfa', 'usak', 'van', 'yozgat', 'zonguldak', 'aksaray', 'bayburt', 'karaman', 'kirikkale', 'batman', 'sirnak', 'bartin', 'ardahan', 'igdir', 'yalova', 'karabuk', 'kilis', 'osmaniye', 'duzce']
kurlar = ['lira', 'tl', 'dolar', 'euro', 'türk lirası']
diller = ["ingilizce", "almanca", "japonca", "türkçe", "çince", "ispanyolca"]
kurdict = {
	"lira": "TRY",
	"tl": "TRY",
	"türk lirası": "TRY",
	"dolar": "USD",
	"euro": "EUR",
	"€": "EUR"
}
dil_regex = [('(çince|ispanyolca|portekizce|japonca|italyanca|ingilizce|fransızca|arapça)', '{DİL}')]
dildict = {
	"ingilizce": "en",
	"ispanyolca": "es",
	"portekizce": "pt",
	"çince": "zh-TW",
	"italyanca": "it",
	"fransızca": "fr",
	"arapça": "ar"
}
def en_az_iki(a, b):
    return len(set(a) & set(b)) >= 2

def arası(s, start, end):
  return (s.split(start))[1].split(end)[0]

def dil_tag(text):
	text = trnlp.find_stems(text)[0].split("(")[0]
	return "{DİL}" + text + "{/DİL}"

def dil_ayır(text):
	text = trnlp.find_stems(text)[0].split("(")[0]
	return text

def dil_algıla(text):
	nt = ""
	for i in text.split():
		if re.search(dil_regex[0][0], i):
			nt = nt + i
	return nt


if __name__ == '__main__':
	pass












