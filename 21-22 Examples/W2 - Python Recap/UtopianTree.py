def utopianTree(n):
    height = 1
  
    for x in range(n):
        if n % 2 == 0:
          height *= 2
        else:
            height += 1
            
    return n
  
  
  print(utopianTree(5))
