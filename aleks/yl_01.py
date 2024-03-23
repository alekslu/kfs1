# https://leetcode.com/problems/climbing-stairs/
# Kood on ehk veidi ülekommenteeritud. Tegin seda, et suudaksin endale ja teistele hiljem seletada mis koodis toimub.
# Koodi teeb kirjumaks ka asjaolu, et olen appi võtnud kaks listi, mille abil visualiseerida mis koodis sees tehakse - lahenduseks neid vaja tegelikult ei lähe

class Solution(object):
    def climbStairs(self, n):
        # viimasel kahel astmel on alati võimalik teha ainult 1 samm, et jõuda tippu 
        # (ka tipus olles tuleb teha lõppsamm kuigi oled juba kohal)
        # Samme on võimalik teha ühe või kahekaupa, kuna me alustame arvutust trepiastmete tipust, siis maksimum võimalike
        # ühe sammuliste sammude arv on 1 ja kahesammuliste oma samuti 1
        samme_yhekaupa, samme_kahekaupa = 1, 1
        
        numberOfPossibleClimbs = [] #abistav list
        numberOfPossibleClimbs.insert(0, samme_kahekaupa) #abistav list
        
        # Koodi kõige olulisem osa on see for tsükkel, siin peitub lahendus.
        # Käin läbi n-1 trepiastet, sest viimasel astmel enam kuhugi minna pole, seega pole ka midagi arvutada seal
        for trepiaste in range(n-1): 
            # ühekaupa sammud on alati järgmises for ringis väärtuseks samme_kahekaupa muutujale, liikuv väärtus
            eelmine_yhekaupa = samme_yhekaupa 
            # iga uus samme_yhekaupa väärtus on eelmiste samme_yhekaupa ja samme_kahekaupa summa 
            samme_yhekaupa = samme_yhekaupa + samme_kahekaupa 
            # samme_yhekaupa väärtusest saab järgmises tsüklis samme_kahekaupa väärtus
            samme_kahekaupa = eelmine_yhekaupa 

            numberOfPossibleClimbs.insert(samme_yhekaupa, eelmine_yhekaupa) #abistav list
        
        numberOfPossibleClimbs += [samme_yhekaupa]  #abistav list

         # Panen võimalike sammude kombinatsiooni jooksma tagant ette, et visualiseerida paremini 
         # kui palju võimalikke kombinatsioone igal astmel tippu jõudmiseks on
        numberOfPossibleClimbs.reverse()

        numberOfStairs = list(range(0,n+1))  #abistav list
        print(numberOfStairs) 

        # Võimalike sammude kombinatsioonide arv vasatavalt samas järjekorras eelmisel real loodud astmete listiga kuni tippu 
        # (0 on trepi algus, talle vastab kõige suurem võimalik tippu saamise kombinatsioonide arv)
        print(numberOfPossibleClimbs)


        return samme_yhekaupa