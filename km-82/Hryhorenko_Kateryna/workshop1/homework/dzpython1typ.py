def rax(spysok,d):
    if len(spysok)==0:
        print(d)
        return d
    else:
        d+=int(spysok[0])
        rax(spysok[1:],d)
        



spysok=[1,3,5,2,5,32,4]
d=0
rax(spysok,d)
