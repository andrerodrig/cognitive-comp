# Import necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
from NLP.src.nlp_utils import get_sample_Santo_Graal

# Split scene_one into sentences: sentences
scene_one = get_sample_Santo_Graal()
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
word_list = [word_tokenize(sentence) for sentence in sentences]
unique_tokens = set([word for words in word_list for word in words])

# Print the unique tokens result
print(unique_tokens)
print(len(unique_tokens))