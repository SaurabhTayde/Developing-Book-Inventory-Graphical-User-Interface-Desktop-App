import sqlite3

# OOP is not a must. We can either use it or not use it. Simply functions can be used to build an appplication
# However it is generally accepted that if we have more than two functions which apply operations to the same object, so we should orgnise these functions in something called a class
# OOP is about encapsulating functions inside a class
# 'object instance' and 'object' are same concepts
# 'Instance variables' are the variables that are defined inside the methods of the class. And these variables are accessible by the object instance


class Database:   # Database is name of the class

    def __init__(self, db): # This is init function which means initialize an object. In other programming language it is called constructor since it constructs an object.
                            # 'self means the class object itself
                            # So when we call the class only __init__ function is executed not the other ones. For calling other functions we need to explicitly write name of those functions (after class name)
                            # Functions inside the class are called methods (They are also called 'function attributes' of this class)
                            # We are writing 'self.' in front of every variable here because writing 'self.' makes that variable in 'init' method as global variable and it can be used in other methods (i.e. functions)
                            # The variables that we will be using in methods (using self.) is called instance variables (For Ex. here 'self.conn', 'self.cur' is instance variable)

        self.conn = sqlite3.connect(db)   # Here 'self' is Database (class) object and 'conn' is instance variable
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()


    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows


    def search(self, title="", author="", year="", isbn=""): # We have taken empty string by default since if user enters only one or two or three options then function shouldnt give argument error)
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn=?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows


    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()


    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    #connect()
    #insert("The Venus", "Will Peters", 1931, 913123234)
    #delete(3)
    #update(4, "The moon", "Jerry Smooth", 1917, 123976)
    #print(view())
    #print(search(author = 'John Smith'))
