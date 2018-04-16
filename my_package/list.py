def on_list():
    """Declare l as list (mutable/reference) and print the values"""
    #l = list()
    l = ['1', '2', '3']
    lbis = l[:] #clone with slice
    lbis.reverse()
    print("La valeur de l est ", l)
    print("La taille de l est ", len(l))
    print("La valeur de lbis est ", lbis)
    #Add slice
    #Add range
    #Add comprehension ([x for x in range(5)]
    #Add matrix (matrix = [[1,2],[2,3]
