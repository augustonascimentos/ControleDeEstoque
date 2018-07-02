import Conexao
import os
from time import sleep
import sys
# from prettytable import PrettyTable
from prettytable import from_db_cursor


# FUNÇÕES
def layout():
    print("|=====================================|\n"
          "|       CONTROLE DE ESTOQUE           |\n"
          "|=====================================|")


def logo():
    print("|=====================================|\n"
          "|  BEM VINDO AO CONTROLE DE ESTOQUE   |\n"
          "|=====================================|")


def construcao():
    for cont in range(3, 0, -1):
        print(cont)
        sleep(0.5)
    print("|=====================================|\n"
          "|                                     |\n"
          "|      DESCULPA O TRANSTORNO          |\n"
          "|      ESTAMOS EM CONSTRUÇÃO          |\n"
          "|                                     |\n"
          "|=====================================|")
    return func_menu_principal()


# FUNÇÃO DE PAUSE NO SISTEMA
def pause():
    os.system('pause')


# FUNÇÃO LIMPA TELA


def limpa_tela():

    os.system('cls' if os.name == 'nt' else 'clear')


# FUNÇÃO PARA SAIR DO SOFTWARE


def func_sair():
    limpa_tela()
    print("ENCERRANDO EM...")
    for cont in range(3, 0, -1):
        print(cont)
        sleep(0.5)
    print("|=====================================|\n"
          "|      FINALIZADO COM SUCESSO         |\n"
          "|=====================================|")
    sys.exit(0)


# FUNÇÃO MENU PRINCIPAL #


def func_menu_principal():
    logo()
    menu1 = str(input("\n 1) Cadastrar Equipamento "
                      "\n 2) Cadastrar Usuário "
                      "\n 3) Inventário "
                      "\n 4) Histórico "
                      "\n 5) Sair \n"))
    print("==" * 18)
    if menu1 == '1':
        limpa_tela()
        func_menu_cadastra_equipamento()

    if menu1 == '2':
        limpa_tela()
        func_menu_cadastra_usuario()

    if menu1 == '3':
        limpa_tela()
        inventario()

    if menu1 == '4':
        limpa_tela()
        construcao()

    if menu1 == '5':

        func_sair()


# 1 - FUNÇÃO CADASTRAR EQUIPAMENTO 1


def func_menu_cadastra_equipamento():
    layout()
    menu1 = str(input("\n 1) Novo Equipamento"
                      "\n 2) Alterar Equipamento"
                      "\n 3) Remover Equipamento"
                      "\n 4) Retornar \n"))
    print("==" * 18)
    if menu1 == '1':
        limpa_tela()
        func_novo_equipamento()

    if menu1 == '2':
        limpa_tela()
        alter_equip()

    if menu1 == '3':
        limpa_tela()
        construcao()

    if menu1 == '4':
        limpa_tela()
        return func_menu_principal()


# 1.1 - FUNÇÃO NOVO EQUIPAMENTO 1.1


def func_novo_equipamento():
    func_cadastro_tag()
    func_cadastro_host()
    func_cadastro_modelo()
    func_cadastro_proc()
    func_cadastro_comp()
    func_cadastro_so()
    func_cadastro_ram()
    print("|=====================================|\n"
          "| COMPUTADOR CADASTRADO COM SUCESSO!  |\n"
          "|=====================================|")
    pause()
    limpa_tela()
    func_menu_principal()


# #1.1AA - (FUNÇÕES DE VERIFICAÇÃO DA func_cadastro_tag)


def func_consulta_tag():
    c = Conexao.cnx
    cursor = c.cursor()
    cursor.execute("SELECT TAG FROM pc")
    resultado = [line[0] for line in cursor]
    # cursor.close()
    # c.close()
    return resultado

# #1.1BB - (FUNÇÕES DE VERIFICAÇÃO DA Func_Cadastro_Host)


def func_consulta_host():
    c = Conexao.cnx
    cursor = c.cursor()
    cursor.execute("SELECT HOSTNAME FROM pc")
    resultado = [line[0] for line in cursor]
    return resultado

# 1.1A - FUNÇÃO CADASTRO DE TAG


