# File: objecttier.py
#
# objecttier
#
# Builds Movie-related objects from data retrieved through 
# the data tier.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#   Project #02
#
import datatier


##################################################################
#
# Movie:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#
class Movie:
  # Constructor creating "private" variables with passed in values
  def __init__(self, Movie_ID, Title, Release_Year):
    self._Movie_ID = Movie_ID
    self._Title = Title
    self._Release_Year = Release_Year

  # Property used to have user read _Movie_ID without being able to change it.
  @property
  def Movie_ID(self):
    return self._Movie_ID

  # Property used to have user read _Title without being able to change it.
  @property
  def Title(self):
    return self._Title

  # Property used to have user read _Release_Year without being able to change it.
  @property
  def Release_Year(self):
    return self._Release_Year

# End class Movie.
##################################################################
#
# MovieRating:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#   Num_Reviews: int
#   Avg_Rating: float
#
class MovieRating:
  # Constructor creating "private" variables with passed in values
  def __init__(self, Movie_ID, Title, Release_Year, Num_Reviews, Avg_Rating):
    self._Movie_ID = Movie_ID
    self._Title = Title
    self._Release_Year = Release_Year
    self._Num_Reviews = Num_Reviews
    self._Avg_Rating = Avg_Rating

  # Property used to have user read _Movie_ID without being able to change it.
  @property
  def Movie_ID(self):
    return self._Movie_ID

  # Property used to have user read _Title without being able to change it.
  @property
  def Title(self):
    return self._Title

  # Property used to have user read _Release_Year without being able to change it.
  @property
  def Release_Year(self):
    return self._Release_Year

  # Property used to have user read _Num_Reviews without being able to change it.
  @property
  def Num_Reviews(self):
    return self._Num_Reviews

  # Property used to have user read _Avg_Rating without being able to change it.
  @property
  def Avg_Rating(self):
    return self._Avg_Rating

# End class MovieRating.
##################################################################
#
# MovieDetails:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Date: string, date only (no time)
#   Runtime: int (minutes)
#   Original_Language: string
#   Budget: int (USD)
#   Revenue: int (USD)
#   Num_Reviews: int
#   Avg_Rating: float
#   Tagline: string
#   Genres: list of string
#   Production_Companies: list of string
#
class MovieDetails:
  # Constructor creating "private" variables with passed in values
  def __init__(self, Movie_ID, Title, Release_Date, Runtime, Original_Language, Budget, Revenue, Num_Reviews, Avg_Rating, Tagline, Genres, Production_Companies):
    self._Movie_ID = Movie_ID
    self._Title = Title
    self._Release_Date = Release_Date
    self._Runtime = Runtime
    self._Original_Language = Original_Language
    self._Budget = Budget
    self._Revenue = Revenue
    self._Num_Reviews = Num_Reviews
    self._Avg_Rating = Avg_Rating
    self._Tagline = Tagline
    self._Genres = Genres
    self._Production_Companies = Production_Companies

  # Property used to have user read _Movie_ID without being able to change it.
  @property
  def Movie_ID(self):
    return self._Movie_ID

  # Property used to have user read _Title without being able to change it.
  @property
  def Title(self):
    return self._Title

  # Property used to have user read _Release_Date without being able to change it.
  @property
  def Release_Date(self):
    return self._Release_Date

  # Property used to have user read _Runtime without being able to change it.
  @property
  def Runtime(self):
    return self._Runtime

  # Property used to have user read _Original without being able to change it.
  @property
  def Original_Language(self):
    return self._Original_Language

  # Property used to have user read _Budget without being able to change it.
  @property
  def Budget(self):
    return self._Budget

  # Property used to have user read _Revenue without being able to change it.
  @property
  def Revenue(self):
    return self._Revenue

  # Property used to have user read _Num_Reviews without being able to change it.
  @property
  def Num_Reviews(self):
    return self._Num_Reviews

  # Property used to have user read _Avg_Rating without being able to change it.
  @property
  def Avg_Rating(self):
    return self._Avg_Rating

  # Property used to have user read _Tagline without being able to change it.
  @property
  def Tagline(self):
    return self._Tagline

  # Property used to have user read _Genres without being able to change it.
  @property
  def Genres(self):
    return self._Genres

  # Property used to have user read _Production_Companies without being able to change it.
  @property
  def Production_Companies(self):
    return self._Production_Companies

