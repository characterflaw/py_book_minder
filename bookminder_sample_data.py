import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bookminder_declarative import Base, Author, Series, Book

engine = create_engine('sqlite:///test.db')
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

with open('data/series.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # header row
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            new_series = Series(author_id=row[0], title=row[1])
            session.add(new_series)
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
            new_book = Book(title=row[0], year=row[1], author1_id=row[2], \
                            author2_id=row[3], own_flag=row[4], read_flag=row[5], \
                            series_id=row[6])
            session.add(new_book)
            session.commit()
            line_count += 1
    print(f'Processed {line_count} lines.')


with engine.connect() as con:

    rs = con.execute('SELECT * FROM series LEFT JOIN author on author.id=series.author_id')

    for row in rs:
        print(row)




# 'UPDATE series SET author_id='