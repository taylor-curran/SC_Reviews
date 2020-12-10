# -*- coding: utf-8 -*-
import sqlite3

# Right Click on DB and Click [Copy Relative Path]
db_path = 'Study_Guides_Distribute_Repo/data/Chinook_Sqlite.sqlite'

conn = sqlite3.connect(db_path)
curs = conn.cursor()

# Test Connection
response = curs.execute("SELECT * FROM Track;").fetchone()
print(response)

# ----- Single Table Queries -----
# 1. Find the average invoice total for each customer, 
# return the details for the first 5 ID's
Q1 = """
SELECT CustomerId, AVG(Total)
FROM Invoice 
GROUP BY CustomerId
LIMIT 5;
     """
avg_invoice_for_each_cust = curs.execute(Q1).fetchall()
print("\n--- Average Invoice for Each Customer ---")
print(avg_invoice_for_each_cust)

# 2. Return all columns in Customer for the first 5 
# customers residing in the United States
Q2 = """
SELECT * FROM Customer
WHERE Country = 'USA'
LIMIT 5;
"""
us_customers = curs.execute(Q2).fetchall()
print("\n--- 5 US Customers ---")
print(us_customers)

# 3. Which employee does not report to anyone?
Q3 = """
SELECT FirstName, LastName FROM Employee
WHERE ReportsTo iS NULL;
"""
mr_no_boss= curs.execute(Q3).fetchone()
print("\n--- Reports to None ---")
print(mr_no_boss)

# 4. Find the number of unique composers
Q4 = """
SELECT COUNT(DISTINCT Composer) FROM Track;
     """
n_unique_composers = curs.execute(Q4).fetchone()
print("\n--- N Unique Composers ---")
print(n_unique_composers)

# 5. How many rows are in the Track table?​
Q5 = """
SELECT COUNT(*) FROM Track;
     """
n_rows_track = curs.execute(Q5).fetchall()
print("\n--- N Rows in Track ---")
print(n_rows_track)

# ----- Join Queries -----
# SELECT a1, a2, b1, b2
# FROM A
# INNER JOIN B on B.f = A.f;

# 6. Get the name of all Black Sabbath tracks and the albums they came off of
Q6 = """
SELECT Track.Name, Album.Title FROM Track
INNER JOIN Album ON Album.AlbumId = Track.AlbumId
INNER JOIN Artist ON Artist.ArtistId = Album.ArtistId
WHERE Artist.Name = 'Black Sabbath';
"""
black_sab_tracks = curs.execute(Q6).fetchall()
print("\n--- Black Sabbath Tracks ---")
print(black_sab_tracks)


# 7. What is the most popular genre by number of tracks?
Q7 = """
SELECT Genre.Name FROM Track
INNER JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.GenreId
ORDER BY COUNT(DISTINCT Track.TrackId) DESC
LIMIT 1;
     """
most_popular_genre = curs.execute(Q7).fetchall()
print("\n--- Most Popular Genre ---")
print(most_popular_genre)


# 8. Find all customers that have spent over $20
Q8 = """
SELECT Customer.LastName, Invoice.Total FROM Customer
INNER JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId
WHERE Invoice.Total > 20;
     """
spent_over_20 = curs.execute(Q8).fetchall()
print("\n--- Customers Who've Spent >$20 ---")
print(spent_over_20)


# 9. Find the first and last name, title, and the number of 
# customers each employee has helped. 
# If the customer count is 0 for an employee, 
# it doesn't need to be displayed. 
# Order the employees from most to least customers.
Q9 = """
SELECT Employee.FirstName, Employee.LastName, Employee.Title,
COUNT(Customer.SupportRepId) 
FROM Customer
INNER JOIN Employee ON Employee.EmployeeId = Customer.SupportRepId
GROUP BY Customer.SupportRepId;
     """
n_customers_e_employee = curs.execute(Q9).fetchall()
print("\n--- Number of Customers for Each Employee ---")
print(n_customers_e_employee)
# 10. Return the first and last name of each employee and 
# who they report to​
Q10 = """
SELECT FirstName, LastName, ReportsTo 
FROM Employee
INNER JOIN Employee ON Employee.EmployeeId = Employee.ReportsTo;
      """
#report_relationship = curs.execute(Q10).fetchall()
print("\n--- Who Reports to Who ---")
#print(report_relationship)

curs.close()
conn.close()