class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        
        def check_4(n):
            
            try:
                return 0<=int(n)<=255 and str(int(n)) == n
            
            except:
                return False
            
        def check_6(n):
            
            if(len(n) > 4):
                return False
            
            try:
                return int(n,16) >= 0  and n[0] != '-'
            
            except:
                return False
                
            
        
        
        if(IP.count('.') == 3 and all(check_4(n) for n in IP.split('.'))):
            return 'IPv4'
        
        elif(IP.count(':') == 7 and all(check_6(n) for n in IP.split(':'))):
            return 'IPv6'
        
        else:
            return 'Neither'
            