# Códigos rápidos para Python

## READ - SELECT

Para receber um registro único, usamos `variável = cur.fetchone()`:

```python

sql = "SELECT * FROM table WHERE id = %s"
cur = mysql.connection.cursor()
cur.execute(sql)
row = cur.fetchone()
cur.close()

```

Para receber vários registros, usamos `variável = cur.fetchall()`:

```python

sql = "SELECT * FROM table"
cur = mysql.connection.cursor()
cur.execute(sql)
rows = cur.fetchall()
cur.close()

```

## CREATE - INSERT, UPDATE e DELETE

Como essas interações não tem um retorno, usamos `mysql.connection.commit()`:

```python

sql = "INSERT INTO table (field1, field2) VALUES (%s, %s)"
cur = mysql.connection.cursor()
cur.execute(sql, (var_field1, var_field2,))
mysql.connection.commit()
cur.close()

```

## Caixa de diálogo HTML com modal

```HTML

{% if dialod %}

<dialog id="myDialog">
    <h4>Oba!</h4>
    <p>Isso é uma caixa de diálogo!</p>
    <form method="dialog"><button>OK</button></form>
</dialog>
<script>myDialog.showModal()</script>

{% endif %}

```