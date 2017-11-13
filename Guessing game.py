import random
def menu(n,m):
    print("Guessing Game")
    print("")
    print("Note: type end to end the game early")
    d = int(raw_input("1. 1 vs. 1"
                      "\n2. 1 vs. Comp"))
    while True:
        if d == 1:
            intro(n,m)
            return False
        if d == 2:
            comp()
            return False
        if d!= 1 or d!=2:
            print("Error, please repeat")
def comp():
    d = int(raw_input("Computer Level"
                      "\n 1. Easy"
                      "\n 2. Hard"))
    while True:
        if d == 1:
            easycomp()
            return False
        if d == 2:
            hardcomp()
            return False
        if d!= 1 or d!=2:
            print("Error, please repeat")
def easycomp():
    overall  = 0
    overall2 = 0
    while True:
        d = int(raw_input("1.)Easy(0,10) \n2.)Medium(0,100) \n3.)Hard(0,1000)"))
        if d == 1:
            easylevel(overall,overall2)
            return False
        if d == 2:
            mediumlevel(overall,overall2)
            return False
        if d == 3:
            hardlevel(overall,overall2)
            return False
        if d!=1 or d!=2 or d!=3:
            print("Error please repeat")
def hardcomp():
    overall  = 0
    overall2 = 0
    while True:
        d = int(raw_input("1.)Easy(0,10) \n2.)Medium(0,100) \n3.)Hard(0,1000)"))
        if d == 1:
            easylevel2(overall,overall2)
            return False
        if d == 2:
            mediumlevel2(overall,overall2)
            return False
        if d == 3:
            hardlevel2(overall,overall2)
            return False
        if d!=1 or d!=2 or d!=3:
            print("Error please repeat")

