#
# main.py
#
# Interface tier used for outputting to console the result of our queries.
# This is where the program asks user what they would like to see and outputs
# it to them.
#
# Course: CS 341 Spring 2023
# Author: Ali Abuzir
# System: macOS using Replit
#
######################################################################################
import objecttier
import sqlite3

# Function that output movie id, movie title, movie release year given the movie name.
def movIDTitleAndYear(dbConn, movieName):
  # Calls the objecttier function get_movies to return a list of objects of class Movie which contains the movie id, title and release year.
  movieObjList = objecttier.get_movies(dbConn, movieName)

  # Prints number of movies found in the query.
  print("\n# of movies found:", f"{len(movieObjList)}\n")

  # Does not display if there are more than 100 movies to display.
  if len(movieObjList) > 100:
    print("There are too many movies to display, please narrow your search and try again...")

  else:
    # Loops through the list of Movie objects to print out each objects values.
    for row in movieObjList:
      # Prints to console the movie id, title, and release year.
      print(row.Movie_ID, ":", row.Title, f"({row.Release_Year})")

# End movIDTitleAndYear(dbConn, movieName).
######################################################################################

# Function that outputs the details about a movie for passed in movie_id.
def movieDetails(dbConn, movie_id):
  # Calls the objecttier function get_movie_details to return an object of class MovieDetails that contains the details about a movie given the movie's movie_id.
  details = objecttier.get_movie_details(dbConn, movie_id)
  
  # If data was received from the get_movie_details function and no error resulted from the call.
  if details != None and details != ():
    # Printing out the details of the movie.
    print(details.Movie_ID, ":", details.Title)
    print("  Release Date:", details.Release_Date)
    print("  Runtime:", details.Runtime, "(mins)")
    print("  Orig Language:", details.Original_Language)
    print("  Budget:", f"${details.Budget:,}", "(USD)")
    print("  Revenue:", f"${details.Revenue:,}", "(USD)")
    print("  Num reviews:", details.Num_Reviews)
    print("  Avg Rating:", f"{details.Avg_Rating:.2f}", "(0..10)")
    
    print("  Genres: ", end = "")
    # Looping through the details.Genres list.
    for genre in details.Genres:
      print(f"{genre}, ", end = "")
    print()

    print("  Production companies: ", end = "")
    # Looping through the details.Production_Companies list.
    for company in details.Production_Companies:
      print(f"{company}, ", end = "")
    print()
    
    print("  Tagline:", details.Tagline)

  # If no data was received from the call to get_movie_details, or an error resulted from the call.
  else:
    print("No such movie...")

# End movieDetails(dbConn, movie_id).
######################################################################################

# Function that returns the top N movies with numReviews reviews where N and numReviews are passed into the function.
def topNMovies(dbConn, N, numReviews):
  # Calls the objecttier function get_top_N_movies to get the top N movies with numReviews reviews.
  topMovies = objecttier.get_top_N_movies(dbConn, N, numReviews)

  # If get_top_N_movies did not encounter an error in the data retrieval process and actually received data.
  if topMovies != None:
    # Loops through the list of MovieRating objects that was returned and prints all of their details out.
    for movie in topMovies:
      print(movie.Movie_ID, ":", movie.Title, f"({movie.Release_Year}),", "avg rating =", f"{movie.Avg_Rating:.2f}", f"({movie.Num_Reviews} reviews)")

# End topNMovies(dbConn, N, numReviews).
######################################################################################
# Function that inserts a review for a movie. Given is the movie_id and rating.
def insertReview(dbConn, movie_id, rating):
  # Calls the objecttier function add_review to add the review rating for movie id movie_id.
  insertion = objecttier.add_review(dbConn, movie_id, rating)

  # If insertion is 1, that means we successfully added the movie.
  if insertion == 1:
    print("Review successfully inserted")

  # Else, the movie_id does not exist in the database or the insertion failed.
  else:
    print("No such movie...")

# End insertReview(dbConn, movie_id, rating).
######################################################################################

# Function that takes in a given movie_id and tagline and sets that movie's tagline in the database.
def setTagline(dbConn, movie_id, tagline):
  # Calls the objecttier function set_tagline which adds a tagline to the database for a movie or updates a tagline for a movie if a tagline for the movie already exists in the database.
  setTag = objecttier.set_tagline(dbConn, movie_id, tagline)

  # If the tagline was successfully set for the given movie id.
  if setTag == 1:
    print("Tagline successfully set")

  # Else an error has occurred when attempting to set the given tagline or movie_id does not exist in the database.
  else:
    print("No such movie...")

# End setTagline(dbConn, movie_id, tagline).
######################################################################################

# main
# Prompts users for commands and executes each command with the commands attached function.
def main():
  # Establish connection with database.
  dbConn = sqlite3.connect("MovieLens.db")
  
  print("** Welcome to the MovieLens app **\n")

  # Output number of movies and reviews in database.
  print("General stats:")
  print("  # of movies:", f"{objecttier.num_movies(dbConn):,}")
  print("  # of reviews:", f"{objecttier.num_reviews(dbConn):,}")
  print()

  # Prompt for user to enter command number
  inputChar = input("Please enter a command (1-5, x to exit): ")
  print()

  # Loops through program until user would like to stop by inputting x.
  while (inputChar != 'x'):

    # Gets movie id, title, and year for an existing movie.
    if (inputChar == '1'):
      movieName = input("Enter movie name (wildcards _ and % supported): ")
      movIDTitleAndYear(dbConn, movieName)

    # Gets movie details for an existing movie.
    elif (inputChar == '2'):
      movie_id = int(input("Enter movie id: "))
      print()
      movieDetails(dbConn, movie_id)

    # Gets top n movies with desired number of reviews.
    elif (inputChar == '3'):
      # Input for N.
      N = int(input("N? "))

      # If invalid(-) N given.
      if (N <= 0):
        print("Please enter a positive value for N...")
      # Else a positive was entered for N.
      else:
        # Input for minimum number of reviews.
        numReviews = int(input("min number of reviews? "))

        # If invalid(-) number of minimum reviews given.
        if (numReviews <= 0):
          print("Please enter a positive value for min number of reviews...")
          print()
        # If both N and numReviews are valid for query.
        else:
          print()
          topNMovies(dbConn, N, numReviews)

    # Inserts a review into the database for an existing movie.
    elif (inputChar == '4'):
      rating = int(input("Enter rating (0..10): "))

      # If invalid rating given.
      if (rating < 0 or rating > 10):
        print("Invalid rating...")

      # Rating given is in range 0-10.
      else:
        movie_id = int(input("Enter movie id: "))
        
        print()
        insertReview(dbConn, movie_id, rating)
        print()

    # Sets the tagline for a given existing movie_id.
    elif (inputChar == '5'):
      tagline = input("tagline? ")
      movie_id = int(input("movie id? "))
      print()
      setTagline(dbConn, movie_id, tagline)
      print()

    # If all above cases fail, we pass and move onto the next user input.
    else:
      pass

    # Next user input command.
    print()
    inputChar = input("Please enter a command (1-5, x to exit): ")
    print()

# End main().
######################################################################################

# Call to main().
# Program begins here.
if __name__ == "__main__":
  main()

######################################################################################