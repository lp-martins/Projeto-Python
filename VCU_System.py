from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import VCU_QUERY

#   propriedades da janela  #
appVCU = Tk()
appVCU.title(" Venda de Carros Usados®")
appVCU.geometry("1280x860")
appVCU.configure(background="#f2f2f2")
appVCU.wm_iconbitmap('icon_VCU.ico')

def semComando():
    pass

#  Criação das ABAS  #
ABA = ttk.Notebook(appVCU)
ABA.pack(fill='both', expand=1)

def ABA_CAD_Propri():
    aba1 = Frame(ABA)
    ABA.add(aba1, text="Cadastrar Proprietário")
    aba1.configure(background="#5f0")
    Label(aba1, text="Cadastro de Proprietário de Veículo(s)", background="#009", font="Georgia 20 bold italic", foreground="#fff").pack(pady=20, ipadx=30, ipady=15)

    FrameLab1 = LabelFrame(aba1, text="Dados Pessoais do Proprietário", font="Arial 12 italic", borderwidth='1', relief="solid")
    FrameLab1.configure(background="#e6e6e6")
    FrameLab1.pack(pady=0, ipadx=300, ipady=350)

    def novocadastro():
        vNome.delete(0, END)
        vCPF.delete(0, END)
        vEndereco.delete(0, END)
        vTelefone.delete(0, END)
        vHabilita.delete(0, END)

    def salvardadosPRO():
        Ssql = "SELECT CPF FROM PROPRIETARIOS"
        CPFs = str(VCU_QUERY.DQL(Ssql))
        if vCPF.get() in CPFs and vCPF.get() != "":
            messagebox.showwarning(title="VCU - CPF já Cadastrado!",
                                   message="Este CPF já está cadastrado em nossa base de dados!")
        elif (vNome.get() != "") and (vCPF.get() != "") and (vEndereco.get() != "") and (vTelefone != "") and (
                vHabilita.get() != ""):
            sNome = vNome.get()
            sCPF = vCPF.get()
            sEndereco = vEndereco.get()
            sTelefone = vTelefone.get()
            sHabilita = vHabilita.get()
            squery = "INSERT INTO PROPRIETARIOS(Nome, CPF, Endereço, Telefone, Habilitação) VALUES ('" + sNome + "', '" + sCPF + "', '" + sEndereco + "', '" + sTelefone + "', '" + sHabilita + "')"
            VCU_QUERY.DML(squery)
            messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados cadastrados com sucesso!")
        else:
            messagebox.showwarning(title=" Campos Vazios!",
                                   message="Por favor, preencha todos os campos para realizar o cadastro!")

    # Criação da Tabela para dados cadastrais do proprietario

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



