<h1>วิธีใช้</h1>

docker run  -e dbip=1.1.1.1 -e dbname=dbtest -e dbuser=sa -e dbpass=123456 mssql-container 

<h1>default env</h1>
 dbip=10.33.0.199<br>
 dbname=defaultdb123<br>
 dbuser=sa<br>
 dbpass=1qazXSW@<br>

<h1> path list </h1>
/ = select * from test123 (ต้องมีข้อมูลก่อน ถ้าไม่มีให้เข้า /insert เดียวมันสร้างให้) <br>
/insert = insert data into table (ต้องมี table  ก่อน ถ้าไม่มีให้เข้า/createtable เดียวมันสร้างให้) <br>
/createdb = create databases; "ENV-dbname" <br>
/createtable = create table ( ต้องมี db ก่อน ถ้าไม่มีให้เข้า /createdb เดียวมันสร้างให้)