def easylevel2(overall,overall2):
    end = False
    while end == False:
        s = random.randrange(10)
        ans = raw_input("Enter your guess")
        if ans.lower() in ['end']:
            earlyend(overall,overall2)
            end = True
        else:
            ans = int(ans)
        count = 1
        if end == False:
            while ans != s:
                if end == False:
                    if ans > s:
                        print("Lower")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                    if ans < s:
                        print("Higher")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                if end == True:
                    break
            if end == False:
                if ans == s:
                    s = str(s)
                    count = str(count)
                    print("Correct! The answer was " + s + ". You took " + count + " guess(es).")
                s = random.randrange(10)
                compAns = random.randrange(10)
                count2 = 1
                n = compAns
                e = n
                print(compAns)
                if compAns !=s:
                    while compAns != s:
                        if count2 % 2 == 0:
                            if compAns < e < s < n:
                                e = e
                                n = n
                            elif compAns < e < n < s:
                                n = n
                                e = e
                            elif compAns < n < s < e:
                                n = n
                                e = e
                            elif compAns < n < e < s:
                                n = n
                                e = e
                            elif compAns < s < e < n:
                                n = compAns
                            elif compAns < s < n < e:
                                e = compAns
                            elif s < e < compAns < n:
                                n = compAns
                            elif s < e < n < compAns:
                                n = n
                                e = e
                            elif s < n < e < compAns:
                                n = n
                                e = e
                            elif s < n < compAns < e:
                                e = compAns
                            elif s < compAns < e < n:
                                n = compAns
                            elif s < compAns < n < e:
                                e = compAns
                            elif e < n < compAns < s:
                                e = compAns
                            elif e < n < s < compAns:
                                e = compAns
                            elif e < s < compAns < n:
                                n = compAns
                            elif e < s < n < compAns:
                                n = n
                                e = e
                            elif e < compAns < s < n:
                                e = compAns
                            elif e < compAns < n < s:
                                e = compAns
                            elif n < s < e < compAns:
                                n = n
                                e = e
                            elif n < s < compAns < e:
                                e = compAns
                            elif n < compAns < s < e:
                                n = compAns
                            elif n < compAns < e < s:
                                n = compAns
                            elif n < e < s < compAns:
                                n = compAns
                            elif n < e < compAns < s:
                                n = compAns
                            elif n == e and e < compAns < s:
                                e = compAns
                            elif s < compAns < e and e == n:
                                e = compAns
                            elif compAns < s < e and e == n:
                                e = compAns
                            elif e < s < compAns and e == n:
                                e = compAns
                            elif s < e < compAns and e == n:
                                e = compAns
                            elif compAns < e < s and e == n:
                                e = compAns
                        if count2 % 2 == 1:
                            if compAns < e < s < n:
                                e = e
                                n = n
                            elif compAns < e < n < s:
                                n = n
                                e = e
                            elif compAns < n < s < e:
                                n = n
                                e = e
                            elif compAns < n < e < s:
                                n = n
                                e = e
                            elif compAns < s < e < n:
                                n = compAns
                            elif compAns < s < n < e:
                                e = compAns
                            elif s < e < compAns < n:
                                n = compAns
                            elif s < e < n < compAns:
                                n = n
                                e = e
                            elif s < n < e < compAns:
                                n = n
                                e = e
                            elif s < n < compAns < e:
                                e = compAns
                            elif s < compAns < e < n:
                                n = compAns
                            elif s < compAns < n < e:
                                e = compAns
                            elif e < n < compAns < s:
                                e = compAns
                            elif e < n < s < compAns:
                                e = compAns
                            elif e < s < compAns < n:
                                n = compAns
                            elif e < s < n < compAns:
                                n = n
                                e = e
                            elif e < compAns < s < n:
                                e = compAns
                            elif e < compAns < n < s:
                                e = compAns
                            elif n < s < e < compAns:
                                n = n
                                e = e
                            elif n < s < compAns < e:
                                e = compAns
                            elif n < compAns < s < e:
                                n = compAns
                            elif n < compAns < e < s:
                                n = compAns
                            elif n < e < s < compAns:
                                n = compAns
                            elif n < e < compAns < s:
                                n = compAns
                            elif n == e and e < compAns < s:
                                n = compAns
                            elif s < compAns < e and e == n:
                                n = compAns
                            elif compAns < s < e and e == n:
                                n = compAns
                            elif e < s < compAns and e == n:
                                n = compAns
                            elif s < e < compAns and e == n:
                                n = compAns
                            elif compAns < e < s and e == n:
                                n = compAns
                        if compAns > s:
                            if n > s and e > s:
                                if n > e:
                                    compAns = random.randrange(e)
                                elif n < e:
                                    compAns = random.randrange(n)
                                elif n == e:
                                    compAns = random.randrange(n)
                            elif n > s and e < s:
                                compAns = random.randrange(e + 1, n)
                            elif n < s and e > s:
                                compAns = random.randrange(n + 1, e)
                            elif n == e:
                                compAns = random.randrange(n)
                        elif compAns < s:
                            if n < s and e < s:
                                if n > e:
                                    compAns = random.randrange(n + 1, 10)
                                elif n < e:
                                    compAns = random.randrange(e + 1, 10)
                                elif n == e:
                                    compAns = random.randrange(n + 1, 10)
                            elif n > s and e < s:
                                compAns = random.randrange(e + 1, n)
                            elif n < s and e > s:
                                compAns = random.randrange(n + 1, e)
                            elif n > s and e < s:
                                compAns = random.randrange(e + 1, n)
                            elif n < s and e > s:
                                compAns = random.randrange(n + 1, e)
                            elif n == e:
                                compAns = random.randrange(n + 1, 10)
                        count2 = count2 + 1
                        print(compAns)
                count2 = str(count2)
                s = str(s)
                print("Computer's number is " + s)
                print("Computer took " + count2 + " guess(es).")
                count2 = int(count2)
                count = int(count)
                if count > count2:
                    print("Computer win this round")
                    overall2 = int(overall2)
                    overall = int(overall)
                    overall2 = overall2 +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is "+overall)
                    print("Computer's score is "+ overall2)
                if count < count2:
                    print("You win this round")
                    overall = int(overall)
                    overall2 = int(overall2)
                    overall = overall +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is " + overall)
                    print("Computer's score is " + overall2)
                overall = int(overall)
                overall2 = int(overall2)
                if count == count2:
                    print("Tie")
                if overall == 3:
                    endself()
                elif overall2 == 3:
                    endcomp()
                else:
                    easylevel2(overall,overall2)