# End class MovieDetails.
##################################################################
# 
# num_movies:
#
# Returns: # of movies in the database; if an error returns -1
#
def num_movies(dbConn):
  # SQL query to retreive the number of movies from the MovieLens database.
  sql = """SELECT count(Movie_ID)
           FROM Movies"""

  # Calls datatier function select_one_row which goes to the database and pulls the first row of the results that come back from the cursor which executed the SQL command.
  row = datatier.select_one_row(dbConn, sql)

  # If the select_one_row function returned None, this means that there was an error in retriving our row from the database.
  if (row == None):
    return -1
  # If retrieval of data from database went through sucessfully, we return the first and only member of the tuple returned from select_one_row which contains the number of movies in the database.
  else:
    return row[0]

# End num_movies(dbConn).
##################################################################
# 
# num_reviews:
#
# Returns: # of reviews in the database; if an error returns -1
#
def num_reviews(dbConn):
   # SQL query to retreive the number of ratings from the MovieLens database.
  sql = """SELECT count(Rating)
           FROM Ratings"""

  # Calls datatier function select_one_row which goes to the database and pulls the first row of the results that come back from the cursor which executed the SQL command.
  row = datatier.select_one_row(dbConn, sql)

  # If the select_one_row function returned None, this means that there was an error in retriving our row from the database.
  if (row == None):
    return -1
  # If retrieval of data from database went through sucessfully, we return the first and only member of the tuple returned from select_one_row which contains the number of movies in the database.
  else:
    return row[0]

# End num_reviews(dbConn).
##################################################################
#
# get_movies:
#
# gets and returns all movies whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of movies in ascending order by movie id; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_movies(dbConn, pattern):
  # SQL query to grab movie id, title, and release year from each year in the database ordered in ascending order.
  sql = """SELECT Movie_ID, Title, strftime('%Y', Release_Date)
           FROM Movies
           WHERE Title LIKE ?
           ORDER BY Movie_ID ASC"""

  # Calls datatier function select_n_rows to execute the query and grab its results.
  rows = datatier.select_n_rows(dbConn, sql, [pattern])

  # Holds a list of class Movie objects each containing movie id, title, and release year.
  listOfMovies = []

  # If SQL query was successfully pulled from datanbase without error (!= None).
  if rows != None:
    # Iterates through the returned list of tuples.
    for row in rows:
      # Creates a new Movie object passing in movie id, title, and year in that order and appends that object into listOfMovies.
      currMovie = Movie(row[0], row[1], row[2])
      listOfMovies.append(currMovie)

  # Returns the list of Movie objects.
  return listOfMovies

