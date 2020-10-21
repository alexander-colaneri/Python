import sqlite3

# Whenever possible, separate database queries into a specific file for that.

# Inserting SQL queries into variables:
# "PRIMARY KEY": at each input in the table, the "id" number will be += 1:
CREATE_CARD_TABLE = 'CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY ' \
                    'KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);'
# Right below, we're not making reference to "id", because the keyword
# "PRIMARY KEY" insert a number +1 in each input.
INSERT_ACCOUNT_DATA = 'INSERT INTO card (number, pin, balance) VALUES (?, ?, ?);'
DISPLAY_ALL_CARDS = 'SELECT * FROM card'


def connect():
    return sqlite3.connect('card.s3db')


# Query to create a table:
def create_tables(connection):  # This parameter is necessary, we still
    # don't have access to it, but so whoever calls this function is going
    # to give it the connection that it has to use in order to execute the
    # query.
    with connection:  # This is a "context manager", it guarantees that when
        # the query to create a table is executed, that it will be saved in the file.
        connection.execute(CREATE_CARD_TABLE)


def insert_data_to_database(connection, number, pin, balance):
    with connection:
        connection.execute(INSERT_ACCOUNT_DATA, (number, pin, balance))  #
        # When working with sqlite, it's necessary to indicate the
        # parameters again here, as a tuple of values that will be inserted,
        # each one replacing the question marks "?, ?, ?".)


def display_all_cards(connection):
    with connection:
        connection.execute(DISPLAY_ALL_CARDS).fetchall()  # When you need to
        # show results, which in SQL is when you use "SELECT", don't forget to
        # specify if you want to see all results (fetchall()) or only one
        # (fetchone()).
