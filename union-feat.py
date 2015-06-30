import sys

vectors = {}
all_feat = {}

# Read features of a word line by line and merge them. If a word has a given
# POS, then append the POS to the feature.
for line in sys.stdin:
  things = line.strip().lower().split()
  pos_present = False
  try:
    word, pos = things[0].split('.')
    pos_present = True
  except:
    word = things[0]
  if word not in vectors:
    vectors[word] = {}
  for feat in things[1:]:
    if pos_present:
      feat = feat+'.'+pos
    vectors[word][feat] = 1
    if feat not in all_feat:
      all_feat[feat] = len(all_feat)

print >> sys.stderr, "Vector length:", len(all_feat)
print >> sys.stderr, "Vocab length:", len(vectors)

# Calculate the average sparsity of the resultant vectors
active = 0.
for word in vectors:
  active += len(vectors[word])
print >> sys.stderr, "Sparsity:", 100 * (1 - active/(len(all_feat)*len(vectors)))

# Print the vectors in the following format:
# word active_feat1 active_feat2 ...
for word in vectors:
  print word, " ".join(vectors[word])
