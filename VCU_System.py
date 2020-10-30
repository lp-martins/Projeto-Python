from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import VCU_QUERY

#   propriedades da janela  #
appVCU = Tk()
appVCU.title(" - Venda de Carros Usados®")
appVCU.geometry("1400x860")
appVCU.resizable(False, False)
appVCU.configure(background="#ddf")
appVCU.wm_iconbitmap('icon_VCU.ico')

def salvardadosPRO():
    Ssql = "SELECT CPF FROM PROPRIETARIOS"
    CPFs = str(VCU_QUERY.DQL(Ssql))
    if vCPF.get() in CPFs and vCPF.get() != "":
        messagebox.showwarning(title="VCU - CPF já Cadastrado!", message="Este CPF já está cadastrado em nossa base de dados!")
    elif (vNome.get() != "") and (vCPF.get() != "") and (vEndereco.get() != "") and (vTelefone != "") and (vHabilita.get() != ""):
        sNome = vNome.get()
        sCPF = vCPF.get()
        sEndereco = vEndereco.get()
        sTelefone = vTelefone.get()
        sHabilita = vHabilita.get()
        squery = "INSERT INTO PROPRIETARIOS(Nome, CPF, Endereço, Telefone, Habilitação) VALUES ('"+sNome+"', '"+sCPF+"', '"+sEndereco+"', '" +sTelefone+"', '"+sHabilita+"')"
        VCU_QUERY.DML(squery)
        messagebox.showinfo(title="VCU - Vendas de Carros Usados", message="Dados cadastrados com sucesso!")
    else:
        messagebox.showwarning(title="VCU - Campos Vazios!", message="Por favor, preencha todos os campos para realizar o cadastro!")

def salvardadosVE():
    sModelo = vModelo.get()
    sMarca = vMarca.get()
    sCor = vCor.get()
    sAno = vAno.get()
    sCombust = vCombust.get()
    sProp = vProprietario.get()
    sPagamento = vPagamento.get()
    sRenavam = vRenav.get()
    sPlaca = vPlaca.get()
    sFinanceiro = vFinanceiro.get()
    sFipe = vFipe.get()
    sValorPRO = vPrecoPro.get()
    sAcessorio = vAcessorios.get()
    sStatus = vStatus.get()
    Squery = "SELECT Nome FROM PROPRIETARIOS"
    PropList = VCU_QUERY.DQL(Squery)

    if (vModelo.get() == "") or (vMarca.get() == "") or (vCor.get() == "") or (vAno.get() == "") or (vCombust.get() == "") or (vProprietario.get() == "") or (vPagamento.get() == "") or (vRenav.get() == "") or (vPlaca.get() == "") or (vFinanceiro.get() == "") or (vFipe.get() == "") or (vPrecoPro.get() == "") or (vAcessorios.get() == "") or (vStatus.get() == ""):
        messagebox.showwarning(title="VCU - Campos Vazios!", message="Por favor, preencha todos os campos para realizar o cadastro!")
    elif vProprietario.get() in str(PropList):
        squery = "INSERT INTO VEICULOS(Modelo, Marca, Cor, Ano_de_Lançamento, Combustivel, Proprietario, Formas_de_Pagamento, Renavam, Placa, Situação_Financeira, Valor_FIPE, Valor_Proprietario, Acessorios, Status) VALUES ('"+sModelo+"', '"+sMarca+"', '"+sCor+"', '"+sAno+"', '"+sCombust+"', '"+sProp+"', '"+sPagamento+"', '"+sRenavam+"', '"+sPlaca+"', '"+sFinanceiro+"', '"+sFipe+"', '"+sValorPRO+"', '"+sAcessorio+"', '"+sStatus+"')"
        VCU_QUERY.DML(squery)
        messagebox.showinfo(title="VCU - Vendas de Carros Usados", message="Dados do Veículo Salvo com Sucesso!")
        vModelo.delete(0, END)
        vMarca.delete(0, END)
        vRenav.delete(0, END)
        vPlaca.delete(0, END)
        vCor.delete(0, END)
        vFinanceiro.delete(0, END)
        vAno.delete(0, END)
        vFipe.delete(0, END)
        vCombust.set("")
        vPrecoPro.delete(0, END)
        vProprietario.set("")
        vAcessorios.delete(0, END)
        vPagamento.delete(0, END)
        vStatus.set("")
    else:
        messagebox.showwarning(title="VCU - Proprietário Não Cadastrado!", message="Este proprietário não está cadastrado! Verifique o nome e tente novamente!")

def novocadastro():
    vNome.delete(0, END)
    vCPF.delete(0, END)
    vEndereco.delete(0, END)
    vTelefone.delete(0, END)
    vHabilita.delete(0, END)

# ABA Consultar Proprietário
def ListarProprietarios():
    tv1.delete(*tv1.get_children())
    vquery="SELECT Nome, CPF, Endereço, Telefone, Habilitação FROM PROPRIETARIOS"
    linhas = VCU_QUERY.DQL(vquery)
    for x in linhas:
        tv1.insert("", "end", values=x)

# ABA Consultar Proprietário
def PesquisarNOME():
    tv1.delete(*tv1.get_children())
    if nomePesq4.get() != "":
        vquery = "SELECT Nome, CPF, Endereço, Telefone, Habilitação FROM PROPRIETARIOS WHERE NOME LIKE '%"+nomePesq4.get()+"%'"
        linhas = VCU_QUERY.DQL(vquery)
        nomePesq4.delete(0, END)
        if linhas != []:
            for x in linhas:
                tv1.insert("", "end", values=x)
        else:
            messagebox.showinfo(title="VCU: Atenção!", message="Não encontramos Proprietários com esse Nome!")
    else:
        messagebox.showinfo(title="VCU: Atenção!", message="Nenhuma informação digitada!")

