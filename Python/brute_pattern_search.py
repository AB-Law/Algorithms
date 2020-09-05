def PatternSearch(text, pattern):
    n,m = len(text),len(pattern)
    i=0
    for i in range (n-m+1):
        j=0
        while j < m:
            if(text[i+j]!=pattern[j]):
                break
            j+=1
        if(j == m):
            print("Pattern found", i)


txt = input("Please input the text: ")
pat = input("Please input the pattern to search for: ")
PatternSearch(txt, pat)
