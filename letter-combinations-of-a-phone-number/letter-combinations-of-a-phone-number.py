
# steps
# pick a digit
# for each letter mapped to the digit
# add it to every letter in the existing answer

class Solution:
    def __init__(self):
        self.mapp = {"1":"", "2":"abc", "3":"def",
                      "4":"ghi", "5":"jkl", "6":"mno",
                      "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = []
        for digit in digits:
            combinations = self.helper(self.mapp[digit], combinations)
        return combinations    
    def helper(self, letters, combinations):
        if len(letters) == 0:
            return []
        newCombo = []
        newLetter = letters[0]
        if len(combinations) == 0:
            newCombo.append(newLetter)
        else:
            for letter in combinations:
                newCombo.append(letter + newLetter)
        return newCombo + self.helper(letters[1:], combinations)
        
            
            
        