# End get_movies(dbConn, pattern).
##################################################################
#
# get_movie_details:
#
# gets and returns details about the given movie; you pass
# the movie id, function returns a MovieDetails object. Returns
# None if no movie was found with this id.
#
# Returns: if the search was successful, a MovieDetails obj
#          is returned. If the search did not find a matching
#          movie, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_movie_details(dbConn, movie_id):
  # SQL query to check if the movie_id passed in exits in database.
  movieIDCheck = """SELECT count(Movie_ID)
                    FROM Movies
                    WHERE Movie_ID = ?"""

  # Calls the datatier function select_one_row to check if movie_id exists in the database
  movieCheck = datatier.select_one_row(dbConn, movieIDCheck, [movie_id])

  # If movie_id does not exist in the database or movieCheck returned an error.
  if movieCheck == None or movieCheck[0] == 0:
    return None
  
  # SQL query that joins tables Movies, Movie_Taglines, and Ratings together to gather all movie details except genres and production company names associated with movie_id.
  sql = """SELECT Title, date(Release_Date), Runtime, Original_Language, Budget, Revenue, count(Ratings.Rating), avg(Ratings.Rating), Tagline
           FROM Movies
           LEFT JOIN Movie_Taglines
           ON Movies.Movie_ID = Movie_Taglines.Movie_ID
           LEFT JOIN Ratings
           ON Movies.Movie_ID = Ratings.Movie_ID
           WHERE Movies.Movie_ID = ?"""

  # SQL query to grab all movie id's genres.
  genres = """SELECT Genres.Genre_Name
              FROM Movies
              LEFT JOIN Movie_Genres
              ON Movies.Movie_ID = Movie_Genres.Movie_ID
              LEFT JOIN Genres
              ON Movie_Genres.Genre_ID = Genres.Genre_ID 
              WHERE Movies.Movie_ID = ?
              ORDER BY Genres.Genre_Name ASC"""

  # SQL query to grab all movie id's production company names.
  companies = """SELECT Companies.Company_Name
                 FROM Movies
                 LEFT JOIN Movie_Production_Companies
                 ON Movies.Movie_ID = Movie_Production_Companies.Movie_ID
                 LEFT JOIN Companies
                 ON Movie_Production_Companies.Company_ID = Companies.Company_ID
                 WHERE Movies.Movie_ID = ?
                 ORDER BY Companies.Company_Name ASC"""

  # Calls the datatier function select_one_row to grab the resulting one row with all the details about the movie with the movie id provided.
  row = datatier.select_one_row(dbConn, sql, [movie_id])
  
  # genreRows and companyRows calls the datatier function select_n_rows to grab the corresponding genres and production companies associated with movie_id from the database.
  genreRows = datatier.select_n_rows(dbConn, genres, [movie_id])
  companyRows = datatier.select_n_rows(dbConn, companies, [movie_id])

  # If no error occurred from getting the data from the database for our query and we actually received data from our query.
  if row != None and row != ():
    # Two lists created to hold the results of all the genres and production companies associated with movie_id.
    listOfGenres = []
    listOfCompanies = []

    # Appends to listOfGenres list only if data has been receieved from the genreRows query request and returned no error.
    if genreRows != None and genreRows[0][0] != None:
      for genreRow in genreRows:
        listOfGenres.append(genreRow[0])

    # Appends to listOfCompanies list only if data has been receieved from the companyRows query request and returned no error.
    if companyRows != None and companyRows[0][0] != None:
      for companyRow in companyRows:
        listOfCompanies.append(companyRow[0])

    # Grabs the value returned from query sql for movie tagline.
    tagline = row[8]

    # Changes tagline to have the value of empty string if its value is None for display purposes.
    if (tagline == None):
      tagline = ""

    # Grabs the value returned from query sql for average ratings.
    average = row[7]

    # Changes average to have the value of 0.00 if its value is None for display purposes.
    if (average == None):
      average = 0.00
        
    # Returns a MovieDetails object full of information requested by the movie for the movie details including the genre and companies lists.
    return MovieDetails(movie_id, row[0], row[1], row[2], row[3], row[4], row[5], row[6], average, tagline, listOfGenres, listOfCompanies)
 
    # If an error did occur or we just received no data we return None for query sql.
  else:
    return None
      
# End get_movie_details(dbConn, movie_id).
##################################################################
#
# get_top_N_movies:
#
# gets and returns the top N movies based on their average 
# rating, where each movie has at least the specified # of
# reviews. Example: pass (10, 100) to get the top 10 movies
# with at least 100 reviews.
#
# Returns: returns a list of 0 or more MovieRating objects;
#          the list could be empty if the min # of reviews
#          is too high. An empty list is also returned if
#          an internal error occurs (in which case an error 
#          msg is already output).
#
def get_top_N_movies(dbConn, N, min_num_reviews):
  # SQL query that grabs the top N movies based on average ratings of the movie with at least min_num_reviews reviews.
  sql = """SELECT Movies.Movie_ID, Title, strftime('%Y', Release_Date), count(Ratings.Rating) as numRatings, avg(Ratings.Rating) as avgRating
           FROM Movies
           JOIN Ratings
           ON Movies.Movie_ID = Ratings.Movie_ID
           GROUP BY Movies.Movie_ID
           HAVING numRatings >= ?
           ORDER BY avgRating DESC, Movies.Title ASC
           LIMIT ?"""

  # Attempts to retreive that SQL query information from the database.
  rows = datatier.select_n_rows(dbConn, sql, [min_num_reviews, N])

  # List created to append the top N movies based on average rating with at least min_num_reviews for return
  # This list contains class MovieRating objects as its elements.
  listNMovieRatings = []

  # If the retreival of the data in the database did not have any errors and we actually received data.
  if rows != None:
    # Iterates through the returned list of tuples and creates an object of MovieRating for each tuple and passes those values into the MovieRating constructor for each tuple, then proceeds to appending the object to the list of MovieRating objects for return.
    for row in rows:
      currMovie = MovieRating(row[0], row[1], row[2], row[3], row[4])
      listNMovieRatings.append(currMovie)

  # Returns the list of MovieRating objects.
  return listNMovieRatings

