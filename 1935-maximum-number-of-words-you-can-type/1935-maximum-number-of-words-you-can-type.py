class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        textsplit=text.split()
        c=0
        for i in range(len(textsplit)):
            if any(word in (textsplit[i])  for word in (brokenLetters)):
                c+=1
        return (len(textsplit)-c)
        