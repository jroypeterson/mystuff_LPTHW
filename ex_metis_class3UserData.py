import pandas as pd
import numpy as np

movieData = pd.read_csv("C:\Users\Jason\Desktop\ml-1m\ml-1m\movies.dat", sep = "::", names = ["MovieID","Title","Genres"])
userData = pd.read_csv("C:\Users\Jason\Desktop\ml-1m\ml-1m\users.dat", sep = "::", names = ["UserID","Gender","Age","Occupation","Zip-code"])
ratingData = pd.read_csv("C:\Users\Jason\Desktop\ml-1m\ml-1m\ings.dat", sep = "::", names = ["UserID","MovieID","Rating","Timestamp"])

# movieData Extracting year from title and put in own column
movieData["Year"] = movieData.Title.str.slice(-5,-1) #1
movieData.Year = movieData.Year.astype(int) #2
movieData.Title = movieData.Title.str.slice(0,-7) #3
#creating indicator variables to separate Genre
genresDF = movieData.Genres.str.get_dummies(sep = "|")
#join genresDF and movieData dataset
movieDataWithGenres = movieData.merge(genresDF,left_index=True,right_index=True)
#del genres column
del movieDataWithGenres["Genres"]

myMask1 = np.logical_and(userData.Age==1,np.logical_or(userData.Occupation==4,userData.Occupation==10))
#case where they are not young
myMask1part2 = np.logical_and(userData.Age!=1,np.logical_and(userData.Occupation!=4,userData.Occupation!=10))
myMask1Better = np.logical_or(myMask1,myMask1part2)

userDataMyFilteredTest = userData[myMask1Better]

#Answering question2 using output of question 1
myMask2 = np.logical_or(np.logical_and(userDataMyFilteredTest.Occupation!=10,np.logical_and(userDataMyFilteredTest.Age!=1,userDataMyFilteredTest.Age!=18)),userDataMyFilteredTest.Occupation==10)
userDataFinallyFiltered = userDataMyFilteredTest[myMask2]

#Answer question 3
userData["Zip-code"].unique()
userDataFinallyFiltered = userDataFinallyFiltered[userDataFinallyFiltered["Zip-code"].str.len()>=5]

userDataFinallyFiltered["Zip-code"] = userDataFinallyFiltered["Zip-code"].str.slice(0,5)

print("Before removing garbage:",userData.shape)
print("After removing garbage:",userDataFinallyFiltered.shape)

filledAndCleanedUserAndRatingData = userDataFinallyFiltered.merge(ratingData,on="UserID")
print("Cleaned users joined with ratings:")
print(filledAndCleanedUserAndRatingData.head())
print("")
print("Cleaned users+ratings joined with movies:")
filledAndCleanedAllData = filledAndCleanedUserAndRatingData.merge(movieData,on = "MovieID")
print(filledAndCleanedAllData.head())
