import re
from nltk.tokenize import sent_tokenize
from NLP.src.nlp_utils import get_sample_Santo_Graal

scene_one =  get_sample_Santo_Graal()
sentences =  sent_tokenize(scene_one)
# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
# print(match.start(), match.end())
# print (match)

# Write a regular expression to search for anything in square brackets: pattern1
print(scene_one, '\n')
# pattern1 = re.search(r".*\[.*\].*", scene_one)
# print(pattern1)

# Use re.search to find the first text in square brackets

pattern2 = re.match(r"(^.*\[.*\].*)", scene_one)
print(pattern2)


# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"___"
# print(____)