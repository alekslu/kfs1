#Sinu ülesanne:Kood saab inputina isikukoodi. Kood peab kontrollima:
#1) kas input koosneb ainult numbritest
#2) kas isikukoodil on õige pikkus

#Kood peab terminalis kuvama:
#1) sugu
#2) sünnipäev
#3) kus haiglas sündis
#4) kontrollkoodi

#Näide: 50102182738
#Mees
#2001 veebruar 18
#Tartu sünnitusmaja
#kontrollkood: 38


check = True
while check == True:
    isikukood = int(input("Sisesta enda isikukood: "))
    if len(str(isikukood)) != 11:
        print("Vale isikukood, sisestage uuesti")
    else:
        check = False

isikukood = [int(x) for x in str(isikukood)]

if isikukood[0] == 1 or isikukood[0] == 3 or isikukood[0] == 5 or isikukood[0] == 7:
    print("Mees")
else:
    print("Naine")

birth_year = isikukood[1]*10 + isikukood[2]

if isikukood[0] == 1 or isikukood[0] == 2:
    birth_year += 1800
elif isikukood[0] == 3 or isikukood[0] == 4:
    birth_year += 1900
elif isikukood[0] == 5 or isikukood[0] == 6:
    birth_year += 2000

birth_month = isikukood[3]*10 + isikukood[4]

kuud = {
    1: "jaanuar",
    2: "veebruar",
    3: "märts",
    4: "aprill",
    5: "mai",
    6: "juuni",
    7: "juuli",
    8: "august",
    9: "september",
    10: "oktoober",
    11: "november",
    12: "detsember"
}

birth_day = isikukood[5]*10 + isikukood[6]

print(f"{birth_year} {kuud.get(birth_month)} {birth_day}")

haiglad = {
    "001...010": "Kuressaare haigla",
    "011...019": "Tartu Ülikooli Naistekliinik",
    "021...150": "Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)",
    "151...160": "Keila haigla",
    "161...220": "Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)",
    "221...270": "Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)",
    "271...370": "Maarjamõisa kliinikum (Tartu), Jõgeva haigla",
    "371...420": "Narva haigla",
    "421...470": "Pärnu haigla",
    "471...490": "Haapsalu haigla",
    "491...520": "Järvamaa haigla (Paide)",
    "521...570": "Rakvere haigla, Tapa haigla",
    "571...600": "Valga haigla",
    "601...650": "Viljandi haigla",
    "651...700": "Lõuna-Eesti haigla (Võru), Põlva haigla"
}

def get_kood(number, dict):
    for key, value in dict.items():
        start, end = key.split("...")
        start, end = int(start), int(end)

        if start <= number <= end:
            return value

haigla_kood = isikukood[7]*100 + isikukood[8]*10 + isikukood[9]

haigla_nimi = get_kood(haigla_kood, haiglad)

print(haigla_nimi)

kontrollnumber = (
    isikukood[0]*1 +
    isikukood[1]*2 +
    isikukood[2]*3 +
    isikukood[3]*4 +
    isikukood[4]*5 +
    isikukood[5]*6 +
    isikukood[6]*7 +
    isikukood[7]*8 +
    isikukood[8]*9 +
    isikukood[9]*1
)

kontrollnumber = kontrollnumber % 11
print(f"Kontrollnumber on {kontrollnumber}")