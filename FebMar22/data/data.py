"""
Cohort Project = Movies
User = Table
Movies =    title = text
            genre = text
            actors = select/option
            year = number
            user_id = (person adding movie to database) number
movies = [ => square bracket tell us this is a list
    { => curly bracket tells us that this is going to be 1 row / or 1 instance / or 1 movie in our list and it is a dictionary
        'title': '',
        'genre': '',
        'year': <>,
        'user_id': <> 
    }
]
actors = [
    {
        'firstName': '',
        'lastName': ''
        'movie_id': <>
    }
]
"""
# this is what our data could be return as
movies = [
    {
        'id': 1,
        'title': "Back to the Future",
        'year': 1984,
        'actors': [
            {'firstName': "Michael J", 'lastName': "Fox"},
            {"firstName": "Christopher", 'lastName': "Lloyd"}
        ],
        'genre': "Syfy Drama"
    },
    {
        'id': 2,
        "title": 'Rambo 1st blood',
        'year': 1982,
        'actors': [
            {'firstName': "Sylvester", "lastName": "Stallone"},
            {'firstName': "David", 'lastName': "Caruso"},
            {'firstName': 'Brian', 'lastName': 'Denning'}
        ],
        'genre': 'Action'
    },
    {
        'id': 3,
        'title': 'Teen Wolf',
        'year': 1985,
        'actors': [
            {'firstName': "Michael J", 'lastName': "Fox"},
            {'firstName': "Susan", 'lastName': "Ursitti"}
        ],
        'genre': "Syfy Drama"
    },
    {
        'id': 4,
        'title': "Back to the Future II",
        'year': 1986,
        'actors': [
            {'firstName': "Michael J", 'lastName': "Fox"},
            {"firstName": "Christopher", 'lastName': "Lloyd"}
        ],
        'genre': "Syfy Drama"
    },
    {
        'id': 5,
        'title': "Back to the Future III",
        'year': 1987,
        'actors': [
            {'firstName': "Michael J", 'lastName': "Fox"},
            {"firstName": "Christopher", 'lastName': "Lloyd"}
        ],
        'genre': "Syfy Drama"
    }
]
# check to see if a movie in the list has Christopher Lloyd as an actor listed
"""
Step 1: Loop through all the movies
Step 2: Check each movie to see if it has Christopher Lloyd listed as one of it's actors
Step 3: If yes add movie to a list
Step 4: Print back the list of movies
"""
def checkActors(l, n): # pass in the list of movies and the name we want to check against. 
    myList = [] # Creating an empty list to stor the True results
    for m in l: # Looping through the entire list of movies => Should always the bigger list that contains the smaller list
        for a in m['actors']: # Looping through each movies list of actors
            if a['firstName'] == n: # checking to see if the first name matches 
                myList.append(m['title']) # adding the movie title to our empty list => m can still be called because this loop in inside the bigger one
    print("the final list: ", myList) # printing back the final results

# checkActors(movies, 'Michael J')

# print("one instance of a movie: ", movies[2])