import numpy as np
import pandas as pd

ratingData = pd.read_csv("C:\Users\Jason\Desktop\ml-latest-small\ings.csv",sep = ",",header =0, names = ['UserID','MovieID','Rating','Timestamp'])
# this path above is different on personal vs work computer.
ratingData['FormattedTimestamp'] = pd.to_datetime(ratingData.Timestamp,unit = 's')
ratingData["year"] = ratingData.FormattedTimestamp.dt.year
ratingData["month"] = ratingData.FormattedTimestamp.dt.month
ratingData.drop('Timestamp', axis=1, inplace=True)

monthGroups = ratingData.groupby("month")
ratingsPerMonth = monthGroups.size()
monthWithMostRatings = ratingsPerMonth[ratingsPerMonth==ratingsPerMonth.max()] # can you not work on groupby directly?
avgMonthlyRatings = monthGroups.Rating.mean()
highestAvgRating = avgMonthlyRatings[avgMonthlyRatings==avgMonthlyRatings.max()]

userGroups = ratingData.groupby("UserID")
def enoughRatings (currGroup):
    return currGroup.Rating.size >=30
filteredRatings = userGroups.filter(lambda currGroup: currGroup.Rating.size >=30)
filteredRatings2 = userGroups.filter(enoughRatings)

# first half of the year, rated >4 times, averages, highest averge
firstHalfRatingMask = ratingData.month < 7
firstHalf = ratingData[firstHalfRatingMask] # all movies rated in first half of yr

firstHalfMovieIDGroups = firstHalf.groupby("MovieID") # group by movieID

atLeast5Ratings = firstHalfMovieIDGroups.filter(lambda currGroup: currGroup.Rating.size >= 5) #movies with > 5 ratings
print(atLeast5Ratings.shape)
filteredAvgHighestRating = atLeast5Ratings.groupby("MovieID").Rating.mean() #average rating/movie
filteredAvgHighestRating.sort_values(inplace=True,ascending=False) #sort each movie by average rating
print filteredAvgHighestRating.head()