def func_cadastro_tag():
    while True:

        # SOLICITA QUE O USUÁRIO DIGITE A TAG DO NOVO EQUIPAMENTO.
        print("==" * 18)
        tag = str(input("Digite a TAG do equipamento: ")).strip().upper()
        limpa_tela()

        # VERIFICA SE O USUÁRIO DIGITOU A TAG VAZIA OU NÃO DIGITOU NADA E PRESSIONOU ENTER.
        if tag == '':
            print("==" * 18)
            print("Por favor digite a TAG do equipamento")

        # VERIFICA SE A TAG DIGITADA JÁ EXISTE NO BANCO DE DADOS.
        elif tag in func_consulta_tag():
            print("==" * 18)
            print("A TAG {} já existe, tente novamente!".format(tag))

        # VERIFICA SE A TAG DIGITADA CONTÉM OBRIGATORIAMENTE 8 CARACTERES.
        elif len(tag) < 7 or len(tag) > 7:
            print("==" * 18)
            print("A TAG {} é invalida".format(tag))

        # VERIFICA SE A TAG DIGITADA CONTÉM APENAS LETRAS OU APENAS NÚMEROS.
        elif tag.isalpha() or tag.isdigit():
            print("==" * 18)
            print("A TAG {} é invalida".format(tag))

        # VERIFICA SE A TAG DIGITADA POSSUI ESPAÇOS.
        elif ' ' in tag:
            print("==" * 18)
            print("A TAG {} é invalida".format(tag))

        # CASO A TAG DIGITADA PELO O USUÁRIO NÃO SE ENCAIXE EM NENHUMA CONDIÇÃO ACIMA,
        # ELA SERÁ CADASTRADA NO BANCO DE DADOS.
        else:
            c = Conexao.cnx
            cursor = c.cursor()
            cursor.execute("INSERT INTO pc (TAG) VALUES (%s)", (tag,))
            cursor.fetchone()
            c.commit()
            # cursor.close()
            # c.close()
            print("==" * 18)
            print("A TAG {} foi cadastrada com sucesso!".format(tag))
            break

# 1.1B - FUNÇÃO CADASTRO DE HOSTNAME


def func_cadastro_host():
    while True:

        # SOLICITA QUE O USUÁRIO DIGITE O HOSTNAME DO NOVO EQUIPAMENTO.
        print("==" * 18)
        host = str(input("Digite o HOSTNAME do equipamento: ")).strip().upper()
        limpa_tela()

        # VERIFICA SE O USUÁRIO DIGITOU O HOSTNAME VAZIO OU NÃO DIGITOU NADA E PRESSIONOU ENTER.
        if host == '':
            print("==" * 18)
            print("Por favor digite o HOSTNAME do equipamento")

        # VERIFICA SE O HOSTNAME DIGITADO JÁ EXISTE NO BANCO DE DADOS.
        elif host in func_consulta_host():
            print("==" * 18)
            print("O HOSTNAME {} já existe, tente novamente!".format(host))

        # VERIFICA SE O HOSTNAME DIGITADO CONTÉM APENAS NÚMEROS.
        elif host.isdigit():
            print("==" * 18)
            print("O HOSTNAME {} é invalido".format(host))

        # VERIFICA SE A TAG DIGITADA POSSUI ESPAÇOS.
        elif ' ' in host:
            print("==" * 18)
            print("O HOSTNAME {} é invalido".format(host))

        # CASO A TAG DIGITADA PELO O USUÁRIO NÃO SE ENCAIXE EM NENHUMA CONDIÇÃO ACIMA,
        # ELA SERÁ CADASTRADA NO BANCO DE DADOS.
        else:
            c = Conexao.cnx
            cursor = c.cursor()
            cursor.getlastrowid()
            cursor.execute("UPDATE pc SET HOSTNAME = %s WHERE ID ORDER BY ID DESC LIMIT 1", (host,))
            c.commit()
            # cursor.close()
            # c.close()
            print("==" * 18)
            print("O HOSTNAME {} foi cadastrado com sucesso!".format(host))
            break

# 1.1C - FUNÇÃO CADASTRO DO MODELO DO EQUIPAMENTO


def func_cadastro_modelo():
    while True:
        print("==" * 18)
        mod = str(input("Digite o MODELO do equipamento: ")).strip().upper()
        limpa_tela()

        # VERIFICA SE O USUÁRIO DIGITOU O MODELO VAZIO OU NÃO DIGITOU NADA E PRESSIONOU ENTER.
        if mod == '':
            print("==" * 18)
            print("Por favor digite um MODELO para o equipamento")

        else:
            c = Conexao.cnx
            cursor = c.cursor()
            cursor.getlastrowid()
            cursor.execute("UPDATE pc SET MODELO = %s WHERE ID ORDER BY ID DESC LIMIT 1", (mod,))
            c.commit()
            print("==" * 18)
            print("O MODELO {} foi cadastrado com sucesso!".format(mod))
            break

# 1.1D - FUNÇÃO PARA CADASTRO DO MODELO DO PROCESSADOR


