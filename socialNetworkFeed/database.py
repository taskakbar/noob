import sqlite3
 
conn = sqlite3.connect('database.db', check_same_thread=False)

def drop_table():
        connection = sqlite3.connect('database.db')  # You can create a new database by changing the name within the quotes
        cursor = connection.cursor() # The database will be saved in the location where your 'py' file is saved
        dropTableStatement = "DROP TABLE POIN_SISWA"
        cursor.execute(dropTableStatement)
        connection.close()

def create_db_poin():
    conn = sqlite3.connect('database.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
    c.execute('''CREATE TABLE POIN_SISWA
                (
                [ide] INTEGER PRIMARY KEY AUTOINCREMENT,
                [nama_siswa]text,  
                [n_induk]text,
                [nisn]text,
                [h_siswa]text,  
                [p_kebaikan]integer,  
                [p_keburukan]integer,  
                [datenum] integer)''')
    conn.commit()
def create_db_siswa():
    conn = sqlite3.connect('database.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
    c.execute('''CREATE TABLE DATA_SISWA
                (
                [ide] INTEGER PRIMARY KEY AUTOINCREMENT,
                [nama_siswa]text,  
                [n_induk]text,
                [nisn]text,
                [ttl]text,
                [jenis]text, 
                [agama]text, 
                [a_ke]text,
                [status_dk]text,  
                [alamat]text,  
                [h_siswa]text,  
                [n_ayah]text,  
                [h_ayah]text,  
                [n_ibu]text,
                [h_ibu]text,
                [datenum] integer)''')
    conn.commit()

def add_data_siswa(nama_siswa,n_induk,nisn,ttl,jenis,agama,a_ke,status_dk,alamat,h_siswa,n_ayah,h_ayah,n_ibu,h_ibu,datenum):
    conn.execute('insert into DATA_SISWA(nama_siswa,n_induk,nisn,ttl,jenis,agama,a_ke,status_dk,alamat,h_siswa,n_ayah,h_ayah,n_ibu,h_ibu,datenum) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', ( nama_siswa,n_induk,nisn,ttl,jenis,agama,a_ke,status_dk,alamat,h_siswa,n_ayah,h_ayah,n_ibu,h_ibu,datenum))
    conn.commit()
    print("siswa ditambhkan")
    return 1
def add_poin_siswa(nama_siswa,n_induk,nisn,h_siswa,p_kebaikan,p_keburukan,datenum):
    conn.execute('insert into POIN_SISWA(nama_siswa,n_induk,nisn,h_siswa,p_kebaikan,p_keburukan,datenum) values (?,?,?,?,?,?,?)', ( nama_siswa,n_induk,nisn,h_siswa,p_kebaikan,p_keburukan,datenum))
    conn.commit()
    print('selesai menambahkan poin')
def fetch_data_siswa():
    nisn= '011111100111'
    curr=conn.execute("SELECT* from POIN_SISWA")
    # curr=conn.execute("SELECT ide, SUM(p_kebaikan)  from POIN_SISWA WHERE nisn = '" +nisn+"'")
    data = curr.fetchall ()
    conn.commit()
    for row in data : 
        print(row)
        # return row
if __name__ == "__main__":
    # drop_table()
    # create_db_siswa()
    # add_data_siswa('M Husada', '5', '5', 'Pringsewu', 'pria', 'islam', '5', 'kandung', 'Pringsewu', '217898778', 'BA', '28985945', 'ibu', '8487488', 201909131535)
    # fetch_data_siswa()
    create_db_poin()
    # add_poin_siswa('Akbar', '011001000000', '011111100111', '081278977780', 90, 10,  217898778 )
    
    pass