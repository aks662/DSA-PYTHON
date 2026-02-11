from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ans=False
        n=len(s)

        mp_target = Counter(t)
        mp_string={}

        length=n
        # length_new=n

        l_p=0
        right_idx=0
        left_idx=0

        unique=len(mp_target)                   # or can use if mp_string in mp_target
        char=0

        for r_p in range(n):
            
            mp_string[s[r_p]]=mp_string.get(s[r_p],0)+1    #1
            
            if s[r_p] in mp_target and mp_string[s[r_p]]== mp_target[s[r_p]] :
                char+=1                                        #2
            
            
            if char==unique:
                ans=True           #3
                
            while unique==char:      #4
                #update first
                length_new=r_p-l_p+1       #4.2                                    
                
                if length_new<=length:       #4.3
                    left_idx=l_p
                    right_idx=r_p
                    length=length_new
                #shrink then   
                mp_string[s[l_p]]=mp_string.get(s[l_p])-1       #4.1
                    
                if s[l_p] in mp_target and mp_string[s[l_p]] < mp_target[s[l_p]]:     #4.4
                    char-=1 
                    
                    
                l_p+=1                  #4.5
            

        if ans :                        #5
            return (s[left_idx:right_idx+1])
        else:
            return ("")              
                        