

def calculate_rating(ratings):
    return sum(ratings)/float(len(ratings))


def get_better_movie(ratings1, ratings2):
    overall_rating1 = calculate_rating(ratings1)
    overall_rating2 = calculate_rating(ratings2)
    if (overall_rating1 > overall_rating2):
        return 'First Movie'
    elif (overall_rating2 > overall_rating1):
        return 'Second Movie'
    else:
        'Both Movies are equal'

