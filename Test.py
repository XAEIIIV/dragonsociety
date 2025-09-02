list=(1,2,3,4,5,6)
indexlist=0
def bruteforce():
    for x in list:
        print(x)
        indexlist= indexlist+1
        if indexlist==len(list):
            print("Done")
bruteforce()
