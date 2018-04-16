#Declare s as set (mutable/reference) and print the values
def on_set():
    """Declare s as set (mutable/reference) and print the values \
    set ne peut pas contenir de type mutable comme les list
    """
    #s = set()
    s = {'pomme', 'pomme', 'banane', 2}
    s.add('abricot')
    sbis = {'pomme', 'framboise', 2}
    #s & sbis
    #s | sbis
    print(s)