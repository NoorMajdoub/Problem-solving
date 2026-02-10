import sys
dic={}
n=0
for line in sys.stdin:
    line =line.rstrip('\n')
   # print(line)
    #we capture the n
    if line.isnumeric() and len(dic)==0:
        n=int(line)
        continue #next boy in the line loop

    try :
            name,nb=line.split()
            dic[name]=nb
    except Exception:
             
        if line in dic.keys():
            print(f"{line}={dic[line]}")
        else :
            print(f"Not found")
        
    
