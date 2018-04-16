#Standard library
#Current directory
#Lib/site-packages (modules tiers)

"""
0 Brésil : 1635 points
1 Argentine : 1529 points
2 Allemagne : 1433 points
3 Chili : 1386 points
4 Belgique : 1371 points
"""
def print_rank():
    """print a rank by using two separate lists"""
    equipes = ['Brésil', 'Argentine', 'Allemagne', 'Chili', 'Belgique'] # equipes defined as list
    scores = [1635, 1529, 1433, 1386, 1371] # scores defined as list
    # browse the two lists together
    # enumerate allows to retrieve a list of tuples (index, value) => https://openclassrooms.com/courses/pratiques-avancees-et-meconnues-en-python
    # zip allows to iterate on n lists / returns a list of tuples => https://openclassrooms.com/courses/pratiques-avancees-et-meconnues-en-python
    for r, (e,s) in enumerate(zip(equipes, scores)):
        print(r,e, ':',s, 'points')


def print_rank_poor_solution_with_range():
    equipes = ['Brésil', 'Argentine', 'Allemagne', 'Chili', 'Belgique']
    scores = [1635, 1529, 1433, 1386, 1371]
    for r,e,s in zip(range(1,len(equipes)+1),equipes, scores):
        print(r,e, ':',s, 'points')
