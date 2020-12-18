import pyautogui as madbhai
import time
import random

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

# LOGO FOR MAD SPAM

print(red+bold+"<-. (`-')  (`-')  _ _(`-')    (`-').->_  (`-') (`-')  _ <-. (`-')  ")
print(red+bold+"   \(OO )_ (OO ).-/( (OO ).-> ( OO)_  \-.(OO ) (OO ).-/    \(OO )_ ")
print(red+bold+",--./  ,-.)/ ,---.  \    .'_ (_)--\_) _.'    \ / ,---.  ,--./  ,-.)")
print(lgreen+"|   `.'   || \ /`.\ '`'-..__)/    _ /(_...--'' | \ /`.\ |   `.'   |")
print(lgreen+"|  |'.'|  |'-'|_.' ||  |  ' |\_..`--.|  |_.' | '-'|_.' ||  |'.'|  |")
print(lgreen+"|  |   |  (|  .-.  ||  |  / :.-._)   \  .___.'(|  .-.  ||  |   |  |")
print(cyan+"|  |   |  ||  | |  ||  '-'  /\       /  |      |  | |  ||  |   |  |")
print(cyan+"`--'   `--'`--' `--'`------'  `-----'`--'      `--' `--'`--'   `--'")
print(lgreen+"                                                               V1.0 \n"+clear)


print (lgreen+bold+"         <===[[ coded by Mr. Mad Bhai ]]===> "+clear)
print (yellow+bold+"     <===(( search on youtube Mr. Mad Bhai ))===> "+clear)
print (lgreen+bold+"   <==={{ This Tool is made for Spamming... }}===> "+clear)
print (red+bold+"<===[( This Tool is Made For Educational Purpose Only. )]===> \n"+clear)

# wait to start
startingtime = input(yellow+"After How many Second You Wana to start: "+clear)
print(red+"Your Spammer send msg after", startingtime, "Second.\n"+clear)

# Spammer Range Input
spam_range = input (cyan+"Put Spam Range: "+clear)
time.sleep (int(startingtime))

# Taking File For Spam
mad_spam = open('madspam.txt', 'r').read()
mad_spam = mad_spam.splitlines()

# Please Don't Copy code
# Its Mad Bhai Here

# spam Number range
for _ in range (int(spam_range)): 
    madbhai.typewrite(random.choice(mad_spam))
    madbhai.press('enter')

# Taking User Name for Thanking
print("Your Spammer sended msg", spam_range, "times.\n")

user = input(lgreen+bold+"Put your name: "+clear)
print(yellow+"Hello", user, "Thanks For Using Mad Spam..."+clear)

