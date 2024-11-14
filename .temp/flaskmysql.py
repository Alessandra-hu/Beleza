# Importa as dependências do aplicativo
from flask import Flask
from flask_mysqldb import MySQL

# Cria um aplicativo Flask chamado "app"
app = Flask(__name__)

# Configurações de acesso ao MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crudtrecos'

# Setup da conexão com MySQL
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_USE_UNICODE'] = True
app.config['MYSQL_CHARSET'] = 'utf8mb4'

# Variável de conexão com o MySQL
mysql = MySQL(app)


@app.before_request
def start():

    # Setup do MySQL para corrigir acentuação
    cur = mysql.connection.cursor()
    cur.execute("SET NAMES utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    cur.execute("SET character_set_client=utf8mb4")
    cur.execute("SET character_set_results=utf8mb4")

    # Setup do MySQL para dias da semana e meses em português
    cur.execute("SET lc_time_names = 'pt_BR'")


@app.route("/")
def index():

    # Um id qualquer
    id = 1

    # Um valor qualquer
    var_field1 = "mensagem"
    var_field2 = "informação"

    # Para receber um registro único, usamos `variável = cur.fetchone()`:
    sql = "SELECT * FROM table WHERE id = %s"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    cur.close()

    print(row)

    # Para receber vários registros, usamos `variável = cur.fetchall()`:
    sql = "SELECT * FROM table"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()

    print(rows)

    # Para as outras interações (INSERT, UPDATE e DELETE) não tem um retorno, usamos `mysql.connection.commit()`:
    sql = "INSERT INTO table (field1, field2) VALUES (%s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(sql, (var_field1, var_field2,))
    mysql.connection.commit()
    cur.close()

    return 'Concluído'


# Executa o servidor HTTP se estiver no modo de desenvolvimento
# Remova / comente essas linhas no modo de produção
if __name__ == '__main__':
    app.run(debug=True)
