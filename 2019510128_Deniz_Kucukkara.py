from bs4 import BeautifulSoup as bs
import requests

firstbook_list_word_for_repetition = []
secondbook_list_word_for_repetition = []
lastkeylist = []
lastvaluelist = []
keyfor1_stbook = []
valuesfor1_stbook = []
keyfor2_ndbook = []
valuesfor2_ndbook = []
first_book =""
exit = True

second_book =""
manybooks = 0
basic_adress = "https://en.wikibooks.org/wiki/" #basic_adress is the link required to direct us to the site
stopwords =["a","'", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all",
            "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst",
            "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at",
            "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below"
            , "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could",
            "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else",
            "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill",
            "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had",
            "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however",
            "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd",
            "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name",
            "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often",
            "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please",
            "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six",
            "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the",
            "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin",
            "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty",
            "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where",
            "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose",
            "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the", "won't", "non", "b", "line", "i","$","k"]
punctuation_marks = '!,.;:(#?[]&)=><&@^%_-0123456789*/`{}"|~\n\t'



def max_word_finder_for_dic(txt_file, purified_words) :  #Here the book saved in .txt opens. Then stop words and punctuation are deleted.

    book_file = open(txt_file)
    book_readline = book_file.readlines()
    book_file.close()
    for lines in book_readline:
        line = lines.split(" ")

        for words in line:
            words = words.lower() #All letters are shrunk to distinguish words

            for marks in punctuation_marks:
                if marks in words:
                    index_of_letters = words.index(marks) # if the word has a sign, it is deleted and a space is put in its place
                    words = words.replace(marks, " ")
                    words = words[0:index_of_letters]

            check_stopwords = 0
            for stop_words in stopwords: #not saved if word is stop word
                if (words == stop_words) or words == "":
                    check_stopwords = 1
                    break
            if check_stopwords == 0 : # if it is not a stop word it's append the list
                purified_words.append(words)
    dictionaries_for_count(purified_words)



def dictionaries_for_count(lists) :
    word_list = dict()

    for words in lists :
        if words not in word_list : # if word not in dict it will saved in there
            word_list[words] = 1
        elif words in word_list : # if dictionary contains the word words.value getting increase
            word_list[words]+=1


    if s==0: # s = 0 means code checks first book
        from_big_to_small(keyfor1_stbook, valuesfor1_stbook, word_list)

    elif s!=0 : #s != 0 means code checks second book
        from_big_to_small(keyfor2_ndbook, valuesfor2_ndbook, word_list)



def from_big_to_small(key_list, value_list, word_list) :

    for values in word_list.values(): #The dictionary is saved in the list to make the necessary checks more conveniently below.
        value_list.append(values)
    for keys in word_list.keys():
        key_list.append(keys)

    for values in range(len(word_list.keys())): #Sorting from large to small by performing double checks

        for values2 in range(len(word_list.keys())):
             if value_list[values] > value_list[values2]:
                value_list[values], value_list[values2] = value_list[values2],value_list[values]
                key_list[values], key_list[values2] = key_list[values2], key_list[values]


    d = 0
    while (word_input - 1 >= d): #the user's desired number of big words are saved in the list
        lastkeylist.append(key_list[d])
        lastvaluelist.append((value_list[d]))
        d += 1


def just_first_book_print(key_list, value_list) :
    d=0
    while (word_input - 1 >= d): #prints for first_book option
        print(' {:<4d} {:<13s} {:<15d}'.format(d + 1, key_list[d], value_list[d]))
        d += 1
def print_for_double(key_list, value_list) :
    first_book_value_calc = -1

    for i in range(word_input): # print for double option
        first_book_value_calc += 1
        k = -1
        for key2 in key_list:
            k += 1
            if key2 == lastkeylist[first_book_value_calc]:
                print(' {:<4d} {:<13s} {:<15d} {:<16d}{:<15d} '.format(first_book_value_calc + 1, lastkeylist[first_book_value_calc],
                                                                       lastvaluelist[first_book_value_calc], value_list[k],
                                                                       (value_list[k] + lastvaluelist[first_book_value_calc])))

def distinct(compare_one,compare_two, compare_one_value) :
    l=1
    m=-1
    for key in compare_one : #in these loops it controls distinct words. If they don't contain same words k become len(list) and code prints the key
        k=0
        m+=1
        for key2 in compare_two :
            if key != key2 :
                k+=1
        if k== len(compare_two):
            print(' {:<4d} {:<13s} {:<15d}'.format(l,key, compare_one_value[m]))
            l+=1
        if l>word_input :
            break


