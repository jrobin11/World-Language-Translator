import countries
import requests
from Abrevs import Abrevs
import json
from X2D import L2C
from X2D import C2L
# Suggestions: Do an AutoFill
ltc = L2C()
abr = Abrevs()
ctl = C2L()
## root insert, left and right subroots,
## Continent -> CNTRY -> Language
def findAllLangs(country):
   for C in ctl.CountryToLang[country]:
      print(C, end=", ")
   print()

def findAllCountry(Language):
   for L in ltc.LangToCountry[Language]:
      print(L, end=", ")
   print()

def allCountries():
   CountryList = [*ctl.CountryToLang]
   for c in CountryList:
      print(c)

def allLanguages():
   LanguageList = [*ltc.LangToCountry]
   for l in LanguageList:
      print(l)
   
def Translate(srcLang, targLang, q):
   source = abr.abrdict[srcLang]
   target = abr.abrdict[targLang]
   q.replace(" ", "%20")
   q.replace(",", "%2C")
   url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

   payload = f"q={q}&target={target}&source={source}"
   headers = {
      "content-type": "application/x-www-form-urlencoded",
      "Accept-Encoding": "application/gzip",
      "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
      "X-RapidAPI-Key": "2aa4f8b066msh764f3836b75cef3p10cddcjsncc25d59d550a"
   }

   response = requests.request("POST", url, data=payload, headers=headers)
   resjson = json.loads(response.text)
   print(resjson["data"]["translations"][0]["translatedText"])
