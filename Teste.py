import mysql.connector
import subprocess
import sys
import os
from prettytable import PrettyTable
from prettytable import from_db_cursor

cnx = mysql.connector.connect(user='root', password='', database='controle_hardware',)


'''c = cnx
cursor = c.cursor()
cursor.execute("SELECT TAG FROM pc")'''
#resultado = [line[1] for line in cursor]
#print(resultado)
#results = cursor.fetchone()
'''tag = results[1]
hostname = results[2]
modelo = results[3]
processador = results[4]
tipo = results[5]
so = results[6]
ram = results[7]'''

#results2 = cursor.fetchone()
#print(results2)


'''kkkk = results2[2]
asw = kkkk[2]
print(asw)'''

#print(results)
#print(results2)
'''if so == 1:
    a = 'WINDOWS'
if ram == 1:
    b = '8 GB'''


#x = PrettyTable()
#x.field_names = ["SERVICE TAG", "HOSTNAME", "MODELO DO COMPUTADOR", "PROCESSADOR", "TIPO DE COMPUTADOR", "SISTEMA OPERACIONAL", "MEMÓRIA RAM"]
#x.add_row([tag, hostname, modelo, processador, tipo, a, b])
#resultado = from_db_cursor(cursor,padding_width=5)
#print(resultado,)


def consulta():

    c = cnx
    cursor = c.cursor()
    cursor.execute("SELECT TAG FROM pc")
    resultado = [line[0] for line in cursor]
    return resultado


a = str(input('digite: '))

if a in consulta():
    print('parabens vc ta no banco')
else:
    print('nao')
