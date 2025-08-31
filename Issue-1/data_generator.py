from english_words import get_english_words_set
import os

web2lowerset = get_english_words_set(['web2'], lower=True)

## Now generate data files of different sizes.

filenames = ["500MBfile.txt", "1GBfile.txt", "2GBfile.txt"]


for file in filenames:

    ## Clean if any files already exist
    if os.path.exists(file):
        os.remove(file)

    while True:
        with open(file, "a") as f:
            counter = 0
            for word in web2lowerset:
                f.write(word + " ")
                counter += 1
                if counter % 100 == 0:
                    f.write("\n")

        if file == "2GBfile.txt" and os.path.getsize(file) >= 2*1024 * 1024 * 1024:
            break
        elif file == "1GBfile.txt" and os.path.getsize(file) >= 1024 * 1024 * 1024:
            break
        elif file == "500MBfile.txt" and os.path.getsize(file) >= 500 * 1024 * 1024:
            break