def func_cadastro_proc():
    while True:
        print("==" * 18)
        proc = str(input("Escola o modelo do PROCESSADOR: \n 1) [i5] \n 2) [i7] \n"))
        limpa_tela()

        if proc != '1' and proc != '2':
            print("==" * 18)
            print("Por favor escolha uma opção válida.")

        else:
            if proc == '1':
                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET PROCESSADOR = 'I5' WHERE ID ORDER BY ID DESC LIMIT 1")
                c.commit()
                print("==" * 18)
                print("PROCESSADOR cadastrado com sucesso.")
                break

            else:
                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET PROCESSADOR = 'I7' WHERE ID ORDER BY ID DESC LIMIT 1")
                c.commit()
                print("==" * 18)
                print("PROCESSADOR cadastrado com sucesso.")
                break

# 1.1E - FUNÇÃO PARA CADASTRO DO TIPO DE DESKTOP(NOTEBOOK/DESKTOP)


def func_cadastro_comp():
    while True:
        print("==" * 18)
        comp = str(input("Escolha o modelo do COMPUTADOR: \n 1) [DESKTOP] \n 2) [NOTEBOOK] \n"))
        limpa_tela()

        if comp != '1' and comp != '2':
            print("==" * 18)
            print("Por favor escolha uma opção válida.")

        else:
            if comp == '1':
                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET TIPO = 'DESKTOP' WHERE ID ORDER BY ID DESC LIMIT 1")
                c.commit()
                print("==" * 18)
                print("DESKTOP cadastrado com sucesso.")
                break

            else:
                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET TIPO = 'NOTEBOOK' WHERE ID ORDER BY ID DESC LIMIT 1")
                c.commit()
                print("==" * 18)
                print("NOTEBOOK cadastrado com sucesso.")
                break

# 1.1F - FUNÇÃO PARA CADASTRO DO TIPO DE SISTEMA OPERACIONAL


def func_cadastro_so():
    while True:
        print("==" * 18)
        so = str(input("Escolha o Sistema Operacional do COMPUTADOR: \n 1) [WINDOWS] \n 2) [LINUX] \n 3) [IOS] \n"))
        limpa_tela()

        if so != '1' and so != '2' and so != '3':
            print("==" * 18)
            print("Por favor escolha uma opção válida.")

        else:
            if so == '1':
                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET ID_SO = '1' WHERE ID ORDER BY ID DESC LIMIT 1")
                c.commit()
                print("==" * 18)
                print("O sistema operacional WINDOWS foi cadastrado com sucesso")
                break

            if so == '2':
                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET ID_SO = '2' WHERE ID ORDER BY ID DESC LIMIT 1")
                c.commit()
                print("==" * 18)
                print("O sistema operacional LINUX foi cadastrado com sucesso")
                break

            if so == '3':
                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET ID_SO = '3' WHERE ID ORDER BY ID DESC LIMIT 1")
                c.commit()
                print("==" * 18)
                print("O sistema operacional IOS foi cadastrado com sucesso")
                break

# 1.1G - FUNÇÃO PARA CADASTRO DA QUANTIDADE DE MEMÓRIA DO COMPUTADOR


def func_cadastro_ram():
    while True:
        print("==" * 18)
        ram = str(input("Qual a quantidade de memória do computador? \n 1) [8 GB] \n 2) [16 GB] \n"))
        limpa_tela()

        if ram != '1' and ram != '2':  # and ram != '3':
            print("==" * 18)
            print("Por favor escolha uma opção válida.")

        else:
            if ram == '1':
                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET ID_RAM = '1' WHERE ID ORDER BY ID DESC LIMIT 1")
                c.commit()
                break

            if ram == '2':
                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET ID_RAM = '2' WHERE ID ORDER BY ID DESC LIMIT 1")
                c.commit()
                break

            """if ram == '3':
                print("==" * 18)
                ram3 = str(input("Digite a quantidade de memória do computador: \n"))
                limpa_tela()

                c = Conexao.cnx
                cursor = c.cursor()
                cursor.getlastrowid()
                cursor.execute("UPDATE pc SET ID_RAM = (%s) WHERE ID ORDER BY ID DESC LIMIT 1",(ram3,))
                c.commit()
                print("==" * 18)
                print("Memória RAM cadastrada com sucesso.")
                break"""

# 1.2 - FUNÇÃO PARA ALTERAR EQUIPAMENTO CADASTRADO


