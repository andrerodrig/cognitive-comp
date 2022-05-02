import re
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import regexp_tokenize
from NLP.src.nlp_utils import get_sample_Santo_Graal

# Split the script into lines: lines
holy_grail = get_sample_Santo_Graal()
lines = holy_grail.split('\n')

# Replace all script lines for speaker
pattern = "([A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?|^.*):"
lines = [re.sub(pattern, '', l) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s, r'\w+') for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
plt.figure(figsize=(10,10))
plt.hist(line_num_words)
plt.xlabel("Line length")
plt.ylabel("Line number")

# Show the plot
plt.show()