# End get_top_N_movies(dbConn, N, min_num_reviews).
##################################################################
#
# add_review:
#
# Inserts the given review --- a rating value 0..10 --- into
# the database for the given movie. It is considered an error
# if the movie does not exist (see below), and the review is
# not inserted.
#
# Returns: 1 if the review was successfully added, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def add_review(dbConn, movie_id, rating):
  # SQL query to check if the movie_id passed in exits in database.
  movieIDCheck = """SELECT count(Movie_ID)
                    FROM Movies
                    WHERE Movie_ID = ?"""

  # Executes the movieIDCheck query.
  row = datatier.select_one_row(dbConn, movieIDCheck, [movie_id])

  # If the movieIDCheck query execution did not result in an error, and returned data from the database in which we found the movie id.
  if row != None and row != () and row[0] != 0:
    # SQL query to insert a new row into the Ratings table.
    sql = """INSERT INTO Ratings(Movie_ID, Rating)
           Values(?, ?)"""

    # Calls the datatier function perform_action which executes our query to add a row into our Ratings table with the given values.
    rowsModified = datatier.perform_action(dbConn, sql, [movie_id, rating])

    # If our query did not return an error, we return 1 to indicate a success in adding our row into the Ratings table.
    if rowsModified != -1:
      return 1
    # Else, our query failed to insert our row of given values into the Ratings table so we return 0 to indicate an error for insertion into our Ratings table.
    else:
      return 0

  # Else if Movie_ID check failed to execute or we returned no data from the database, we return 0 to indicate an error for insertion into our Ratings table.
  else:
    return 0

# End add_review(dbConn, movie_id, rating).
##################################################################
#
# set_tagline:
#
# Sets the tagline --- summary --- for the given movie. If
# the movie already has a tagline, it will be replaced by
# this new value. Passing a tagline of "" effectively 
# deletes the existing tagline. It is considered an error
# if the movie does not exist (see below), and the tagline
# is not set.
#
# Returns: 1 if the tagline was successfully set, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def set_tagline(dbConn, movie_id, tagline):
   # SQL query to check if the movie_id passed in exists in database and checks if there is an existing tagline for that movie_id. If we have the first count return 0, then movie_id is not in the database, if we have a 0 in the second count but non zero in the first count, then the movie exists but doesn't have a tagline, if they are both nonzero, then we update the tagline for that movie as one exists. These conditions are allowed to be checked because of that left join and how it works.
  movieCheck = """SELECT count(Movies.Movie_ID), count(Movie_Taglines.Movie_ID)
                  FROM Movies
                  LEFT JOIN Movie_Taglines
                  ON Movies.Movie_ID = Movie_Taglines.Movie_ID
                  WHERE Movies.Movie_ID = ?"""

  # Executes the movieIDCheck query.
  movieCheckRow = datatier.select_one_row(dbConn, movieCheck, [movie_id])

  # If the movieIDCheck query execution did not result in an error, and returned data from the database in which we found the movie in the database.
  if movieCheckRow != None and movieCheckRow != () and movieCheckRow[0] != 0:
    # At this point, if our Movie_Taglines does not contain the Movie_ID, we insert the tagline as the movie does exist after the previous checks.
    if (movieCheckRow[1] == 0):
      # SQL query to insert values into the Movie_Taglines table.
      sqlInsert = """INSERT INTO Movie_Taglines(Movie_ID, Tagline)
                     Values(?, ?)"""

      # Calls the datatier function to insert values into Movie_Taglines table.
      rowsModified = datatier.perform_action(dbConn, sqlInsert, [movie_id, tagline])

      # If there was no error in inserting the values into our table.
      if (rowsModified != -1):
        return 1
      # If an error occurred when attempting to insert data into the Movie_Taglines table.
      else:
        return 0

    # Else, meaning that our Movie_Taglines table did contain movie_id, we want to update that tagline.
    else:
      # SQL query to update the Tagline column for the columns that contain movie_id, which should be 1 in this case as Movie_ID is the primary key.
      sqlUpdate = """UPDATE Movie_Taglines
                     Set Tagline = ?
                     WHERE Movie_ID = ?"""

      # Calls the datatier function to update the column Tagline for the movie id given.
      rowsModified = datatier.perform_action(dbConn, sqlUpdate, [tagline, movie_id])

      # If there was no error in updating the values into our table.
      if rowsModified != -1:
        return 1
      # If an error occurred when attempting to update data into the Movie_Taglines table.
      else:
        return 0

  # Else, if when we checked our table for the movie_id, we encountered an error, or no data was returned.
  else:
    return 0

# End set_tagline(dbConn, movie_id, tagline).