def mediumlevel2(overall,overall2):
    end = False
    while end == False:
        s = random.randrange(100)
        ans = raw_input("Enter your guess")
        if ans.lower() in ['end']:
            earlyend(overall, overall2)
            end = True
        else:
            ans = int(ans)
        count = 1
        if end == False:
            while ans != s:
                if end == False:
                    if ans > s:
                        print("Lower")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                    if ans < s:
                        print("Higher")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                if end == True:
                    break
            if end == False:
                if ans == s:
                    s = str(s)
                    count = str(count)
                    print("Correct! The answer was " + s + ". You took " + count + " guess(es).")
                s = random.randrange(100)
                compAns = random.randrange(100)
                count2 = 1
                n = compAns
                e = n
                print(compAns)
                if compAns != s:
                    while compAns != s:
                        if count2 % 2 == 0:
                            if compAns < e < s < n:
                                e = e
                                n = n
                            elif compAns < e < n < s:
                                n = n
                                e = e
                            elif compAns < n < s < e:
                                n = n
                                e = e
                            elif compAns < n < e < s:
                                n = n
                                e = e
                            elif compAns < s < e < n:
                                n = compAns
                            elif compAns < s < n < e:
                                e = compAns
                            elif s < e < compAns < n:
                                n = compAns
                            elif s < e < n < compAns:
                                n = n
                                e = e
                            elif s < n < e < compAns:
                                n = n
                                e = e
                            elif s < n < compAns < e:
                                e = compAns
                            elif s < compAns < e < n:
                                n = compAns
                            elif s < compAns < n < e:
                                e = compAns
                            elif e < n < compAns < s:
                                e = compAns
                            elif e < n < s < compAns:
                                e = compAns
                            elif e < s < compAns < n:
                                n = compAns
                            elif e < s < n < compAns:
                                n = n
                                e = e
                            elif e < compAns < s < n:
                                e = compAns
                            elif e < compAns < n < s:
                                e = compAns
                            elif n < s < e < compAns:
                                n = n
                                e = e
                            elif n < s < compAns < e:
                                e = compAns
                            elif n < compAns < s < e:
                                n = compAns
                            elif n < compAns < e < s:
                                n = compAns
                            elif n < e < s < compAns:
                                n = compAns
                            elif n < e < compAns < s:
                                n = compAns
                            elif n == e and e < compAns < s:
                                e = compAns
                            elif s < compAns < e and e == n:
                                e = compAns
                            elif compAns < s < e and e == n:
                                e = compAns
                            elif e < s < compAns and e == n:
                                e = compAns
                            elif s < e < compAns and e == n:
                                e = compAns
                            elif compAns < e < s and e == n:
                                e = compAns
                        if count2 % 2 == 1:
                            if compAns < e < s < n:
                                e = e
                                n = n
                            elif compAns < e < n < s:
                                n = n
                                e = e
                            elif compAns < n < s < e:
                                n = n
                                e = e
                            elif compAns < n < e < s:
                                n = n
                                e = e
                            elif compAns < s < e < n:
                                n = compAns
                            elif compAns < s < n < e:
                                e = compAns
                            elif s < e < compAns < n:
                                n = compAns
                            elif s < e < n < compAns:
                                n = n
                                e = e
                            elif s < n < e < compAns:
                                n = n
                                e = e
                            elif s < n < compAns < e:
                                e = compAns
                            elif s < compAns < e < n:
                                n = compAns
                            elif s < compAns < n < e:
                                e = compAns
                            elif e < n < compAns < s:
                                e = compAns
                            elif e < n < s < compAns:
                                e = compAns
                            elif e < s < compAns < n:
                                n = compAns
                            elif e < s < n < compAns:
                                n = n
                                e = e
                            elif e < compAns < s < n:
                                e = compAns
                            elif e < compAns < n < s:
                                e = compAns
                            elif n < s < e < compAns:
                                n = n
                                e = e
                            elif n < s < compAns < e:
                                e = compAns
                            elif n < compAns < s < e:
                                n = compAns
                            elif n < compAns < e < s:
                                n = compAns
                            elif n < e < s < compAns:
                                n = compAns
                            elif n < e < compAns < s:
                                n = compAns
                            elif n == e and e < compAns < s:
                                n = compAns
                            elif s < compAns < e and e == n:
                                n = compAns
                            elif compAns < s < e and e == n:
                                n = compAns
                            elif e < s < compAns and e == n:
                                n = compAns
                            elif s < e < compAns and e == n:
                                n = compAns
                            elif compAns < e < s and e == n:
                                n = compAns
                        if compAns > s:
                            if n > s and e > s:
                                if n > e:
                                    compAns = random.randrange(e)
                                elif n < e:
                                    compAns = random.randrange(n)
                                elif n == e:
                                    compAns = random.randrange(n)
                            elif n > s and e < s:
                                compAns = random.randrange(e + 1, n)
                            elif n < s and e > s:
                                compAns = random.randrange(n + 1, e)
                            elif n == e:
                                compAns = random.randrange(n)
                        elif compAns < s:
                            if n < s and e < s:
                                if n > e:
                                    compAns = random.randrange(n + 1, 100)
                                elif n < e:
                                    compAns = random.randrange(e + 1, 100)
                                elif n == e:
                                    compAns = random.randrange(n + 1, 100)
                            elif n > s and e < s:
                                compAns = random.randrange(e + 1, n)
                            elif n < s and e > s:
                                compAns = random.randrange(n + 1, e)
                            elif n > s and e < s:
                                compAns = random.randrange(e + 1, n)
                            elif n < s and e > s:
                                compAns = random.randrange(n + 1, e)
                            elif n == e:
                                compAns = random.randrange(n + 1, 100)
                        count2 = count2 + 1
                        print(compAns)
                count2 = str(count2)
                s = str(s)
                print("Computer's number is " + s +
                      "\nComputer took " + count2 + " guess(es).")
                count2 = int(count2)
                count = int(count)
                if count > count2:
                    print("Computer win this round")
                    overall2 = int(overall2)
                    overall = int(overall)
                    overall2 = overall2 +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is "+overall)
                    print("Computer's score is "+ overall2)
                if count < count2:
                    print("You win this round")
                    overall = int(overall)
                    overall2 = int(overall2)
                    overall = overall +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is " + overall)
                    print("Computer's score is " + overall2)
                overall = int(overall)
                overall2 = int(overall2)
                if count == count2:
                    print("Tie")
                if overall == 3:
                    endself()
                elif overall2 == 3:
                    endcomp()
                else:
                    mediumlevel2(overall,overall2)

