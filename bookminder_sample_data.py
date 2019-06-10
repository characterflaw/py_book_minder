import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bookminder_declarative import Base, Author, Series, Book, BookAuthor

engine = create_engine('sqlite:///test.db', echo=True)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Series  in the `series` table
# new_series = Series(title='Wheel of Time')
# session.add(new_series)
# session.commit()

# # Insert an Author in the `author` table
# new_author = Author(first_name='Robert', last_name='Jordan')
# session.add(new_author)
# session.commit()


import_records = True

if import_records:
    with open('data/authors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # header row
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                new_author = Author(first_name=row[0], last_name=row[1])
                session.add(new_author)
                session.commit()
                line_count += 1
        print(f'Processed {line_count} lines.')

    with open('data/books.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                new_book = Book(title=row[0], year=row[1], own_flag=row[2], read_flag=row[3], \
                                series_id=row[4])
                session.add(new_book)
                session.commit()
                line_count += 1
        print(f'Processed {line_count} lines.')

    with open('data/book_authors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                new_book_author = BookAuthor(book_id=row[0], author_id=row[1])
                session.add(new_book_author)
                session.commit()
                line_count += 1
        print(f'Processed {line_count} lines.')

    with open('data/series.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # header row
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                new_series = Series(title=row[0])
                session.add(new_series)
                session.commit()
                line_count += 1
        print(f'Processed {line_count} lines.')

# our_user = session.query(Author).filter_by(first_name='Stephanie').first()
# print(our_user)
# <User(name='ed', fullname='Ed Jones', nickname='edsnickname')>



# with engine.connect() as con:
#
#     rs = con.execute('SELECT * FROM author where first_name = \'Stephanie\'')
#
#     for row in rs:
#         print(row)




# # 'UPDATE series SET author_id='

# with engine.connect() as con:
#
#
#     # query = """
#     #   SELECT * FROM book b LEFT JOIN author a on b.author1_id=a.id
#     # ;"""
#
#     # query = """
#     # SELECT *
#     # FROM series
#     # LEFT JOIN author on author.id=series.author_id
#     # ;"""
#
#     print('Book')
#     query = """
#     SELECT *
#     FROM book b
#     -- JOIN author a ON (a.id = b.author1_id) AND (a.id = b.author2_id)
#     ;"""
#     rs = con.execute(query)
#     print(rs.first())
#     print()
#
#     print('Book with Author1')
#     query = """
#     SELECT *
#     FROM book b
#     JOIN author a ON a.id = b.author1_id
#     ;"""
#     rs = con.execute(query)
#     print(rs.first())
#     print()
#
#     print('Book with Author2')
#     query = """
#     SELECT *
#     FROM book b
#     JOIN author a ON a.id = b.author2_id
#     ;"""
#     rs = con.execute(query)
#     print(rs.first())
#     print()
#
#     print('Book with Series')
#     query = """
#     SELECT *
#     FROM series s
#     JOIN book b ON s.id = b.series_id
#     ;"""
#     rs = con.execute(query)
#     print(rs.first())
#     print()




    # print('Book with Series')
    # query = """
    # SELECT b.title, s.title, a.first_name, a.last_name, a2.first_name, a2.last_name
    # FROM author a, series s
    # JOIN book b ON (s.id = b.series_id) AND (a.id = b.author1_id)
    # JOIN book b2 ON a.id = b2.author2_id
    # ;"""
    # rs = con.execute(query)
    # print(rs.first())
    # print()




    # rs = con.execute('SELECT * FROM book b LEFT JOIN author a on b.author1_id=a.id, b.author2_id=a.id')
    # rs = con.execute('SELECT * FROM book b LEFT JOIN author a on b.author1_id=a.id')
    # rs = con.execute('SELECT * FROM series LEFT JOIN author on author.id=series.author_id')

    # for row in rs:
    #     print(row)


# display Authors by last name
# with engine.connect() as con:
#
#     rs = con.execute('SELECT * FROM author ORDER BY last_name')
#     # rs.first()
#
#     for row in rs:
#         print(row)

# with engine.connect() as con:
#     query = """
#       SELECT b.title, a.first_name, a.last_name
#       FROM book b, author a, bookauthors ba
#       WHERE b.id = ba.book_id
#         AND a.id = ba.author_id
#         AND b.id = 31
#     ;"""
#
#     rs = con.execute(query)
#     # rs.first()
#
#     for row in rs:
#         print(row)


with engine.connect() as con:
    query = """
      SELECT b.title, a.first_name, a.last_name
      FROM book b, author a, bookauthors ba
      WHERE b.id = ba.book_id
        AND a.id = ba.author_id
        AND b.id = 171
    ;"""

    rs = con.execute(query)
    # rs.first()

    for row in rs:
        print(row)

# with engine.connect() as con:
#
#     new_book = Book(title='The Silmarillion', year=1977, own_flag=False, read_flag=True)
#     session.add(new_book)
#     session.commit()
#     dex = new_book.id
#     print()
#
# #    book_id = session.  #  rs.inserted_primary_key()
#
#     new_ba = BookAuthor(book_id=dex, author_id=18)
#     session.add(new_ba)
#     session.commit()
#     dex = new_ba.id
#     print(f'dex: {dex}')




# the_author = session.query(Author).filter_by(last_name='Cline').first()
# print(the_author.id)




#     query = f"""
#       INSERT INTO bookauthors VALUES ({dex}, 18)
#     ;"""
#
#
#     # for row in rs:
#     #     print(row)
#
#
#
# # with engine.connect() as con:
#     query = """
#       SELECT b.title, a.first_name, a.last_name
#       FROM book b, author a, bookauthors ba
#       WHERE b.id = ba.book_id
#         AND a.id = ba.author_id
#         AND b.id = 172
#     ;"""
#
#     rs = con.execute(query)
#     # rs.first()
#
#     for row in rs:
#         print(row)