def alter_equip():
    while True:
        # SOLICITA QUE O USUÁRIO DIGITE A TAG DO NOVO EQUIPAMENTO.
        print("==" * 18)
        altag = str(input("Digite a TAG que deseja alterar: \n"))
        limpa_tela()

        # VERIFICA SE O USUÁRIO DIGITOU A TAG VAZIA OU NÃO DIGITOU NADA E PRESSIONOU ENTER.
        if altag == '':
            print("==" * 18)
            print("Por favor digite a TAG do equipamento")

        # VERIFICA SE A TAG DIGITADA CONTÉM OBRIGATORIAMENTE 7 CARACTERES.
        elif len(altag) < 7 or len(altag) > 7:
            print("==" * 18)
            print("A TAG {} é invalida".format(altag))

        # VERIFICA SE A TAG DIGITADA CONTÉM APENAS LETRAS OU APENAS NÚMEROS.
        elif altag.isalpha() or altag.isdigit():
            print("==" * 18)
            print("A TAG {} é invalida".format(altag))

        # VERIFICA SE A TAG DIGITADA POSSUI ESPAÇOS.
        elif ' ' in altag:
            print("==" * 18)
            print("A TAG {} é invalida".format(altag))

        elif altag in func_consulta_tag():
            c = Conexao.cnx
            cursor = c.cursor()
            cursor.execute("SELECT * FROM pc WHERE TAG = %s", (altag,))
            resultado = from_db_cursor(cursor)
            print(resultado)

            alterar = str(input("O que você deseja alterar ?\n"
                            "\n"
                            "1) TAG\n"
                            "2) HOSTNAME\n"
                            "3) MODELO\n"
                            "4) PROCESSADOR\n"
                            "5) TIPO DE COMPUTADOR\n"
                            "6) SISTEMA OPERACIONAL\n"
                            "7) MEMÓRIA RAM\n"))

            if alterar != '1' and alterar != '2' and alterar != '3' and alterar != '4' and alterar != '5' \
                    and alterar != '6' and alterar != '7':
                print("==" * 18)
                print("Por favor escolha uma opção válida.")

            else:
                if alterar == '1':
                    while True:             
                        # SOLICITA QUE O USUÁRIO DIGITE A TAG DO NOVO EQUIPAMENTO.
                        print("==" * 18)
                        tag = str(input("Digite a nova TAG do equipamento:\n")).strip().upper()
                        limpa_tela()

                        # VERIFICA SE O USUÁRIO DIGITOU A TAG VAZIA OU NÃO DIGITOU NADA E PRESSIONOU ENTER.
                        if tag == '':
                            print("==" * 18)
                            print("Por favor digite a TAG do equipamento")

                        # VERIFICA SE A TAG DIGITADA JÁ EXISTE NO BANCO DE DADOS.
                        elif tag in func_consulta_tag():
                            print("==" * 18)
                            print("A TAG {} já existe, tente novamente!".format(tag))

                        # VERIFICA SE A TAG DIGITADA CONTÉM OBRIGATORIAMENTE 8 CARACTERES.
                        elif len(tag) < 7 or len(tag) > 7:
                            print("==" * 18)
                            print("A TAG {} é invalida".format(tag))

                        # VERIFICA SE A TAG DIGITADA CONTÉM APENAS LETRAS OU APENAS NÚMEROS.
                        elif tag.isalpha() or tag.isdigit():
                            print("==" * 18)
                            print("A TAG {} é invalida".format(tag))

                        # VERIFICA SE A TAG DIGITADA POSSUI ESPAÇOS.
                        elif ' ' in tag:
                            print("==" * 18)
                            print("A TAG {} é invalida".format(tag))

                        # CASO A TAG DIGITADA PELO O USUÁRIO NÃO SE ENCAIXE EM NENHUMA CONDIÇÃO ACIMA,
                        # ELA SERÁ CADASTRADA NO BANCO DE DADOS.
                        else:
                            c = Conexao.cnx
                            cursor = c.cursor()
                            cursor.execute("UPDATE pc SET TAG = %s WHERE TAG = %s", (tag,altag,))
                            cursor.fetchone()
                            c.commit()
                            print("==" * 18)
                            print("A nova TAG {} foi cadastrada com sucesso!".format(tag))
                            break


# 1.3 - FUNÇÃO PARA REMOVER EQUIPAMENTO CADASTRADO


def func_remover_equip():
    construcao()


# 2 - FUNÇÃO CADASTRO DE USUÁRIO - 2


def func_menu_cadastra_usuario():
    layout()
    menu1 = str(input("\n 1) Novo Usuário"
                      "\n 2) Alterar Usuário"
                      "\n 3) Remover Usuário"
                      "\n 4) Retornar \n"))
    print("==" * 18)
    if menu1 == '1':
        limpa_tela()
        construcao()

    if menu1 == '2':
        limpa_tela()
        construcao()

    if menu1 == '3':
        limpa_tela()
        construcao()

    if menu1 == '4':
        limpa_tela()

        return func_menu_principal()


# 3 - MOSTRAR TODOS OS EQUIPAMENTOS CADASTRADOS


def inventario():
    c = Conexao.cnx
    cursor = c.cursor()
    cursor.execute("SELECT * FROM pc")
    resultado = from_db_cursor(cursor)
    print(resultado)
    pause()
    limpa_tela()
    return func_menu_principal()


# CHAMADA DO MENU PRINCIPAL #

limpa_tela()
func_menu_principal()
