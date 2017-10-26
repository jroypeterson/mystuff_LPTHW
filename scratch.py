import numpy as np
import pandas as pd

ratingData = pd.read_csv("C:\Users\Jason.Peterson\Desktop\ml-latest-small\ings.csv",sep = ",",header =0, names = ['UserID','MovieID','Rating','Timestamp'])

ratingData['FormattedTimestamp'] = pd.to_datetime(ratingData.Timestamp,unit = 's')
ratingData.FormattedTimestamp

ratingData["year"] = ratingData.FormattedTimestamp.dt.year
ratingData["month"] = ratingData.FormattedTimestamp.dt.month
'''
crappyRatingMask = ratingData.Rating < 3
print("Crappy rating mask:\n",crappyRatingMask.head())
crappyRatings = ratingData[crappyRatingMask]
print crappyRatings.head()

'''
# apply january mask to compute descriptive stats on this
janratingmask = ratingData.month == 1 # not really sure what we are doing here tbh
print("January rating mask:\n",janratingmask.head())
janratings = ratingData[janratingmask] # why is this required and why doesn't janratingmask.head() display the data?
print janratings.head()
print("Jan ratings: \n", janratings.Rating.head())
print ("Avg. Jan rating:", janratings.Rating.mean())

# apply january mask to compute descriptive stats on this
jancrappyratingmask = janratings.Rating < 3
print("January crappy rating mask:\n",jancrappyratingmask.head())
jan_crappy_ratings = janratings[jancrappyratingmask]
print("January and crappy ratings:\n", jan_crappy_ratings.head())
print ("Avg. Jan crappy rating:", jan_crappy_ratings.Rating.mean())
