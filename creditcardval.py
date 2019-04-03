import re
T=int(raw_input())
while(T>0):
    inp=raw_input()
    if(not(inp[0]=='4' or inp[0]=='5' or inp[0]=='6')):
        print "Invalid"
        T-=1
        continue
    if "-" in inp:
        if(not(inp[4]=='-' and inp[9]=='-' and inp[14]=='-' and inp.count("-")==3)):
            print "Invalid"
            T-=1
            continue
    inp=inp.replace("-","")
    try:
        test=int(inp)
        if(len(inp)!=16):
            print "Invalid"
            T-=1
            continue
        count=0
        for i in range(1,16):
            if(inp[i]==inp[i-1]):
                count+=1
                if(count==4):
                    print "Invalid"
                    break
            else:
                count=1
        if(count==4):
            T-=1
            continue
    except ValueError:
        print "Invalid"
        T-=1
        continue
    print "Valid"
    T-=1
