# Import the necessary modules

from nltk.tokenize import regexp_tokenize, TweetTokenizer
from NLP.src.nlp_utils import get_tweets_sample

tweets = get_tweets_sample()

# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#[\w]+"
# Use the pattern on the first tweet in the tweets list
hashtags = regexp_tokenize(tweets[0], pattern1)

print("1: ", hashtags)

# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"[#@][\w]+"
# # Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print("2: ", mentions_hashtags)

# # Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print("3: ", all_tokens)