# ABA Consultar Proprietário
def PesquisarCPF():
    tv1.delete(*tv1.get_children())
    if nomePesq6.get() != "":
        vquery = "SELECT Nome, CPF, Endereço, Telefone, Habilitação FROM PROPRIETARIOS WHERE CPF LIKE '%"+nomePesq6.get()+"%'"
        linhas = VCU_QUERY.DQL(vquery)
        nomePesq6.delete(0, END)
        if linhas != []:
            for x in linhas:
                tv1.insert("", "end", values=x)
        else:
            messagebox.showinfo(title="VCU: Atenção!", message="Não encontramos Proprietários com este CPF!")
    else:
        messagebox.showinfo(title="VCU: Atenção!", message="Nenhuma informação digitada!")

# ABA Consultar Veículo
def ListarVeiculos():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM VEICULOS order by Modelo"
    linhas = VCU_QUERY.DQL(vquery)
    for x in linhas:
        tv.insert("", "end", values=x)

# ABA Consultar Veículo
def PesquisarMODE():
    tv.delete(*tv.get_children())
    if nomePesq.get() != "":
        vquery = "SELECT * FROM VEICULOS WHERE Modelo LIKE '%"+nomePesq.get()+"%'"
        linhas = VCU_QUERY.DQL(vquery)
        nomePesq.delete(0, END)
        if linhas != []:
            for x in linhas:
                tv.insert("", "end", values=x)
        else:
            messagebox.showinfo(title="VCU: Atenção!", message="Não encontramos veículos com esse Modelo!")
    else:
        messagebox.showinfo(title="VCU: Atenção!", message="Nenhuma informação digitada!")

# ABA Consultar Veículo
def PesquisarPROP():
    tv.delete(*tv.get_children())
    if nomePesq1.get() != "":
        vquery = "SELECT * FROM VEICULOS WHERE Proprietario LIKE '%"+nomePesq1.get()+"%'"
        linhas = VCU_QUERY.DQL(vquery)
        nomePesq1.delete(0, END)
        if linhas != []:
            for x in linhas:
                tv.insert("", "end", values=x)
        else:
            messagebox.showinfo(title="VCU: Atenção!", message="Não encontramos veículos com esse Proprietário!")
    else:
        messagebox.showinfo(title="VCU: Atenção!", message="Nenhuma informação digitada!")

# ABA Consultar Veículo
def PesquisarPLAC():
    tv.delete(*tv.get_children())
    if nomePesq2.get() != "":
        vquery = "SELECT * FROM VEICULOS WHERE Placa LIKE '%"+nomePesq2.get()+"%'"
        linhas = VCU_QUERY.DQL(vquery)
        nomePesq2.delete(0, END)
        if linhas != []:
            for x in linhas:
                tv.insert("", "end", values=x)
        else:
            messagebox.showinfo(title="VCU: Atenção!", message="Não encontramos veículos com essa Placa!")
    else:
        messagebox.showinfo(title="VCU: Atenção!", message="Nenhuma informação digitada!")

# ABA Consultar Veículo
def PesquisarSTAT():
    tv.delete(*tv.get_children())
    if txtBuscStt.get() != "":
        Status = txtBuscStt.get()
        vquery = "SELECT * FROM VEICULOS WHERE Status ='"+Status+"'"
        linhas = VCU_QUERY.DQL(vquery)
        if linhas != []:
            for x in linhas:
                tv.insert("", "end", values=x)
        else:
            messagebox.showinfo(title="VCU: Atenção!", message="Não encontramos veículos com esse Status!")
    else:
        messagebox.showinfo(title="VCU: Atenção!", message="Nenhuma Opção escolhida!")

# Mini Botão na ABA de cadastrar Veículos, para atualizar a lista de proprietários
#def AtuaListPRO():
    squery = "SELECT Nome FROM PROPRIETARIOS"
    ListaPRO = (VCU_QUERY.DQL(squery))
    vProprietario.set(ListaPRO)
    return (ListaPRO)

def DeletarPRO():
    try:
        cquery = "SELECT Proprietario FROM VEICULOS"
        PropricomVE = VCU_QUERY.DQL(cquery)
        ItemSelect = tv1.selection()[0]
        Valores = tv1.item(ItemSelect, "values")
        ValorSelect = Valores[0]
        if ValorSelect not in str(PropricomVE):
            MsgResult = messagebox.askyesno(title="VCU - Atenção!!!", message="Deseja mesmo exluir o Proprietário selecionado?")
            if MsgResult == True:
                dquery = "DELETE FROM PROPRIETARIOS WHERE Nome ='" + ValorSelect + "'"
                tv1.delete(ItemSelect)
                VCU_QUERY.DML(dquery)
        else:
            messagebox.showwarning(title="VCU - Atenção!!!", message="Não é possivel excluir um proprietário que tenha veículos disponíveis!")
    except:
        messagebox.showinfo(title="VCU - Atenção", message="Nenhum item selecionado!")

