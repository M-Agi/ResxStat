Script to extract localization statistics.
Parses a localization *.resx file (or a directory of *.resx files) and prints out statistics about the text(s).

Tasks/Features:
1.: The first argument has to be either a directory or a singular *.resx file. If it is a directory, it has to be scanned for all the *.resx files and all of them has to be parsed.
2.: For each *.resx file a statistic result has to be printed (and a full summary too preferably). This should contain the following:
- How many entries it has (name).
- How many words & characters the translated texts have (value).
- The number of characters in the longest translated text.
- How many unique words (preferably signs and numbers ,.-='"0123 ... should not be counted as a unique word) the translated texts have.
3.: Again if multiple files are parsed the statistics should be done for the whole directory (combination of the files) too!
