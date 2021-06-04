import sys

""" Part 1 - This functions build the title-actors dictionary. 
The keys are movie titles, and the values are the cast lists of each movie."""

def make_title_dict():    
    titleActorDict = {} # create an empty dict (movie title -> key, list of actor(s) )    
    fHandle = open ("imdb.txt", "r") # open file for reading
    lines = fHandle.readlines() # list of lines from the input file 
        
    # add your code below
    for i in range(0, len(lines), 2):
        movies = lines[i].strip()
        actors = lines[i+1].strip()
        if movies not in titleActorDict:
          titleActorDict[movies] = actors
        elif type(titleActorDict[movies])== list:
          titleActorDict[movies].append(actors)
        else:
          titleActorDict[movies] = [titleActorDict[movies], actors]
    fHandle.close() 
    return titleActorDict
#---------------------------------------------------------------------------------------------------------
""" Part 2 - This function builds the actor-titles dictionary. The keys are actors,
and the values are lists of movies in which the actors appeared. """
def make_actor_dict():
  actorTitleDict = {} # create an empty dict   
   # add your code here   
  fHandle = open ("imdb.txt", "r") #open file for reading
  lines = fHandle.readlines()
  for i in range(0, len(lines), 2):#every other line
        movies = lines[i].strip()
        actors = lines[i+1].strip()
        if actors not in actorTitleDict:
          actorTitleDict[actors] = movies
        elif type(actorTitleDict[actors])== list:
          actorTitleDict[actors].append(movies)
        else:
          actorTitleDict[actors] = [actorTitleDict[actors], movies]
  fHandle.close()
  return actorTitleDict

# Part 1 - Build the movie title -> actors dictionary   
titleActorDict = make_title_dict()
print ('(Part 1) Using the titleActor dictionary to answer questions.\n')

print ('\t(A)What is the length of the longest cast list?')
maxLenFilm = ""
maxLen = sys.maxsize * -1
for film in titleActorDict.keys() : # loop through each key (film) in the dict 
    if len(titleActorDict[film]) > maxLen: # look-up key/film in dict and check length of cast 
        maxLen = len(titleActorDict[film])
        maxLenFilm = film 
print ("\t\t", maxLenFilm , " has longest cast list of ", maxLen, '\n') 

print ('\t(B)How many films are in the dictionary?')
print("\t\t",len(titleActorDict), '\n')#using the len counts the keys in the dict


print ('\t(C)What is the length of the shortest cast list?')
minLenFilm = ""
minLen = maxLen
for film in titleActorDict.keys() : # loop through each key (film) in the dict 
    if len(titleActorDict[film]) < minLen: # look-up key/film in dict and check length of cast 
        minLen = len(titleActorDict[film])
        minLenFilm = film
print("\t\t", minLenFilm, "has the shortest cast list of", minLen, '\n')


print ('\t(D)Did "Tom Hanks" appear in "Catch Me If You Can"?')
if "Tom Hanks" in titleActorDict["Catch Me If You Can"]:#checks if the key has value tom hanks in it
  print("\t\tyes\n")
else:
  print("\t\tno\n")


print ('\t(E)Ask user to enterDid "Tom Hanks" appear in "Catch Me If You Can"? \n')
#GREETINGS COMRADES idk what he wants us to do here, maybe check if user input exists as a value for key object catch me if you can?


print ('\t(F)List all the movies in which "Owen Wilson" appears.')
for film in titleActorDict.keys() :
  if "Owen Wilson" in titleActorDict[film]: #checks for keys that contain the value "Owen Wilson"
    print("\t\t",film)
print()

print ('\t(G)List all the actors who appeared in both "Silver Linings Playbook" and "American Hustle"')
for actors in titleActorDict["Silver Linings Playbook"]:
  if actors in titleActorDict["Silver Linings Playbook"] and actors in titleActorDict["American Hustle"]:
    print("\t\t",actors)
print()
       
# Part 2 - build the actor -> movie titles  dictionary 
print ('*'*50)
actorTitleDict = make_actor_dict( )
print ('(Part 2) Use the --actorTitleDict-- dictionary to answer questions.\n')


print ('\t(A) List (again) all the movies in which Owen Wilson appears.')
list_of_movies = list(actorTitleDict["Owen Wilson"])#converts the Owen Wilson key into a list
i=0
while i< len(list_of_movies):
  print("\t\t",list_of_movies[i])#prints what used to be each value in the Owen Wilson key
  i+=1
print()

print ('\t(B) How many actors are in the dictionary ?')
print("\t\t",len(actorTitleDict), '\n')

print ('\t(C) Which actor (or actors) has been in the largest number of films in the database?')
maxLenFilm = ""
maxLen = sys.maxsize * -1
for actors in actorTitleDict.keys() : # loop through each key
    if len(actorTitleDict[actors]) > maxLen: # look-up key
        maxLen = len(actorTitleDict[actors])
        maxLenFilm = actors
print ("\t\t", maxLenFilm , " has performed in the most films, starring in ", maxLen," movies.")
print()

print ('\t(E) Did "Tom Hanks" appear in "Catch Me If You Can"?')
if "Catch Me If You Can" in actorTitleDict["Tom Hanks"]:#checks if the key has value catch me if you can
  print("\t\t yes \n")
else:
  print("\t\t no \n")

print ('\t(F) What are all the films in which both Clint Eastwood and Morgan Freeman appeared?')
for films in actorTitleDict["Clint Eastwood"]:
  if films in actorTitleDict["Morgan Freeman"] and films in actorTitleDict["Clint Eastwood"]:
    print("\t\t",films)