try:
    fh=open("anuma.txt","r")
    try:
        fh.write("this is my testfile for exception handling")
    finally:
        print("going to close the file")
        fh.close()
except IOError:
    print("error: cant find any file")