class conditionalStatements:
    def checkString(self, s: str) -> bool:
        found_b = False 
        
        for char in s:
            if char == 'b':
                found_b = True
            elif char == 'a' and found_b:
               
                return False
        return True
s = "abab"
obj = conditionalStatements()
print(obj.checkString(s))  
