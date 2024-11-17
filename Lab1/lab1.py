from datetime import datetime
import os
from collections import defaultdict
import itertools

class Review:
    def __init__(self,cID,productID,date,rating,text):
        self.cID=cID
        self.productID=productID
        self.date=datetime.strptime(date,'%Y-%m-%d')
        self.rating=int(rating)
        self.text=text

valid=0
invalid=0

def processReviews():
    global valid,invalid #access global valid and invalid varialble
    reviews=[]
    for file in os.listdir():
        if file.endswith('.txt') and file!='summary.txt':
            with open(file,'r') as reviewFile:
                for line in reviewFile:
                    lineStrip = line.strip().split(maxsplit=4)
                    #.strip() removes trailing and leading whitespaces
                    # .split() splits the string into list wherever it encounters whitespaces
                    # split maximum of 4 substrings => (maxsplit=4) 
                    if len(lineStrip)==5:
                        try:
                            cid, productid, date, rating, text = lineStrip
                            reviews.append(Review(cid,productid,date,rating,text))
                            valid+=1
                        except ValueError as e:
                            print("Value Error: ", e);
                            invalid+=1
                    else:
                        invalid+=1

    return reviews

def calcAverageRatings(reviews):
    productRatings=defaultdict(list)
    #Create an empty dictionary with each key mapping to values as lists

    for review in reviews:
        productRatings[review.productID].append(review.rating)
    
    averageRatings={productID: sum(ratings)/len(ratings) for productID,ratings in productRatings.items() }
    return averageRatings
    

if __name__=="__main__":
    reviews=processReviews()
    
    averageRatings = calcAverageRatings(reviews)
    averageRatings = dict(sorted(averageRatings.items(),key=lambda x : x[1],reverse=True));
    #Sort Dictionary based on it's value => (key=lambda x :x[1])
    #Sort Desceding => (reverse=True)

    if averageRatings != {}:
        topRatings = dict(itertools.islice(averageRatings.items(), 3));
        #slice the dictionary and get first key,value pairs from the dictionary

        with open("summary.txt","w") as file:
            file.write("----Summary----\n")
            file.write(f"Total Reviews Processed: {valid+invalid}\n")
            file.write(f"Valid Reviews Processed: {valid}\n")
            file.write(f"Invalid Reviews Processed: {invalid}\n")
    
            file.write("----Top Products----\n")
            for productID,averageRating in topRatings.items():
                file.write(f"Product ID : {productID}, Average Rating : {averageRating}\n")

    else:
        print("no .txts found with proper review formats")