def hardlevel2(overall,overall2):
    end = False
    while end == False:
        s = random.randrange(1000)
        ans = raw_input("Enter your guess")
        if ans.lower() in ['end']:
            earlyend(overall, overall2)
            end = True
        else:
            ans = int(ans)
        count = 1
        if end == False:
            while ans != s:
                if end == False:
                    if ans > s:
                        print("Lower")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                    if ans < s:
                        print("Higher")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                if end == True:
                    break
            if end == False:
                if ans == s:
                    s = str(s)
                    count = str(count)
                    print("Correct! The answer was " + s + ". You took " + count + " guess(es).")
                s = random.randrange(1000)
                compAns = random.randrange(1000)
                count2 = 1
                n = compAns
                e = n
                print(compAns)
                if compAns != s:
                    while compAns != s:
                        if count2 % 2 == 0:
                            if compAns < e < s < n:
                                e = e
                                n = n
                            elif compAns < e < n < s:
                                n = n
                                e = e
                            elif compAns < n < s < e:
                                n = n
                                e = e
                            elif compAns < n < e < s:
                                n = n
                                e = e
                            elif compAns < s < e < n:
                                n = compAns
                            elif compAns < s < n < e:
                                e = compAns
                            elif s < e < compAns < n:
                                n = compAns
                            elif s < e < n < compAns:
                                n = n
                                e = e
                            elif s < n < e < compAns:
                                n = n
                                e = e
                            elif s < n < compAns < e:
                                e = compAns
                            elif s < compAns < e < n:
                                n = compAns
                            elif s < compAns < n < e:
                                e = compAns
                            elif e < n < compAns < s:
                                e = compAns
                            elif e < n < s < compAns:
                                e = compAns
                            elif e < s < compAns < n:
                                n = compAns
                            elif e < s < n < compAns:
                                n = n
                                e = e
                            elif e < compAns < s < n:
                                e = compAns
                            elif e < compAns < n < s:
                                e = compAns
                            elif n < s < e < compAns:
                                n = n
                                e = e
                            elif n < s < compAns < e:
                                e = compAns
                            elif n < compAns < s < e:
                                n = compAns
                            elif n < compAns < e < s:
                                n = compAns
                            elif n < e < s < compAns:
                                n = compAns
                            elif n < e < compAns < s:
                                n = compAns
                            elif n == e and e < compAns < s:
                                e = compAns
                            elif s < compAns < e and e == n:
                                e = compAns
                            elif compAns < s < e and e == n:
                                e = compAns
                            elif e < s < compAns and e == n:
                                e = compAns
                            elif s < e < compAns and e == n:
                                e = compAns
                            elif compAns < e < s and e == n:
                                e = compAns
                        if count2 % 2 == 1:
                            if compAns < e < s < n:
                                e = e
                                n = n
                            elif compAns < e < n < s:
                                n = n
                                e = e
                            elif compAns < n < s < e:
                                n = n
                                e = e
                            elif compAns < n < e < s:
                                n = n
                                e = e
                            elif compAns < s < e < n:
                                n = compAns
                            elif compAns < s < n < e:
                                e = compAns
                            elif s < e < compAns < n:
                                n = compAns
                            elif s < e < n < compAns:
                                n = n
                                e = e
                            elif s < n < e < compAns:
                                n = n
                                e = e
                            elif s < n < compAns < e:
                                e = compAns
                            elif s < compAns < e < n:
                                n = compAns
                            elif s < compAns < n < e:
                                e = compAns
                            elif e < n < compAns < s:
                                e = compAns
                            elif e < n < s < compAns:
                                e = compAns
                            elif e < s < compAns < n:
                                n = compAns
                            elif e < s < n < compAns:
                                n = n
                                e = e
                            elif e < compAns < s < n:
                                e = compAns
                            elif e < compAns < n < s:
                                e = compAns
                            elif n < s < e < compAns:
                                n = n
                                e = e
                            elif n < s < compAns < e:
                                e = compAns
                            elif n < compAns < s < e:
                                n = compAns
                            elif n < compAns < e < s:
                                n = compAns
                            elif n < e < s < compAns:
                                n = compAns
                            elif n < e < compAns < s:
                                n = compAns
                            elif n == e and e < compAns < s:
                                n = compAns
                            elif s < compAns < e and e == n:
                                n = compAns
                            elif compAns < s < e and e == n:
                                n = compAns
                            elif e < s < compAns and e == n:
                                n = compAns
                            elif s < e < compAns and e == n:
                                n = compAns
                            elif compAns < e < s and e == n:
                                n = compAns
                        if compAns > s:
                            if n > s and e > s:
                                if n > e:
                                    compAns = random.randrange(e)
                                elif n < e:
                                    compAns = random.randrange(n)
                                elif n == e:
                                    compAns = random.randrange(n)
                            elif n > s and e < s:
                                compAns = random.randrange(e + 1, n)
                            elif n < s and e > s:
                                compAns = random.randrange(n + 1, e)
                            elif n == e:
                                compAns = random.randrange(n)
                        elif compAns < s:
                            if n < s and e < s:
                                if n > e:
                                    compAns = random.randrange(n + 1, 1000)
                                elif n < e:
                                    compAns = random.randrange(e + 1, 1000)
                                elif n == e:
                                    compAns = random.randrange(n + 1, 1000)
                            elif n > s and e < s:
                                compAns = random.randrange(e + 1, n)
                            elif n < s and e > s:
                                compAns = random.randrange(n + 1, e)
                            elif n > s and e < s:
                                compAns = random.randrange(e + 1, n)
                            elif n < s and e > s:
                                compAns = random.randrange(n + 1, e)
                            elif n == e:
                                compAns = random.randrange(n + 1, 1000)
                        count2 = count2 + 1
                        print(compAns)
                count2 = str(count2)
                s = str(s)
                print("Computer's number is " + s +
                      "\nComputer took " + count2 + " guess(es).")
                count2 = int(count2)
                count = int(count)
                if count > count2:
                    print("Computer win this round")
                    overall2 = int(overall2)
                    overall = int(overall)
                    overall2 = overall2 +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is "+overall)
                    print("Computer's score is "+ overall2)
                if count < count2:
                    print("You win this round")
                    overall = int(overall)
                    overall2 = int(overall2)
                    overall = overall +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is " + overall)
                    print("Computer's score is " + overall2)
                if count == count2:
                    print("Tie")
                overall = int(overall)
                overall2 = int(overall2)
                if overall == 3:
                    endself()
                elif overall2 == 3:
                    endcomp()
                else:
                    hardlevel2(overall,overall2)

