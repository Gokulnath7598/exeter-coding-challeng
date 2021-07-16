# module for csv file handling
import csv
# module for regex
import re
try:
    # File to be Translated
    fin = open("t8.shakespeare.txt", "r")
    data = fin.read()
    fin.close()

    # File containing list of words to be translated
    flist = open("find_words.txt", "r")
    list = flist.readlines()

    # list to store occurance of words
    occurance = []
    list = [x.strip() for x in list]

    # csv file containing french words
    with open('french_dictionary.csv', mode='r') as inp:
        reader = csv.reader(inp)
        # a dictionary containing translations
        dict_from_csv = {rows[0]: rows[1] for rows in reader}

    for word in list:
        w = r"\b{}\b".format(word)

        # counting occurance of a word in the file
        count = len(re.findall(w, data,re.IGNORECASE))

        # replacing the words
        data = re.sub(w, dict_from_csv[word], data, flags=re.IGNORECASE)

        # updating occurance list
        occurance.append([word, dict_from_csv[word], str(count)])

    # opening and saving translated file
    fout = open("t8.shakespeare.translated.txt", "wt", encoding='UTF-8')
    fout.write(data)
    fout.close()

    # opening and saving occurance in a csv file
    with open("frequency.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['English word', 'French word', 'Frequency'])
        csvwriter.writerows(occurance)
    csvfile.close()

except Exception as e:
    # in case of any error printed here
    print("Error: ",e)







