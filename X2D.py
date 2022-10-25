import xlrd
LangToCountry = {}
CountryToLang = {}
wb = xlrd.open_workbook('apiLC.xls')
sh = wb.sheet_by_index(0)   

for i in range(104):
    lang = sh.cell(0, i).value
    LangToCountry[lang] = []
    if lang == "":
        continue
    for j in range(58):
        count = sh.cell(j+1, i).value
        if count == "":
            break
        LangToCountry[lang].append(count)

wb2 = xlrd.open_workbook('CountLang.xls')
sh2 = wb2.sheet_by_index(0)

for i in range(238):
    country = sh2.cell(0, i).value
    CountryToLang[country] = []
    if country == "":
        continue
    for j in range(14):
        count = sh2.cell(j+1, i).value
        if count == "":
            break
        CountryToLang[country].append(count)

class L2C:
    def __init__(self):
        self.LangToCountry = LangToCountry

class C2L:
    def __init__(self):
        self.CountryToLang = CountryToLang

