import os

def rename_files():

	# get all the files as a list
	# using os.listdir()
    list_of_files = os.listdir(r'C:\Users\Shaurya Singhal\Desktop\Machine Learning\programs\jumbled_photos')
    print(list_of_files)


    # to rename the files using `os.rename(src,dest)`
    # first we have to change our current directory to dir of files ,whose name is to be change
    os.chdir(r'C:\Users\Shaurya Singhal\Desktop\Machine Learning\programs\jumbled_photos')
    for word in list_of_files :
        index = 0
        firstchar = False
        for each_letter in word:
            if(each_letter.isalpha()):
                firstchar = True
                break
            index += 1
        os.rename(word , word[index:])

rename_files()