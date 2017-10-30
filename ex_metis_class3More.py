import pandas as pd
import numpy as np

movieData = pd.read_csv("C:\Users\Jason\Desktop\ml-1m\ml-1m\movies.dat", sep = "::", names = ["MovieID","Title","Genres"])
userData = pd.read_csv("C:\Users\Jason\Desktop\ml-1m\ml-1m\users.dat", sep = "::", names = ["UserID","Gender","Age","Occupation","Zip-code"])
ratingData = pd.read_csv("C:\Users\Jason\Desktop\ml-1m\ml-1m\ings.dat", sep = "::", names = ["UserID","MovieID","Rating","Timestamp"])

# Extracting year from title and put in own column
movieData["Year"] = movieData.Title.str.slice(-5,-1) #1
movieData.Year = movieData.Year.astype(int) #2
movieData.Title = movieData.Title.str.slice(0,-7) #3

#creating indicator variables to separate Genre
genresDF = movieData.Genres.str.get_dummies(sep = "|")

#join genresDF and movieData dataset
movieDataWithGenres = movieData.merge(genresDF,left_index=True,right_index=True)

#del genres column
del movieDataWithGenres["Genres"]

#Figure out which decade each movie was in
yearsData = movieData[["Title","Year"]] #1
minYear = yearsData.Year.min() #2
maxYear = yearsData.Year.max() #3
print("Earliest year: %d Latest year: %d"%(minYear,maxYear)) #4

minDecade = np.floor_divide(minYear,10)*10 #5
maxDecade = np.floor_divide(maxYear,10)*10 #6
print("Earliest decade: %d End of Final Decade: %d"%(minDecade,maxDecade)) #7

allDecades = np.arange(minDecade,maxDecade+10,10) #8
print("All decades: %s" %(allDecades)) #9

yearsData["Decade"] = pd.cut(yearsData.Year,allDecades) #10
moviesPerDecade = yearsData.groupby("Decade").size() #11
moviesPerDecade.sort(ascending=False,inplace=True)   #12

print("Decade with the most movies:") #13
print(moviesPerDecade) #14
