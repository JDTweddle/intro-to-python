# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words") 

def report_long_words(words):
  longer_than_ten_no_hyphen = filter_longer_than_ten_and_no_hyphen(words)
  longer_than_fifteen = modify_longer_than_fifteen(longer_than_ten_no_hyphen)
  report = ', '.join(longer_than_fifteen)
  return f"These words are quite long: {report}"

def filter_longer_than_ten_and_no_hyphen(words):
  longer_than_ten_no_hyphen = []
  for word in words:
    if len(word) > 10 and '-' not in word:
      longer_than_ten_no_hyphen.append(word)
  return longer_than_ten_no_hyphen

def modify_longer_than_fifteen(words):
  longer_than_fifteen = []
  for word in words:
    if len(word) > 15:
      truncated_word = word[:15] + '...'
      longer_than_fifteen.append(truncated_word)
    else:
       longer_than_fifteen.append(word)
  return longer_than_fifteen

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Done!