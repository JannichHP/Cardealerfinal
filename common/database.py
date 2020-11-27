import psycopg2

DATABASE_URI = Dyrox.mysql.pythonanywhere-services.com

database = sqlite3.connect(DATABASE_URI)
cursor = database.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS car_table (vin_number, car_name, car_color)')

database.close()


database = sqlite3.connect(DATABASE_URI)
cursor = database.cursor()

cursor.execute('SELECT * FROM car_table WHERE vin_number=?', (vin_number,))

database.close()

#achieving data from