def AtualizarPRO():
    def UpdatePRO():
        if (AtNome.get() != "") and (AtCPF.get() != "") and (AtEndereco.get() != "") and (AtTelefone.get() != "") and (AtHabilita.get() != ""):
            UpNome = AtNome.get()
            UpCPF = AtCPF.get()
            UpEndereco = AtEndereco.get()
            UpTelefone = AtTelefone.get()
            UpHabilita = AtHabilita.get()
            Upquery = "UPDATE PROPRIETARIOS SET Nome='" + UpNome + "', CPF='" + UpCPF + "', Endereço='" + UpEndereco + "', Telefone='" + UpTelefone + "', Habilitação='" + UpHabilita + "' WHERE CPF = '" + UpCPF + "'"
            QUERYup = "UPDATE VEICULOS SET Proprietario='"+AtNome.get()+"' WHERE Proprietario='"+NomePRO+"'"
            VCU_QUERY.DML(Upquery)
            VCU_QUERY.DML(QUERYup)
            messagebox.showinfo(title="VCU - Vendas de Carros Usados", message="Dados Atualizados com sucesso!")
        else:
            messagebox.showwarning(title="VCU - Campos Vazios!", message="Por favor, preencha todos os campos para realizar o cadastro!")
    try:
        ItemSelectPRO = tv1.selection()[0]
        valoresPRO = tv1.item(ItemSelectPRO, "values")
        NomePRO = valoresPRO[0]
        CPFpro = valoresPRO[1]
        EnderecoPRO = valoresPRO[2]
        TelefonePRO = valoresPRO[3]
        HabilitaPRO = valoresPRO[4]

        AppATTpro = Tk()
        AppATTpro.title("VCU - Atualizando dados do Proprietário")
        AppATTpro.geometry("900x800")
        AppATTpro.resizable(False, False)
        AppATTpro.configure(background="#fd0")
        AppATTpro.focus_force()
        AppATTpro.grab_set()

        ABAatt = ttk.Notebook(AppATTpro)
        ABAatt.place(x=10, y=10, width=880, height=780)

        FrameAttPro = LabelFrame(ABAatt, text="Dados Pessoais do Proprietário", font="Arial 12 italic", borderwidth='1', relief="solid")
        FrameAttPro.configure(background="#e6e6e6")
        FrameAttPro.place(x=0, y=0, width=880, height=780)

        Label(FrameAttPro, text="Nome Completo: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=280, y=148)
        AtNome = ttk.Entry(FrameAttPro)
        AtNome.configure(font="Arial 14")
        AtNome.place(x=280, y=170, width=310, height=30)
        AtNome.insert(0, NomePRO)

        Label(FrameAttPro, text="CPF: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=280, y=218)
        AtCPF = Entry(FrameAttPro)
        AtCPF.configure(font="Arial 14")
        AtCPF.place(x=280, y=240, width=310, height=30)
        AtCPF.insert(0, CPFpro)

        Label(FrameAttPro, text="Endereço: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=280, y=288)
        AtEndereco = Entry(FrameAttPro)
        AtEndereco.configure(font="Arial 14")
        AtEndereco.place(x=280, y=310, width=310, height=30)
        AtEndereco.insert(0, EnderecoPRO)

        Label(FrameAttPro, text="Telefone para Contato: ", background="#e6e6e6", foreground="#009", font="Arial 12").place( x=280, y=358)
        AtTelefone = Entry(FrameAttPro)
        AtTelefone.configure(font="Arial 14")
        AtTelefone.place(x=280, y=380, width=310, height=30)
        AtTelefone.insert(0, TelefonePRO)

        Label(FrameAttPro, text="Habilitação: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=280, y=428)
        AtHabilita = Entry(FrameAttPro)
        AtHabilita.configure(font="Arial 14")
        AtHabilita.place(x=280, y=450, width=310, height=30)
        AtHabilita.insert(0, HabilitaPRO)

        btnSalvarAttPRO = Button(FrameAttPro, text="Salvar Alterações", background="#fd0", foreground="#000", font="ArialBlk 12 bold", command=UpdatePRO)
        btnSalvarAttPRO.place(x=350, y=500, width=180, height=30)

        AppATTpro.mainloop()
    except:
        messagebox.showinfo(title="VCU - Atenção", message="Nenhum item selecionado!")

def DeletarVE():
    try:
        ItemSelect = tv.selection()[0]
        Valores = tv.item(ItemSelect, "values")
        ValorSelect = Valores[8]
        MsgResult = messagebox.askyesno(title="VCU - Atenção!!!", message="Deseja mesmo exluir o Veículo selecionado?")
        if MsgResult == True:
            dquery = "DELETE FROM VEICULOS WHERE Placa ='" + ValorSelect + "'"
            tv.delete(ItemSelect)
            VCU_QUERY.DML(dquery)
    except:
        messagebox.showinfo(title="VCU - Atenção", message="Nenhum item selecionado!")

def AtualizarVE():
    def UpdateVE():
        if (atModeloV.get() != "") and (atMarcaV.get() != "") and (atCorV.get() != "") and (atAnoV.get() != "") and (atCombustV.get() != "") and (atProprietarioV.get() != "") and (atPagamentoV.get() != "") and (atRenavV.get() != "") and (atPlacaV.get() != "") and (atFinanceiroV.get() != "") and (atFipeV.get() != "") and (atPrecoProV.get() != "") and (atAcessoriosV.get() != "") and (atStatusV.get() != ""):
            UpModelo = atModeloV.get()
            UpMarca = atMarcaV.get()
            UpCor = atCorV.get()
            UpAnoLanc = atAnoV.get()
            UpCombust = atCombustV.get()
            UpProprieta = atProprietarioV.get()
            UpFormPag = atPagamentoV.get()
            UpRenavam = atRenavV.get()
            UpPlaca = atPlacaV.get()
            UpSituaFin = atFinanceiroV.get()
            UpValorFip = atFipeV.get()
            UpValorPRO = atPrecoProV.get()
            UpAcessorio = atAcessoriosV.get()
            UpStatus = atStatusV.get()

            Upquery = "UPDATE VEICULOS SET Modelo='"+UpModelo+"', Marca='"+UpMarca+"', Cor='"+UpCor+"', Ano_de_Lançamento='"+UpAnoLanc+"', Combustivel='"+UpCombust+"', Proprietario='"+UpProprieta+"', Formas_de_Pagamento='"+UpFormPag+"', Renavam='"+UpRenavam+"', Placa='"+UpPlaca+"', Situação_Financeira='"+UpSituaFin+"', Valor_FIPE='"+UpValorFip+"', Valor_Proprietario='"+UpValorPRO+"', Acessorios='"+UpAcessorio+"', Status='"+UpStatus+"' WHERE Placa = '" + UpPlaca + "'"
            VCU_QUERY.DML(Upquery)
            messagebox.showinfo(title="VCU - Vendas de Carros Usados", message="Dados Atualizados com sucesso!")
        else:
            messagebox.showwarning(title="VCU - Campos Vazios!",
                                   message="Por favor, preencha todos os campos para realizar o cadastro!")

    try:
        ItemSelectVE = tv.selection()[0]
        ValoresVE = tv.item(ItemSelectVE, "values")
        ModeloVE = ValoresVE[0]
        MarcaVE = ValoresVE[1]
        CorVE = ValoresVE[2]
        AnoLancVE = ValoresVE[3]
        CombustVE = ValoresVE[4]
        ProprietaVE = ValoresVE[5]
        FormPagVE = ValoresVE[6]
        RenavVE = ValoresVE[7]
        PlaacaVE = ValoresVE[8]
        SituaFinVE = ValoresVE[9]
        ValorFipVE = ValoresVE[10]
        ValorPropVE = ValoresVE[11]
        AcessoVE = ValoresVE[12]
        StatussVE = ValoresVE[13]

        AppATTve = Tk()
        AppATTve.title("VCU - Atualizando dados do Veículo")
        AppATTve.geometry("900x800")
        AppATTve.resizable(False, False)
        AppATTve.configure(background="#fd0")
        AppATTve.focus_force()
        AppATTve.grab_set()

        ABAattVE = ttk.Notebook(AppATTve)
        ABAattVE.place(x=10, y=10, width=880, height=780)

        FrameAttVE = LabelFrame(ABAattVE, text="Dados do Veículo", font="Arial 12 italic", borderwidth='1', relief="solid")
        FrameAttVE.configure(background="#e6e6e6")
        FrameAttVE.place(x=0, y=0, width=880, height=780)

        Label(FrameAttVE, text="Modelo: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110, y=48)
        atModeloV = Entry(FrameAttVE)
        atModeloV.configure(font="Arial 14")
        atModeloV.place(x=110, y=70, width=310, height=30)
        atModeloV.insert(0, ModeloVE)

        Label(FrameAttVE, text="Renavan: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440, y=48)
        atRenavV = Entry(FrameAttVE)
        atRenavV.configure(font="Arial 14")
        atRenavV.place(x=440, y=70, width=310, height=30)
        atRenavV.insert(0, RenavVE)

        Label(FrameAttVE, text="Marca: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110, y=118)
        atMarcaV = Entry(FrameAttVE)
        atMarcaV.configure(font="Arial 14")
        atMarcaV.place(x=110, y=140, width=310, height=30)
        atMarcaV.insert(0, MarcaVE)

        Label(FrameAttVE, text="Placa: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440, y=118)
        atPlacaV = Entry(FrameAttVE)
        atPlacaV.configure(font="Arial 14")
        atPlacaV.place(x=440, y=140, width=310, height=30)
        atPlacaV.insert(0, PlaacaVE)

        Label(FrameAttVE, text="Cor: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110, y=188)
        atCorV = Entry(FrameAttVE)
        atCorV.configure(font="Arial 14")
        atCorV.place(x=110, y=210, width=310, height=30)
        atCorV.insert(0, CorVE)

        Label(FrameAttVE, text="Situação Financeira: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440, y=188)
        atFinanceiroV = Entry(FrameAttVE)
        atFinanceiroV.configure(font="Arial 14")
        atFinanceiroV.place(x=440, y=210, width=310, height=30)
        atFinanceiroV.insert(0, SituaFinVE)

        Label(FrameAttVE, text="Ano de Lançamento: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110, y=258)
        atAnoV = Entry(FrameAttVE)
        atAnoV.configure(font="Arial 14")
        atAnoV.place(x=110, y=280, width=310, height=30)
        atAnoV.insert(0, AnoLancVE)

        Label(FrameAttVE, text="Valor na Tabela FIPE: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440, y=258)
        atFipeV = Entry(FrameAttVE)
        atFipeV.configure(font="Arial 14")
        atFipeV.place(x=440, y=280, width=310, height=30)
        atFipeV.insert(0, ValorFipVE)

        Label(FrameAttVE, text="Combustível: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110, y=328)
        atCombustV = ttk.Combobox(FrameAttVE, values="Gasolina Etanol Gasolina/Etanol Diesel Elétrico ")
        atCombustV.configure(font="Arial 14")
        atCombustV.place(x=110, y=350, width=310, height=30)
        atCombustV.insert(0, CombustVE)

        Label(FrameAttVE, text="Valor do proprietário: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440, y=328)
        atPrecoProV = Entry(FrameAttVE)
        atPrecoProV.configure(font="Arial 14")
        atPrecoProV.place(x=440, y=350, width=310, height=30)
        atPrecoProV.insert(0, ValorPropVE)

        Label(FrameAttVE, text="Proprietário: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110, y=398)
        atProprietarioV = ttk.Combobox(FrameAttVE, values=AtuaListPRO())
        atProprietarioV.configure(font="Arial 14")
        atProprietarioV.place(x=110, y=420, width=310, height=30)
        atProprietarioV.insert(0, ProprietaVE)

        Label(FrameAttVE, text="Acessórios: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440, y=398)
        atAcessoriosV = Entry(FrameAttVE)
        atAcessoriosV.configure(font="Arial 14")
        atAcessoriosV.place(x=440, y=420, width=310, height=30)
        atAcessoriosV.insert(0, AcessoVE)

        Label(FrameAttVE, text="Formas de pagamento: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110, y=468)
        atPagamentoV = Entry(FrameAttVE)
        atPagamentoV.configure(font="Arial 14")
        atPagamentoV.place(x=110, y=490, width=310, height=30)
        atPagamentoV.insert(0, FormPagVE)

        Label(FrameAttVE, text="Status: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440, y=468)
        atStatusV = ttk.Combobox(FrameAttVE, values="Disponível Vendido")
        atStatusV.configure(font="Arial 14")
        atStatusV.place(x=440, y=490, width=310, height=30)
        atStatusV.insert(0, StatussVE)

        btnSalvarVE = Button(FrameAttVE, text="Salvar Alterações", background="#fd0", foreground="#000", font="ArialBlk 12 bold", command=UpdateVE)
        btnSalvarVE.place(x=360, y=550, width=150, height=30)

        AppATTve.mainloop()
    except:
        messagebox.showinfo(title="VCU - Atenção", message="Nenhum item selecionado!")

def AtuaListPRO():
    squery = "SELECT Nome FROM PROPRIETARIOS"
    ListaPRO = VCU_QUERY.DQL(squery)
    vProprietario['values'] = ListaPRO

def semComando():
    pass


#  Criação das ABAS  #
ABA = ttk.Notebook(appVCU)
ABA.place(x=0, y=0, width=1400, height=860)

aba1 = Frame(ABA)
ABA.add(aba1, text="Cadastrar Cliente")
aba1.configure(background="#5f0")

aba2 = Frame(ABA)
ABA.add(aba2, text="Cadastrar Veículo")
aba2.configure(background="#5f0")

aba3 = Frame(ABA)
ABA.add(aba3, text="Consultar Proprietário")
aba3.configure(background="#06f")

aba4 = Frame(ABA)
ABA.add(aba4, text="Consultar Veículo")
aba4.configure(background="#06f")

# label FRAME = Dados Pessoais do Proprietário
FrameLab1 = LabelFrame(aba1, text="Dados Pessoais do Proprietário", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameLab1.configure(background="#e6e6e6")
FrameLab1.place(x=385, y=100, width=600, height=680)

FrameLab2 = LabelFrame(aba2, text="Dados do Veículo", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameLab2.configure(background="#e6e6e6")
FrameLab2.place(x=280, y=100, width=750, height=680)

FrameLab3 = LabelFrame(aba3, text="Buscar Proprietários", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameLab3.configure(background="#e6e6e6")
FrameLab3.place(x=220, y=10, width=900, height=800)

FrameLab4 = LabelFrame(aba4, text="Buscar Veículos", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameLab4.configure(background="#e6e6e6")
FrameLab4.place(x=90, y=10, width=1200, height=800)

### Gridview da ABA CONSULTAR VEÍCULO ###
quadroGrid = LabelFrame(FrameLab4, text="Dados dos Veículos", relief="flat", background="#e6e6e6")
quadroGrid.place(x=10, y=10, width=1180, height=760)

tv = ttk.Treeview(quadroGrid, columns=('Modelo', 'Marca', 'Cor', 'Ano', 'Combustivel', 'Proprietário', 'Formas de Pagamento', 'Renavam', 'Placa', 'Situação Financeira', 'Valor FIPE', 'Valor do Proprietário', 'Acessórios', 'Status'), show='headings')
tv.configure(height=22)
tv.column('Modelo', minwidth=75, width=80)
tv.column('Marca', minwidth=50, width=50)
tv.column('Cor', minwidth=40, width=40)
tv.column('Ano', minwidth=50, width=50)
tv.column('Combustivel', minwidth=75, width=80)
tv.column('Proprietário', minwidth=95, width=100)
tv.column('Formas de Pagamento', minwidth=130, width=130)
tv.column('Renavam', minwidth=55, width=60)
tv.column('Placa', minwidth=55, width=60)
tv.column('Situação Financeira', minwidth=110, width=110)
tv.column('Valor FIPE', minwidth=75, width=80)
tv.column('Valor do Proprietário', minwidth=115, width=120)
tv.column('Acessórios', minwidth=95, width=100)
tv.column('Status', minwidth=75, width=80)

tv.heading('Modelo', text='Modelo')
tv.heading('Marca', text='Marca')
tv.heading('Cor', text='Cor')
tv.heading('Ano', text='Ano')
tv.heading('Combustivel', text='Combustivel')
tv.heading('Proprietário', text='Proprietário')
tv.heading('Formas de Pagamento', text='Formas de Pagamento')
tv.heading('Renavam', text='Renavam')
tv.heading('Placa', text='Placa')
tv.heading('Situação Financeira', text='Situação Financeira')
tv.heading('Valor FIPE', text='Valor FIPE')
tv.heading('Valor do Proprietário', text='Valor do Proprietário')
tv.heading('Acessórios', text='Acessórios')
tv.heading('Status', text='Status')
tv.pack(side=LEFT)
tv.place(x=0, y=0)

# Scrollbar Vertical ABA CONSULTAR VEÍCULO
VScroll = ttk.Scrollbar(quadroGrid, orient="vertical", command=tv.yview)
VScroll.place(x=1145, y=2, height=465)

# Scrollbar Vertical ABA CONSULTAR VEÍCULO
OScroll = ttk.Scrollbar(quadroGrid, orient="horizontal", command=tv.xview)
OScroll.place(x=0, y=469, width=1145)

#configurar as Scrolls da ABA CONSULTAR VEÍCULO
tv.configure(yscrollcommand=VScroll.set, xscrollcommand=OScroll.set)

# Gridview da ABA CONSULTAR PROPRIETARIO
quadroGrid1 = LabelFrame(FrameLab3, text="Dados dos Proprietários", relief="flat", background="#e6e6e6")
quadroGrid1.place(x=10, y=10, width=860, height=760)

tv1 = ttk.Treeview(quadroGrid1, columns=('Nome Completo', 'CPF', 'Endereço', 'Telefone', 'Habilitação'), show='headings')
tv1.configure(height=23)
tv1.column('Nome Completo', minwidth=240, width=240)
tv1.column('CPF', minwidth=140, width=140)
tv1.column('Endereço', minwidth=200, width=220)
tv1.column('Telefone', minwidth=130, width=140)
tv1.column('Habilitação', minwidth=90, width=90)

tv1.heading('Nome Completo', text='Nome Completo')
tv1.heading('CPF', text='CPF')
tv1.heading('Endereço', text='Endereço')
tv1.heading('Telefone', text='Telefone')
tv1.heading('Habilitação', text='Habilitação')
tv1.pack(side=LEFT)
tv1.place(x=0, y=0)

# Scrollbar Vertical ABA Consultar PROPRIETARIO
VScroll2 = ttk.Scrollbar(quadroGrid1, orient="vertical", command=tv1.yview)
VScroll2.place(x=835, y=2, height=490)

# Scrollbar Vertical ABA Consultar PROPRIETARIO
OScroll2 = ttk.Scrollbar(quadroGrid1, orient="horizontal", command=tv1.xview)
OScroll2.place(x=0, y=489, width=835)

#configurar as Scrolls ABA Consultar PROPRIETARIO
tv1.configure(yscrollcommand=VScroll2.set, xscrollcommand=OScroll2.set)

### FRAMES da ABA CONSULTAR PROPRIETARIOS ###
# Frame de SELECT
FrameBusca1 = LabelFrame(quadroGrid1, text="Opções de busca", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameBusca1.configure(background="#e6e6e6")
FrameBusca1.place(x=2, y=510, width=850, height=108)

# Frame de Atualizar
FrameAtualizar = LabelFrame(quadroGrid1, text="Atualizar Registro Selecionado", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameAtualizar.configure(background="#e6e6e6")
FrameAtualizar.place(x=2, y=630, width=420, height=108)

# Frame de Excluir
FrameExcluir = LabelFrame(quadroGrid1, text="Excluir Registro Selecionado", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameExcluir.configure(background="#e6e6e6")
FrameExcluir.place(x=430, y=630, width=420, height=108)

### FRAMES da ABA CONSULTAR VEÍCULOS ###
# Frame de SELECT
FrameBusca = LabelFrame(quadroGrid, text="Opções de busca", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameBusca.configure(background="#e6e6e6")
FrameBusca.place(x=2, y=500, width=1170, height=108)

FrameAttVE = LabelFrame(quadroGrid, text="Atualizar dados do Veículo Selecionado", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameAttVE.configure(background="#e6e6e6")
FrameAttVE.place(x=2, y=620, width=330, height=108)

FrameDelVE = LabelFrame(quadroGrid, text="Excluir dados do Veículo Selecionado", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameDelVE.configure(background="#e6e6e6")
FrameDelVE.place(x=415, y=620, width=330, height=108)

FrameVendaVE = LabelFrame(quadroGrid, text="Realizar Venda do Veículo Selecionado", font="Arial 12 italic", borderwidth='1', relief="solid")
FrameVendaVE.configure(background="#e6e6e6")
FrameVendaVE.place(x=840, y=620, width=330, height=108)

#  Criando os menús #  Criando os menús #  Criando os menús #  Criando os menús
barraMenu = Menu(appVCU)

menuArquivo = Menu(barraMenu, tearoff=0)
menuArquivo.add_command(label="Novo Cadastro", command=novocadastro)
menuArquivo.add_separator()
menuArquivo.add_command(label="Abrir Cadastro", command=semComando)
menuArquivo.add_separator()
menuArquivo.add_command(label="Excluir Cadastro", command=semComando)
menuArquivo.add_separator()
menuArquivo.add_command(label="Fechar aplicação", command=appVCU.quit)
barraMenu.add_cascade(label="Arquivos VCU", menu=menuArquivo)

menuOpcoes = Menu(barraMenu, tearoff=0)
menuOpcoes.add_command(label="Excluir Proprietário", command=semComando)
menuOpcoes.add_separator()
menuOpcoes.add_command(label="Excluir Veículo", command=semComando)
menuOpcoes.add_separator()
menuOpcoes.add_command(label="Busca Personalizada", command=semComando)
menuOpcoes.add_separator()
menuOpcoes.add_command(label="Ver todos os Veículos Cadastrados", command=semComando)
menuOpcoes.add_separator()
menuOpcoes.add_command(label="Ver todos os Proprietários Cadastrados", command=semComando)
barraMenu.add_cascade(label="Opções de Consulta", menu=menuOpcoes)

menuVCU = Menu(barraMenu, tearoff=0)
menuVCU.add_command(label="Informações da Versão", command=semComando)
menuVCU.add_separator()
menuVCU.add_command(label="Desenvolvedores", command=semComando)
menuVCU.add_separator()
menuVCU.add_command(label="Redes Sociais do Software", command=semComando)
barraMenu.add_cascade(label="Destalhes do software", menu=menuVCU)

# Criação da Tabela para dados cadastrais do proprietario # Criação da Tabela para dados cadastrais do proprietario
Label(aba1, text="Cadastro dos Proprietários de Veículos", background="#009", font="Georgia 20 bold italic", foreground="#fff").place(x=385, y=10, width=600, height=50)

Label(FrameLab1, text="Nome Completo: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=130, y=48)
vNome = Entry(FrameLab1)
vNome.configure(font="Arial 14")
vNome.place(x=130, y=70, width=310, height=30)

Label(FrameLab1, text="CPF: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=130, y=118)
vCPF = Entry(FrameLab1)
vCPF.configure(font="Arial 14")
vCPF.place(x=130, y=140, width=310, height=30)

Label(FrameLab1, text="Endereço: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=130, y=188)
vEndereco = Entry(FrameLab1)
vEndereco.configure(font="Arial 14")
vEndereco.place(x=130, y=210, width=310, height=30)

Label(FrameLab1, text="Telefone para Contato: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=130, y=258)
vTelefone = Entry(FrameLab1)
vTelefone.configure(font="Arial 14")
vTelefone.place(x=130, y=280, width=310, height=30)

Label(FrameLab1, text="Habilitação: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=130, y=328)
vHabilita = Entry(FrameLab1)
vHabilita.configure(font="Arial 14")
vHabilita.place(x=130, y=350, width=310, height=30)

btnSalvar = Button(FrameLab1, text="Cadastrar", background="#009", foreground="#fff", font="ArialBlk 12 bold", command=salvardadosPRO)
btnSalvar.place(x=130, y=400, width=150, height=30)

btnNovo = Button(FrameLab1, text="Novo Cadastro", background="#090", foreground="#fff", font="ArialBlk 12 bold", command=novocadastro)
btnNovo.place(x=290, y=400, width=150, height=30)

Label(FrameLab1, text="VCU", background="#e6e6e6", foreground="#009", font="ArialBlk 140 bold").place(x=100, y=450, height=180)

#tabela para dados cadastrais do veículo
Label(aba2, text="Cadastro de Informações do Veículo", background="#009", font="Georgia 20 bold italic", foreground="#fff").place(x=280, y=10, width=750, height=50)

Label(FrameLab2, text="Modelo: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50, y=48)
vModelo = Entry(FrameLab2)
vModelo.configure(font="Arial 14")
vModelo.place(x=50, y=70, width=310, height=30)

Label(FrameLab2, text="Renavan: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=380, y=48)
vRenav = Entry(FrameLab2)
vRenav.configure(font="Arial 14")
vRenav.place(x=380, y=70, width=310, height=30)

Label(FrameLab2, text="Marca: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50, y=118)
vMarca = Entry(FrameLab2)
vMarca.configure(font="Arial 14")
vMarca.place(x=50, y=140, width=310, height=30)

Label(FrameLab2, text="Placa: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=380, y=118)
vPlaca = Entry(FrameLab2)
vPlaca.configure(font="Arial 14")
vPlaca.place(x=380, y=140, width=310, height=30)

Label(FrameLab2, text="Cor: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50, y=188)
vCor = Entry(FrameLab2)
vCor.configure(font="Arial 14")
vCor.place(x=50, y=210, width=310, height=30)

Label(FrameLab2, text="Situação Financeira: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=380, y=188)
vFinanceiro = Entry(FrameLab2)
vFinanceiro.configure(font="Arial 14")
vFinanceiro.place(x=380, y=210, width=310, height=30)

Label(FrameLab2, text="Ano de Lançamento: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50, y=258)
vAno = Entry(FrameLab2)
vAno.configure(font="Arial 14")
vAno.place(x=50, y=280, width=310, height=30)

Label(FrameLab2, text="Valor na Tabela FIPE: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=380, y=258)
vFipe = Entry(FrameLab2)
vFipe.configure(font="Arial 14")
vFipe.place(x=380, y=280, width=310, height=30)

Label(FrameLab2, text="Combustível: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50, y=328)
vCombust = ttk.Combobox(FrameLab2, values="Gasolina Etanol Gasolina/Etanol Diesel Elétrico ")
vCombust.configure(font="Arial 14")
vCombust.place(x=50, y=350, width=310, height=30)

btnAtual = Button(FrameLab2, text="Atualizar lista", background="#090", foreground="#fff", font="georgia 8 bold italic", command=AtuaListPRO)
btnAtual.place(x=257, y=398, height=17)

Label(FrameLab2, text="Valor do proprietário: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=380, y=328)
vPrecoPro = Entry(FrameLab2)
vPrecoPro.configure(font="Arial 14")
vPrecoPro.place(x=380, y=350, width=310, height=30)

Label(FrameLab2, text="Proprietário: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50, y=398)

vProprietario = ttk.Combobox(FrameLab2)
vProprietario.configure(font="Arial 14")
vProprietario.place(x=50, y=420, width=310, height=30)

Label(FrameLab2, text="Acessórios: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=380, y=398)
vAcessorios = Entry(FrameLab2)
vAcessorios.configure(font="Arial 14")
vAcessorios.place(x=380, y=420, width=310, height=30)

Label(FrameLab2, text="Formas de pagamento: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50, y=468)
vPagamento = Entry(FrameLab2)
vPagamento.configure(font="Arial 14")
vPagamento.place(x=50, y=490, width=310, height=30)

Label(FrameLab2, text="Status: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=380, y=468)
vStatus = ttk.Combobox(FrameLab2, values="Disponível Vendido")
vStatus.configure(font="Arial 14")
vStatus.place(x=380, y=490, width=310, height=30)

btnSalvar = Button(FrameLab2, text="Salvar", background="#009", foreground="#fff", font="ArialBlk 12 bold", command=salvardadosVE)
btnSalvar.place(x=300, y=550, width=150, height=30)

### elementos para quadro de pesquisa na ABA Consultar VEÍCULO ###
# Busca por MODELO
LabelPesq = Label(FrameBusca, text="Busca por Modelo:")
LabelPesq.configure(font="Arial 12", background="#e6e6e6")
LabelPesq.place(x=10, y=10)

nomePesq = Entry(FrameBusca)
nomePesq.configure(width=25, font="arial 14")
nomePesq.place(x=145, y=10)

btnPesq = Button(FrameBusca, text="Pesquisar", command=PesquisarMODE)
btnPesq.configure(font="arial 10 bold", background="#009", foreground="#fff")
btnPesq.place(x=430, y=10)

#Busca por PROPRIETARIO
LabelPesq1 = Label(FrameBusca, text="Busca por Proprietario:")
LabelPesq1.configure(font="Arial 12", background="#e6e6e6")
LabelPesq1.place(x=10, y=50)

nomePesq1 = Entry(FrameBusca)
nomePesq1.configure(width=25, font="arial 14")
nomePesq1.place(x=175, y=50)

btnPesq1 = Button(FrameBusca, text="Pesquisar", command=PesquisarPROP)
btnPesq1.configure(font="arial 10 bold", background="#009", foreground="#fff")
btnPesq1.place(x=460, y=50)

# Busca por PLACA
LabelPesq2 = Label(FrameBusca, text="Busca por Placa:")
LabelPesq2.configure(font="Arial 12", background="#e6e6e6")
LabelPesq2.place(x=520, y=10)

nomePesq2 = Entry(FrameBusca)
nomePesq2.configure(width=25, font="arial 14")
nomePesq2.place(x=645, y=10)

btnPesq2 = Button(FrameBusca, text="Pesquisar", command=PesquisarPLAC)
btnPesq2.configure(font="arial 10 bold", background="#009", foreground="#fff")
btnPesq2.place(x=930, y=10)

# Busca por STATUS
LabelPesq3 = Label(FrameBusca, text="Busca por Status:")
LabelPesq3.configure(font="Arial 12", background="#e6e6e6")
LabelPesq3.place(x=550, y=50)

txtBuscStt = ttk.Combobox(FrameBusca, values="Disponível Vendido")
txtBuscStt.configure(width=20, font="arial 14")
txtBuscStt.place(x=680, y=50)

btnPesq3 = Button(FrameBusca, text="Pesquisar", command=PesquisarSTAT)
btnPesq3.configure(font="arial 10 bold", background="#009", foreground="#fff")
btnPesq3.place(x=930, y=50)

# botao q busca TODOS os registros na ABA Consultar VEÍCULOS
btnBuscaTudo = Button(FrameBusca, text="Buscar Tudo", command=ListarVeiculos)
btnBuscaTudo.configure(width=12, height=2, font="arial 11 bold", background="#009", foreground="#fff")
btnBuscaTudo.pack(side='right')

# botao Atualizar na ABA Consultar VEICULOS
btnAttVE = Button(FrameAttVE, text="Atualizar dados do Veículo", command=AtualizarVE)
btnAttVE.configure(font="arial 12 bold", background="#fd0", foreground="#000")
btnAttVE.place(x=50, y=20, width=220, height=40)

# botao Excluir na ABA Consultar VEICULOS
btnExcVE = Button(FrameDelVE, text="Excluir dados do Veículo", command=DeletarVE)
btnExcVE.configure(font="arial 12 bold", background="#f00", foreground="#fff")
btnExcVE.place(x=50, y=20, width=220, height=40)

# botao Vender na ABA Consultar VEICULOS
btnVendVE = Button(FrameVendaVE, text="Vender Veículo", command=semComando)
btnVendVE.configure(font="arial 12 bold", background="#0f3", foreground="#000")
btnVendVE.place(x=50, y=20, width=220, height=40)

# Elementos para quadro de pesquisa da ABA Consultar PROPRIETARIOS
# Busca por NOME
LabelPesq4 = Label(FrameBusca1, text="Busca por Nome:")
LabelPesq4.configure(font="Arial 12", background="#e6e6e6")
LabelPesq4.place(x=10, y=10)

nomePesq4 = Entry(FrameBusca1)
nomePesq4.configure(width=15, font="arial 14")
nomePesq4.place(x=140, y=10)

btnPesq4 = Button(FrameBusca1, text="Pesquisar", command=PesquisarNOME)
btnPesq4.configure(font="arial 10 bold", background="#009", foreground="#fff")
btnPesq4.place(x=315, y=10)

#Busca por CPF
LabelPesq6 = Label(FrameBusca1, text="Busca por CPF:")
LabelPesq6.configure(font="Arial 12", background="#e6e6e6")
LabelPesq6.place(x=10, y=50)

nomePesq6 = Entry(FrameBusca1)
nomePesq6.configure(width=15, font="arial 14")
nomePesq6.place(x=130, y=50)

btnPesq6 = Button(FrameBusca1, text="Pesquisar", command=PesquisarCPF)
btnPesq6.configure(font="arial 10 bold", background="#009", foreground="#fff")
btnPesq6.place(x=305, y=50)

# botao q busca TODOS os registros na ABA Consultar PROPRIETÁRIOS
btnBuscaTudo5 = Button(FrameBusca1, text="Buscar Tudo", command=ListarProprietarios)
btnBuscaTudo5.configure(width=10, height=2, font="arial 11 bold", background="#0f3", foreground="#000")
btnBuscaTudo5.place(x=530, y=15, width=200, height=50)

#botão Atualizar dados do Proprietário
btnAttPRO = Button(FrameAtualizar, text="Atualizar Registro", command=AtualizarPRO)
btnAttPRO.configure(font="arial 12 bold", background="#fd0", foreground="#000")
btnAttPRO.place(x=120, y=18, width=200, height=50)

#Botão Excluir dados do Proprietário
btnDelPRO = Button(FrameExcluir, text="Excluir Registro", command=DeletarPRO)
btnDelPRO.configure(font="arial 12 bold", background="#f00", foreground="#fff")
btnDelPRO.place(x=120, y=18, width=200, height=50)

#  executa o programa em loop  #
appVCU.config(menu=barraMenu)
appVCU.mainloop()