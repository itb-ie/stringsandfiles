import datetime
fp = open("my_diary.txt", "a")
while True:
    entry = input("What are you doing now (type quit to exit)")
    now = datetime.datetime.now()
    today = now.strftime("%d/%m/%y %H:%M")
    if entry == "quit":
        break
    # \n means new line
    fp.write(f"{today} {entry}\n")
fp.close()
