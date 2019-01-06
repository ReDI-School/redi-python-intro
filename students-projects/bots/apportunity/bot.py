
import sys


def parse_csv_file(filename):
    """
    Read the contents of a .csv file and put them into a useful data structure:

    ddict = {
        "category1": { "location1": [entry1, entry2], "location2": [entry3] },
        "category2": { "location1": []}
    }

    Parameters
    ----------
    filename : string
        The path to the .csv file to read.

    Returns
    -------
    dict
        A dictionary containing all the apportunities.
    """
    import csv  # import a library

    ddict = {}  # make an empty dictionary

    with open(filename) as f:  # with open(...) takes care of closing after the block

        csv_reader = csv.reader(f, delimiter=',')

        # for each index and row, do the following
        for i, row in enumerate(csv_reader):

            # skip the first line because it contains the header/column names
            if i == 0:
                continue

            # assign the elements of each row to variables
            title, location, _, category, details, link = row

            # if category is not a key in ddict, add category as a key to ddict
            if not category in ddict:
                ddict[category] = {}

            # if location is not a secondary key in ddict, add location as a secondary key to ddict
            if not location in ddict[category].keys():
                ddict[category][location] = []

            # add title, link, and details as a list to this category and location
            ddict[category][location].append([title, link, details])

    return ddict


if __name__ == "__main__":

    filename = sys.argv[1]

    # read file from disk and parse it into useful data structures
    # 1. get the different (unique) options in the column "category"
    # 2. get the different (unique) options in "location" (for a particular category)
    # 3. for a given category and location, what are the opportunities
    apportunities = parse_csv_file(filename)

    # GREETING AND INTRODUCTION
    print("Hallo, I'm Apportunity Bot. What's your name?")
    user_input = input()

    # check for keywords "is " and "am " to find name, else use whole string as name
    if "is " in user_input:
        idx = user_input.index("is ")
        user_name = user_input[idx+3:]
    elif "am " in user_input:
        idx = user_input.index("am ")
        user_name = user_input[idx+3:]
    elif "'m " in user_input:
        idx = user_input.index("'m ")
        user_name = user_input[idx+3:]
    elif "'s " in user_input:
        idx = user_input.index("'s ")
        user_name = user_input[idx+3:]
    else:
        user_name = user_input

    # CATEGORY
    # present the different categories
    categories = list(apportunities.keys())
    printable_categories = ", ".join(categories[:-1]) + " or " + categories[-1]
    # TODO: include some description of what this program is about
    print("Hi {}! Choose one of the following categories you would like to know about: {}.".format(user_name, printable_categories))
    # get the user's reply and filter it for the desired category
    user_categories = []
    while len(user_categories) != 1:
        user_input = input()
        user_categories = []
        for category in categories:
            if category.lower() in user_input.lower():
                user_categories.append(category)
        if len(user_categories) > 1:
            print("Please choose one at a time!")
        elif len(user_categories) == 0:
            print("Your choice doesn't match. Pick one of {}.".format(printable_categories))
    category = user_categories[0]

    # LOCATION
    locations = list(apportunities[category].keys())
    if len(locations) == 1:
        print("We have {}s in the following location: {}. Are you interested in learning more about it?".format(category, locations[0]))
        user_input = input()
        if user_input.lower() in ["yes", "yea", "yeah", "okay", "ok", "o.k.", "yup", "yep"]:
            # go to DETAILS
            location = locations[0]
            print("Here is more detailed information:")
            print()
            for entry in apportunities[category][location]:
                title, link, details = entry
                print(title)
                print()
                # print(link)
                print(details)
            print
        else:
            # if No, TODO:
            pass
    else:
        printable_locations = ", ".join(locations[:-1]) + " and " + locations[-1]
        print("We have {}s in the following locations: {}. Which location are you interested in?".format(category, locator, printable_locations))
        user_locations = []
        while len(user_locations) != 1:
            user_input = input()
            user_locations = []
            for location in locations:
                if location.lower() in user_input.lower():
                    user_locations.append(location)
            if len(user_locations) > 1:
                print("Please choose one at a time!")
            elif len(user_locations) == 0:
                printable_locations = printable_locations.replace("and", "or")
                print("Your choice doesn't match. Pick one of {}.".format(printable_locations))
        location = user_locations[0]

    # # DETAILS
    # # link or no link
    # # if no link, then more or goodbye
    # # if more, go to category
    # # if goodbye, then goodbye