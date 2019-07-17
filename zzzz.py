def findK (n, k ): 
    a = list() 
      
    # insert all the odd  
    # numbers from 1 to n. 
    i = 1
    while i < n: 
        a.append(i) 
        i = i + 2
      
    # insert all the even  
    # numbers from 1 to n. 
    i = 2
    while i < n: 
        a.append(i) 
        i = i + 2
          
    return (a[k - 1]) 
  
