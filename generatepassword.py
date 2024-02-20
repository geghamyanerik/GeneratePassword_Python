import string
import random



def generatePassword(theLength):
    letters = string.ascii_letters
    digit = string.digits
    totalChars = letters + digit
    finallPassword = ""
    for i in range(theLength):
        finallPassword+= random.choice(totalChars)
    return finallPassword
        





def main():
    while True:
       
        theLength = int(input("Enter password length : "))
      
        
        thePassword = generatePassword(theLength)
        
        print("Your password " +thePassword)
       
        break
       
main()
