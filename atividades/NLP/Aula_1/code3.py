import re
from nltk.tokenize import sent_tokenize
from NLP.src.nlp_utils import get_sample_Santo_Graal

scene_one =  get_sample_Santo_Graal()
sentences =  sent_tokenize(scene_one)
# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print("1: ", match)
print("2: ", match.start(), match.end())

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = re.findall(r"(\[.*?\])", scene_one)
print("3: ", pattern1)

# Use re.search to find the first text in square brackets
pattern2 = re.search(r"\[[\S]+\]", scene_one)
print("4: ", pattern2)


# Find the script notation at the beginning of the fourth sentence and print it
pattern3 = r"^.*:"
print("5: ", re.search(pattern3, scene_one))

print("6: ", re.search(pattern3, sentences[3]))