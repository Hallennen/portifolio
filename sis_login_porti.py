from tkinter import *
from tkinter import ttk as tk
import os
import psycopg2


#app de validação de senha e usuario 

'''abrindo conexão com o BD  * * TIVE A NECESSIDADE DE FAZER A CONEXAO DE FORMA 
            MANUAL INVES DE CRIAR UMA FUNÇÃO'''
            
def conexao_banco():
    global cur
    global con

    con = psycopg2.connect(host='localhost', database='user', user='postgres',password='1804' )
    cur = con.cursor()   
    

            #//função para entrar 
def entrar():
    os.system('cls')
    try:
            # FAZ A BUSCA NO BANCO DE DADOS 
        conexao_banco()
        valida_usuario = """SELECT nome FROM registros WHERE senha = '{}'""".format(dig_senha.get())
        cur.execute(valida_usuario)         
        v_usuario = cur.fetchone()
        con.close()

            # PRINTA O QUE FOI DIGITADO PELO USUARIO
        print('usuario: '+dig_email.get())
        print('senha: '+dig_senha.get())
        # print(v_usuario[0])

            # VALIDA O USUARIO SE ESTÁ NO BANCO DE DADOS
        if str(dig_email.get().capitalize()) == str(v_usuario[0]):
            print('OK! Logado')
                
        else:
            print('Usuario/Senha invalido')

    except:
        print('usuario não encontrado')
        
        
            #//função para cadastrar
def cadastrar():
    try:
        con = psycopg2.connect(host='localhost', database='user', user='postgres',password='1804' )
        cur = con.cursor() 
        name_bd = """SELECT nome FROM registros WHERE nome = '{}'""".format(cadastro_nome.get().capitalize())
        cur.execute(name_bd)
        req = cur.fetchone()
        con.close()
        print(req)
        
            #VALIDA SE O DADO INSERIDO JÁ POSSUI CADASTRO NO BD
        if cadastro_nome.get().capitalize() in str(req):
            print('USUARIO JÁ CADASTRADO')
            ok = tk.Label(text='USUARIO JÁ CADASTRADO',foreground='red')
            ok.place(x=120, y=170)

            # CASO NÃO POSSUA CADASTRO SEGUE COM A INSERÇÃO NO BD
        else:
            con = psycopg2.connect(host='localhost', database='user', user='postgres',password='1804' )
            cur = con.cursor() 
            nome_novo_user = cadastro_nome.get().capitalize()
            email_novo_user = cadastro_email.get()
            senha_novo_user = cadastro_senha.get()

            inserção_usuario = """INSERT INTO registros (nome,email,senha)
                                        VALUES ('{}','{}','{}')""".format(nome_novo_user,email_novo_user,senha_novo_user)
            cur.execute(inserção_usuario)
            con.commit()
            con.close()
            tela_cad.destroy()
            print('CADASTRADO')
            ok = tk.Label(text='CADASTRO EFETUADO',foreground='green')
            ok.place(x=130, y=160)

    except:
       print('erro na sintaxe')

       
            #TELA TKINTER DE CADASTRO
def tela_cadastro():
    global tela_cad
    global cadastro_nome
    global cadastro_email
    global cadastro_senha
    tela_cad =Tk()
    tela_cad.title('CADASTRO')
    tela_cad.geometry('400x300+500+240')

    text1 = tk.Label(tela_cad, text='Cadastro',font=('',19))
    text1.place( y= 30, x= 150)

    text1 = tk.Label(tela_cad, text='Nome:', font=('arial',12))
    text1.place( y=90 , x=15)
    cadastro_nome = Entry(tela_cad)
    cadastro_nome.place(width=270 , height=25,y=90 , x=80)

    text2 = tk.Label(tela_cad, text='E-mail:',font=('arial',12))
    text2.place( y=140 , x=15)
    cadastro_email = Entry(tela_cad)
    cadastro_email.place(width=270 , height=25,y=140 , x=80)
    
    text3 = tk.Label(tela_cad, text='Senha:',font=('arial',12))
    text3.place( y=190 , x=15)
    cadastro_senha = Entry(tela_cad, show='*')
    cadastro_senha.place(width=270 , height=25,y=190 , x=80)

    button_cadastro = tk.Button(tela_cad, text=('CADASTRAR'),command= cadastrar)
    button_cadastro.place(y=240, x=160,)



        #APLICAÇÃO RODANDO NO TKINTER
tela = Tk()

tela.title('LOGIN')
tela.geometry('400x200+500+240')

txt_inicial = tk.Label(text='Login', font=('', 17))
txt_inicial.place(x= 180 , y= 15 )

email = tk.Label(text=('Email:'),class_=str(),font=('subline',15))
email.place(x=15 , y=60)
dig_email = Entry()
dig_email.place(width=270 , height=25, x=80 , y=63)


senha = tk.Label(text=('Senha:'),class_=str(),font=('subline',15))
senha.place(x=15 , y=95)
dig_senha = Entry(show='*')
dig_senha.place(width=270 , height=25, x=80 , y=95,)

login = tk.Button(text=('ENTRAR'), command= entrar)
login.place(x=100 , y=130, width=220 , height=25)

info =tk.Label(text='Não tem uma conta ? ->', foreground='red' )
info.place(x=80 , y=172 )

button_cadastro = tk.Button(text=('CADASTRAR'), command= tela_cadastro)
button_cadastro.place(x=260 , y=168)


tela.mainloop()

