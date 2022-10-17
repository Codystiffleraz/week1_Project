my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_list = [
    {
        "title": "Verity",
        "author": "Colleen Hoover",
        "year": 2018,
        "rating": 3.9,
        "pages": 433
    },
    {
        "title": "Mad Honey",
        "author": "Barbara Kingsolver",
        "year": 2020,
        "rating": 4.8,
        "pages": 302
    },
    {
        "title": "Where the Crawdads Sing",
        "author": "Delia Owens",
        "year": 2018,
        "rating": 3.22,
        "pages": 332
    }
]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below


def book_reader(dict):

    book_sentence = f"The books is {dict['title']}, and was written by {dict['author']}. The year it was published was {dict['year']} and is rated a {dict['rating']}. The book is {dict['pages']} pages long"

    return book_sentence


print(book_reader(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def get_book_title(dict):
    book_title = dict["title"]
    return book_title


def get_book_author(dict):
    book_author = dict["author"]
    return book_author


def get_book_year(dict):
    book_year = dict["year"]
    return book_year


def get_book_rating(dict):
    book_rating = dict["rating"]
    return book_rating


def get_book_pages(dict):
    book_pages = dict["pages"]
    return book_pages

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below


def reader_from_list(dict_list):
    for dict in dict_list:
        print(book_reader(dict))


def get_set_of_authors(dict_list):
    author_set = set()

    for dict in dict_list:
        author_set.add(dict["author"])

    return author_set


def get_total_pages(dict_list):
    total_pages = 0

    for dict in dict_list:
        total_pages += dict["pages"]

    return total_pages


reader_from_list(my_book_list)
print(get_set_of_authors(my_book_list))
print(get_total_pages(my_book_list))
