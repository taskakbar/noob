from flask import Flask, render_template, request, redirect ,url_for
from flask_cors import CORS
from models import create_post, get_posts
import webbrowser
import sqlite3
conn = sqlite3.connect('database.db', check_same_thread=False)

from _date import timestamp
from database import add_data_siswa, add_poin_siswa
from update_sqlite import update_data_siswa, delete_data_siswa
app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def login():
     
            
    if request.method == 'GET':
        pass 
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name == "z" and  email == "z":
            return redirect(url_for('simpan_data_siswa'))
  
 
    return render_template ('login.html' )
 
@app.route('/panel_guru_bk', methods=['GET', 'POST'])
def simpan_data_siswa(): 

    curr=conn.execute("SELECT* from DATA_SISWA ")
    data = curr.fetchall ()

    if request.method == 'POST' and  "Tambah_Poin" in request.form :
        nisn =request.form.get('nisn')
        curr=conn.execute("SELECT* from POIN_SISWA WHERE nisn = '" + nisn +"'")
        data = curr.fetchall ()
        return render_template('form_point.html',data_siswa = data)
 
    
    if request.method == 'POST' and  "Simpan_baru" in request.form: #
        nama_siswa = request.form.get('nama_siswa')
        n_induk = request.form.get('n_induk')
        nisn =request.form.get('nisn')
        ttl =request.form.get('ttl')
        jenis =request.form.get('jenis')
        agama =request.form.get('agama')  
        a_ke =request.form.get('a_ke')
        status_dk =request.form.get('status_dk')
        alamat =request.form.get('alamat')
        h_siswa =request.form.get('h_siswa')
        n_ayah =request.form.get('n_ayah')
        h_ayah =request.form.get('h_ayah')
        n_ibu =request.form.get('n_ibu')
        h_ibu = request.form.get('h_ibu')
        datenum = timestamp()
        add_data_siswa(nama_siswa,n_induk,nisn,ttl,jenis,agama,a_ke,status_dk,alamat,h_siswa,n_ayah,h_ayah,n_ibu,h_ibu,datenum)
        print(nama_siswa,n_induk,nisn,ttl,jenis,agama,a_ke,status_dk,alamat,h_siswa,n_ayah,h_ayah,n_ibu,h_ibu,datenum)
        return redirect(url_for('simpan_data_siswa'))
    
    if request.method == 'POST' and  "Simpan_Edit" in request.form :
        id = request.form.get('id')
        nama_siswa = request.form.get('nama_siswa')
        n_induk = request.form.get('n_induk')
        nisn =request.form.get('nisn')
        ttl =request.form.get('ttl')
        jenis =request.form.get('jenis')
        agama =request.form.get('agama')  
        a_ke =request.form.get('a_ke')
        status_dk =request.form.get('status_dk')
        alamat =request.form.get('alamat')
        h_siswa =request.form.get('h_siswa')
        n_ayah =request.form.get('n_ayah')
        h_ayah =request.form.get('h_ayah')
        n_ibu =request.form.get('n_ibu')
        h_ibu = request.form.get('h_ibu')
        datenum = timestamp()
        update_data_siswa(nama_siswa,n_induk,nisn,ttl,jenis,agama,a_ke,status_dk,alamat,h_siswa,n_ayah,h_ayah,n_ibu,h_ibu,id)
        print(nama_siswa,n_induk,nisn,ttl,jenis,agama,a_ke,status_dk,alamat,h_siswa,n_ayah,h_ayah,n_ibu,h_ibu,datenum)
        return redirect(url_for('simpan_data_siswa'))
    
    if request.method == 'POST' and  "Hapus_Edit" in request.form :
        id = request.form.get('id')
        delete_data_siswa(id)
        return redirect(url_for('simpan_data_siswa'))
        
    if request.method == 'POST' and  "Lihat_Detail" in request.form :

        id = request.form.get('id')
        nama_siswa = request.form.get('nama_siswa')
        n_induk = request.form.get('n_induk')
        nisn =request.form.get('nisn')
        curr=conn.execute("SELECT* from DATA_SISWA WHERE nisn = '" +nisn+"'")
        data = curr.fetchall ()
        curr2=conn.execute("SELECT SUM (p_kebaikan)  from POIN_SISWA WHERE nisn =  '" +nisn+"'")
        

        data2 = curr2.fetchall ()
        tup = data2[0]
        p_kebaikan= str(tup[0])
        listt = []
        listt.append(p_kebaikan)
      
        
        print(listt)
         
             
        return render_template('catatan_siswa.html',data_siswa = data,poin_siswa = listt)

    
    if request.method == 'POST' and  "Catatan_siswa" in request.form :
        return redirect(url_for('catatan_siswa'))

    if request.method == 'POST' and  "Data_siswa" in request.form :
        return redirect(url_for('simpan_data_siswa'))

    
    return render_template('panel_guru_bk.html',data_siswa = data) #else This

 
@app.route('/catatan_siswa', methods=['GET', 'POST'])
def catatan_siswa():
    curr=conn.execute("SELECT* from DATA_SISWA ")
    data = curr.fetchall ()

    if request.method == 'POST' and  "Catatan_siswa" in request.form :
        return redirect(url_for('catatan_siswa'))

    if request.method == 'POST' and  "Data_siswa" in request.form :
        return redirect(url_for('simpan_data_siswa'))

    if request.method == 'POST' and  "Tambah_Poin" in request.form :
        nisn =request.form.get('nisn')
        curr=conn.execute("SELECT* from DATA_SISWA WHERE nisn = 1") #'" + nisn +"'")
        data = curr.fetchall ()
        return render_template('form_point.html',data_siswa = data)
    if request.method == 'POST' and  "Catatan_siswa" in request.form :
        nisn =request.form.get('nisn')
        curr=conn.execute("SELECT* from POIN_SISWA WHERE  nisn = 1") #'" + nisn +"'")
        data = curr.fetchall ()
        return render_template('form_point.html',data_siswa = data)
 
 

    if request.method == 'POST' and  "Tambah_poin_siswa" in request.form: 
        nama_siswa = request.form.get('nama_siswa')
        n_induk = request.form.get('n_induk')
        nisn =request.form.get('nisn')
        h_siswa =request.form.get('h_siswa')
        p_kebaikan =request.form.get('p_kebaikan')
        p_keburukan =request.form.get('p_keburukan')
        datenum = timestamp()
        add_poin_siswa(nama_siswa,n_induk,nisn,h_siswa,p_kebaikan,p_keburukan,datenum)

    return render_template('form_point.html',data_siswa = data) 
 
 
@app.route('/form_point', methods=['GET', 'POST'])
def form_point():
 
    if request.method == 'POST' and  "Tambah_Poin" in request.form :
        return redirect(url_for('form_point'))




    return render_template ('form_point.html' )
 

if __name__ == '__main__':
    app.run(debug=True, port=8080)