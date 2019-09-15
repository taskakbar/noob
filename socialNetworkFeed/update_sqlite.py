import sqlite3
conn = sqlite3.connect('database.db', check_same_thread=False)


def delete_data_siswa(ide):
    database = 'database.db'
    conn = create_connection(database)    
    curr=conn.execute("DELETE from DATA_SISWA WHERE ide is " + str(ide))
    data = curr.fetchall ()
    conn.commit()
    print(ide)  

def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql =  ''' UPDATE DATA_SISWA
                SET nama_siswa = ? ,  n_induk = ? ,  nisn = ? ,  ttl = ? , jenis = ? , agama = ? , a_ke = ? , status_dk = ? , alamat = ? , h_siswa = ? , n_ayah = ? , h_ayah = ?, n_ibu = ?, h_ibu = ? 
                WHERE ide  = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except TypeError as e:
        print(e)
    return None

def update_data_siswa(nama_siswa,n_induk,nisn,ttl,jenis,agama,a_ke,status_dk,alamat,h_siswa,n_ayah,h_ayah,n_ibu,h_ibu,ide):
    database = 'database.db'
    conn = create_connection(database)
    with conn:
        update_task(conn, (nama_siswa,n_induk,nisn,ttl,jenis,agama,a_ke,status_dk,alamat,h_siswa,n_ayah,h_ayah,n_ibu,h_ibu,ide))
        print('update_data_siswa selesai')
        
 
if __name__ == '__main__':
    # update_data("denis","pria","jakarta","1A","62811518818888",1)
    pass


 