def endcomp():
    print("Computer wins")
def endself():
    print("You win")
def easylevel(overall,overall2):
    end = False
    while end == False:
        s = random.randrange(10)
        ans = raw_input("Enter your guess")
        if ans.lower() in ['end']:
            earlyend(overall, overall2)
            end = True
        else:
            ans = int(ans)
        count = 1
        if end == False:
            while ans != s:
                if end == False:
                    if ans > s:
                        print("Lower")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall,overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                    if ans < s:
                        print("Higher")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                if end == True:
                    break
            if end == False:
                if ans == s:
                    s = str(s)
                    count = str(count)
                    print("Correct! The answer was " + s + ". You took " + count + " guess(es).")
                s = random.randrange(10)
                compAns = random.randrange(10)
                count2 = 1
                while compAns != s:
                    compAns = random.randrange(10)
                    count2 = count2 + 1
                count2 = str(count2)
                print("Computer took " + count2 + " guess(es).")
                count2 = int(count2)
                count = int(count)
                if count > count2:
                    print("Computer win this round")
                    overall2 = int(overall2)
                    overall = int(overall)
                    overall2 = overall2 +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is "+overall)
                    print("Computer's score is "+ overall2)
                if count < count2:
                    print("You win this round")
                    overall = int(overall)
                    overall2 = int(overall2)
                    overall = overall +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is " + overall)
                    print("Computer's score is " + overall2)
                if count == count2:
                    print("Tie")
                overall = int(overall)
                overall2 = int(overall2)
                if overall == 3:
                    endself()
                elif overall2 == 3:
                    endcomp()
                else:
                    easylevel(overall,overall2)
