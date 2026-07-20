score_user=int(input("Enter your score: "))
if score_user < 0 or score_user > 100:
    raise ValueError("Score must be between 0 and 100")
if score_user >= 90:
    print("You are qualified for the next round")
else:
    print("You are failed")
