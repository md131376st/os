alphabet = 'abcdefghijklmnopqrstuvwxyz'
numOfTestcases = int(raw_input())
i = 0
while i < numOfTestcases:
    numOfWords = int(raw_input())
    first = []
    last = []
    for alpha in alphabet:
        first.append([alpha, 0])
        last.append([alpha, 0])

    while numOfWords > 0 :
        sts = [raw_input()]
        first[alphabet.find(sts[0][0])][1] += 1
        last[alphabet.find(sts[0][-1])][1] += 1
        numOfWords -= 1

    ok, f, l = 1, 0, 0
    for n in xrange(0,26):
        dif = first[n][1] - last[n][1]
        if dif > 1 or dif < -1 or (dif == 1 and f ==1) or (dif == -1 and l == 1):
            ok = 0
            print 'not possible'
            break
        elif dif == 1: f = 1
        elif dif == -1: l = 1

    if ok == 1: print 'possible'
            
    i += 1