def ABA_CAD_Veic():
    aba2 = Frame(ABA)
    ABA.add(aba2, text="Cadastrar Veículo")
    aba2.configure(background="#5f0")
    Label(aba2, text="Cadastro de Informações do Veículo", background="#009", font="Georgia 20 bold italic", foreground="#fff").pack(pady=20, ipadx=120, ipady=15)

    def AtuaListPRO():
        squery = "SELECT Nome FROM PROPRIETARIOS"
        ListaPRO = VCU_QUERY.DQL(squery)
        vProprietario['values'] = ListaPRO

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

        if (vModelo.get() == "") or (vMarca.get() == "") or (vCor.get() == "") or (vAno.get() == "") or (
                vCombust.get() == "") or (vProprietario.get() == "") or (vPagamento.get() == "") or (
                vRenav.get() == "") or (vPlaca.get() == "") or (vFinanceiro.get() == "") or (vFipe.get() == "") or (
                vPrecoPro.get() == "") or (vAcessorios.get() == "") or (vStatus.get() == ""):
            messagebox.showwarning(title=" Campos Vazios!",
                                   message="Por favor, preencha todos os campos para realizar o cadastro!")
        elif vProprietario.get() in str(PropList):
            squery = "INSERT INTO VEICULOS(Modelo, Marca, Cor, Ano_de_Lançamento, Combustivel, Proprietario, Formas_de_Pagamento, Renavam, Placa, Situação_Financeira, Valor_FIPE, Valor_Proprietario, Acessorios, Status) VALUES ('" + sModelo + "', '" + sMarca + "', '" + sCor + "', '" + sAno + "', '" + sCombust + "', '" + sProp + "', '" + sPagamento + "', '" + sRenavam + "', '" + sPlaca + "', '" + sFinanceiro + "', '" + sFipe + "', '" + sValorPRO + "', '" + sAcessorio + "', '" + sStatus + "')"
            VCU_QUERY.DML(squery)
            messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados do Veículo Salvo com Sucesso!")
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
            messagebox.showwarning(title=" Proprietário Não Cadastrado!",
                                   message="Este proprietário não está cadastrado! Verifique o nome e tente novamente!")

    FrameLab2 = LabelFrame(aba2, text="Dados do Veículo", font="Arial 12 italic", borderwidth='1', relief="solid")
    FrameLab2.configure(background="#e6e6e6")
    FrameLab2.pack(pady=0, ipadx=380, ipady=350)

    # tabela para dados cadastrais do veículo

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

    Label(FrameLab2, text="Ano de Lançamento: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50,
                                                                                                                 y=258)
    vAno = Entry(FrameLab2)
    vAno.configure(font="Arial 14")
    vAno.place(x=50, y=280, width=310, height=30)

    Label(FrameLab2, text="Valor na Tabela FIPE: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=380, y=258)
    vFipe = Entry(FrameLab2)
    vFipe.configure(font="Arial 14")
    vFipe.place(x=380, y=280, width=310, height=30)

    Label(FrameLab2, text="Combustível: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50, y=328)
    vCombust = ttk.Combobox(FrameLab2, values="Gasolina Etanol Gasolina/Etanol Diesel Elétrico ", state="readonly")
    vCombust.configure(font="Arial 14")
    vCombust.place(x=50, y=350, width=310, height=30)

    btnAtual = Button(FrameLab2, text="Atualizar lista", background="#090", foreground="#fff", font="georgia 8 bold italic", command=AtuaListPRO)
    btnAtual.place(x=257, y=398, height=17)

    Label(FrameLab2, text="Valor do proprietário: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=380, y=328)
    vPrecoPro = Entry(FrameLab2)
    vPrecoPro.configure(font="Arial 14")
    vPrecoPro.place(x=380, y=350, width=310, height=30)

    Label(FrameLab2, text="Proprietário: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=50, y=398)
    vProprietario = ttk.Combobox(FrameLab2, state="readonly")
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
    vStatus = ttk.Combobox(FrameLab2, values="Disponível Vendido", state="readonly")
    vStatus.configure(font="Arial 14")
    vStatus.place(x=380, y=490, width=310, height=30)

    btnSalvar = Button(FrameLab2, text="Salvar", background="#009", foreground="#fff", font="ArialBlk 12 bold", command=salvardadosVE)
    btnSalvar.place(x=300, y=550, width=150, height=30)

def ABA_Consu_Propri():
    aba3 = Frame(ABA)
    ABA.add(aba3, text="Consultar Proprietário")
    aba3.configure(background="#06f")

    FrameLab3 = LabelFrame(aba3, text="Buscar Proprietários", font="Arial 12 italic", borderwidth='1', relief="solid")
    FrameLab3.configure(background="#e6e6e6")
    FrameLab3.pack(pady=10, ipadx=440, ipady=400)

    # ABA Consultar Proprietário
    def PesquisarCPF():
        tv1.delete(*tv1.get_children())
        if nomePesq6.get() != "":
            vquery = "SELECT Nome, CPF, Endereço, Telefone, Habilitação FROM PROPRIETARIOS WHERE CPF LIKE '%" + nomePesq6.get() + "%'"
            linhas = VCU_QUERY.DQL(vquery)
            nomePesq6.delete(0, END)
            if linhas != []:
                for x in linhas:
                    tv1.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos Proprietários com este CPF!")
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    # ABA Consultar Proprietário
    def PesquisarNOME():
        tv1.delete(*tv1.get_children())
        if nomePesq4.get() != "":
            vquery = "SELECT Nome, CPF, Endereço, Telefone, Habilitação FROM PROPRIETARIOS WHERE NOME LIKE '%" + nomePesq4.get() + "%'"
            linhas = VCU_QUERY.DQL(vquery)
            nomePesq4.delete(0, END)
            if linhas != []:
                for x in linhas:
                    tv1.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos Proprietários com esse Nome!")
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    # ABA Consultar Proprietário
    def ListarProprietarios():
        tv1.delete(*tv1.get_children())
        vquery = "SELECT Nome, CPF, Endereço, Telefone, Habilitação FROM PROPRIETARIOS"
        linhas = VCU_QUERY.DQL(vquery)
        for x in linhas:
            tv1.insert("", "end", values=x)

    def DeletarPRO():
        try:
            cquery = "SELECT Proprietario FROM VEICULOS"
            PropricomVE = VCU_QUERY.DQL(cquery)
            ItemSelect = tv1.selection()[0]
            Valores = tv1.item(ItemSelect, "values")
            ValorSelect = Valores[0]
            if ValorSelect not in str(PropricomVE):
                MsgResult = messagebox.askyesno(title=" Atenção!!!",
                                                message="Deseja mesmo exluir o Proprietário selecionado?")
                if MsgResult == True:
                    dquery = "DELETE FROM PROPRIETARIOS WHERE Nome ='" + ValorSelect + "'"
                    tv1.delete(ItemSelect)
                    VCU_QUERY.DML(dquery)
            else:
                messagebox.showwarning(title=" Atenção!!!",
                                       message="Não é possivel excluir um proprietário que tenha veículos disponíveis!")
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

    def AtualizarPRO():
        def UpdatePRO():
            if (AtNome.get() != "") and (AtCPF.get() != "") and (AtEndereco.get() != "") and (
                    AtTelefone.get() != "") and (AtHabilita.get() != ""):
                UpNome = AtNome.get()
                UpCPF = AtCPF.get()
                UpEndereco = AtEndereco.get()
                UpTelefone = AtTelefone.get()
                UpHabilita = AtHabilita.get()
                Upquery = "UPDATE PROPRIETARIOS SET Nome='" + UpNome + "', CPF='" + UpCPF + "', Endereço='" + UpEndereco + "', Telefone='" + UpTelefone + "', Habilitação='" + UpHabilita + "' WHERE CPF = '" + UpCPF + "'"
                QUERYup = "UPDATE VEICULOS SET Proprietario='" + AtNome.get() + "' WHERE Proprietario='" + NomePRO + "'"
                VCU_QUERY.DML(Upquery)
                VCU_QUERY.DML(QUERYup)
                messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados Atualizados com sucesso!")
            else:
                messagebox.showwarning(title=" Campos Vazios!",
                                       message="Por favor, preencha todos os campos para realizar o cadastro!")

        try:
            ItemSelectPRO = tv1.selection()[0]
            valoresPRO = tv1.item(ItemSelectPRO, "values")
            NomePRO = valoresPRO[0]
            CPFpro = valoresPRO[1]
            EnderecoPRO = valoresPRO[2]
            TelefonePRO = valoresPRO[3]
            HabilitaPRO = valoresPRO[4]

            AppATTpro = Toplevel()
            AppATTpro.title(" Atualizando dados do Proprietário")
            AppATTpro.geometry("900x800")
            AppATTpro.resizable(False, False)
            AppATTpro.configure(background="#fd0")
            AppATTpro.focus_force()
            AppATTpro.grab_set()

            ABAatt = ttk.Notebook(AppATTpro)
            ABAatt.place(x=10, y=10, width=880, height=780)

            FrameAttPro = LabelFrame(ABAatt, text="Dados Pessoais do Proprietário", font="Arial 12 italic",
                                     borderwidth='1', relief="solid")
            FrameAttPro.configure(background="#e6e6e6")
            FrameAttPro.place(x=0, y=0, width=880, height=780)

            Label(FrameAttPro, text="Nome Completo: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(
                x=280, y=148)
            AtNome = ttk.Entry(FrameAttPro)
            AtNome.configure(font="Arial 14")
            AtNome.place(x=280, y=170, width=310, height=30)
            AtNome.insert(0, NomePRO)

            Label(FrameAttPro, text="CPF: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=280,
                                                                                                             y=218)
            AtCPF = Entry(FrameAttPro)
            AtCPF.configure(font="Arial 14")
            AtCPF.place(x=280, y=240, width=310, height=30)
            AtCPF.insert(0, CPFpro)

            Label(FrameAttPro, text="Endereço: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=280,
                                                                                                                  y=288)
            AtEndereco = Entry(FrameAttPro)
            AtEndereco.configure(font="Arial 14")
            AtEndereco.place(x=280, y=310, width=310, height=30)
            AtEndereco.insert(0, EnderecoPRO)

            Label(FrameAttPro, text="Telefone para Contato: ", background="#e6e6e6", foreground="#009",
                  font="Arial 12").place(x=280, y=358)
            AtTelefone = Entry(FrameAttPro)
            AtTelefone.configure(font="Arial 14")
            AtTelefone.place(x=280, y=380, width=310, height=30)
            AtTelefone.insert(0, TelefonePRO)

            Label(FrameAttPro, text="Habilitação: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(
                x=280, y=428)
            AtHabilita = Entry(FrameAttPro)
            AtHabilita.configure(font="Arial 14")
            AtHabilita.place(x=280, y=450, width=310, height=30)
            AtHabilita.insert(0, HabilitaPRO)

            btnSalvarAttPRO = Button(FrameAttPro, text="Salvar Alterações", background="#fd0", foreground="#000",
                                     font="ArialBlk 12 bold", command=UpdatePRO)
            btnSalvarAttPRO.place(x=350, y=500, width=180, height=30)

            AppATTpro.transient(appVCU)
            AppATTpro.mainloop()
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")


    # Gridview da ABA CONSULTAR PROPRIETARIO
    quadroGrid1 = LabelFrame(FrameLab3, text="Dados dos Proprietários", relief="flat", background="#e6e6e6")
    quadroGrid1.place(x=10, y=10, width=860, height=760)

    tv1 = ttk.Treeview(quadroGrid1, columns=('Nome Completo', 'CPF', 'Endereço', 'Telefone', 'Habilitação'),
                       show='headings')
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

    # configurar as Scrolls ABA Consultar PROPRIETARIO
    tv1.configure(yscrollcommand=VScroll2.set, xscrollcommand=OScroll2.set)

    ### FRAMES da ABA CONSULTAR PROPRIETARIOS ###
    # Frame de SELECT
    FrameBusca1 = LabelFrame(quadroGrid1, text="Opções de busca", font="Arial 12 italic", borderwidth='3')
    FrameBusca1.configure(background="#e6e6e6")
    FrameBusca1.place(x=2, y=510, width=850, height=108)

    # Frame de Atualizar
    FrameAtualizar = LabelFrame(quadroGrid1, text="Atualizar Registro Selecionado", font="Arial 12 italic",
                                borderwidth='3')
    FrameAtualizar.configure(background="#e6e6e6")
    FrameAtualizar.place(x=2, y=630, width=420, height=108)

    # Frame de Excluir
    FrameExcluir = LabelFrame(quadroGrid1, text="Excluir Registro Selecionado", font="Arial 12 italic", borderwidth='3')
    FrameExcluir.configure(background="#e6e6e6")
    FrameExcluir.place(x=430, y=630, width=420, height=108)

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

    # Busca por CPF
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

    # botão Atualizar dados do Proprietário
    btnAttPRO = Button(FrameAtualizar, text="Atualizar Registro", command=AtualizarPRO)
    btnAttPRO.configure(font="arial 12 bold", background="#fd0", foreground="#000")
    btnAttPRO.place(x=120, y=18, width=200, height=50)

    # Botão Excluir dados do Proprietário
    btnDelPRO = Button(FrameExcluir, text="Excluir Registro", command=DeletarPRO)
    btnDelPRO.configure(font="arial 12 bold", background="#f00", foreground="#fff")
    btnDelPRO.place(x=120, y=18, width=200, height=50)


def ABA_Consu_Veic():
    aba4 = Frame(ABA)
    ABA.add(aba4, text="Consultar Veículo")
    aba4.configure(background="#06f")

    FrameLab4 = LabelFrame(aba4, text="Buscar Veículos", font="Arial 12 italic", borderwidth='1', relief="solid")
    FrameLab4.configure(background="#e6e6e6")
    FrameLab4.pack(pady=15, ipadx=595, ipady=390)

    def AtuaListPRO():
        pass

    # ABA Consultar Veículo
    def ListarVeiculos():
        tv.delete(*tv.get_children())
        vquery = "SELECT * FROM VEICULOS order by Modelo"
        linhas = VCU_QUERY.DQL(vquery)
        for x in linhas:
            tv.insert("", "end", values=x)

    # ABA Consultar Veículo
    def PesquisarMODE():
        tv.delete(*tv.get_children())
        if nomePesq.get() != "":
            vquery = "SELECT * FROM VEICULOS WHERE Modelo LIKE '%" + nomePesq.get() + "%'"
            linhas = VCU_QUERY.DQL(vquery)
            nomePesq.delete(0, END)
            if linhas != []:
                for x in linhas:
                    tv.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos veículos com esse Modelo!")
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    # ABA Consultar Veículo
    def PesquisarPROP():
        tv.delete(*tv.get_children())
        if nomePesq1.get() != "":
            vquery = "SELECT * FROM VEICULOS WHERE Proprietario LIKE '%" + nomePesq1.get() + "%'"
            linhas = VCU_QUERY.DQL(vquery)
            nomePesq1.delete(0, END)
            if linhas != []:
                for x in linhas:
                    tv.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos veículos com esse Proprietário!")
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    # ABA Consultar Veículo
    def PesquisarPLAC():
        tv.delete(*tv.get_children())
        if nomePesq2.get() != "":
            vquery = "SELECT * FROM VEICULOS WHERE Placa LIKE '%" + nomePesq2.get() + "%'"
            linhas = VCU_QUERY.DQL(vquery)
            nomePesq2.delete(0, END)
            if linhas != []:
                for x in linhas:
                    tv.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos veículos com essa Placa!")
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    # ABA Consultar Veículo
    def PesquisarSTAT():
        tv.delete(*tv.get_children())
        if txtBuscStt.get() != "":
            Status = txtBuscStt.get()
            vquery = "SELECT * FROM VEICULOS WHERE Status ='" + Status + "'"
            linhas = VCU_QUERY.DQL(vquery)
            if linhas != []:
                for x in linhas:
                    tv.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos veículos com esse Status!")
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma Opção escolhida!")

    def DeletarVE():
        try:
            ItemSelect = tv.selection()[0]
            Valores = tv.item(ItemSelect, "values")
            ValorSelect = Valores[8]
            MsgResult = messagebox.askyesno(title=" Atenção!!!", message="Deseja mesmo exluir o Veículo selecionado?")
            if MsgResult == True:
                dquery = "DELETE FROM VEICULOS WHERE Placa ='" + ValorSelect + "'"
                tv.delete(ItemSelect)
                VCU_QUERY.DML(dquery)
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

    def AtualizarVE():
        def UpdateVE():
            if (atModeloV.get() != "") and (atMarcaV.get() != "") and (atCorV.get() != "") and (
                    atAnoV.get() != "") and (atCombustV.get() != "") and (atProprietarioV.get() != "") and (
                    atPagamentoV.get() != "") and (atRenavV.get() != "") and (atPlacaV.get() != "") and (
                    atFinanceiroV.get() != "") and (atFipeV.get() != "") and (atPrecoProV.get() != "") and (
                    atAcessoriosV.get() != "") and (atStatusV.get() != ""):
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

                Upquery = "UPDATE VEICULOS SET Modelo='" + UpModelo + "', Marca='" + UpMarca + "', Cor='" + UpCor + "', Ano_de_Lançamento='" + UpAnoLanc + "', Combustivel='" + UpCombust + "', Proprietario='" + UpProprieta + "', Formas_de_Pagamento='" + UpFormPag + "', Renavam='" + UpRenavam + "', Placa='" + UpPlaca + "', Situação_Financeira='" + UpSituaFin + "', Valor_FIPE='" + UpValorFip + "', Valor_Proprietario='" + UpValorPRO + "', Acessorios='" + UpAcessorio + "', Status='" + UpStatus + "' WHERE Placa = '" + UpPlaca + "'"
                VCU_QUERY.DML(Upquery)
                messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados Atualizados com sucesso!")
            else:
                messagebox.showwarning(title=" Campos Vazios!",
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

            AppATTve = Toplevel()
            AppATTve.title(" Atualizando dados do Veículo")
            AppATTve.geometry("900x800")
            AppATTve.resizable(False, False)
            AppATTve.configure(background="#fd0")
            AppATTve.wm_iconbitmap('icon_VCU.ico')
            AppATTve.focus_force()
            AppATTve.grab_set()

            ABAattVE = ttk.Notebook(AppATTve)
            ABAattVE.place(x=10, y=10, width=880, height=780)

            FrameAttVE = LabelFrame(ABAattVE, text="Dados do Veículo", font="Arial 12 italic", borderwidth='1',
                                    relief="solid")
            FrameAttVE.configure(background="#e6e6e6")
            FrameAttVE.place(x=0, y=0, width=880, height=780)

            Label(FrameAttVE, text="Modelo: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110,
                                                                                                               y=48)
            atModeloV = Entry(FrameAttVE)
            atModeloV.configure(font="Arial 14")
            atModeloV.place(x=110, y=70, width=310, height=30)
            atModeloV.insert(0, ModeloVE)

            Label(FrameAttVE, text="Renavan: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440,
                                                                                                                y=48)
            atRenavV = Entry(FrameAttVE)
            atRenavV.configure(font="Arial 14")
            atRenavV.place(x=440, y=70, width=310, height=30)
            atRenavV.insert(0, RenavVE)

            Label(FrameAttVE, text="Marca: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110,
                                                                                                              y=118)
            atMarcaV = Entry(FrameAttVE)
            atMarcaV.configure(font="Arial 14")
            atMarcaV.place(x=110, y=140, width=310, height=30)
            atMarcaV.insert(0, MarcaVE)

            Label(FrameAttVE, text="Placa: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440,
                                                                                                              y=118)
            atPlacaV = Entry(FrameAttVE)
            atPlacaV.configure(font="Arial 14")
            atPlacaV.place(x=440, y=140, width=310, height=30)
            atPlacaV.insert(0, PlaacaVE)

            Label(FrameAttVE, text="Cor: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=110,
                                                                                                            y=188)
            atCorV = Entry(FrameAttVE)
            atCorV.configure(font="Arial 14")
            atCorV.place(x=110, y=210, width=310, height=30)
            atCorV.insert(0, CorVE)

            Label(FrameAttVE, text="Situação Financeira: ", background="#e6e6e6", foreground="#009",
                  font="Arial 12").place(x=440, y=188)
            atFinanceiroV = Entry(FrameAttVE)
            atFinanceiroV.configure(font="Arial 14")
            atFinanceiroV.place(x=440, y=210, width=310, height=30)
            atFinanceiroV.insert(0, SituaFinVE)

            Label(FrameAttVE, text="Ano de Lançamento: ", background="#e6e6e6", foreground="#009",
                  font="Arial 12").place(x=110, y=258)
            atAnoV = Entry(FrameAttVE)
            atAnoV.configure(font="Arial 14")
            atAnoV.place(x=110, y=280, width=310, height=30)
            atAnoV.insert(0, AnoLancVE)

            Label(FrameAttVE, text="Valor na Tabela FIPE: ", background="#e6e6e6", foreground="#009",
                  font="Arial 12").place(x=440, y=258)
            atFipeV = Entry(FrameAttVE)
            atFipeV.configure(font="Arial 14")
            atFipeV.place(x=440, y=280, width=310, height=30)
            atFipeV.insert(0, ValorFipVE)

            Label(FrameAttVE, text="Combustível: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(
                x=110, y=328)
            atCombustV = ttk.Combobox(FrameAttVE, values="Gasolina Etanol Gasolina/Etanol Diesel Elétrico ")
            atCombustV.configure(font="Arial 14")
            atCombustV.place(x=110, y=350, width=310, height=30)
            atCombustV.insert(0, CombustVE)

            Label(FrameAttVE, text="Valor do proprietário: ", background="#e6e6e6", foreground="#009",
                  font="Arial 12").place(x=440, y=328)
            atPrecoProV = Entry(FrameAttVE)
            atPrecoProV.configure(font="Arial 14")
            atPrecoProV.place(x=440, y=350, width=310, height=30)
            atPrecoProV.insert(0, ValorPropVE)

            Label(FrameAttVE, text="Proprietário: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(
                x=110, y=398)
            atProprietarioV = ttk.Combobox(FrameAttVE, values=AtuaListPRO())
            atProprietarioV.configure(font="Arial 14")
            atProprietarioV.place(x=110, y=420, width=310, height=30)
            atProprietarioV.insert(0, ProprietaVE)

            Label(FrameAttVE, text="Acessórios: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(
                x=440, y=398)
            atAcessoriosV = Entry(FrameAttVE)
            atAcessoriosV.configure(font="Arial 14")
            atAcessoriosV.place(x=440, y=420, width=310, height=30)
            atAcessoriosV.insert(0, AcessoVE)

            Label(FrameAttVE, text="Formas de pagamento: ", background="#e6e6e6", foreground="#009",
                  font="Arial 12").place(x=110, y=468)
            atPagamentoV = Entry(FrameAttVE)
            atPagamentoV.configure(font="Arial 14")
            atPagamentoV.place(x=110, y=490, width=310, height=30)
            atPagamentoV.insert(0, FormPagVE)

            Label(FrameAttVE, text="Status: ", background="#e6e6e6", foreground="#009", font="Arial 12").place(x=440,
                                                                                                               y=468)
            atStatusV = ttk.Combobox(FrameAttVE, values="Disponível Vendido")
            atStatusV.configure(font="Arial 14")
            atStatusV.place(x=440, y=490, width=310, height=30)
            atStatusV.insert(0, StatussVE)

            btnSalvarVE = Button(FrameAttVE, text="Salvar Alterações", background="#fd0", foreground="#000",
                                 font="ArialBlk 12 bold", command=UpdateVE)
            btnSalvarVE.place(x=360, y=550, width=150, height=30)

            AppATTve.transient(appVCU)
            AppATTve.mainloop()
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

    def VenderVE():
        try:
            ItemSelectVE = tv.selection()[0]
            ValoresVE = tv.item(ItemSelectVE, "values")
            ModeloVE = ValoresVE[0]
            MarcaVE = ValoresVE[1]
            CorVE = ValoresVE[2]
            AnoLancVE = ValoresVE[3]
            CombustVE = ValoresVE[4]
            ProprietaVE = ValoresVE[5]
            RenavVE = ValoresVE[7]
            PlaacaVE = ValoresVE[8]
            SituaFinVE = ValoresVE[9]
            ValorFipVE = ValoresVE[10]
            ValorPropVE = ValoresVE[11]
            AcessoVE = ValoresVE[12]

            selectQuery = "SELECT * FROM PROPRIETARIOS WHERE Nome ='" + ProprietaVE + "'"
            PROvenda = VCU_QUERY.DQL(selectQuery)

            NomePROvenda = "nome"
            CpfPROvenda = "CPF"
            EndPROvenda = "Endereço"
            FonePROvenda = "telefone"
            for x in PROvenda:
                NomePROvenda = x[0]
                CpfPROvenda = x[1]
                EndPROvenda = x[2]
                FonePROvenda = x[3]

            AppVENDA = Toplevel()
            AppVENDA.title(" Operação de Venda do Veículo")
            AppVENDA.geometry("900x800")
            AppVENDA.resizable(False, False)
            AppVENDA.configure(background="#0f3")
            AppVENDA.wm_iconbitmap('icon_VCU.ico')
            AppVENDA.focus_force()
            AppVENDA.grab_set()

            ABAvenda = ttk.Notebook(AppVENDA)
            ABAvenda.place(x=10, y=10, width=880, height=780)

            # __________________________Frame Operações de venda___________________________#

            FrameVENDA = LabelFrame(ABAvenda, text="Informações da VENDA", font="Arial 12 italic bold", foreground="#000",
                                    borderwidth='1', relief="solid")
            FrameVENDA.configure(background="#e6e6e6")
            FrameVENDA.place(x=0, y=0, width=880, height=780)

            # __________________________Frame dados do Veículo___________________________#

            FrameDadosVE = LabelFrame(FrameVENDA, text="Dados do Veículo", font="Arial 11 bold", foreground="#099",
                                      borderwidth='3')
            FrameDadosVE.configure(background="#e6e6e6")
            FrameDadosVE.place(x=20, y=10, width=840, height=220)

            Label(FrameDadosVE, text="Modelo: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20,
                                                                                                                   y=10)
            ModeloVEND = Entry(FrameDadosVE)
            ModeloVEND.place(x=80, y=10, width=260, height=22.499)
            ModeloVEND.insert(0, ModeloVE)
            ModeloVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Renavan: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(
                x=350, y=10)
            RenavVEND = Entry(FrameDadosVE)
            RenavVEND.place(x=420, y=10, width=140, height=22.499)
            RenavVEND.insert(0, RenavVE)
            RenavVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Placa: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=570,
                                                                                                                  y=10)
            PlacaVEND = Entry(FrameDadosVE)
            PlacaVEND.place(x=620, y=10, width=150, height=22.499)
            PlacaVEND.insert(0, PlaacaVE)
            PlacaVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Marca: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20,
                                                                                                                  y=40)
            MarcaVEND = Entry(FrameDadosVE)
            MarcaVEND.place(x=70, y=40, width=230, height=22.499)
            MarcaVEND.insert(0, MarcaVE)
            MarcaVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Ano de Lançamento: ", background="#FFF", foreground="#000",
                  font="Arial 10 bold").place(x=310, y=40)
            AnoVEND = Entry(FrameDadosVE)
            AnoVEND.place(x=450, y=40, width=140, height=22.4)
            AnoVEND.insert(0, AnoLancVE)
            AnoVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Cor: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=600,
                                                                                                                y=40)
            CorVEND = Entry(FrameDadosVE)
            CorVEND.place(x=635, y=40, width=180, height=22.4)
            CorVEND.insert(0, CorVE)
            CorVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Combustível: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(
                x=20, y=70)
            CombustVEND = Entry(FrameDadosVE)
            CombustVEND.place(x=110, y=70, width=120, height=22.4)
            CombustVEND.insert(0, CombustVE)
            CombustVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Proprietário: ", background="#FFF", foreground="#000",
                  font="Arial 10 bold").place(x=240, y=70)
            ProprieVEND = Entry(FrameDadosVE)
            ProprieVEND.place(x=330, y=70, width=350, height=22.4)
            ProprieVEND.insert(0, ProprietaVE)
            ProprieVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Situação Financeira: ", background="#FFF", foreground="#000",
                  font="Arial 10 bold").place(x=20, y=100)
            FinancVEND = Entry(FrameDadosVE)
            FinancVEND.place(x=160, y=100, width=655, height=22.4)
            FinancVEND.insert(0, SituaFinVE)
            FinancVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Valor na Tabela FIPE: ", background="#FFF", foreground="#000",
                  font="Arial 10 bold").place(x=20, y=130)
            FipeVEND = Entry(FrameDadosVE)
            FipeVEND.place(x=165, y=130, width=95, height=22.4)
            FipeVEND.insert(0, ValorFipVE)
            FipeVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Valor do proprietário: ", background="#FFF", foreground="#000",
                  font="Arial 10 bold").place(x=270, y=130)
            PrecoProV = Entry(FrameDadosVE)
            PrecoProV.place(x=415, y=130, width=100, height=22.4)
            PrecoProV.insert(0, ValorPropVE)
            PrecoProV.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosVE, text="Acessórios: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(
                x=20, y=160)
            AcessorioV = Entry(FrameDadosVE)
            AcessorioV.place(x=95, y=160, width=720, height=22.4)
            AcessorioV.insert(0, AcessoVE)
            AcessorioV.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            # ________________________Frame dados do Proprietário_________________________#

            FrameDadosPRO = LabelFrame(FrameVENDA, text="Dados do Proprietário", font="Arial 11 bold",
                                       foreground="#099", borderwidth='3')
            FrameDadosPRO.configure(background="#e6e6e6")
            FrameDadosPRO.place(x=20, y=240, width=840, height=140)

            Label(FrameDadosPRO, text="Nome: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20,
                                                                                                                  y=10)
            NomeVEND = Entry(FrameDadosPRO)
            NomeVEND.place(x=70, y=10, width=350, height=22.4)
            NomeVEND.insert(0, NomePROvenda)
            NomeVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosPRO, text="CPF: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=430,
                                                                                                                 y=10)
            CpfVEND = Entry(FrameDadosPRO)
            CpfVEND.place(x=470, y=10, width=150, height=22.4)
            CpfVEND.insert(0, CpfPROvenda)
            CpfVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosPRO, text="Telefone: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(
                x=630, y=10)
            FoneVEND = Entry(FrameDadosPRO)
            FoneVEND.place(x=700, y=10, width=115, height=22.4)
            FoneVEND.insert(0, FonePROvenda)
            FoneVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosPRO, text="Endereço: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(
                x=20, y=40)
            EnderecVEND = Entry(FrameDadosPRO)
            EnderecVEND.place(x=90, y=40, width=725, height=22.4)
            EnderecVEND.insert(0, EndPROvenda)
            EnderecVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            Label(FrameDadosPRO, text="Responsável: ", background="#FFF", foreground="#000",
                  font="Arial 10 bold").place(x=20, y=70)
            ResponVEND = Entry(FrameDadosPRO)
            ResponVEND.place(x=110, y=70, width=300, height=22.4)
            ResponVEND.insert(0, NomePROvenda)
            ResponVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#900", state="readonly")

            # ________________________Frame dados do Cliente/Comprador_________________________#

            FrameDadosCLI = LabelFrame(FrameVENDA, text="Dados do Cliente/Comprador", font="Arial 11 bold",
                                       foreground="#099", borderwidth='3')
            FrameDadosCLI.configure(background="#e6e6e6")
            FrameDadosCLI.place(x=20, y=390, width=840, height=160)

            Label(FrameDadosCLI, text="Nome: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20,
                                                                                                                  y=10)
            NomeCliVEND = Entry(FrameDadosCLI)
            NomeCliVEND.place(x=70, y=10, width=350, height=22.4)
            NomeCliVEND.configure(font="Arial 12", foreground="#009", background="#f2f2f2")

            Label(FrameDadosCLI, text="CPF: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=430,
                                                                                                                 y=10)
            CpfCliVEND = Entry(FrameDadosCLI)
            CpfCliVEND.place(x=470, y=10, width=150, height=22.4)
            CpfCliVEND.configure(font="Arial 12", foreground="#009", background="#f2f2f2")

            Label(FrameDadosCLI, text="RG: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=630,
                                                                                                                y=10)
            RgCliVEND = Entry(FrameDadosCLI)
            RgCliVEND.place(x=660, y=10, width=155, height=22.4)
            RgCliVEND.configure(font="Arial 12", foreground="#009", background="#f2f2f2")

            Label(FrameDadosCLI, text="Endereço: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(
                x=20, y=40)
            EndCliVEND = Entry(FrameDadosCLI)
            EndCliVEND.place(x=90, y=40, width=725, height=22.4)
            EndCliVEND.configure(font="Arial 12", foreground="#009", background="#f2f2f2")

            Label(FrameDadosCLI, text="Fone/Whats: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(
                x=20, y=70)
            FoneCliVEND = Entry(FrameDadosCLI)
            FoneCliVEND.place(x=105, y=70, width=150, height=22.4)
            FoneCliVEND.configure(font="Arial 12", foreground="#009", background="#f2f2f2")

            # ________________________Frame dados Monetários_________________________#

            FrameDadosFIN = LabelFrame(FrameVENDA, text="Dados Financeiros", font="Arial 11 bold", foreground="#099",
                                       borderwidth='3')
            FrameDadosFIN.configure(background="#e6e6e6")
            FrameDadosFIN.place(x=20, y=560, width=840, height=180)

            AppVENDA.transient(appVCU)
            AppVENDA.mainloop()
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

    ### Gridview da ABA CONSULTAR VEÍCULO ###
    quadroGrid = LabelFrame(FrameLab4, text="Dados dos Veículos", relief="flat", background="#e6e6e6")
    quadroGrid.place(x=10, y=10, width=1180, height=760)

    tv = ttk.Treeview(quadroGrid, columns=(
    'Modelo', 'Marca', 'Cor', 'Ano', 'Combustivel', 'Proprietário', 'Formas de Pagamento', 'Renavam', 'Placa',
    'Situação Financeira', 'Valor FIPE', 'Valor do Proprietário', 'Acessórios', 'Status'), show='headings')
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

    # configurar as Scrolls da ABA CONSULTAR VEÍCULO
    tv.configure(yscrollcommand=VScroll.set, xscrollcommand=OScroll.set)

    ### FRAMES da ABA CONSULTAR VEÍCULOS ###
    # Frame de SELECT
    FrameBusca = LabelFrame(quadroGrid, text="Opções de busca", font="Arial 12 italic", borderwidth='3')
    FrameBusca.configure(background="#e6e6e6")
    FrameBusca.place(x=2, y=500, width=1170, height=108)

    FrameAttVE = LabelFrame(quadroGrid, text="Atualizar dados do Veículo Selecionado", font="Arial 12 italic", borderwidth='3')
    FrameAttVE.configure(background="#e6e6e6")
    FrameAttVE.place(x=2, y=620, width=330, height=108)

    FrameDelVE = LabelFrame(quadroGrid, text="Excluir dados do Veículo Selecionado", font="Arial 12 italic", borderwidth='3')
    FrameDelVE.configure(background="#e6e6e6")
    FrameDelVE.place(x=415, y=620, width=330, height=108)

    FrameVendaVE = LabelFrame(quadroGrid, text="Realizar Venda do Veículo Selecionado", font="Arial 12 italic", borderwidth='3')
    FrameVendaVE.configure(background="#e6e6e6")
    FrameVendaVE.place(x=840, y=620, width=330, height=108)

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

    # Busca por PROPRIETARIO
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
    txtBuscStt.configure(width=20, font="arial 14", state="readonly")
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
    btnVendVE = Button(FrameVendaVE, text="Vender Veículo", command=VenderVE)
    btnVendVE.configure(font="arial 12 bold", background="#0f3", foreground="#000")
    btnVendVE.place(x=50, y=20, width=220, height=40)


