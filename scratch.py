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
ratingData["Rating"] = ratingData.Rating.astype(float)
movieGroups = ratingData.groupby("MovieID")
avgRatingPerMovie = movieGroups.Rating.mean()
highestRatingMask = avgRatingPerMovie==avgRatingPerMovie.max()
print avgRatingPerMovie[highestRatingMask]
