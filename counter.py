def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    senderList = {}
    totalCount = 0
    highestSender = ""

    for line in handle:
        if not line.startswith("From ") : continue
        line = line.split()
        sender = line[1]
        senderList[sender] = senderList.get(sender, 0) + 1
        
    for sender, count in senderList.items():
        if count > totalCount:
            totalCount = count
            highestSender = sender
    print(highestSender, totalCount)


## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
