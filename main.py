from random import randint,shuffle

import sqlite3
conn = sqlite3.connect("zxc.db")
cursor = conn.cursor()
#cursor.execute('SELECT * FROM q1')
#data = cursor.fetchall()
#print(data)
cursor.execute('''DROP TABLE IF EXISTS q''')
def create(name):
    conn = sqlite3.connect("zxc.db")
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name} (
        q TEXT, 
        a TEXT,
        w1 TEXT,
        w2 TEXT,
        w3 TEXT)''')
    conn.commit() 
def ad(list_q, name):
    conn = sqlite3.connect("zxc.db")
    cursor = conn.cursor()
    print(list_q)
    cursor.executemany(f'''INSERT INTO {name} 
                 (q, a, w1, w2, w3) 
                  VALUES (?,?,?,?,?)''', list_q)
    conn.commit() 
#conn = sqlite3.connect("zxc.db")
#cursor = conn.cursor()
#cursor.execute('''DROP TABLE IF EXISTS q1''')
#cursor.execute('''DROP TABLE IF EXISTS q2''')
#cursor.execute('''DROP TABLE IF EXISTS q3''')
#create('q1')
#ad([("ГО3йда1", "ГОйда", "52", "69", "96"),("ГО2йда1", "ГОйда", "52", "69", "96"),("ГОйд1а1", "ГОйда", "52", "69", "96")],'q1')
#create('q2')
#ad([("ГО3йда2", "ГОйда", "52", "69", "96"),("ГО2йда2", "ГОйда", "52", "69", "96"),("ГОйд1а2", "ГОйда", "52", "69", "96")],'q2')
#create('q3')
#ad([("ГО3йда3", "ГОйда", "52", "69", "96"),("ГО2йда3", "ГОйда", "52", "69", "96"),("ГОйд1а3", "ГОйда", "52", "69", "96")],'q3')
#conn.commit() 
#cursor.execute('SELECT * FROM q1')
#data = cursor.fetchall()
#print(data)
#cursor.execute('SELECT * FROM q2')
#data = cursor.fetchall()
#print(data)
#cursor.execute('SELECT * FROM q3')
#data = cursor.fetchall()
#print(data)
#cursor.execute('''INSERT INTO vopros1 (q, a, w1, w2, w3) 
#                VALUES ("ГОйда", "ГОйда", "52", "69", "96")''')
#list_q = [('q'+str(i),'a','w1','w2','w3') for i in range(10)]
#print(list_q)
#cursor.executemany('''INSERT INTO vopros1 
#                 (q, a, w1, w2, w3) 
#                  VALUES (?,?,?,?,?)''', list_q)      
#cursor.execute('SELECT * FROM vopros1')
#data = cursor.fetchall()
#print(data)
conn.commit()
def get_q(index, table):
    conn = sqlite3.connect("zxc.db")
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    data = cursor.fetchall()
    #print(data[index])
    return data[index]
def chek_q(index, otvet, table):
    conn = sqlite3.connect("zxc.db")
    cursor = conn.cursor()
    vopros = get_q(index, table)
    ans = vopros[1]
    if ans == otvet:
        return True
    else:
        return False
def get_t():
    conn = sqlite3.connect("zxc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    data = cursor.fetchall()
    return data
def get_l(table):
    conn = sqlite3.connect("zxc.db")
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    #print(cursor.fetchall())
    return len(cursor.fetchall())
#print(get_t())
#print(chek_q(2,'wq','q1'))
#get_q(5)
#a = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'.split()
#l = len(a)
#p = ['Мужчина',"ЖИенщина"]
#name = [''.join(a[0:randint(0,l-1)]) for i in range(10)]
#fname = [''.join(a[0:randint(0,l-1)]) for i in range(10)]
#age = [randint(0,52) for i in range(10)]
#pol = [p[randint(0,1)] for i in range(10)]
#print(name)
#print(fname)
#print(age)
#print(pol)
#list_q = [(name[i],fname[i],age[i],pol[i]) for i in range(10)]
#"""cursor.execute('''CREATE TABLE questions (
#    Fimya TEXT, 
#    Imilia TEXT,
#    age INT,
#    pol TEXT)''')"""
##cursor.execute('''INSERT INTO questions (Fimya, Imilia, age, pol) 
##                    VALUES ("Саша", "Шпак", 52, "Мужчина")''')
#cursor.executemany('''INSERT INTO questions 
#                 (Fimya, Imilia, age, pol) 
#                  VALUES (?,?,?,?)''', list_q)
##cursor.execute('SELECT * FROM questions')
##cursor.execute('SELECT * FROM questions WHERE pol="Мужчина"')
#data = cursor.fetchall()
##print(len(data))
#cursor.execute('SELECT * FROM questions')
#data = cursor.fetchall()
#print(len(data))
#conn.commit()

from random import randint, shuffle
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
@app.route("/test",methods=['GET','POST'])
def test():
    if len(session) == 0:
        return redirect(url_for('index'))
    if session['id'] == get_l(session['table']):
        return redirect(url_for('result'))
    if request.method == "POST":
        answer = request.form.get('ans_text')
        index = session['id']
        table = session['table']
        if answer != None:
            session['id'] += 1
            if chek_q(index,answer,table):
                session['score'] += 1
                return redirect(url_for('test'))
            else:
                return redirect(url_for('test'))
    zzxc = get_q(session['id'], session['table'])
    q = zzxc[0]
    v = list(zzxc[1:])
    shuffle(v)
    return render_template('index2.html',q=q,v=v,i=session['id'])

@app.route("/result")
def result():
    if len(session) == 0:
        return redirect(url_for('index'))
    return f"""<h1>Ваш счет: {session['score']} из {session['id']}</h1> <a href="/">qweqwe</a>"""
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        zxc = request.form.get('list_down')
        session['table'] = zxc
        session['id'] = 0
        session['score'] = 0
        return redirect(url_for('test'))
    return render_template('index1.html',q1=get_t()[0][0], q2 = get_t()[1][0], q3=get_t()[2][0])
    #return '<a href="/test">LF</a>'
app.config['SECRET_KEY'] = 'qweqweqweqwe111111'
if __name__ == "__main__":
    app.run(debug=True, host=('192.168.8.172'))

#pyinstaller --onfile --noconsole