def mediumlevel(overall,overall2):
    end = False
    while end == False:
        s = random.randrange(100)
        ans = raw_input("Enter your guess")
        if ans.lower() in ['end']:
            earlyend(overall, overall2)
            end = True
        else:
            ans = int(ans)
        count = 1
        if end == False:
            while ans != s:
                if end == False:
                    if ans > s:
                        print("Lower")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                    if ans < s:
                        print("Higher")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                if end == True:
                    break
            if end == False:
                if ans == s:
                    s = str(s)
                    count = str(count)
                    print("Correct! The answer was " + s + ". You took " + count + " guess(es).")
                s = random.randrange(100)
                compAns = random.randrange(100)
                count2 = 1
                while compAns != s:
                    compAns = random.randrange(100)
                    count2 = count2 + 1
                count2 = str(count2)
                print("Computer took " + count2 + " guess(es).")
                count2 = int(count2)
                count = int(count)
                if count > count2:
                    print("Computer win this round")
                    overall2 = int(overall2)
                    overall = int(overall)
                    overall2 = overall2 +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is "+overall)
                    print("Computer's score is "+ overall2)
                if count < count2:
                    print("You win this round")
                    overall = int(overall)
                    overall2 = int(overall2)
                    overall = overall +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is " + overall)
                    print("Computer's score is " + overall2)
                if count == count2:
                    print("Tie")
                overall = int(overall)
                overall2 = int(overall2)
                if overall == 3:
                    endself()
                elif overall2 == 3:
                    endcomp()
                else:
                    mediumlevel(overall,overall2)
