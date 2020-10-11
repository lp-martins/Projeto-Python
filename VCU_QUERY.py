import sqlite3
from sqlite3 import Error
from tkinter import messagebox
import os

pastaAPP_VCU = os.path.dirname(__file__)
nameDB = pastaAPP_VCU+"\VCU_DB.db"

# Conexão com Banco de Dados
def ConexaoDB():
    try:
        conex = sqlite3.connect(nameDB)
    except Error as ex:
        messagebox.showwarning(title="VCU - Ocorreu um Erro!", message=ex)
    return conex

def DQL(query): #SELECT
    vcon = ConexaoDB()
    c = vcon.cursor()
    c.execute(query)
    resposta = c.fetchall()
    vcon.close()
    return resposta

def DML(query): # INSERT, UPDATE, DELETE
    try:
        vcon = ConexaoDB()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        messagebox.showwarning(title="VCU - Ocorreu um Erro!", message=ex)
