def find_replace():
    """
    This is a function for finding and replacing a word in a text file.
    It loads the text file, changes desired text/characters and returns 
    the result as string
    
    Params:
    **
    file_name: accepts input as text file name including extension 
    e.g. "example.txt"
    
    **
    find_word: accepts word/characters to be replaced in text and
    and converts to string format
    
    **
    replace_word: accepts replacement word/characters and converts 
    to string
    """
    
    #import 'logging' and create log file
    import logging
    logging.basicConfig(filename = 'find_replace.log', level = logging.DEBUG, format = '%(asctime)s %(message)s')
    
    try:
        #load .txt file and store content in variable
        file_name = str(input('File Name: '))
        file = open (file_name, 'r+')
        file.seek(0)
        text_file = file.read()
        logging.info('file [ %s ] loaded succesfully'%file_name)
    except:
        logging.error ('''
        Error loading file: Please check 
                -- file name spelling
                -- file extension spelling
                -- if file exists
                ''')
        print ('''
        Error loading file: Please check 
                -- file name spelling
                -- file extension spelling
                -- if file exists
                ''')
    try:
        #ask user to input words for
        #find and replace operation
        find_word = str(input('find_word: '))
        replace_word = str(input('replace_with: '))
        
        #check if word to be found exists in text file
        if find_word in text_file:
            logging.info('''find_word "{a}" and replace_word "{b}"
            entered'''.format(a = find_word, b = replace_word))
        else:
            logging.warning("'",find_word,"'",' not found')
            print ("'",find_word,"'",' not found')
            
    except:
        logging.error('''
        Error loading word: Please check 
                -- text must be string
               ''')
        print ('''
        Error loading word: Please check 
                -- text must be string
               ''')
    try:    
        #replace old word with new word
        changed_text = text_file.replace(find_word, replace_word)
        if changed_text!=text_file:
            #save new version of text into text file
            file.seek(0)
            file.write(changed_text)
            logging.info('''All instances of "{a}" sucessfully replaced with "{b}" 
            '''.format(a = find_word, b = replace_word))
            logging.shutdown()
            #return new version of text for other operations
            return changed_text
        else:
            logging.warning('''
        Error replacing text: Please check
                -- word to be changed must be in text
                -- word should not be replaced with same word
                ''')
            logging.shutdown()
    except:
        logging.error('''
        Error replacing text: Please check
                -- word to be changed must be in text
                -- word should not be replaced with same word
                ''')
        print ('''
        Error replacing text: Please check
                -- word to be changed must be in text
                -- word should not be replaced with same word
                ''')  
        logging.shutdown()