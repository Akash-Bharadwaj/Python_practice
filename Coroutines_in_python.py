
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)  #it calls the coroutines
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")  # from here it starts run from while loop part , it saves the run time of function
search.send("harry")
input("press any key")
search.send("harry and")
input("press any key")
search.send("thi si")
search.close()

