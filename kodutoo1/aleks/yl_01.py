# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        samme_yhekaupa, samme_kahekaupa = 1, 1
    
        for trepiaste in range(n-1): 
            eelmine_yhekaupa = samme_yhekaupa
            samme_yhekaupa = samme_yhekaupa + samme_kahekaupa
            samme_kahekaupa = eelmine_yhekaupa 
        
        # Mõttetu lisadefineerimine, aga et oleks arusaadavam
        koik_voimalikud_kombinatsioonid = samme_yhekaupa
        return koik_voimalikud_kombinatsioonid 