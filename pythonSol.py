#Write a function that takes a string as input and reverse only the vowels of a string.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1} #Create the dictionary with the vowels
        indices = {}
        letters = [] 
        j = -1 #Counter that will keep track of the length of "letters"
        for i, char in enumerate(s):
            if char in dic: #If it is a vowel
                indices[i] = char 
                letters.append(char) #Add it to the end 
                j += 1 #To reflect that the letters array increased
        i = 0 
        new_string =  ""
        for i in range(0, len(s)):
            if i in indices:
                new_string += letters[j]
                j -= 1 
            else:
                new_string += s[i]
        return new_string
                
    #Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        indices = {}
        letters = []
        counter = -1 #Keep track of the letters
        for i, char in enumerate(S):
            if (ord(char) > 64) and (ord(char) < 91): #Upper case letter
                indices[i] = char
                letters.append(char)
                counter += 1
            elif (ord(char) > 96) and (ord(char) < 123): #Upper case letter
                indices[i] = char
                letters.append(char)
                counter += 1
        new_string = ""
        for i in range(0, len(S)):
            if i in indices:
                new_string += letters[counter]
                counter -= 1
            else:
                new_string += S[i]
        return new_string