def extraction_data(rotate_adress, book ) : # In there thanks to requests and beautifulsoap code gets the book and write in .txt file

        req = requests.get(rotate_adress + '/Print_version'  )
        if req.status_code == 200:
            soup = bs(req.content, 'lxml')
            file = open(book + ".txt", "w")
            for links in soup.find_all(class_="mw-parser-output"): # retrieves all data in the given class
                file.write(links.text.encode('utf8').decode('ascii', 'ignore')) # Asci converts to encode because it can be a problem
            file.close()
        else : # if link has lower p code controls that and continues
            req = requests.get(rotate_adress + '/print_version')
            if req.status_code == 200:
                soup = bs(req.content, 'lxml')
                file = open(book + ".txt", "w")
                for links in soup.find_all(class_="mw-parser-output"):
                    file.write(links.text.encode('utf8').decode('ascii', 'ignore'))
                file.close()


while((manybooks !=1 or manybooks !=2) and exit == True) : # continues until the user enters the correct number

    try : # If the user enters a wrong input, the code is not broken and gives a warning message
        manybooks = int(input("\tPress 1 to learn about a book, press 2 to compare between two books\n\t\tPress :  "))
        if(manybooks == 1) :

            first_book = input("\n\tThe title of the book you want to learn\n\tName :  ").replace(" ", "_")
            print("\n\tThe number of words you want to find (Default is 20)\n\tNumber :  ", end =" ")
            try : # If the user does not enter a value, it switches to default setting.
                
                word_input = int(input())
            except :
                word_input = 20
                break
            break
        elif(manybooks==2) :
            first_book = input("\tThe name of the first book\n\tName :  ").replace(" ", "_")          
            second_book = input("\tThe name of the second book\n\tName :  ").replace(" ", "_")
            print("\n\tThe number of words you want to find (Default is 20)\n\tNumber :  ", end =" ")
            try:# If the user does not enter a value, it switches to default setting.
                word_input = int(input())
            except:
                word_input = 20
                break
            break
        else : # If the user enters a wrong value, the code is not broken and gives a warning message
            guide = ''
            while guide != 'a' or guide != 'A' or guide != 'E' or guide != 'e' : # In there if user want to exit he/she can
                guide =  (input("\tYou cannot select more than 2 or less than 1 book. Press 'E' to exit to 'A' to try again.\n\t\tPress : "))
                if guide =='A' or guide == 'a':
                    break
                elif guide == 'E' or guide == 'e':
                    exit = False
                    break
                else :
                    print('\t\tYou pressed wrong key please wait...')

    except (ValueError, ) :
        print('\n\t\tValue Error')
        print('\t\tWrong input please wait\n\n')
        print('------------------------------------------------------------------------------')
        continue

if exit ==False :
    print('\t\tSee You ')
rotate_adress = basic_adress + first_book
if(manybooks==1) : #if user entered 1
    s = 0
    try :
        extraction_data(rotate_adress, 'first_book')# In there thanks to requests and beautifulsoap code gets the book and write in .txt file
        max_word_finder_for_dic('first_book.txt', firstbook_list_word_for_repetition) # find out how many times words occur
        print('\nCOMMON WORDS\n', 'NO  ', "WORD\t", '   FREQ_1\t')
        just_first_book_print(keyfor1_stbook, valuesfor1_stbook) # print
    except :
        print('\t\tThe book you are looking for is not available on Wikisource\n\t\t See you.')
elif(manybooks ==2) : # if user entered 2
    rotate_adress2 = basic_adress + second_book
    s = 0
    try :
        extraction_data(rotate_adress, 'first_book')
        max_word_finder_for_dic('first_book.txt', firstbook_list_word_for_repetition)
        s = 1
        extraction_data(rotate_adress2, 'second_book')
        print('\nCOMMON WORDS\n', 'NO  ', "WORD\t", '   FREQ_1\t', "   FREQ_2\t", "   FREQ_SUM")
        max_word_finder_for_dic('second_book.txt', secondbook_list_word_for_repetition)
        print_for_double(keyfor2_ndbook, valuesfor2_ndbook)
        print('BOOK 1 : ',first_book,'\nDISTINCT WORDS\n', 'NO  ', "WORD\t", '   FREQ_1\t')
        distinct(keyfor1_stbook, keyfor2_ndbook, valuesfor1_stbook)
        print('BOOK 2 : ',second_book,'\nDISTINCT WORDS\n', 'NO  ', "WORD\t", '   FREQ_1\t')
        distinct(keyfor2_ndbook, keyfor1_stbook, valuesfor2_ndbook)
    except :
        print('\t\tThe book you are looking for is not available on Wikisource\n\t\t See you.')

