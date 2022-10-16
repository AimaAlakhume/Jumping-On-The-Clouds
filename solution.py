def jumpingOnClouds(c):
  
    jumps = 0
    pos = 0
    
    while pos < len(c) - 1:
        if pos + 2 < len(c) and c[pos + 2] == 0:
            pos += 2
            jumps += 1
        else:
            pos += 1
            jumps += 1
    
    return jumps
