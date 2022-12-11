from asyncio.windows_events import NULL
from logging import exception
import mysql.connector





class Error(Exception):
    pass
class NotFoundInTableException(Error):
    pass
class SqlConnector:
    def __init__(self, user, password):
        self.db = mysql.connector.connect(host='localhost', password = password, user = user, database = 'toyota')
        self.mycursor = self.db.cursor()

    def selectAll(table):
        values = []
        mycursor.execute("SELECT * FROM "+table)
        for i in mycursor:
            values.append(i)
        return values

    def select(con_attributes, table ,conditions):
        conditionString = ' '.join(map(str, conditions))
        values = []
        print("SELECT "+con_attributes+" FROM "+table+" WHERE "+conditionString)
        mycursor.execute("SELECT "+con_attributes+" FROM "+table+" WHERE "+conditionString)
        for i in mycursor:
            values.append(i)
        return values


    def insert(table, attributes, values):
        stringFormatting = []
        for i in attributes:
            stringFormatting.append('%s')
        attributeString = ','.join(map(str,attributes))
        valuesString = ','.join(map(str,stringFormatting))
        print("INSERT INTO "+table+" ("+attributeString+") VALUES ("+(valuesString)+")",(values))
        try:
            mycursor.execute("INSERT INTO "+table+" ("+attributeString+") VALUES ("+(valuesString)+")",(values))
            db.commit()
        except:
            print("Already Exists")

    def update(table, pk, key, attribute, value):
        try:
            if check(table, pk, key):
                print("UPDATE "+table+" SET "+attribute+" = %s  WHERE "+pk+" = %s;",(value, key))
            else:
                raise NotFoundInTableException
        except NotFoundInTableException:
            print("Cannot Update, Item Not Found")
        
    def view(viewname,con_attributes, table ,conditions):
        conditionString = ' '.join(map(str, conditions))
        values = []
        print("CREATE VIEW "+viewname+"_"+table+" AS SELECT "+con_attributes+" FROM "+table+" WHERE "+conditionString)
        mycursor.execute("CREATE VIEW "+viewname+"_"+table+" AS SELECT "+con_attributes+" FROM "+table+" WHERE "+conditionString)
        db.commit()
        for i in mycursor:
            values.append(i)
        return values

    def delete(table, key, value):
    

        try:
            # set foreign key checks to 0 in order to delete from table
            mycursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            print("DELETE FROM "+table+" WHERE "+key+" = "+value+";")
            check(table, key, value)
            print("DELETE FROM "+table+" WHERE "+key+" = "+value+";")
            mycursor.execute("DELETE FROM "+table+" WHERE "+key+" = "+value+";")
            # enable foreign key checks after items deleted
            mycursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
            db.commit()

        except NotFoundInTableException:
            print("Cannot Delete, Item Not Found")

    def check(table, key, value):
        val = []
        val.append(value)
        print(val)
        print(("SELECT "+key+" FROM "+table+" WHERE "+key+" = "+value+";"))
        mycursor.execute("SELECT "+key+" FROM "+table+" WHERE "+key+" = "+value+";")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    # comment out "create index" to avoid errors on compile
    # def create_index(db, table, column):
        # query = "CREATE INDEX {column}_index ON {table} ({column}).format(table=table, column=column)
        # mycursor.execute(query)
       




