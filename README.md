<h1>default env</h1>
 dbip=10.33.0.199<br>
 dbname=defaultdb123<br>
 dbuser=sa<br>
 dbpass=1qazXSW@<br>

<h1> path list </h1>
/ = query <br>
/insert = insert data into table (ต้องมี table  ก่อน ถ้าไม่มีให้เข้า/createtable เดียวมันสร้างให้) <br>
/createdb = create databases; "ENV-dbname" <br>
/createtable = create table ( ต้องมี db ก่อน ถ้าไม่มีให้เข้า /createdb เดียวมันสร้างให้)

    path('insert',views.insert),
    path('createdb',views.createdb),
    path('createtable',views.createtable),
