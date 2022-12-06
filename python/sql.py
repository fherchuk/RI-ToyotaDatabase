from asyncio.windows_events import NULL
from logging import exception
import mysql.connector
db = mysql.connector.connect(host='localhost', password= 'default', user= 'root', database = 'toyota')
mycursor = db.cursor()

class Error(Exception):
    pass
class NotFoundInTableException(Error):
    pass

def select(table, attributes):
    attributeString = ','.join(map(str,attributes))
    values = []
    mycursor.execute("SELECT "+attributeString+" FROM "+table)
    for i in mycursor:
        values.append(i)
    return values

def select(table, attributes, conditions):
    attributeString = ','.join(map(str,attributes))
    values = []
    mycursor.execute("SELECT "+attributeString+" FROM "+table+" WHERE "+conditions)
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
        if check(table, pk, key) is not None:
            print("UPDATE "+table+" SET "+attribute+" = %s  WHERE "+pk+" = %s;",(value, key))
        else:
            raise NotFoundInTableException
    except NotFoundInTableException:
        print("Cannot Update, Item Not Found")


def delete(table, key, value):
    try:
        if check(table, key, value) is not None:
            val = []
            val.append(value)
            print("DELETE FROM "+table+" WHERE "+key+" = (%s);",(val))
            mycursor.execute("DELETE FROM "+table+" WHERE "+key+" = (%s);",(val))
            db.commit()
        else:
            raise NotFoundInTableException
    except NotFoundInTableException:
        print("Cannot Delete, Item Not Found")

def check(table, key, value):
    result = None
    val = []
    val.append(value)
    print(("SELECT "+key+" FROM "+table+" WHERE "+key+" = (%s);",(val)))
    mycursor.execute("SELECT "+key+" FROM "+table+" WHERE "+key+" = (%s);",(val))
    for i in mycursor:
        result = i

    return result
        
        


#print(select("vehicles", ["vehicle_year", "make"],))
#print(select("vehicles", "*" ,"vehicle_year = 2019"))
insert("vehicles", ["VIN","vehicle_year","make","model", "color"],[111111111611111, 2019, "Toyota", "4Runner", "Red"])
delete("vehicles", "VIN", "111111111611111")
#update("vehicles","VIN", "111111111611111","model","Tacoma")
delete("vehicles","VIN","22222")

#print(check("vehicles", "VIN", "111111111611111"))