#  Criando os menús da tela principal #
barraMenu = Menu(appVCU)

# Menu do Proprietario
menuPro = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label=" Opções do Proprietário", menu=menuPro)
menuPro.add_command(label="Cadastrar Proprietário", command=ABA_CAD_Propri)
menuPro.add_separator()
menuPro.add_command(label="Buscar Proprietário", command=ABA_Consu_Propri)

# Menu do Veículo
menuVeic = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Opções do Veículo", menu=menuVeic)
menuVeic.add_command(label="Cadastrar Veículo", command=ABA_CAD_Veic)
menuVeic.add_separator()
menuVeic.add_command(label="Buscar Veículo", command=ABA_Consu_Veic)

# Menu Informações do Software
menuVCU = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Opções do software", menu=menuVCU)
menuVCU.add_command(label="Informações da Versão", command=semComando)
menuVCU.add_separator()
menuVCU.add_command(label="Desenvolvedores", command=semComando)
menuVCU.add_separator()
menuVCU.add_command(label="Support", command=semComando)
menuVCU.add_separator()
menuVCU.add_command(label="Ajuda", command=semComando)
menuVCU.add_separator()
menuVCU.add_command(label="Redes Sociais do Software", command=semComando)

CloseApp = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Fechar App", menu=CloseApp)
CloseApp.add_command(label="Sair", command=quit)


#  executa o programa em loop  #
appVCU.config(menu=barraMenu)
appVCU.mainloop()