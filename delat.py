def swayam(n,b,g):
    i = 0
    while (i<n):
        pos = g.find(b[0])
        if pos<0:
            break
        g = g[pos+1:] + g[:pos]
        b = b[1:]
        i +=1
	
    print(str(len(b)),end = "")
    
if __name__ == '__main__':    
    n = int(input())
    b = input()
    g = input()
    swayam(n,b,g)
