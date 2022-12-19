import random

ans1 = "it is certain"
ans2 = "it is decidedly so"
ans3 = "without a doubt"
ans4 = "definitely"
ans5 = "you may rely on it"
ans6 = "as i can see it, yes"
ans7 = "most likey"
ans8 = "outlook good"
ans9 = "yes"
ans10 = "signs point to yes"
ans11 = "reply hazy, try again"
ans12 = "ask again later"
ans13 = "better not tell you now"
ans14 = "cannot predict now"
ans15 = "concentrate and ask agian"
ans16 = "dont count on it"
ans17 = "my reply is no"
ans18 = "my sources say no"
ans19 = "outlook not so good"
ans20 = "very doubtful"

name = input ("enter your name")
input (name + ",what is your questoin for the magic 8 ball? ")

choice = random.randint(1,20)
if choice == 1:
    answer = ans1
elif choice == 2:
    answer= ans2
elif choice == 3:
    answer= ans3
elif choice == 4:
    answer= ans4
elif choice == 5:
    answer= ans5
elif choice == 6:
    answer= ans6
elif choice == 7:
    answer= ans7
elif choice == 8:
    answer= ans8
elif choice == 9:
    answer= ans9
elif choice == 10:
    answer= ans10
elif choice == 11:
    answer= ans11
elif choice == 12:
    answer= ans12
elif choice == 13:
    answer= ans13
elif choice == 14:
    answer= ans14
elif choice == 15:
    answer= ans15
elif choice == 16:
    answer= ans16
elif choice == 17:
    answer= ans17
elif choice == 18:
    answer= ans18
elif choice == 19:
    answer= ans19
else:
    answer= ans20
print("************************************")
print ("magic 8 ball:", answer)
