#Leetcode https://leetcode.com/problems/3sum-closest/
#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#Return the sum of the three integers.
#You may assume that each input would have exactly one solution.

#Lahendused tunduvad toimivat, kuid on Leetcode jaoks Submittimisel aeglased. Tuleks täiustada


from itertools import combinations  

#nums = [-1,2,1,-4]
#target = 1

#nums = [0,0,0]
#target = 1

nums = [745,912,-435,435,-290,857,354,927,-768,409,-450,13,-508,589,415,-383,-903,921,-641,532,36,-614,-522,-417,631,-601,452,-846,-788,-115,264,840,820,-284,699,860,96,-453,165,-443,973,552,-228,453,478,-139,888,667,249,31,346,-915,-431,-874,-449,-471,-833,-599,-929,-295,-971,77,536,393,-43,321,404,-310,698,-657,615,-801,-973,-870,-569,953,-133,-827,451,-101,-707,72,-862,-317,633,-120,722,262,-493,204,-515,-325,-628,6,84,577,923,11,-191,636,733,379,494,867,535,-797,345,-564,673,-237,847,-368,-873,694,186,-635,364,714,-790,-719,-152,106,-679,-812,233,-253,498,-59,-868,-786,0,-146,-486,-995,470,-207,341,-690,977,-796,757,878,-90,-72,-214,-451,-106,-795,-180,403,-255,493,467,-459,623,762,-192,-271,-463,259,967,725,884,-250,610,377,763,-61,358,664,987,122,-482,-87,109,658,-366,1000,-63,-902,-96,316,-742,516,-287,-716,719,-959,-683,-787,662,-653,-779,868,635,151,-343,496,230,591,-944,-404,-448,-773,-772,-326,-76,-335,821,-839,-875,-765,-703,-91,-542,-48,876,-381,396,-520,-134,-747,444,-487,731,-596,-78,-872,256,-82,-578,601,528,894,-771,-852,400,796,-495,147,571,-849,-674,-880,-892,218,803,966,909,-142,226,370,-401,223,229,-810,741,-93,-755,399,448,629,547,-568,593,193,-603,960,-282,555,241,449,572,832,56,-584,-618,-921,158,607,-693,802,-842,-24,886,397,-362,98,-727,344,287,-378,-476,508,-838,-480,-580,979,418,-103,-332,-737,254,713,-642,-551,-649,-162,-590,950,-173,-218]
target = -8392

def threeSumClosest(nums, target):
    kombinatsioonid = list(combinations(nums, 3)) #selle osa pean ilmselt ümber kirjutama (Time Limit Exceeded)
    kinnita_vahe = -1 #väärtustan tulemusega mis ei saa tulla, sest otsin absoluutväärtust hilisemas koodis

    for kombo in kombinatsioonid:
        kombo_summa = sum(kombo)

        absoluut_vahe = abs(target - kombo_summa)
        
        if absoluut_vahe < kinnita_vahe or kinnita_vahe == -1:
            l2him = kombo_summa
            kinnita_vahe = absoluut_vahe

    print(l2him)


threeSumClosest(nums, target)


''' 
Leetcode keskkonda kopeerimiseks::

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        kombinatsioonid = list(combinations(nums, 3)) #selle osa pean ilmselt ümber kirjutama (Time Limit Exceeded)
        
        kinnita_vahe = -1 #väärtustan tulemusega mis ei saa tulla, sest otsin absoluutväärtust hilisemas koodis

        for kombo in kombinatsioonid:
            kombo_summa = sum(kombo)

            absoluut_vahe = abs(target - kombo_summa)
            
            if absoluut_vahe < kinnita_vahe or kinnita_vahe == -1:
                l2him = kombo_summa
                kinnita_vahe = absoluut_vahe

        return l2him

'''