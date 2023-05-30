tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]
number_of_tweets = len(tweets)
happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

# store the final answer in this variable
number_of_happy_tweets = 0

# perform the calculations here
for tweet in tweets:
    for word in happy_words:
        if word in tweet:
            number_of_happy_tweets += 1

print("Number of happy tweets:", number_of_happy_tweets)

happy_fraction = number_of_happy_tweets/len(tweets)
print("The fraction of happy tweets is:", happy_fraction)

# store the final answer in this variable
number_of_sad_tweets = 0

# perform the calculations here
for tweet in tweets:
    for word in sad_words:
        if word in tweet:
            number_of_sad_tweets += 1

print("Number of sad tweets:", number_of_sad_tweets)

sad_fraction = number_of_sad_tweets / len(tweets)
print("The fraction of sad tweets is:", sad_fraction)
sentiment_score = happy_fraction - sad_fraction
print("The sentiment score for the given tweets is", sentiment_score)

if sentiment_score > 0:
    print("The overall sentiment is happy")
else:
    print("The overall sentiment is sad")

# store the final answer in this variable
number_of_neutral_tweets = len(tweets) - (number_of_sad_tweets + number_of_happy_tweets)


neutral_fraction = number_of_neutral_tweets / len(tweets)
print(neutral_fraction)