def hardlevel(overall,overall2):
    end = False
    while end == False:
        s = random.randrange(1000)
        ans = raw_input("Enter your guess")
        if ans.lower() in ['end']:
            earlyend(overall, overall2)
            end = True
        else:
            ans = int(ans)
        count = 1
        if end == False:
            while ans != s:
                if end == False:
                    if ans > s:
                        print("Lower")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                    if ans < s:
                        print("Higher")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyend(overall, overall2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                if end == True:
                    break
            if end == False:
                if ans == s:
                    s = str(s)
                    count = str(count)
                    print("Correct! The answer was " + s + ". You took " + count + " guess(es).")
                s = random.randrange(1000)
                compAns = random.randrange(1000)
                count2 = 1
                while compAns != s:
                    compAns = random.randrange(1000)
                    count2 = count2 + 1
                count2 = str(count2)
                print("Computer took " + count2 + " guess(es).")
                count2 = int(count2)
                count = int(count)
                if count > count2:
                    print("Computer win this round")
                    overall2 = int(overall2)
                    overall = int(overall)
                    overall2 = overall2 +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is "+overall)
                    print("Computer's score is "+ overall2)
                if count < count2:
                    print("You win this round")
                    overall = int(overall)
                    overall2 = int(overall2)
                    overall = overall +1
                    overall2 = str(overall2)
                    overall = str(overall)
                    print("Your score is " + overall)
                    print("Computer's score is " + overall2)
                if count == count2:
                    print("Tie")
                overall = int(overall)
                overall2 = int(overall2)
                if overall == 3:
                    endself()
                elif overall2 == 3:
                    endcomp()
                else:
                    hardlevel(overall,overall2)
def intro(n,m):
    overall  = n
    overall2 = m
    player1 = raw_input("Player 1 name:")
    player2 = raw_input("Player 2 name:")
    while True:
        d = int(raw_input("1.)Easy(0,10) \n2.)Medium(0,100) \n3.)Hard(0,1000)"))
        if d == 1:
            easy(overall,overall2,player1,player2)
            return False
        if d == 2:
            medium(overall,overall2,player1,player2)
            return False
        if d == 3:
            hard(overall,overall2,player1,player2)
            return False
        if d!=1 or d!=2 or d!=3:
            print("Error please repeat")
def easy(overall,overall2,player1,player2):
    end = False
    while end == False:
        print("It is " + player1 + "'s turn")
        s = random.randrange(10)
        ans = raw_input("Enter your guess")
        if ans.lower() in ['end']:
            earlyendplayer(overall, overall2, player1, player2)
            end = True
        else:
            ans = int(ans)
        if end == False:
            count = 1
            while ans != s:
                if end == False:
                    if ans > s:
                        print("Lower")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyendplayer(overall, overall2, player1, player2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                    elif ans < s:
                        print("Higher")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyendplayer(overall, overall2, player1, player2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                if end == True:
                    break
            if end == False:
                if ans == s:
                    s = str(s)
                    count = str(count)
                    print("Correct! The answer was " + s + ". You took " + count + " guess(es).")
                print("It is " + player2 + "'s turn")
                n = random.randrange(10)
                ans = raw_input("Enter your guess")
                if ans.lower() in ['end']:
                    earlyendplayer(overall, overall2, player1, player2)
                    end = True
                else:
                    ans = int(ans)
                if end == False:
                    count2 = 1
                    while ans != n:
                        if end == False:
                            if ans > n:
                                print("Lower")
                                ans = raw_input("Enter your guess")
                                if ans.lower() in ['end']:
                                    earlyendplayer(overall, overall2, player1, player2)
                                    end = True
                                else:
                                    ans = int(ans)
                                count2 = count2 + 1
                            elif ans < n:
                                print("Higher")
                                ans = raw_input("Enter your guess")
                                if ans.lower() in ['end']:
                                    earlyendplayer(overall, overall2, player1, player2)
                                    end = True
                                else:
                                    ans = int(ans)
                                count2 = count2 + 1
                            if count2 > count:
                                ans = str(ans)
                                print("The answer is " + ans)
                            if end == True:
                                break
                    if end == False:
                        if ans == n:
                            n = str(n)
                            count2 = str(count2)
                            print("Correct! The answer was " + n + ". You took " + count2 + " guess(es).")
                        count = int(count)
                        count2 = int(count2)
                        if count > count2:
                            print("This round's winner is " + player2)
                            overall2 = int(overall2)
                            overall = int(overall)
                            overall2 = overall2 + 1
                            overall2 = str(overall2)
                            overall = str(overall)
                            print(player1 + "'s score is " + overall)
                            print(player2 + "'s score is " + overall2)
                        if count < count2:
                            print("This round's winner is " + player1)
                            overall = int(overall)
                            overall2 = int(overall2)
                            overall = overall + 1
                            overall2 = str(overall2)
                            overall = str(overall)
                            print(player1 + "'s score is " + overall)
                            print(player2 + "'s score is " + overall2)
                        if count == count2:
                            print("Tie")
                        overall = int(overall)
                        overall2 = int(overall2)
                        if overall == 3:
                            ending(player1)
                        elif overall2 == 3:
                            end2(player2)
                        else:
                            easy(overall, overall2, player1, player2)
def medium(overall,overall2, player1,player2):
    end = False
    while end == False:
        print("It is " + player1 + "'s turn")
        s = random.randrange(100)
        ans = raw_input("Enter your guess")
        if ans.lower() in ['end']:
            earlyendplayer(overall, overall2, player1, player2)
            end = True
        else:
            ans = int(ans)
        if end == False:
            count = 1
            while ans != s:
                if end == False:
                    if ans > s:
                        print("Lower")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyendplayer(overall, overall2, player1, player2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                    elif ans < s:
                        print("Higher")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyendplayer(overall, overall2, player1, player2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                if end == True:
                    break
            if end == False:
                if ans == s:
                    s = str(s)
                    count = str(count)
                    print("Correct! The answer was " + s + ". You took " + count + " guess(es).")
                print("It is " + player2 + "'s turn")
                n = random.randrange(100)
                ans = raw_input("Enter your guess")
                if ans.lower() in ['end']:
                    earlyendplayer(overall, overall2, player1, player2)
                    end = True
                else:
                    ans = int(ans)
                if end == False:
                    count2 = 1
                    while ans != n:
                        if end == False:
                            if ans > n:
                                print("Lower")
                                ans = raw_input("Enter your guess")
                                if ans.lower() in ['end']:
                                    earlyendplayer(overall, overall2, player1, player2)
                                    end = True
                                else:
                                    ans = int(ans)
                                count2 = count2 + 1
                            elif ans < n:
                                print("Higher")
                                ans = raw_input("Enter your guess")
                                if ans.lower() in ['end']:
                                    earlyendplayer(overall, overall2, player1, player2)
                                    end = True
                                else:
                                    ans = int(ans)
                                count2 = count2 + 1
                            if count2 > count:
                                ans = str(ans)
                                print("The answer is " + ans)
                            if end == True:
                                break
                    if end == False:
                        if ans == n:
                            n = str(n)
                            count2 = str(count2)
                            print("Correct! The answer was " + n + ". You took " + count2 + " guess(es).")
                        count = int(count)
                        count2 = int(count2)
                        if count > count2:
                            print("This round's winner is " + player2)
                            overall2 = int(overall2)
                            overall = int(overall)
                            overall2 = overall2 + 1
                            overall2 = str(overall2)
                            overall = str(overall)
                            print(player1 + "'s score is " + overall)
                            print(player2 + "'s score is " + overall2)
                        if count < count2:
                            print("This round's winner is " + player1)
                            overall = int(overall)
                            overall2 = int(overall2)
                            overall = overall + 1
                            overall2 = str(overall2)
                            overall = str(overall)
                            print(player1 + "'s score is " + overall)
                            print(player2 + "'s score is " + overall2)
                        if count == count2:
                            print("Tie")
                        overall = int(overall)
                        overall2 = int(overall2)
                        if overall == 3:
                            ending(player1)
                        elif overall2 == 3:
                            end2(player2)
                        else:
                            medium(overall, overall2, player1, player2)
def hard(overall, overall2, player1, player2):
    end = False
    while end == False:
        print("It is " + player1 +"'s turn")
        s = random.randrange(1000)
        ans = raw_input("Enter your guess")
        if ans.lower() in ['end']:
            earlyendplayer(overall, overall2, player1, player2)
            end = True
        else:
            ans = int(ans)
        if end == False:
            count = 1
            while ans != s:
                if end == False:
                    if ans > s:
                        print("Lower")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyendplayer(overall, overall2, player1, player2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count +1
                    elif ans < s:
                        print("Higher")
                        ans = raw_input("Enter your guess")
                        if ans.lower() in ['end']:
                            earlyendplayer(overall, overall2, player1, player2)
                            end = True
                        else:
                            ans = int(ans)
                        count = count + 1
                if end == True:
                    break
            if end == False:
                if ans == s:
                    s = str(s)
                    count = str(count)
                    print("Correct! The answer was " + s + ". You took "+ count + " guess(es).")
                print("It is " + player2 + "'s turn")
                n = random.randrange(1000)
                ans = raw_input("Enter your guess")
                if ans.lower() in ['end']:
                    earlyendplayer(overall, overall2, player1, player2)
                    end = True
                else:
                    ans = int(ans)
                if end == False:
                    count2 = 1
                    while ans != n:
                        if end == False:
                            if ans > n:
                                print("Lower")
                                ans = raw_input("Enter your guess")
                                if ans.lower() in ['end']:
                                    earlyendplayer(overall, overall2, player1, player2)
                                    end = True
                                else:
                                    ans = int(ans)
                                count2 = count2 + 1
                            elif ans < n:
                                print("Higher")
                                ans = raw_input("Enter your guess")
                                if ans.lower() in ['end']:
                                    earlyendplayer(overall, overall2, player1, player2)
                                    end = True
                                else:
                                    ans = int(ans)
                                count2 = count2 + 1
                            if count2 > count:
                                ans = str(ans)
                                print("The answer is " + ans)
                            if end == True:
                                break
                    if end == False:
                        if ans == n:
                            n = str(n)
                            count2 = str(count2)
                            print("Correct! The answer was " + n + ". You took " + count2 + " guess(es).")
                        count = int(count)
                        count2 = int(count2)
                        if count > count2:
                            print("This round's winner is " + player2)
                            overall2 = int(overall2)
                            overall = int(overall)
                            overall2 = overall2 +1
                            overall2 = str(overall2)
                            overall = str(overall)
                            print(player1 +"'s score is "+overall)
                            print(player2 +"'s score is "+ overall2)
                        if count < count2:
                            print("This round's winner is " + player1)
                            overall = int(overall)
                            overall2 = int(overall2)
                            overall = overall +1
                            overall2 = str(overall2)
                            overall = str(overall)
                            print(player1 +"'s score is "+overall)
                            print(player2 +"'s score is "+ overall2)
                        if count == count2:
                            print("Tie")
                        overall = int(overall)
                        overall2 = int(overall2)
                        if overall == 3:
                            ending(player1)
                        elif overall2 == 3:
                            end2(player2)
                        else:
                            hard(overall,overall2,player1,player2)
def ending(player1):
    print("The winner of the game is " + player1)
def end2(player2):
    print("The winner of the game is " + player2)
def earlyend(overall,overall2):
    if overall == overall2:
        print('Tie')
    elif overall > overall2:
        print("You win")
    elif overall2 > overall:
        print("Comp wins")
def earlyendplayer(overall, overall2, player1, player2):
    if overall == overall2:
        print('Tie')
    elif overall > overall2:
        print(player1 + 'wins')
    elif overall2 > overall:
        print(player2 + 'wins')
def main():
    n=0
    m=0
    menu(n,m)
main()