class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        temp_divisor=abs(divisor)
        temp_dividend=abs(dividend)
        ans=0
        while temp_dividend>=temp_divisor:
            d_n=temp_divisor
            quot=1
            
            while temp_dividend>=(d_n<<1):
                d_n<<=1
                quot<<=1
                
            temp_dividend-=d_n   
            ans+=quot
        if (dividend < 0) != (divisor < 0):
            ans = -ans

        if  ans>2**(31)-1:
            return  2**(31)-1
        elif ans<(-2**(31)):
            return -2**(31)
             
        return (ans)
        