from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sqlite3 import Error
from reportlab.pdfgen import canvas
import webbrowser
from time import strftime
import VCU_QUERY

#   propriedades da janela  #
appVCU = Tk()
appVCU.title(" Venda de Carros Usados®")
appVCU.geometry("1280x700")
appVCU.configure(background="#f2f2f2")
appVCU.wm_iconbitmap('icon_VCU.ico')

#  Criação das ABAS  #
ABA = ttk.Notebook(appVCU)
ABA.pack(fill='both', expand=1)

abaBemVindo = Frame(ABA)
ABA.add(abaBemVindo, text="Tela Inicial")

img = PhotoImage(file="Car_VCU.png")
Label(abaBemVindo, text="Sistema de Venda de Carros Usados", font="Centaur 50 bold", background="white").pack(fill='both', expand=True)

lblImagem = Label(abaBemVindo, image=img, background="white").pack(fill='y', expand=True)
abaBemVindo.configure(background="white")

def tic():
    relogio['text'] = strftime('%d/%m/%Y  %H:%M:%S')
def tac():
    tic()
    relogio.after(1000, tac)

relogio = ttk.Label(abaBemVindo, background="white",foreground="black", font='Helvetica 25 bold')
relogio.pack(fill='none', expand=True, side='top')
tac()

def Config_Vendedores():
    abaConf_Vend = Frame(ABA)
    ABA.add(abaConf_Vend, text="Propriedades dos Vendedores")
    abaConf_Vend.configure(background="darkgray")
    ABA.forget(0)

    # Label Frame
    lblFramVend = LabelFrame(abaConf_Vend, text="Opções dos Vendedores", font="arialBlack 12 bold italic", bg="darkgray", fg="black", relief="ridge", borderwidth="10" )
    lblFramVend.pack(fill='none', expand=True, ipadx=200, ipady=200)

    def CadVendedor():
        appCadVend = Toplevel()
        appCadVend.title(" Cadastro de Vendedores")
        appCadVend.geometry("900x700")
        appCadVend.resizable(False, False)
        appCadVend.configure(background="black")
        appCadVend.wm_iconbitmap('icon_VCU.ico')
        appCadVend.focus_force()
        appCadVend.grab_set()

        def SalvarVendedor():
            CodVddrSQL = "SELECT CodVendr FROM Vendedores"
            CodVendedor = str(VCU_QUERY.DQL(CodVddrSQL))

            if txtCodVendedor.get() != "" and txtCodVendedor.get() in CodVendedor:
                messagebox.showwarning(title=" Código já Cadastrado!",
                                       message="Este Código já está Existe em nossa base de dados! Por favor, escolha outro")
            elif (txtCodVendedor.get() != "" and txtNomeVendedor.get() != "") and (txtRgVendedor.get() != "") and (txtCpfVendedor.get() != "") and (txtEndVendedor != "") and (txtFoneVendedor.get() != ""):
                sCodvddr = txtCodVendedor.get()
                sNomevddr = txtNomeVendedor.get()
                sRGvddr = txtRgVendedor.get()
                sCPFvddr = txtCpfVendedor.get()
                sEnderecovddr = txtEndVendedor.get()
                sTelefonevddr = txtFoneVendedor.get()

                SalvarVDDRquery = "INSERT INTO Vendedores(CodVendr, NomeVendr, RGVendr, CPFVendr, EndVendr, FoneVendr) VALUES ('" + sCodvddr + "', '" + sNomevddr + "', '" + sRGvddr + "', '" + sCPFvddr + "', '" + sEnderecovddr + "', '" + sTelefonevddr + "')"
                VCU_QUERY.DML(SalvarVDDRquery)
                messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados cadastrados com sucesso!")
                txtCodVendedor.delete(0, END)
                txtNomeVendedor.delete(0, END)
                txtRgVendedor.delete(0, END)
                txtCpfVendedor.delete(0, END)
                txtEndVendedor.delete(0, END)
                txtFoneVendedor.delete(0, END)

                txtCodVendedor.focus_set()
            else:
                messagebox.showwarning(title=" Campos Vazios!", message="Por favor, preencha todos os campos para realizar o cadastro!")

        def TelaInicial():
            appCadVend.destroy()
            ABA.forget(0)
            ABA.add(abaBemVindo, text="Tela Inicial")
            abaBemVindo.configure(background="white")

        #Frame na ABA cadastro de Vendedores#
        FramCadVend = LabelFrame(appCadVend, text="Novo Vendedor", font="arial 11", foreground="#f00", relief='flat')
        FramCadVend.pack(padx=10, pady=120, ipadx=300, ipady=200)

        Label(FramCadVend, text="Cód. Vendedor(5):", font="arial 11", foreground="#000").place(x=10, y=20)
        txtCodVendedor = Entry(FramCadVend)
        txtCodVendedor.configure(font="arial 12")
        txtCodVendedor.place(x=10, y=45, width=110, height=25)

        Label(FramCadVend, text="Nome: ", font="arial 11", foreground="#000").place(x=10, y=75)
        txtNomeVendedor = Entry(FramCadVend)
        txtNomeVendedor.configure(font="arial 11")
        txtNomeVendedor.place(x=10, y=100, width=430, height=25)

        Label(FramCadVend, text="RG: ", font="arial 11", foreground="#000").place(x=10, y=130)
        txtRgVendedor = Entry(FramCadVend)
        txtRgVendedor.configure(font="arial 11")
        txtRgVendedor.place(x=10, y=155, width=170, height=25)

        Label(FramCadVend, text="CPF: ", font="arial 11", foreground="#000").place(x=200, y=130)
        txtCpfVendedor = Entry(FramCadVend)
        txtCpfVendedor.configure(font="arial 11")
        txtCpfVendedor.place(x=200, y=155, width=240, height=25)

        Label(FramCadVend, text="Endereço: ", font="arial 11", foreground="#000").place(x=10, y=185)
        txtEndVendedor = Entry(FramCadVend)
        txtEndVendedor.configure(font="arial 11")
        txtEndVendedor.place(x=10, y=208, width=570, height=25)

        Label(FramCadVend, text="Fone/WhatsApp: ", font="arial 11", foreground="#000").place(x=10, y=240)
        txtFoneVendedor = Entry(FramCadVend)
        txtFoneVendedor.configure(font="arial 11")
        txtFoneVendedor.place(x=10, y=265, width=170, height=25)

        btnSalvarVendedor = Button(FramCadVend, text="Salvar", font="ArialBlack 12 bold", bg="blue", fg="white", relief="raised", borderwidth='7', command=SalvarVendedor)
        btnSalvarVendedor.place(x=170, y=310, width=130, height=40)

        btnSairVendedor = Button(FramCadVend, text="Sair", font="ArialBlack 12 bold", bg="green", fg="white", relief="raised", borderwidth='7', command=TelaInicial)
        btnSairVendedor.place(x=320, y=310, width=140, height=40)

        appCadVend.transient(appVCU)
        appCadVend.mainloop()

    def BuscarVendedor():
        appBuscVend = Toplevel()
        appBuscVend.title(" Buscar Vendedores")
        appBuscVend.geometry("900x700")
        appBuscVend.resizable(False, False)
        appBuscVend.configure(background="#ddd")
        appBuscVend.wm_iconbitmap('icon_VCU.ico')
        appBuscVend.focus_force()
        appBuscVend.grab_set()

        # Frames da Tela de Vendedores
        lblFramBuscVend = LabelFrame(appBuscVend, text="Consulta dos Vendedores", font="arialBlack 12 bold italic", bg="#ddd", fg="black", relief="flat")
        lblFramBuscVend.pack(ipadx=420, ipady=500, pady=10)

        FramOpcBuscVendedor = LabelFrame(lblFramBuscVend, text="Opções de Busca", foreground="#f00", font="Arial 11", relief='raised', borderwidth='2')
        FramOpcBuscVendedor.configure(background="#ddd")
        FramOpcBuscVendedor.place(x=2, y=340, width=832, height=170)

        FramAttVendedor = LabelFrame(lblFramBuscVend, text="Atualizar Vendedor Selecionado", foreground="#f00", font="Arial 11", relief='raised', borderwidth='2')
        FramAttVendedor.configure(background="#ddd")
        FramAttVendedor.place(x=2, y=516, width=400, height=140)

        FramDeletVendedor = LabelFrame(lblFramBuscVend, text="Excluir Vendedor Selecionado", foreground="#f00", font="Arial 11", relief='raised', borderwidth='2')
        FramDeletVendedor.configure(background="#ddd")
        FramDeletVendedor.place(x=434, y=516, width=400, height=140)

        # Visualizador dos dados, TreeView na tela de Consultar Vendedor
        tv3 = ttk.Treeview(lblFramBuscVend, columns=('Código', 'Nome', 'RG', 'CPF', 'Endereço', 'Telefone'), show='headings')
        tv3.configure(height=23)
        tv3.column('Código', minwidth=62, width=62)
        tv3.column('Nome', minwidth=200, width=200)
        tv3.column('RG', minwidth=90, width=90)
        tv3.column('CPF', minwidth=90, width=90)
        tv3.column('Endereço', minwidth=268, width=268)
        tv3.column('Telefone', minwidth=100, width=100)

        tv3.heading('Código', text="Cód. Vendedor")
        tv3.heading('Nome', text='Nome')
        tv3.heading('RG', text='RG')
        tv3.heading('CPF', text='CPF')
        tv3.heading('Endereço', text='Endereço')
        tv3.heading('Telefone', text='Telefone')
        tv3.pack(side=LEFT)
        tv3.place(x=0, y=0, height=320)

        # Scrollbar Vertical e Horizontal da tela de Consulta de Vendedores
        VScrollV = ttk.Scrollbar(lblFramBuscVend, orient="vertical", command=tv3.yview)
        VScrollV.place(x=815, y=2, height=317)
        OScrollO = ttk.Scrollbar(lblFramBuscVend, orient="horizontal", command=tv3.xview)
        OScrollO.place(x=0, y=322, width=812)
        tv3.configure(yscrollcommand=VScrollV.set, xscrollcommand=OScrollO.set)

        def PesqCodVendedor():
            tv3.delete(*tv3.get_children())
            if txtBuscCod.get() != "":
                CodVendd = txtBuscCod.get()
                vquery = "SELECT CodVendr, NomeVendr, RGVendr, CPFVendr, EndVendr, FoneVendr FROM Vendedores WHERE CodVendr = '" + CodVendd + "'"
                linhas = VCU_QUERY.DQL(vquery)
                if linhas != []:
                    txtBuscCod.delete(0, END)
                    for x in linhas:
                        tv3.insert("", "end", values=x)
                else:
                    messagebox.showinfo(title=" Atenção!", message="Não encontramos Vendedores com esse Código!")
            else:
                messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

        def PesqNomeVendedor():
            tv3.delete(*tv3.get_children())
            if txtBuscNome.get() != "":
                NomeVendd = txtBuscNome.get()
                vquery = "SELECT CodVendr, NomeVendr, RGVendr, CPFVendr, EndVendr, FoneVendr FROM Vendedores WHERE NomeVendr LIKE '%" + NomeVendd + "%'"
                linhas = VCU_QUERY.DQL(vquery)
                if linhas != []:
                    txtBuscNome.delete(0, END)
                    for x in linhas:
                        tv3.insert("", "end", values=x)
                else:
                    messagebox.showinfo(title=" Atenção!", message="Não encontramos Vendedores com esse Nome!")
            else:
                messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

        def PesqRGVendedor():
            tv3.delete(*tv3.get_children())
            if txtBuscRg.get() != "":
                RgVendd = txtBuscRg.get()
                vquery = "SELECT CodVendr, NomeVendr, RGVendr, CPFVendr, EndVendr, FoneVendr FROM Vendedores WHERE RGVendr = '" + RgVendd + "'"
                linhas = VCU_QUERY.DQL(vquery)
                if linhas != []:
                    txtBuscRg.delete(0, END)
                    for x in linhas:
                        tv3.insert("", "end", values=x)
                else:
                    messagebox.showinfo(title=" Atenção!", message="Não encontramos Vendedores com esse RG!")
            else:
                messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

        def ListarVendedores():
            tv3.delete(*tv3.get_children())
            vquery = "SELECT CodVendr, NomeVendr, RGVendr, CPFVendr, EndVendr, FoneVendr FROM Vendedores"
            linhas = VCU_QUERY.DQL(vquery)
            for x in linhas:
                tv3.insert("", "end", values=x)

        def AttVendedor():
            def UpdateVendedor():
                if (txtATTNomeVendr.get() != "") and (txtATTRgVendr.get() != "") and (txtATTCpfVendr.get() != "") and (txtATTEndVendr.get() != "") and (txtATTFoneVendr.get() != ""):
                    UpCod = txtATTCodVendr.get()
                    UpNome = txtATTNomeVendr.get()
                    UpRG = txtATTRgVendr.get()
                    UpCPF = txtATTCpfVendr.get()
                    UpEndereco = txtATTEndVendr.get()
                    UpFone = txtATTFoneVendr.get()

                    AttProquery = "UPDATE Vendedores SET NomeVendr='" + UpNome + "', RGVendr='" + UpRG + "', CPFVendr='" + UpCPF + "', EndVendr='" + UpEndereco + "', FoneVendr='" + UpFone + "' WHERE CodVendr = '" + UpCod + "'"
                    VCU_QUERY.DML(AttProquery)
                    messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados Atualizados com sucesso!")
                    appAttVendedor.destroy()
                else:
                    messagebox.showwarning(title=" Campos Vazios!", message="Por favor, preencha todos os campos para realizar o cadastro!")

            try:
                ItemSelectVendr = tv3.selection()[0]
                valoresVendr = tv3.item(ItemSelectVendr, "values")

                CodVendrAtt = valoresVendr[0]
                NomeVendrAtt = valoresVendr[1]
                RgVendrAtt = valoresVendr[2]
                CpfVendrAtt = valoresVendr[3]
                EndVendrAtt = valoresVendr[4]
                FoneVendrAtt = valoresVendr[5]

                appAttVendedor = Toplevel()
                appAttVendedor.title(" Atualizando dados do Vendedor")
                appAttVendedor.geometry("900x700")
                appAttVendedor.resizable(False, False)
                appAttVendedor.configure(background="#ddd")
                appAttVendedor.wm_iconbitmap('icon_VCU.ico')
                appAttVendedor.focus_force()
                appAttVendedor.grab_set()

                FramCadVend = LabelFrame(appAttVendedor, text="Novo Vendedor", font="arial 11", foreground="#f00", relief='flat')
                FramCadVend.pack(padx=10, pady=120, ipadx=300, ipady=200)

                Label(FramCadVend, text="Cód. Vendedor(5):", font="arial 11", foreground="#000").place(x=10, y=20)
                txtATTCodVendr = Entry(FramCadVend)
                txtATTCodVendr.place(x=10, y=45, width=110, height=25)
                txtATTCodVendr.insert(0, CodVendrAtt)
                txtATTCodVendr.configure(font="arial 12", state='readonly')

                Label(FramCadVend, text="Nome: ", font="arial 11", foreground="#000").place(x=10, y=75)
                txtATTNomeVendr = Entry(FramCadVend)
                txtATTNomeVendr.place(x=10, y=100, width=430, height=25)
                txtATTNomeVendr.insert(0, NomeVendrAtt)
                txtATTNomeVendr.configure(font="arial 11")

                Label(FramCadVend, text="RG: ", font="arial 11", foreground="#000").place(x=10, y=130)
                txtATTRgVendr = Entry(FramCadVend)
                txtATTRgVendr.place(x=10, y=155, width=170, height=25)
                txtATTRgVendr.insert(0, RgVendrAtt)
                txtATTRgVendr.configure(font="arial 11")

                Label(FramCadVend, text="CPF: ", font="arial 11", foreground="#000").place(x=200, y=130)
                txtATTCpfVendr = Entry(FramCadVend)
                txtATTCpfVendr.place(x=200, y=155, width=240, height=25)
                txtATTCpfVendr.insert(0, CpfVendrAtt)
                txtATTCpfVendr.configure(font="arial 11")

                Label(FramCadVend, text="Endereço: ", font="arial 11", foreground="#000").place(x=10, y=185)
                txtATTEndVendr = Entry(FramCadVend)
                txtATTEndVendr.place(x=10, y=208, width=570, height=25)
                txtATTEndVendr.insert(0, EndVendrAtt)
                txtATTEndVendr.configure(font="arial 11")

                Label(FramCadVend, text="Fone/WhatsApp: ", font="arial 11", foreground="#000").place(x=10, y=240)
                txtATTFoneVendr = Entry(FramCadVend)
                txtATTFoneVendr.place(x=10, y=265, width=170, height=25)
                txtATTFoneVendr.insert(0, FoneVendrAtt)
                txtATTFoneVendr.configure(font="arial 11")

                btnATTSalvarVendr = Button(FramCadVend, text="Salvar alterações", font="ArialBlack 12 bold", bg="yellow", fg="black", relief="raised", borderwidth='7', command=UpdateVendedor)
                btnATTSalvarVendr.place(x=240, y=310, width=160, height=40)

                appAttVendedor.transient(appBuscVend)
                appAttVendedor.mainloop()
            except:
                messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

        def DeletarVendedor():
            try:
                ItemSelect = tv3.selection()[0]
                Valores = tv3.item(ItemSelect, "values")
                CodVendrDEL = Valores[0]

                Message.bell(FramDeletVendedor)
                MsgResult = messagebox.askyesno(title=" Atenção!!!", message="Deseja mesmo exluir o Vendedor selecionado?")
                if MsgResult == True:
                    dquery = "DELETE FROM Vendedores WHERE CodVendr ='" + CodVendrDEL + "'"
                    tv3.delete(ItemSelect)
                    VCU_QUERY.DML(dquery)
            except:
                messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

        # Campos do Frame Opções de Busca da tela consultar Vendedores
        #Busca por Código
        Label(FramOpcBuscVendedor, text="Busca/Código: ", background="#ddd", foreground="#000", font="Arial 12").place(x=20, y=10)
        txtBuscCod = Entry(FramOpcBuscVendedor)
        txtBuscCod.configure(font="arial 12")
        txtBuscCod.place(x=130, y=10, width=60, height=25)

        btnBuscCod = Button(FramOpcBuscVendedor, text="Pesquisar", font="arial 11 bold", bg="#00f", fg="#fff", command=PesqCodVendedor)
        btnBuscCod.place(x=192, y=10, height=25)

        # Busca por Nome
        Label(FramOpcBuscVendedor, text="Busca/Nome: ", background="#ddd", foreground="#000", font="Arial 12").place(x=20, y=55)
        txtBuscNome = Entry(FramOpcBuscVendedor)
        txtBuscNome.configure(font="arial 12")
        txtBuscNome.place(x=120, y=55, width=310, height=25)

        btnBuscNome = Button(FramOpcBuscVendedor, text="Pesquisar", font="arial 11 bold", bg="#00f", fg="#fff", command=PesqNomeVendedor)
        btnBuscNome.place(x=432, y=55, height=25)

        # Busca por RG
        Label(FramOpcBuscVendedor, text="Busca/RG: ", background="#ddd", foreground="#000", font="Arial 12").place(x=20, y=100)
        txtBuscRg = Entry(FramOpcBuscVendedor)
        txtBuscRg.configure(font="arial 12")
        txtBuscRg.place(x=100, y=100, width=160, height=25)

        btnBuscRg = Button(FramOpcBuscVendedor, text="Pesquisar", font="arial 11 bold", bg="#00f", fg="#fff", command=PesqRGVendedor)
        btnBuscRg.place(x=262, y=100, height=25)

        #Botão que Busta todos os Vendedores
        btnBuscTudo = Button(FramOpcBuscVendedor, text="Buscar Tudo", font="arial 12 bold", bg="#00f", fg="#fff", relief="raised", borderwidth='7', command=ListarVendedores)
        btnBuscTudo.place(x=630, y=40, width=140, height=55)

        # Botão atualizar dados do Vendedor
        btnAttVendedor = Button(FramAttVendedor, text="Atualizar Vendedor", font="ArialBlack 12 bold", bg="yellow", fg="black", relief="raised", borderwidth='7', command=AttVendedor)
        btnAttVendedor.place(x=115, y=40, width=180, height=40)

        # Botão Excluir dados do Vendedor
        btnDeletVendedor = Button(FramDeletVendedor, text="Excluir Vendedor", font="ArialBlack 12 bold", bg="red", fg="white", relief="raised", borderwidth='7', command=DeletarVendedor)
        btnDeletVendedor.place(x=120, y=40, width=180, height=40)

        appBuscVend.transient(appVCU)
        appBuscVend.mainloop()

    def TelaInicial():
        ABA.forget(0)
        ABA.add(abaBemVindo, text="Tela Inicial")
        abaBemVindo.configure(background="white")

    # Botão cadastrar Vendedor
    btnCadVend = Button(lblFramVend, text="Cadastrar Vendedor", font="ArialBlack 12 bold", bg="#0f3", fg="black", relief="raised", borderwidth='7', command=CadVendedor)
    btnCadVend.place(x=108, y=110)

    #Botão Consultar Vendedor
    btnConsulVend = Button(lblFramVend, text="Buscar Vendedores", font="ArialBlack 12 bold", bg="blue", fg="white", relief="raised", borderwidth='7', command=BuscarVendedor)
    btnConsulVend.place(x=108, y=175)

    #Botão Sair da ABA e ir para Tela inicial
    btnSairVend = Button(lblFramVend, text="Voltar", font="ArialBlack 12 bold", bg="white", fg="black", relief="raised", borderwidth='7', command=TelaInicial)
    btnSairVend.place(x=160, y=245)

def Relatorio_Venda():
    appRelat = Toplevel()
    appRelat.title(" Venda de Carros Usados®")
    appRelat.geometry("800x600")
    appRelat.configure(background="#c3c3c3")
    appRelat.resizable(False, False)
    appRelat.wm_iconbitmap('icon_VCU.ico')
    appRelat.focus_force()
    appRelat.grab_set()

    FrameRelat = LabelFrame(appRelat, text="Relatório de Vendas", font="Arial 12 bold", bg="#c3c3c3", fg="black", relief='groove', borderwidth='3')
    FrameRelat.place(x=20, y=20, width=760, height=550)

    # Visualizador dos dados, TreeView na tela de Consultar Vendedor
    tvRelat = ttk.Treeview(FrameRelat, columns=('Cód. Venda', 'Cód. Cliente', 'Cód. Vendedor', 'Cód. Veiculo', 'Data', 'Valor Bruto', 'Desconto', 'Valor Vendido', 'Pagamento'), show='headings')
    tvRelat.configure(height=23)
    tvRelat.column('Cód. Venda', minwidth=55, width=55)
    tvRelat.column('Cód. Cliente', minwidth=55, width=55)
    tvRelat.column('Cód. Vendedor', minwidth=65, width=65)
    tvRelat.column('Cód. Veiculo', minwidth=55, width=55)
    tvRelat.column('Data', minwidth=60, width=60)
    tvRelat.column('Valor Bruto', minwidth=60, width=60)
    tvRelat.column('Desconto', minwidth=60, width=60)
    tvRelat.column('Valor Vendido', minwidth=80, width=80)
    tvRelat.column('Pagamento', minwidth=90, width=90)

    tvRelat.heading('Cód. Venda', text="cod.Venda")
    tvRelat.heading('Cód. Cliente', text='cod.Cliente')
    tvRelat.heading('Cód. Vendedor', text='cod.Vendedor')
    tvRelat.heading('Cód. Veiculo', text='cod.Veiculo')
    tvRelat.heading('Data', text='Data')
    tvRelat.heading('Valor Bruto', text='Valor Bruto')
    tvRelat.heading('Desconto', text='Desconto')
    tvRelat.heading('Valor Vendido', text='Valor Vendido')
    tvRelat.heading('Pagamento', text='Pagamento')

    tvRelat.pack(side=LEFT)
    tvRelat.place(x=0, y=0, width=734, height=320)

    # Scrollbar Vertical e Horizontal da tela Relatório de Vendas
    VScrollV = ttk.Scrollbar(FrameRelat, orient="vertical", command=tvRelat.yview)
    VScrollV.place(x=736, y=2, height=317)
    OScrollO = ttk.Scrollbar(FrameRelat, orient="horizontal", command=tvRelat.xview)
    OScrollO.place(x=2, y=322, width=732)
    tvRelat.configure(yscrollcommand=VScrollV.set, xscrollcommand=OScrollO.set)

    # valor atribuido para Label que mostra a quantidade de vendas
    qtdVendido = StringVar()
    qtdVendido.set("0")

    ValorVendido = StringVar()
    ValorVendido.set("0")

    # Label que indica a quantidade de vendas
    Label(FrameRelat, text="Total de vendas", bg="#c3c3c3", fg="black", font="Arial 18 bold").place(x=100, y=370)
    Label(FrameRelat, textvariable=qtdVendido, bg="#c3c3c3", fg="red", font="Arial 35 bold").place(x=100, y=420, width=180)

    Label(FrameRelat, text="Valor total em vendas", bg="#c3c3c3", fg="black", font="Arial 18 bold").place(x=390, y=370)
    Label(FrameRelat, textvariable=ValorVendido, bg="#c3c3c3", fg="red", font="Arial 35 bold").place(x=350, y=420, width=330)

    SelecVendas = "SELECT CodNota, fk_CodCli, fk_CodVendr, fk_CodVeicV, DataVenda, ValorBruto, ValorDesc, ValorVenda, FormaPgto FROM Nota_de_Venda"
    Vendas = VCU_QUERY.DQL(SelecVendas)

    if Vendas != []:
        VendasTotal = len(Vendas)
        qtdVendido.set(VendasTotal)
        for x in Vendas:
            tvRelat.insert("", "end", values=x)

        SelecTQUERY = "SELECT SUM(ValorVenda) FROM Nota_de_Venda"
        ValoresVenda = str(VCU_QUERY.DQL(SelecTQUERY)).replace('[', "").replace(']', "").replace('(', "").replace(')', "").replace(',', "")

        ValorVendido.set("R$ " + ValoresVenda + ',00')
    else:
        messagebox.showinfo(title=" Atenção!", message="Ainda não possuímos vendas!")

    appRelat.transient(appVCU)
    appRelat.mainloop()

def ABA_CAD_Propri():
    aba1 = Frame(ABA)
    ABA.add(aba1, text="Cadastrar Proprietário")
    aba1.configure(background="black")
    ABA.forget(0)

    def salvardadosPRO():
        CpfCnpjSQL = "SELECT CpfCnpjProp FROM Proprietarios"
        CPFs = str(VCU_QUERY.DQL(CpfCnpjSQL))

        CodProSQL = "SELECT CodProp FROM Proprietarios"
        CodigosPro = str(VCU_QUERY.DQL(CodProSQL))

        if vCodPRO.get() != "" and vCodPRO.get() in CodigosPro:
            messagebox.showwarning(title="VCU - Código já Cadastrado!",
                                   message="Este Código já está Existe em nossa base de dados! Por favor, escolha outro")
        elif vCpfPRO.get() in CPFs and vCpfPRO.get() != "":
            messagebox.showwarning(title="VCU - CPF/CNPJ já Cadastrado!",
                                   message="Este CPF/CNPJ já está cadastrado em nossa base de dados!")
        elif (vCodPRO.get() != "" and vNomePRO.get() != "") and (vCpfPRO.get() != "") and (vEnderPRO.get() != "") and (vFonePRO != "") and (
                vResponPRO.get() != ""):
            sCod = vCodPRO.get()
            sNome = vNomePRO.get()
            sCPF = vCpfPRO.get()
            sEndereco = vEnderPRO.get()
            sTelefone = vFonePRO.get()
            sResponsa = vResponPRO.get()
            SalvarPROquery = "INSERT INTO Proprietarios(CodProp, NomeRazaoProp, CpfCnpjProp, EndeProp, FoneProp, RespProp) VALUES ('" + sCod + "', '" + sNome + "', '" + sCPF + "', '" + sEndereco + "', '" + sTelefone + "', '" + sResponsa + "')"
            VCU_QUERY.DML(SalvarPROquery)
            messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados cadastrados com sucesso!")

            vCodPRO.delete(0, END)
            vNomePRO.delete(0, END)
            vCpfPRO.delete(0, END)
            vEnderPRO.delete(0, END)
            vFonePRO.delete(0, END)
            vResponPRO.delete(0, END)
            vCodPRO.focus_set()
        else:
            messagebox.showwarning(title=" Campos Vazios!", message="Por favor, preencha todos os campos para realizar o cadastro!")

    def TelaInicial():
        ABA.forget(0)
        ABA.add(abaBemVindo, text="Tela Inicial")
        abaBemVindo.configure(background="white")

    # Criação da Tabela para dados cadastrais do proprietario

    FrameLab1 = LabelFrame(aba1, text="Cadastro de informações do proprietário", font="Arial 12 italic bold", borderwidth='1', relief="flat")
    FrameLab1.configure(background="#e6e6e6", foreground="#000")
    FrameLab1.pack(fill='none', expand=True, ipadx=300, ipady=180, side='top')

    Label(FrameLab1, text="Cód. Proprietário(5): ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=28)
    vCodPRO = Entry(FrameLab1)
    vCodPRO.configure(font="Arial 12")
    vCodPRO.place(x=30, y=50, width=150, height=25)

    Label(FrameLab1, text="Nome Completo/Razão Social: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=78)
    vNomePRO = Entry(FrameLab1)
    vNomePRO.configure(font="Arial 12")
    vNomePRO.place(x=30, y=100, width=530, height=25)

    Label(FrameLab1, text="CPF/CNPJ: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=128)
    vCpfPRO = Entry(FrameLab1)
    vCpfPRO.configure(font="Arial 12")
    vCpfPRO.place(x=30, y=150, width=260, height=25)

    Label(FrameLab1, text="Telefone para Contato: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=300, y=128)
    vFonePRO = Entry(FrameLab1)
    vFonePRO.configure(font="Arial 12")
    vFonePRO.place(x=300, y=150, width=260, height=25)

    Label(FrameLab1, text="Endereço: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=178)
    vEnderPRO = Entry(FrameLab1)
    vEnderPRO.configure(font="Arial 12")
    vEnderPRO.place(x=30, y=200, width=530, height=25)

    Label(FrameLab1, text="Responsável: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=228)
    vResponPRO = Entry(FrameLab1)
    vResponPRO.configure(font="Arial 12")
    vResponPRO.place(x=30, y=250, width=530, height=25)

    btnSalvar = Button(FrameLab1, text="Cadastrar", background="blue", foreground="#fff", font="ArialBlk 12 bold", relief="raised", borderwidth='6', command=salvardadosPRO)
    btnSalvar.place(x=140, y=290, width=150, height=40)

    btnNovo = Button(FrameLab1, text="Voltar", background="#0f3", foreground="black", font="ArialBlk 12 bold", relief="raised", borderwidth='6', command=TelaInicial)
    btnNovo.place(x=310, y=290, width=150, height=40)


def ABA_CAD_Veic():
    aba2 = Frame(ABA)
    ABA.add(aba2, text="Cadastrar Veículo")
    aba2.configure(background="black")
    ABA.forget(0)

    def salvardadosVE():
        sCodVE = vCodVE.get()
        sCodPRO = vCodProV.get()
        sMarca = vMarca.get()
        sModelo = vModelo.get()
        sFabric = vAnoFabric.get()
        sCor = vCor.get()
        sCombust = vCombust.get()
        sPlaca = vPlaca.get()
        sRenavam = vRenav.get()
        sPortas = vPortas.get()
        sVidroEl = vVidroElet.get()
        sTravaEl = vTravaElet.get()
        sAlarme = vAlarme.get()
        sArCondic = vArCondic.get()
        sSom = vSom.get()
        sOutrosAce = vOutroAces.get()
        sVencIPVA = vVencIPVA.get()
        sValorMulta = vValorMultas.get()
        sValorFipe = vValorFipe.get()
        sValorPro = vValorPro.get()

        Squery = "SELECT CodProp FROM Proprietarios"
        CodPropList = VCU_QUERY.DQL(Squery)

        VEquery = "SELECT CodVeicV FROM Veiculos"
        CodVeList = VCU_QUERY.DQL(VEquery)

        if (sCodVE == "") or (sCodPRO == "") or (sMarca == "") or (sModelo == "") or (sFabric == "") or (sCor == "") or (sCombust == "") or (
                sPlaca == "") or (sRenavam == "") or (sPortas == "") or (
                sVidroEl == "") or (sTravaEl == "") or (sAlarme == "") or (sArCondic == "") or (
                sSom == "") or (sOutrosAce == "") or (sVencIPVA == "") or (sValorMulta == "") or (sValorFipe == "") or (sValorPro == ""):
            messagebox.showwarning(title=" Campos Vazios!", message="Por favor, preencha todos os campos para realizar o cadastro!")
        elif sCodVE in str(CodVeList):
            messagebox.showwarning(title=" Código de Veículo já existe!", message="O Código do veículo informado já existe! Por favor digite outro!")
        elif sCodPRO in str(CodPropList):
            SalvarVEquery = "INSERT INTO Veiculos(CodVeicV, fk_CodProp, MarcaV, ModeloV, AnoFabV, CorV, CombV, PlacaV, RenavanV, PortasV, AcessVEV, AcessTEV, AcessAlV, AcessArV, AcessSomV, AcessOutV, VencIPVA, DocMultasV, ValFipeV, ValVendaMinV) VALUES ('" + sCodVE + "', '" + sCodPRO + "', '" + sMarca + "', '" + sModelo + "', '" + sFabric + "', '" + sCor + "', '" + sCombust + "', '" + sPlaca + "', '" + sRenavam + "', '" + sPortas + "', '" + sVidroEl + "', '" + sTravaEl + "', '" + sAlarme + "', '" + sArCondic + "', '" + sSom + "', '" + sOutrosAce + "', '" + sVencIPVA + "', '" + sValorMulta + "', '" + sValorFipe + "', '" + sValorPro + "')"
            VCU_QUERY.DML(SalvarVEquery)
            messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados do Veículo Salvo com Sucesso!")
            vCodVE.delete(0, END)
            vCodProV.delete(0, END)
            vMarca.delete(0, END)
            vModelo.delete(0, END)
            vAnoFabric.delete(0, END)
            vCor.delete(0, END)
            vCombust.set("")
            vPlaca.delete(0, END)
            vRenav.delete(0, END)
            vPortas.set("")
            vVidroElet.set("")
            vTravaElet.set("")
            vAlarme.set("")
            vArCondic.set("")
            vSom.set("")
            vOutroAces.delete(0, END)
            vVencIPVA.delete(0, END)
            vValorMultas.delete(0, END)
            vValorFipe.delete(0, END)
            vValorPro.delete(0, END)

            vCodVE.focus_set()
        else:
            messagebox.showwarning(title=" Proprietário Não Cadastrado!",
                                   message="Código de proprietário não confere com nenhum proprietário Cadastrado! Verifique o código digitado e tente novamente!")

    def TelaInicial():
        ABA.forget(0)
        ABA.add(abaBemVindo, text="Tela Inicial")
        abaBemVindo.configure(background="white")

    FrameLab2 = LabelFrame(aba2, text="Cadastro de informações do veículo", font="Arial 12 italic bold", borderwidth='1', relief="flat")
    FrameLab2.configure(background="#e6e6e6")
    FrameLab2.pack(fill='none', expand=True, ipadx=380, ipady=210, side='top')

    # tabela para dados cadastrais do veículo

    Label(FrameLab2, text="Código Veículo(5): ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=28)
    vCodVE = Entry(FrameLab2)
    vCodVE.configure(font="Arial 12")
    vCodVE.place(x=30, y=50, width=130, height=25)

    Label(FrameLab2, text="Código Proprietário(5): ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=180, y=28)
    vCodProV = Entry(FrameLab2)
    vCodProV.configure(font="Arial 12")
    vCodProV.place(x=180, y=50, width=150, height=25)

    Label(FrameLab2, text="Marca: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=78)
    vMarca = Entry(FrameLab2)
    vMarca.configure(font="Arial 12")
    vMarca.place(x=30, y=100, width=310, height=25)

    Label(FrameLab2, text="Modelo: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=360, y=78)
    vModelo = Entry(FrameLab2)
    vModelo.configure(font="Arial 12")
    vModelo.place(x=360, y=100, width=370, height=25)

    Label(FrameLab2, text="Ano de Fabricação: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=128)
    vAnoFabric = Entry(FrameLab2)
    vAnoFabric.configure(font="Arial 12")
    vAnoFabric.place(x=30, y=150, width=180, height=25)

    Label(FrameLab2, text="Cor: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=230, y=128)
    vCor = Entry(FrameLab2)
    vCor.configure(font="Arial 12")
    vCor.place(x=230, y=150, width=240, height=25)

    Label(FrameLab2, text="Combustível: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=490, y=128)
    vCombust = ttk.Combobox(FrameLab2, values="Gasolina Etanol Flex Diesel Elétrico Energia-Solar", state="readonly")
    vCombust.configure(font="Arial 12")
    vCombust.place(x=490, y=150, width=240, height=25)

    Label(FrameLab2, text="Placa: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=178)
    vPlaca = Entry(FrameLab2)
    vPlaca.configure(font="Arial 12")
    vPlaca.place(x=30, y=200, width=310, height=25)

    Label(FrameLab2, text="Renavan: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=360, y=178)
    vRenav = Entry(FrameLab2)
    vRenav.configure(font="Arial 12")
    vRenav.place(x=360, y=200, width=370, height=25)

    Label(FrameLab2, text="Portas: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=228)
    vPortas = ttk.Combobox(FrameLab2, values="2 3 4 5 6", state="readonly")
    vPortas.configure(font="Arial 12")
    vPortas.place(x=30, y=250, width=50, height=25)

    Label(FrameLab2, text="Vidro Elétr.: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=95, y=228)
    vVidroElet = ttk.Combobox(FrameLab2, values="Sim Não", state="readonly")
    vVidroElet.configure(font="Arial 12")
    vVidroElet.place(x=95, y=250, width=80, height=25)

    Label(FrameLab2, text="Trava Elétr.: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=190, y=228)
    vTravaElet = ttk.Combobox(FrameLab2, values="Sim Não", state="readonly")
    vTravaElet.configure(font="Arial 12")
    vTravaElet.place(x=190, y=250, width=80, height=25)

    Label(FrameLab2, text="Alarme: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=285, y=228)
    vAlarme = ttk.Combobox(FrameLab2, values="Sim Não", state="readonly")
    vAlarme.configure(font="Arial 12")
    vAlarme.place(x=285, y=250, width=80, height=25)

    Label(FrameLab2, text="Ar Condic.: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=380, y=228)
    vArCondic = ttk.Combobox(FrameLab2, values="Sim Não", state="readonly")
    vArCondic.configure(font="Arial 12")
    vArCondic.place(x=380, y=250, width=80, height=25)

    Label(FrameLab2, text="Som: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=475, y=228)
    vSom = ttk.Combobox(FrameLab2, values="Sim Não", state="readonly")
    vSom.configure(font="Arial 12")
    vSom.place(x=475, y=250, width=80, height=25)

    Label(FrameLab2, text="Outros: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=570, y=228)
    vOutroAces = Entry(FrameLab2)
    vOutroAces.configure(font="Arial 12")
    vOutroAces.place(x=570, y=250, width=160, height=25)

    Label(FrameLab2, text="Vencimento IPVA: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=278)
    vVencIPVA = Entry(FrameLab2)
    vVencIPVA.configure(font="Arial 12")
    vVencIPVA.place(x=30, y=300, width=130, height=25)

    Label(FrameLab2, text="Valor das Multas: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=180, y=278)
    vValorMultas = Entry(FrameLab2)
    vValorMultas.configure(font="Arial 12")
    vValorMultas.place(x=180, y=300, width=130, height=25)

    Label(FrameLab2, text="Valor na tabela FIPE: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=330, y=278)
    vValorFipe = Entry(FrameLab2)
    vValorFipe.configure(font="Arial 12")
    vValorFipe.place(x=330, y=300, width=150, height=25)

    Label(FrameLab2, text="Valor do proprietário: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=500, y=278)
    vValorPro = Entry(FrameLab2)
    vValorPro.configure(font="Arial 12")
    vValorPro.place(x=500, y=300, width=150, height=25)

    btnSalvar = Button(FrameLab2, text="Cadastrar", background="blue", foreground="#fff", font="ArialBlk 12 bold", relief="raised", borderwidth='6', command=salvardadosVE)
    btnSalvar.place(x=230, y=340, width=130, height=40)

    btnNovoCadVE = Button(FrameLab2, text="Voltar", background="#0f3", foreground="black", font="ArialBlk 12 bold", relief="raised", borderwidth='6', command=TelaInicial)
    btnNovoCadVE.place(x=380, y=340, width=150, height=40)

def ABA_Consu_Propri():
    aba3 = Frame(ABA)
    ABA.add(aba3, text="Consultar Proprietário")
    aba3.configure(background="black")
    ABA.forget(0)

    def TelaInicial():
        ABA.forget(0)
        ABA.add(abaBemVindo, text="Tela Inicial")
        abaBemVindo.configure(background="white")

    FrameLab3 = LabelFrame(aba3, text="Opções da busca dos Proprietários", font="Arial 12 italic bold", borderwidth='1', relief="flat")
    FrameLab3.configure(background="#e6e6e6")
    FrameLab3.pack(fill='none', expand=True, ipadx=440, ipady=305, side='top')

    # ABA Consultar Proprietário
    def PesquisarCPF():
        tv1.delete(*tv1.get_children())
        if nomePesq6.get() != "":
            vquery = "SELECT CodProp, NomeRazaoProp, CpfCnpjProp, EndeProp, FoneProp, RespProp FROM Proprietarios WHERE CpfCnpjProp LIKE '%" + nomePesq6.get() + "%'"
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
            vquery = "SELECT CodProp, NomeRazaoProp, CpfCnpjProp, EndeProp, FoneProp, RespProp FROM Proprietarios WHERE NomeRazaoProp LIKE '%" + nomePesq4.get() + "%'"
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
    def PesqCodPRO():
        tv1.delete(*tv1.get_children())
        if nomePesq7.get() != "":
            vquery = "SELECT CodProp, NomeRazaoProp, CpfCnpjProp, EndeProp, FoneProp, RespProp FROM Proprietarios WHERE CodProp LIKE '%" + nomePesq7.get() + "%'"
            linhas = VCU_QUERY.DQL(vquery)
            nomePesq7.delete(0, END)
            if linhas != []:
                for x in linhas:
                    tv1.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos Proprietários com esse Código!")
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    # ABA Consultar Proprietário
    def ListarProprietarios():
        tv1.delete(*tv1.get_children())
        vquery = "SELECT CodProp, NomeRazaoProp, CpfCnpjProp, EndeProp, FoneProp, RespProp FROM Proprietarios"
        linhas = VCU_QUERY.DQL(vquery)
        for x in linhas:
            tv1.insert("", "end", values=x)

    def DeletarPRO():
        try:
            cquery = "SELECT fk_CodProp FROM Veiculos"
            PropricomVE = VCU_QUERY.DQL(cquery)
            ItemSelect = tv1.selection()[0]
            Valores = tv1.item(ItemSelect, "values")
            ValorSelect = Valores[1]
            codProDeletar = Valores[0]
            if ValorSelect not in str(PropricomVE):
                Message.bell(aba3)
                MsgResult = messagebox.askyesno(title=" Atenção!!!", message="Deseja mesmo exluir o Proprietário selecionado?")
                if MsgResult == True:
                    dquery = "DELETE FROM Proprietarios WHERE CodProp ='" + codProDeletar + "'"
                    tv1.delete(ItemSelect)
                    VCU_QUERY.DML(dquery)
            else:
                messagebox.showwarning(title=" Atenção!!!",
                                       message="Não é possivel excluir um proprietário que tenha veículos Cadastrado!")
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

    def AtualizarPRO():
        def UpdatePRO():
            if (AttCodPRO.get() != "") and (AttNomePRO.get() != "") and (AttCpfPRO.get() != "") and (
                    AttFonePRO.get() != "") and (AttEnderPRO.get() != "") and (AttResponPRO.get() != ""):
                UpCod = AttCodPRO.get()
                UpNome = AttNomePRO.get()
                UpCPF = AttCpfPRO.get()
                UpTelefone = AttFonePRO.get()
                UpEndereco = AttEnderPRO.get()
                UpResponsa = AttResponPRO.get()

                AttProquery = "UPDATE Proprietarios SET CodProp='" + UpCod + "', NomeRazaoProp='" + UpNome + "', CpfCnpjProp='" + UpCPF + "', EndeProp='" + UpEndereco + "', FoneProp='" + UpTelefone + "', RespProp='" + UpResponsa + "' WHERE CodProp = '" + CodigoAntigoAtt + "'"
                AttVEproquery = "UPDATE Veiculos SET fk_CodProp='" + UpCod + "' WHERE fk_CodProp='" + CodigoAntigoAtt + "'"
                VCU_QUERY.DML(AttProquery)
                VCU_QUERY.DML(AttVEproquery)
                messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados Atualizados com sucesso!")
                AppATTpro.destroy()
            else:
                messagebox.showwarning(title=" Campos Vazios!", message="Por favor, preencha todos os campos para realizar o cadastro!")

        try:
            ItemSelectPRO = tv1.selection()[0]
            valoresPRO = tv1.item(ItemSelectPRO, "values")

            CodigoAntigoAtt = valoresPRO[0]
            CodProAtt = valoresPRO[0]
            NomeProAtt = valoresPRO[1]
            CpfCnpjProAtt = valoresPRO[2]
            EndereProAtt = valoresPRO[3]
            FoneProAtt = valoresPRO[4]
            ResponProAtt = valoresPRO[5]

            AppATTpro = Toplevel()
            AppATTpro.title(" Atualizando dados do Proprietário")
            AppATTpro.geometry("900x700")
            AppATTpro.resizable(False, False)
            AppATTpro.configure(background="yellow")
            AppATTpro.wm_iconbitmap('icon_VCU.ico')
            AppATTpro.focus_force()
            AppATTpro.grab_set()

            FrameLabPro = LabelFrame(AppATTpro, text="Dados Pessoais do Proprietário", font="Arial 12 italic bold", borderwidth='1', relief="flat")
            FrameLabPro.configure(background="#e6e6e6", foreground="#000")
            FrameLabPro.pack(fill='none', expand=True, ipadx=300, ipady=300, side='top')

            Label(FrameLabPro, text="Cód. Proprietário(5): ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=28)
            AttCodPRO = Entry(FrameLabPro)
            AttCodPRO.place(x=30, y=50, width=150, height=25)
            AttCodPRO.insert(0, CodProAtt)
            AttCodPRO.configure(font="Arial 12", state='readonly')

            Label(FrameLabPro, text="Nome Completo/Razão Social: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=78)
            AttNomePRO = Entry(FrameLabPro)
            AttNomePRO.configure(font="Arial 12")
            AttNomePRO.place(x=30, y=100, width=530, height=25)
            AttNomePRO.insert(0, NomeProAtt)

            Label(FrameLabPro, text="CPF/CNPJ: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=128)
            AttCpfPRO = Entry(FrameLabPro)
            AttCpfPRO.configure(font="Arial 12")
            AttCpfPRO.place(x=30, y=150, width=260, height=25)
            AttCpfPRO.insert(0, CpfCnpjProAtt)

            Label(FrameLabPro, text="Telefone para Contato: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=300, y=128)
            AttFonePRO = Entry(FrameLabPro)
            AttFonePRO.configure(font="Arial 12")
            AttFonePRO.place(x=300, y=150, width=260, height=25)
            AttFonePRO.insert(0, FoneProAtt)

            Label(FrameLabPro, text="Endereço: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=178)
            AttEnderPRO = Entry(FrameLabPro)
            AttEnderPRO.configure(font="Arial 12")
            AttEnderPRO.place(x=30, y=200, width=530, height=25)
            AttEnderPRO.insert(0, EndereProAtt)

            Label(FrameLabPro, text="Responsável: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=228)
            AttResponPRO = Entry(FrameLabPro)
            AttResponPRO.configure(font="Arial 12")
            AttResponPRO.place(x=30, y=250, width=530, height=25)
            AttResponPRO.insert(0, ResponProAtt)

            btnSalvAttPro = Button(FrameLabPro, text="Salvar Alterações", background="blue", foreground="#fff", font="ArialBlk 12 bold", relief="raised", borderwidth='6', command=UpdatePRO)
            btnSalvAttPro.place(x=225, y=290, height=40)

            Label(FrameLabPro, text="V.C.U", background="#e6e6e6", foreground="#009", font="ArialBlk 140 bold").place(x=50, y=340, height=180)
            Label(FrameLabPro, text="Sistema de Venda de Carros Usados®", background="#e6e6e6", foreground="#009", font="ArialBlk 22 bold").place(x=35, y=510, height=40)

            AppATTpro.transient(appVCU)
            AppATTpro.mainloop()
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")


    # Gridview da ABA CONSULTAR PROPRIETARIO
    quadroGrid1 = LabelFrame(FrameLab3, text="Dados dos Proprietários", foreground="#f00", font="Arial 11", relief="flat", background="#e6e6e6")
    quadroGrid1.place(x=10, y=25, width=860, height=760)

    tv1 = ttk.Treeview(quadroGrid1, columns=('Código', 'Nome', 'CPF/CNPJ', 'Endereço', 'Telefone', 'Responsável'), show='headings')
    tv1.configure(height=23)
    tv1.column('Código', minwidth=60, width=60)
    tv1.column('Nome', minwidth=200, width=200)
    tv1.column('CPF/CNPJ', minwidth=120, width=120)
    tv1.column('Endereço', minwidth=200, width=200)
    tv1.column('Telefone', minwidth=120, width=120)
    tv1.column('Responsável', minwidth=130, width=130)

    tv1.heading('Código', text="Código")
    tv1.heading('Nome', text='Nome/Razão Social')
    tv1.heading('CPF/CNPJ', text='CPF/CNPJ')
    tv1.heading('Endereço', text='Endereço')
    tv1.heading('Telefone', text='Telefone')
    tv1.heading('Responsável', text='Responsável')
    tv1.pack(side=LEFT)
    tv1.place(x=0, y=0, height=320)

    # Scrollbar Vertical ABA Consultar PROPRIETARIO
    VScroll2 = ttk.Scrollbar(quadroGrid1, orient="vertical", command=tv1.yview)
    VScroll2.place(x=835, y=2, height=320)

    # Scrollbar Vertical ABA Consultar PROPRIETARIO
    OScroll2 = ttk.Scrollbar(quadroGrid1, orient="horizontal", command=tv1.xview)
    OScroll2.place(x=0, y=322, width=835)

    # configurar as Scrolls ABA Consultar PROPRIETARIO
    tv1.configure(yscrollcommand=VScroll2.set, xscrollcommand=OScroll2.set)

    ### FRAMES da ABA CONSULTAR PROPRIETARIOS ###
    # Frame de SELECT
    FrameBusca1 = LabelFrame(quadroGrid1, text="Opções de busca", font="Arial 11", foreground="#f00", relief='raised', borderwidth='2')
    FrameBusca1.configure(background="#e6e6e6")
    FrameBusca1.place(x=2, y=340, width=850, height=108)

    # _____Frame de Atualizar_____
    FrameAtualizar = LabelFrame(quadroGrid1, text="Atualizar Registro Selecionado", foreground="#f00", font="Arial 11", relief='raised', borderwidth='2')
    FrameAtualizar.configure(background="#e6e6e6")
    FrameAtualizar.place(x=2, y=455, width=420, height=80)

    # _____Frame de Excluir_____
    FrameExcluir = LabelFrame(quadroGrid1, text="Excluir Registro Selecionado", foreground="#f00", font="Arial 11", relief='raised', borderwidth='2')
    FrameExcluir.configure(background="#e6e6e6")
    FrameExcluir.place(x=430, y=455, width=420, height=80)

    # Elementos para quadro de pesquisa da ABA Consultar PROPRIETARIOS
    # ____Busca por NOME____
    LabelPesq4 = Label(FrameBusca1, text="Busca/Nome:")
    LabelPesq4.configure(font="Arial 12", background="#e6e6e6")
    LabelPesq4.place(x=10, y=10)

    nomePesq4 = Entry(FrameBusca1)
    nomePesq4.configure(width=15, font="arial 14")
    nomePesq4.place(x=110, y=10)

    btnPesq4 = Button(FrameBusca1, text="Pesquisar", command=PesquisarNOME)
    btnPesq4.configure(font="arial 10 bold", background="blue", foreground="#fff")
    btnPesq4.place(x=280, y=10)

    # ____Busca por CPF____
    LabelPesq6 = Label(FrameBusca1, text="Busca/CPF/CNPJ:")
    LabelPesq6.configure(font="Arial 12", background="#e6e6e6")
    LabelPesq6.place(x=10, y=50)

    nomePesq6 = Entry(FrameBusca1)
    nomePesq6.configure(width=15, font="arial 14")
    nomePesq6.place(x=145, y=50)

    btnPesq6 = Button(FrameBusca1, text="Pesquisar", command=PesquisarCPF)
    btnPesq6.configure(font="arial 10 bold", background="blue", foreground="#fff")
    btnPesq6.place(x=315, y=50)

    # ____Busca por Código____
    LabelPesq7 = Label(FrameBusca1, text="Busca/Código:")
    LabelPesq7.configure(font="Arial 12", background="#e6e6e6")
    LabelPesq7.place(x=370, y=10)

    nomePesq7 = Entry(FrameBusca1)
    nomePesq7.configure(width=8, font="arial 14")
    nomePesq7.place(x=480, y=10)

    btnPesq7 = Button(FrameBusca1, text="Pesquisar", command=PesqCodPRO)
    btnPesq7.configure(font="arial 10 bold", background="blue", foreground="#fff")
    btnPesq7.place(x=572, y=10)

    # ____botao q busca TODOS os registros na ABA Consultar PROPRIETÁRIOS____
    btnBuscaTudo5 = Button(FrameBusca1, text="Buscar Tudo", command=ListarProprietarios)
    btnBuscaTudo5.configure(width=10, height=2, font="arial 11 bold", background="blue", foreground="#FFF", relief="raised", borderwidth='6')
    btnBuscaTudo5.place(x=680, y=15, width=150, height=50)

    # botão Atualizar dados do Proprietário
    btnAttPRO = Button(FrameAtualizar, text="Atualizar Registro", command=AtualizarPRO)
    btnAttPRO.configure(font="arial 12 bold", background="yellow", foreground="#000", relief="raised", borderwidth='6')
    btnAttPRO.place(x=120, y=10, width=200, height=35)

    # Botão Excluir dados do Proprietário
    btnDelPRO = Button(FrameExcluir, text="Excluir Registro", command=DeletarPRO)
    btnDelPRO.configure(font="arial 12 bold", background="red", foreground="#fff", relief="raised", borderwidth='6')
    btnDelPRO.place(x=120, y=10, width=200, height=35)

    # Botão Voltar para tela inicial
    btnVoltarPRO = Button(FrameLab3, text='Voltar', font="Arial 12 bold", relief='raised', borderwidth='4', command=TelaInicial)
    btnVoltarPRO.configure(bg="white", fg="black")
    btnVoltarPRO.place(x=780, y=0, height=28)

def ABA_Consu_Veic():
    aba4 = Frame(ABA)
    ABA.add(aba4, text="Consultar Veículo")
    aba4.configure(background="black")
    ABA.forget(0)

    FrameLab4 = LabelFrame(aba4, text="Opções da busca dos veículos", font="Arial 12 bold", foreground="#000", borderwidth='1', relief="flat")
    FrameLab4.configure(background="#e6e6e6")
    FrameLab4.pack(fill='none', expand=True, ipadx=635, ipady=300, side='top')

    # ABA Consultar Veículo
    def ListarVeiculos():
        tv.delete(*tv.get_children())
        vquery = "SELECT CodVeicV, fk_CodProp, MarcaV, ModeloV, AnoFabV, CorV, CombV, PlacaV, RenavanV, PortasV, AcessVEV, AcessTEV, AcessAlV, AcessArV, AcessSomV, AcessOutV, VencIPVA, DocMultasV, ValFipeV, ValVendaMinV FROM Veiculos order by CodVeicV"
        linhas = VCU_QUERY.DQL(vquery)
        for x in linhas:
            tv.insert("", "end", values=x)

    # ABA Consultar Veículo
    def PesquisarMODE():
        tv.delete(*tv.get_children())
        if txtPesqMod.get() != "":
            vquery = "SELECT CodVeicV, fk_CodProp, MarcaV, ModeloV, AnoFabV, CorV, CombV, PlacaV, RenavanV, PortasV, AcessVEV, AcessTEV, AcessAlV, AcessArV, AcessSomV, AcessOutV, VencIPVA, DocMultasV, ValFipeV, ValVendaMinV FROM Veiculos WHERE ModeloV LIKE '%" + txtPesqMod.get() + "%'"
            linhas = VCU_QUERY.DQL(vquery)
            if linhas != []:
                for x in linhas:
                    tv.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos veículos com esse Modelo!")
                txtPesqMod.delete(0, END)
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    # ABA Consultar Veículo
    def PesquisarCodPRO():
        tv.delete(*tv.get_children())
        if txtPesqPro.get() != "":
            vquery = "SELECT CodVeicV, fk_CodProp, MarcaV, ModeloV, AnoFabV, CorV, CombV, PlacaV, RenavanV, PortasV, AcessVEV, AcessTEV, AcessAlV, AcessArV, AcessSomV, AcessOutV, VencIPVA, DocMultasV, ValFipeV, ValVendaMinV FROM Veiculos WHERE fk_CodProp LIKE '%" + txtPesqPro.get() + "%'"
            linhas = VCU_QUERY.DQL(vquery)
            if linhas != []:
                for x in linhas:
                    tv.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos veículos com esse Código de Proprietário!")
                txtPesqPro.delete(0, END)
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    # ABA Consultar Veículo
    def PesquisarPLAC():
        tv.delete(*tv.get_children())
        if txtPesqPlaca.get() != "":
            vquery = "SELECT CodVeicV, fk_CodProp, MarcaV, ModeloV, AnoFabV, CorV, CombV, PlacaV, RenavanV, PortasV, AcessVEV, AcessTEV, AcessAlV, AcessArV, AcessSomV, AcessOutV, VencIPVA, DocMultasV, ValFipeV, ValVendaMinV FROM Veiculos WHERE PlacaV LIKE '%" + txtPesqPlaca.get() + "%'"
            linhas = VCU_QUERY.DQL(vquery)
            if linhas != []:
                for x in linhas:
                    tv.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos veículos com essa Placa!")
                txtPesqPlaca.delete(0, END)
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    # ABA Consultar Veículo
    def PesquisarCodVE():
        tv.delete(*tv.get_children())
        if txtPesqCodVE.get() != "":
            CodVE = txtPesqCodVE.get()
            vquery = "SELECT CodVeicV, fk_CodProp, MarcaV, ModeloV, AnoFabV, CorV, CombV, PlacaV, RenavanV, PortasV, AcessVEV, AcessTEV, AcessAlV, AcessArV, AcessSomV, AcessOutV, VencIPVA, DocMultasV, ValFipeV, ValVendaMinV FROM Veiculos WHERE CodVeicV ='" + CodVE + "'"
            linhas = VCU_QUERY.DQL(vquery)
            if linhas != []:
                for x in linhas:
                    tv.insert("", "end", values=x)
            else:
                messagebox.showinfo(title=" Atenção!", message="Não encontramos veículos com esse Código de Veículo!")
                txtPesqCodVE.delete(0, END)
        else:
            messagebox.showinfo(title=" Atenção!", message="Nenhuma informação digitada!")

    def DeletarVE():
        try:
            ItemSelect = tv.selection()[0]
            Valores = tv.item(ItemSelect, "values")
            ValorSelect = Valores[0]
            Message.bell(aba4)
            MsgResult = messagebox.askyesno(title=" Atenção!!!", message="Deseja mesmo exluir o Veículo selecionado?")
            if MsgResult == True:
                dquery = "DELETE FROM Veiculos WHERE CodVeicV ='" + ValorSelect + "'"
                tv.delete(ItemSelect)
                VCU_QUERY.DML(dquery)
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

    def AtualizarVE():
        def UpdateVE():
            if (vCodVE.get() != "") and (vCodProV.get() != "") and (vMarca.get() != "") and (
                    vModelo.get() != "") and (vAnoFabric.get() != "") and (vCor.get() != "") and (
                    vCombust.get() != "") and (vPlaca.get() != "") and (vRenav.get() != "") and (
                    vPortas.get() != "") and (vVidroElet.get() != "") and (vTravaElet.get() != "") and (
                    vAlarme.get() != "") and (vArCondic.get() != "") and (vSom.get() != "") and (
                    vOutroAces.get() != "") and (vVencIPVA.get() != "") and (vValorMultas.get() != "") and (
                    vValorFipe.get() != "") and (vValorPro.get() != ""):
                sCodV = vCodVE.get()
                sCodProV = vCodProV.get()
                sMarca = vMarca.get()
                sModel = vModelo.get()
                sAnoFabri = vAnoFabric.get()
                sCor = vCor.get()
                sCombust = vCombust.get()
                sPlaca = vPlaca.get()
                sRenavan = vRenav.get()
                sPortas = vPortas.get()
                sVidroEl = vVidroElet.get()
                sTravaEl = vTravaElet.get()
                sAlarm = vAlarme.get()
                sArCond = vArCondic.get()
                sSom = vSom.get()
                sOutros = vOutroAces.get()
                sVencIPVA = vVencIPVA.get()
                sValorMulta = vValorMultas.get()
                sValorFIPE = vValorFipe.get()
                sValorPRO = vValorPro.get()

                Upquery = "UPDATE Veiculos SET CodVeicV='" + sCodV + "', fk_CodProp='" + sCodProV + "', MarcaV='" + sMarca + "', ModeloV='" + sModel + "', AnoFabV='" + sAnoFabri + "', CorV='" + sCor + "', CombV='" + sCombust + "', PlacaV='" + sPlaca + "', RenavanV='" + sRenavan + "', PortasV='" + sPortas + "', AcessVEV='" + sVidroEl + "', AcessTEV='" + sTravaEl + "', AcessAlV='" + sAlarm + "', AcessArV='" + sArCond + "', AcessSomV='" + sSom + "', AcessOutV='" + sOutros + "', VencIPVA='" + sVencIPVA + "', DocMultasV='" + sValorMulta + "', ValFipeV='" + sValorFIPE + "', ValVendaMinV='" + sValorPRO + "' WHERE CodVeicV = '" + CodAntigoAtt + "'"
                VCU_QUERY.DML(Upquery)
                messagebox.showinfo(title=" Vendas de Carros Usados", message="Dados Atualizados com sucesso!")
                AppATTve.destroy()
            else:
                messagebox.showwarning(title=" Campos Vazios!", message="Por favor, preencha todos os campos para realizar o cadastro!")

        try:
            ItemSelectVE = tv.selection()[0]
            ValoresVE = tv.item(ItemSelectVE, "values")

            CodAntigoAtt = ValoresVE[0]
            nCodVE = ValoresVE[0]
            nCodPro = ValoresVE[1]
            nMarca = ValoresVE[2]
            nModel = ValoresVE[3]
            nAnoFabri = ValoresVE[4]
            nCor = ValoresVE[5]
            nCombust = ValoresVE[6]
            nPlaca = ValoresVE[7]
            nRenavan = ValoresVE[8]
            nPortas = ValoresVE[9]
            nVidroEl = ValoresVE[10]
            nTravaEl = ValoresVE[11]
            nAlarm = ValoresVE[12]
            nArCond = ValoresVE[13]
            nSom = ValoresVE[14]
            nOutros = ValoresVE[15]
            nVencIPVA = ValoresVE[16]
            nValorMulta = ValoresVE[17]
            nValorFIPE = ValoresVE[18]
            nValorPRO = ValoresVE[19]

            AppATTve = Toplevel()
            AppATTve.title(" Atualizando dados do Veículo")
            AppATTve.geometry("900x700")
            AppATTve.resizable(False, False)
            AppATTve.configure(background="yellow")
            AppATTve.wm_iconbitmap('icon_VCU.ico')
            AppATTve.focus_force()
            AppATTve.grab_set()

            FrameLab2 = LabelFrame(AppATTve, text="Dados do Veículo", font="Arial 12 italic bold", foreground="#000", borderwidth='4', relief="flat")
            FrameLab2.configure(background="#e6e6e6")
            FrameLab2.pack(fill='none', expand=True, ipadx=380, ipady=310, side='top')

            # tabela para dados cadastrais do veículo

            Label(FrameLab2, text="Código Veículo(5): ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=28)
            vCodVE = Entry(FrameLab2)
            vCodVE.place(x=30, y=50, width=130, height=25)
            vCodVE.insert(0, nCodVE)
            vCodVE.configure(font="Arial 12", state='readonly')

            Label(FrameLab2, text="Código Proprietário(5): ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=180, y=28)
            vCodProV = Entry(FrameLab2)
            vCodProV.configure(font="Arial 12")
            vCodProV.place(x=180, y=50, width=150, height=25)
            vCodProV.insert(0, nCodPro)

            Label(FrameLab2, text="Marca: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=78)
            vMarca = Entry(FrameLab2)
            vMarca.configure(font="Arial 12")
            vMarca.place(x=30, y=100, width=310, height=25)
            vMarca.insert(0, nMarca)

            Label(FrameLab2, text="Modelo: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=360, y=78)
            vModelo = Entry(FrameLab2)
            vModelo.configure(font="Arial 12")
            vModelo.place(x=360, y=100, width=370, height=25)
            vModelo.insert(0, nModel)

            Label(FrameLab2, text="Ano de Fabricação: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=128)
            vAnoFabric = Entry(FrameLab2)
            vAnoFabric.configure(font="Arial 12")
            vAnoFabric.place(x=30, y=150, width=180, height=25)
            vAnoFabric.insert(0, nAnoFabri)

            Label(FrameLab2, text="Cor: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=230, y=128)
            vCor = Entry(FrameLab2)
            vCor.configure(font="Arial 12")
            vCor.place(x=230, y=150, width=240, height=25)
            vCor.insert(0, nCor)

            Label(FrameLab2, text="Combustível: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=490, y=128)
            vCombust = ttk.Combobox(FrameLab2, values="Gasolina Etanol Flex Diesel Elétrico Energia-Solar")
            vCombust.configure(font="Arial 12")
            vCombust.place(x=490, y=150, width=240, height=25)
            vCombust.insert(0, nCombust)

            Label(FrameLab2, text="Placa: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=178)
            vPlaca = Entry(FrameLab2)
            vPlaca.configure(font="Arial 12")
            vPlaca.place(x=30, y=200, width=310, height=25)
            vPlaca.insert(0, nPlaca)

            Label(FrameLab2, text="Renavan: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=360, y=178)
            vRenav = Entry(FrameLab2)
            vRenav.configure(font="Arial 12")
            vRenav.place(x=360, y=200, width=370, height=25)
            vRenav.insert(0, nRenavan)

            Label(FrameLab2, text="Portas: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=228)
            vPortas = ttk.Combobox(FrameLab2, values="2 3 4 ")
            vPortas.configure(font="Arial 12")
            vPortas.place(x=30, y=250, width=50, height=25)
            vPortas.insert(0, nPortas)

            Label(FrameLab2, text="Vidro Elétr.: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=95, y=228)
            vVidroElet = ttk.Combobox(FrameLab2, values="Sim Não")
            vVidroElet.configure(font="Arial 12")
            vVidroElet.place(x=95, y=250, width=80, height=25)
            vVidroElet.insert(0, nVidroEl)

            Label(FrameLab2, text="Trava Elétr.: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=190, y=228)
            vTravaElet = ttk.Combobox(FrameLab2, values="Sim Não")
            vTravaElet.configure(font="Arial 12")
            vTravaElet.place(x=190, y=250, width=80, height=25)
            vTravaElet.insert(0, nTravaEl)

            Label(FrameLab2, text="Alarme: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=285, y=228)
            vAlarme = ttk.Combobox(FrameLab2, values="Sim Não")
            vAlarme.configure(font="Arial 12")
            vAlarme.place(x=285, y=250, width=80, height=25)
            vAlarme.insert(0, nAlarm)

            Label(FrameLab2, text="Ar Condic.: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=380, y=228)
            vArCondic = ttk.Combobox(FrameLab2, values="Sim Não")
            vArCondic.configure(font="Arial 12")
            vArCondic.place(x=380, y=250, width=80, height=25)
            vArCondic.insert(0, nArCond)

            Label(FrameLab2, text="Som: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=475, y=228)
            vSom = ttk.Combobox(FrameLab2, values="Sim Não")
            vSom.configure(font="Arial 12")
            vSom.place(x=475, y=250, width=80, height=25)
            vSom.insert(0, nSom)

            Label(FrameLab2, text="Outros: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=570, y=228)
            vOutroAces = Entry(FrameLab2)
            vOutroAces.configure(font="Arial 12")
            vOutroAces.place(x=570, y=250, width=160, height=25)
            vOutroAces.insert(0, nOutros)

            Label(FrameLab2, text="Vencimento IPVA: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=30, y=278)
            vVencIPVA = Entry(FrameLab2)
            vVencIPVA.configure(font="Arial 12")
            vVencIPVA.place(x=30, y=300, width=130, height=25)
            vVencIPVA.insert(0, nVencIPVA)

            Label(FrameLab2, text="Valor das Multas: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=180, y=278)
            vValorMultas = Entry(FrameLab2)
            vValorMultas.configure(font="Arial 12")
            vValorMultas.place(x=180, y=300, width=130, height=25)
            vValorMultas.insert(0, nValorMulta)

            Label(FrameLab2, text="Valor na tabela FIPE: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=330, y=278)
            vValorFipe = Entry(FrameLab2)
            vValorFipe.configure(font="Arial 12")
            vValorFipe.place(x=330, y=300, width=150, height=25)
            vValorFipe.insert(0, nValorFIPE)

            Label(FrameLab2, text="Valor do proprietário: ", background="#e6e6e6", foreground="#000", font="Arial 11").place(x=500, y=278)
            vValorPro = Entry(FrameLab2)
            vValorPro.configure(font="Arial 12")
            vValorPro.place(x=500, y=300, width=150, height=25)
            vValorPro.insert(0, nValorPRO)

            btnUpdate = Button(FrameLab2, text="Salvar Alterações", background="blue", foreground="#fff", font="ArialBlk 12 bold", relief="raised", borderwidth='6', command=UpdateVE)
            btnUpdate.place(x=300, y=340, width=160, height=40)

            Label(FrameLab2, text="V.C.U", background="#e6e6e6", foreground="#009", font="ArialBlk 140 bold").place(x=130, y=380, height=180)
            Label(FrameLab2, text="Sistema de Venda de Carros Usados®", background="#e6e6e6", foreground="#009", font="ArialBlk 22 bold").place(x=115, y=550, height=40)

            AppATTve.transient(appVCU)
            AppATTve.mainloop()
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

    def VenderVE():
        try:
            ItemSelectVE = tv.selection()[0]
            ValoresVE = tv.item(ItemSelectVE, "values")

            vVendcodVE = ValoresVE[0]
            vVendcodPRO = ValoresVE[1]
            vVendMarca = ValoresVE[2]
            vVendModel = ValoresVE[3]
            vVendAnoFabri = ValoresVE[4]
            vVendCor = ValoresVE[5]
            vVendCombust = ValoresVE[6]
            vVendPlaca = ValoresVE[7]
            vVendRenavan = ValoresVE[8]
            vVendPortas = ValoresVE[9]
            vVendVidroEl = ValoresVE[10]
            vVendTravaEl = ValoresVE[11]
            vVendAlarm = ValoresVE[12]
            vVendArCond = ValoresVE[13]
            vVendSom = ValoresVE[14]
            vVendOutros = ValoresVE[15]
            vVendVencIPVA = ValoresVE[16]
            vVendValorMulta = ValoresVE[17]
            vVendValorFIPE = ValoresVE[18]
            vVendValorPRO = ValoresVE[19]

            selectQuery = "SELECT CodProp, NomeRazaoProp, CpfCnpjProp, EndeProp, FoneProp, RespProp FROM Proprietarios WHERE CodProp ='" + vVendcodPRO + "'"
            PROvenda = VCU_QUERY.DQL(selectQuery)

            NomePROvenda = "nome"
            CpfPROvenda = "CPF"
            EndPROvenda = "Endereço"
            FonePROvenda = "telefone"
            ResponPROvenda = "responsavel"
            for x in PROvenda:
                NomePROvenda = x[1]
                CpfPROvenda = x[2]
                EndPROvenda = x[3]
                FonePROvenda = x[4]
                ResponPROvenda = x[5]

            # noinspection PyUnboundLocalVariable
            # Para Orçamento
            def Gerar_PDF():
                try:
                    SelecCODvddr = "SELECT CodVendr FROM Vendedores"
                    CodVendedor = VCU_QUERY.DQL(SelecCODvddr)

                    cod_Venddr = vCodVendrVendaFIN.get()
                    if vCodVendrVendaFIN.get == "" or vValBrutVenFIN.get() == "" or vValDescVenFIN.get() == "" or vValorTotaVendFIN.get() == "" or vDataVendaFIN.get() == "" or vFormaPGVendaFIN.get() == "":
                        messagebox.showwarning(title="Campo Vazio!", message="Preencha todos os campos do quadro 'Considerações Finais' para poder emitir um Orçamento!")
                    elif len(cod_Venddr) < 5 or cod_Venddr not in str(CodVendedor):
                        messagebox.showwarning(title="Atenção!", message="Código de Vendedor não existe! Verifique o código digitado e tente novamente.")
                        vCodVendrVendaFIN.delete(0, END)
                        vCodVendrVendaFIN.focus_set()
                    else:
                        def Abrir_PDF():
                            webbrowser.open("Orcamento.pdf")

                        Can = canvas.Canvas("Orcamento.pdf")

                        Can.setFont("Helvetica-Bold", 24)
                        Can.drawString(180, 790, 'Orçamento de veículo')

                        # Criar uma linha separadora
                        Can.rect(25, 765, 540, 1, fill=True, stroke=False)

                        Can.setFont("Helvetica-Bold", 13)
                        Can.drawString(250, 745, 'Dados do Veículo')

                        Can.setFont("Helvetica-Bold", 11)
                        Can.drawString(30, 715, 'Cód. do Veículo: ')
                        Can.drawString(30, 700, 'Marca: ')
                        Can.drawString(30, 685, 'Modelo: ')
                        Can.drawString(30, 670, 'Ano de Fabricação: ')
                        Can.drawString(30, 655, 'Cor: ')
                        Can.drawString(30, 640, 'Combustível: ')
                        Can.drawString(30, 625, 'Placa: ')
                        Can.drawString(30, 610, 'Renavan: ')
                        Can.drawString(30, 595, 'Vencimento IPVA: ')
                        Can.drawString(190, 595, 'Valor de FIPE: ')
                        Can.drawString(370, 595, 'Valor do Proprietário: ')

                        Can.drawString(330, 715, 'Portas: ')
                        Can.drawString(330, 700, 'Vidro Elétr.: ')
                        Can.drawString(330, 685, 'Trava Elétr.: ')
                        Can.drawString(330, 670, 'Alarme: ')
                        Can.drawString(330, 655, 'Ar Condic.: ')
                        Can.drawString(330, 640, 'Som: ')
                        Can.drawString(330, 625, 'Outros: ')

                        # Valores atribuidos dos campos preenchidos na tela de venda
                        Can.setFont("Helvetica", 12)
                        Can.drawString(121, 715, vVendcodVE)
                        Can.drawString(68, 700, vVendMarca)
                        Can.drawString(75, 685, vVendModel)
                        Can.drawString(136, 670, vVendAnoFabri)
                        Can.drawString(57, 655, vVendCor)
                        Can.drawString(103, 640, vVendCombust)
                        Can.drawString(66, 625, vVendPlaca)
                        Can.drawString(82, 610, vVendRenavan)
                        Can.drawString(127, 595, vVendVencIPVA)
                        Can.drawString(267, 595, 'R$ ' + vVendValorFIPE + ',00')
                        Can.drawString(487, 595, 'R$ ' + vVendValorPRO + ',00')

                        Can.drawString(372, 715, vVendPortas)
                        Can.drawString(397, 700, vVendVidroEl)
                        Can.drawString(397, 685, vVendTravaEl)
                        Can.drawString(375, 670, vVendAlarm)
                        Can.drawString(393, 655, vVendArCond)
                        Can.drawString(361, 640, vVendSom)
                        Can.drawString(372, 625, vVendOutros)

                        # Criar uma linha separadora
                        Can.rect(25, 580, 540, 1, fill=True, stroke=False)

                        Can.setFont("Helvetica-Bold", 13)
                        Can.drawString(250, 560, 'Dados Financeiros')

                        Can.setFont("Helvetica-Bold", 11)
                        Can.drawString(30, 530, 'Vendedor: ')
                        Can.drawString(30, 515, 'Valor Bruto: ')
                        Can.drawString(30, 500, 'Valor em Multas: ')
                        Can.drawString(30, 485, 'Valor de Desconto: ')
                        Can.drawString(30, 470, 'Valor Final com Desconto: ')
                        Can.drawString(30, 455, 'Forma de pagamento: ')

                        # Valores atribuidos dos campos preenchidos na tela de venda
                        codVENDR = vCodVendrVendaFIN.get()
                        valBRUTO = vValBrutVenFIN.get()
                        valMulta = ValMultaVEND.get()
                        valDESC = vValDescVenFIN.get()
                        valTOTAL = vValorTotaVendFIN.get()
                        formaPAGA = vFormaPGVendaFIN.get()

                        SelecQuery = "SELECT NomeVendr FROM Vendedores WHERE CodVendr = '"+codVENDR+"'"
                        NomeVendedor = VCU_QUERY.DQL(SelecQuery)

                        NAMEvendr = str(NomeVendedor)
                        NAMEvendr = NAMEvendr.replace(']', "").replace('[', "").replace('(', "").replace(')', "").replace("'", "").replace(',', "")

                        Can.setFont("Helvetica", 12)
                        Can.drawString(88, 530, NAMEvendr)
                        Can.drawString(98, 515, 'R$ ' + valBRUTO + ',00')
                        Can.drawString(122, 500, 'R$ ' + valMulta + ',00')
                        Can.drawString(135, 485, 'R$ ' + valDESC + ',00')
                        Can.drawString(172, 470, 'R$ ' + valTOTAL + ',00')
                        Can.drawString(148, 455, formaPAGA)

                        # Criar uma linha separadora
                        Can.rect(25, 440, 540, 1, fill=True, stroke=False)

                        Can.setFont("Helvetica-Bold", 13)
                        Can.drawString(148, 420, 'V.C.U - Sistema de Venda de Carros Usados®')

                        Can.showPage()
                        Can.save()
                        Abrir_PDF()
                except Error as ex:
                    messagebox.showwarning(title="VCU - Ocorreu um Erro!", message=ex)

            def FinalizarVenda():
                # Buscar todos os códigos de Clientes Cadastrados
                SelecCli = "SELECT CodCli FROM Clientes"
                ClientesCAD = VCU_QUERY.DQL(SelecCli)

                # Buscar todos os códigos das Notas de venda
                SelecVenda = "SELECT CodNota FROM Nota_de_Venda"
                VendasCAD = VCU_QUERY.DQL(SelecVenda)

                # Buscar todos os códigos dos Vendedores
                SelecVenddor = "SELECT CodVendr FROM Vendedores"
                VenddoresCAD = VCU_QUERY.DQL(SelecVenddor)

                if vCodVendaFin.get() in str(VendasCAD):
                    messagebox.showwarning(title="Atenção!!!", message="Este código de Nota já existe! Por favor, escolha outro.")
                    vCodVendaFin.focus_set()
                elif vCodVendrVendaFIN.get() not in str(VenddoresCAD):
                    messagebox.showwarning(title="Atenção!!!", message="Código de Vendedor inválido!")
                    vCodVendrVendaFIN.focus_set()
                else:
                    if CodClienteVEND.get() not in str(ClientesCAD):
                        codCliv = CodClienteVEND.get()
                        nomeCliv = NomeCliVEND.get()
                        rgCliv = RgCliVEND.get()
                        cpfCliv = CpfCliVEND.get()
                        endeCliv = EndCliVEND.get()
                        foneCliv = FoneCliVEND.get()

                        SalvarCLI = "INSERT INTO Clientes(CodCli, NomeCli, RgCli, CpfCli, EndCli, FoneCli) VALUES ('" + codCliv + "', '" + nomeCliv + "','" + rgCliv + "', '" + cpfCliv + "', '" + endeCliv + "', '" + foneCliv + "')"
                        VCU_QUERY.DML(SalvarCLI)
                    if vCodVendaFin.get() != "" and vCodVendrVendaFIN.get() != "" and vValBrutVenFIN.get() != "" and vValDescVenFIN.get() != "" and vValorTotaVendFIN.get() != "" and vDataVendaFIN.get() != "" and vFormaPGVendaFIN.get() != "":
                        codigoVend = vCodVendaFin.get()
                        codigoClient = CodClienteVEND.get()
                        codigoVenddor = vCodVendrVendaFIN.get()
                        codigoVeiculo = CodVeVEND.get()
                        data_Venda = vDataVendaFIN.get()
                        valBRUTO = vValBrutVenFIN.get()
                        valDESC = vValDescVenFIN.get()
                        valTOTAL = vValorTotaVendFIN.get()
                        FormPagamento = vFormaPGVendaFIN.get()

                        SalvarNOTA = "INSERT INTO Nota_de_Venda(CodNota, fk_CodCli, fk_CodVendr, fk_CodVeicV, DataVenda, ValorBruto, ValorDesc, ValorVenda, FormaPgto) VALUES ('" + codigoVend + "', '" + codigoClient + "', '" + codigoVenddor + "', '" + codigoVeiculo + "', '" + data_Venda + "', '" + valBRUTO + "', '" + valDESC + "', '" + valTOTAL + "', '" + FormPagamento + "')"
                        VCU_QUERY.DML(SalvarNOTA)
                        messagebox.showinfo(title="Venda de Veiculo", message="Venda Realizada Com Sucesso!!")
                        AppVENDA.destroy()
                    else:
                        messagebox.showinfo(title="Atenção!!!", message="Verifique os Campos Vazios em Considerações finais!")

            def Valor_Final():
                try:
                    vBrutoD = vValBrutVenFIN.get()
                    vDescoD = vValDescVenFIN.get()
                    vFinal = int(vBrutoD) - int(vDescoD)
                    vValorTotaVendFIN.insert(0, vFinal)
                except:
                    pass

            AppVENDA = Toplevel()
            AppVENDA.title(" Operação de Venda do Veículo")
            AppVENDA.geometry("900x700")
            AppVENDA.resizable(False, False)
            AppVENDA.configure(background="#0f3")
            AppVENDA.wm_iconbitmap('icon_VCU.ico')
            AppVENDA.focus_force()
            AppVENDA.grab_set()

            ABAvenda = ttk.Notebook(AppVENDA)
            ABAvenda.place(x=10, y=10, width=880, height=680)

            # __________________________Frame Operações de venda___________________________#

            FrameVENDA = LabelFrame(ABAvenda, text="Informações da VENDA", font="Arial 12 italic bold", foreground="#000", borderwidth='1', relief="flat")
            FrameVENDA.configure(background="#e6e6e6")
            FrameVENDA.place(x=0, y=0, width=878, height=680)

            # __________________________Frame dados do Veículo___________________________#

            FrameDadosVE = LabelFrame(FrameVENDA, text="Dados do Veículo", font="Arial 11", foreground="#f00", relief='raised', borderwidth='2')
            FrameDadosVE.configure(background="#e6e6e6")
            FrameDadosVE.place(x=20, y=5, width=840, height=185)

            Label(FrameDadosVE, text="Cód. Veículo: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=10)
            CodVeVEND = Entry(FrameDadosVE)
            CodVeVEND.place(x=115, y=10, width=60, height=22.499)
            CodVeVEND.insert(0, vVendcodVE)
            CodVeVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Marca: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=185, y=10)
            MarcaVEND = Entry(FrameDadosVE)
            MarcaVEND.place(x=235, y=10, width=125, height=22.499)
            MarcaVEND.insert(0, vVendMarca)
            MarcaVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Modelo: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=370, y=10)
            ModeloVEND = Entry(FrameDadosVE)
            ModeloVEND.place(x=430, y=10, width=140, height=22.499)
            ModeloVEND.insert(0, vVendModel)
            ModeloVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Ano de Fabricação: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=583, y=10)
            AnoVEND = Entry(FrameDadosVE)
            AnoVEND.place(x=715, y=10, width=100, height=22.4)
            AnoVEND.insert(0, vVendAnoFabri)
            AnoVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Cor: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=40)
            CorVEND = Entry(FrameDadosVE)
            CorVEND.place(x=55, y=40, width=160, height=22.4)
            CorVEND.insert(0, vVendCor)
            CorVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Combustível: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=225, y=40)
            CombustVEND = Entry(FrameDadosVE)
            CombustVEND.place(x=315, y=40, width=120, height=22.4)
            CombustVEND.insert(0, vVendCombust)
            CombustVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Placa: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=445, y=40)
            PlacaVEND = Entry(FrameDadosVE)
            PlacaVEND.place(x=495, y=40, width=105, height=22.499)
            PlacaVEND.insert(0, vVendPlaca)
            PlacaVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Renavan: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=610, y=40)
            RenavVEND = Entry(FrameDadosVE)
            RenavVEND.place(x=680, y=40, width=135, height=22.499)
            RenavVEND.insert(0, vVendRenavan)
            RenavVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Portas: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=70)
            PortasVEND = Entry(FrameDadosVE)
            PortasVEND.place(x=75, y=70, width=20, height=22.4)
            PortasVEND.insert(0, vVendPortas)
            PortasVEND.configure(font="Arial 11", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Vidro Elétr.: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=105, y=70)
            VidEleVEND = Entry(FrameDadosVE)
            VidEleVEND.place(x=185, y=70, width=35, height=22.4)
            VidEleVEND.insert(0, vVendVidroEl)
            VidEleVEND.configure(font="Arial 11", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Trava Elétr.: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=230, y=70)
            TravEleVEND = Entry(FrameDadosVE)
            TravEleVEND.place(x=315, y=70, width=35, height=22.4)
            TravEleVEND.insert(0, vVendTravaEl)
            TravEleVEND.configure(font="Arial 11", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Alarme: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=360, y=70)
            AlarmVEND = Entry(FrameDadosVE)
            AlarmVEND.place(x=420, y=70, width=35, height=22.4)
            AlarmVEND.insert(0, vVendAlarm)
            AlarmVEND.configure(font="Arial 11", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Ar Condic.: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=465, y=70)
            ArCondVEND = Entry(FrameDadosVE)
            ArCondVEND.place(x=545, y=70, width=35, height=22.4)
            ArCondVEND.insert(0, vVendArCond)
            ArCondVEND.configure(font="Arial 11", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Som: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=590, y=70)
            SomVEND = Entry(FrameDadosVE)
            SomVEND.place(x=630, y=70, width=35, height=22.4)
            SomVEND.insert(0, vVendSom)
            SomVEND.configure(font="Arial 11", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Outro: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=675, y=70)
            OutroVEND = Entry(FrameDadosVE)
            OutroVEND.place(x=725, y=70, width=90, height=22.4)
            OutroVEND.insert(0, vVendOutros)
            OutroVEND.configure(font="Arial 11", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Vencimento IPVA: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=100)
            VencIpvaVEND = Entry(FrameDadosVE)
            VencIpvaVEND.place(x=145, y=100, width=100, height=22.4)
            VencIpvaVEND.insert(0, vVendVencIPVA)
            VencIpvaVEND.configure(font="Arial 11", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Valor em Multas: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=255, y=100)
            ValMultaVEND = Entry(FrameDadosVE)
            ValMultaVEND.place(x=370, y=100, width=100, height=22.4)
            ValMultaVEND.insert(0, vVendValorMulta)
            ValMultaVEND.configure(font="Arial 11", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Valor na Tabela FIPE: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=130)
            FipeVEND = Entry(FrameDadosVE)
            FipeVEND.place(x=165, y=130, width=95, height=22.4)
            FipeVEND.insert(0, vVendValorFIPE)
            FipeVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosVE, text="Valor do proprietário: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=270, y=130)
            PrecoProV = Entry(FrameDadosVE)
            PrecoProV.place(x=415, y=130, width=100, height=22.4)
            PrecoProV.insert(0, vVendValorPRO)
            PrecoProV.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            # ________________________Frame dados do Proprietário_________________________#

            FrameDadosPRO = LabelFrame(FrameVENDA, text="Dados do Proprietário", font="Arial 11", foreground="#f00", relief='raised', borderwidth='2')
            FrameDadosPRO.configure(background="#e6e6e6")
            FrameDadosPRO.place(x=20, y=195, width=840, height=160)

            Label(FrameDadosPRO, text="Cód. Proprietário: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=10)
            CodProVEND = Entry(FrameDadosPRO)
            CodProVEND.place(x=140, y=10, width=75, height=22.499)
            CodProVEND.insert(0, vVendcodPRO)
            CodProVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosPRO, text="Nome/Razão Social: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=225, y=10)
            NomeVEND = Entry(FrameDadosPRO)
            NomeVEND.place(x=362, y=10, width=450, height=22.4)
            NomeVEND.insert(0, NomePROvenda)
            NomeVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosPRO, text="CPF/CNPJ: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=40)
            CpfVEND = Entry(FrameDadosPRO)
            CpfVEND.place(x=95, y=40, width=180, height=22.4)
            CpfVEND.insert(0, CpfPROvenda)
            CpfVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosPRO, text="Telefone: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=290, y=40)
            FoneVEND = Entry(FrameDadosPRO)
            FoneVEND.place(x=360, y=40, width=160, height=22.4)
            FoneVEND.insert(0, FonePROvenda)
            FoneVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosPRO, text="Endereço: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=70)
            EnderecVEND = Entry(FrameDadosPRO)
            EnderecVEND.place(x=90, y=70, width=725, height=22.4)
            EnderecVEND.insert(0, EndPROvenda)
            EnderecVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            Label(FrameDadosPRO, text="Responsável: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=100)
            ResponVEND = Entry(FrameDadosPRO)
            ResponVEND.place(x=110, y=100, width=300, height=22.4)
            ResponVEND.insert(0, ResponPROvenda)
            ResponVEND.configure(font="Arial 10", background="#f2f2f2", foreground="#009", state="readonly")

            # ________________________Frame dados do Cliente/Comprador_________________________#

            FrameDadosCLI = LabelFrame(FrameVENDA, text="Dados do Cliente/Comprador", font="Arial 11", foreground="#f00", relief='raised', borderwidth='2')
            FrameDadosCLI.configure(background="#e6e6e6")
            FrameDadosCLI.place(x=20, y=360, width=840, height=130)

            Label(FrameDadosCLI, text="Cód. Cliente: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=10)
            CodClienteVEND = Entry(FrameDadosCLI)
            CodClienteVEND.place(x=110, y=10, width=60, height=22.499)
            CodClienteVEND.configure(font="Arial 11 bold", background="#f2f2f2", foreground="#000")

            Label(FrameDadosCLI, text="Nome: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=190, y=10)
            NomeCliVEND = Entry(FrameDadosCLI)
            NomeCliVEND.place(x=240, y=10, width=400, height=22.4)
            NomeCliVEND.configure(font="Arial 11 bold", foreground="#000", background="#f2f2f2")

            Label(FrameDadosCLI, text="CPF: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=40)
            CpfCliVEND = Entry(FrameDadosCLI)
            CpfCliVEND.place(x=60, y=40, width=150, height=22.4)
            CpfCliVEND.configure(font="Arial 11 bold", foreground="#000", background="#f2f2f2")

            Label(FrameDadosCLI, text="RG: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=230, y=40)
            RgCliVEND = Entry(FrameDadosCLI)
            RgCliVEND.place(x=260, y=40, width=155, height=22.4)
            RgCliVEND.configure(font="Arial 11 bold", foreground="#000", background="#f2f2f2")

            Label(FrameDadosCLI, text="Fone/Whats: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=435, y=40)
            FoneCliVEND = Entry(FrameDadosCLI)
            FoneCliVEND.place(x=520, y=40, width=150, height=22.4)
            FoneCliVEND.configure(font="Arial 11 bold", foreground="#000", background="#f2f2f2")

            Label(FrameDadosCLI, text="Endereço: ", background="#FFF", foreground="#000", font="Arial 10 bold").place(x=20, y=70)
            EndCliVEND = Entry(FrameDadosCLI)
            EndCliVEND.place(x=90, y=70, width=725, height=22.4)
            EndCliVEND.configure(font="Arial 11 bold", foreground="#000", background="#f2f2f2")

            # ________________________Frame Considerações Finais_________________________#

            FrameDadosFIN = LabelFrame(FrameVENDA, text="Considerações Finais", font="Arial 11", foreground="#f00", relief='raised', borderwidth='2')
            FrameDadosFIN.configure(background="#e6e6e6")
            FrameDadosFIN.place(x=20, y=495, width=840, height=160)

            Label(FrameDadosFIN, text="Cód. Venda(8): ", font="Arial 10 bold", bg="#FFF", fg="#000").place(x=20, y=10)
            vCodVendaFin = Entry(FrameDadosFIN)
            vCodVendaFin.configure(font="arial 11 bold", background="#f2f2f2", foreground="#000")
            vCodVendaFin.place(x=120, y=10, width=80, height=22.4)

            Label(FrameDadosFIN, text="Cód. VENDEDOR: ", font="Arial 10 bold", bg="#FFF", fg="#000").place(x=220, y=10)
            vCodVendrVendaFIN = Entry(FrameDadosFIN)
            vCodVendrVendaFIN.configure(font="arial 11 bold", background="#f2f2f2", foreground="#000")
            vCodVendrVendaFIN.place(x=335, y=10, width=90, height=22.4)

            Label(FrameDadosFIN, text="Valor Bruto: ", font="Arial 10 bold", bg="#FFF", fg="#000").place(x=20, y=40)
            vValBrutVenFIN = Entry(FrameDadosFIN)
            vValBrutVenFIN.insert(0, vVendValorPRO)
            vValBrutVenFIN.configure(font="arial 11 bold", background="#f2f2f2", foreground="#000", state='readonly')
            vValBrutVenFIN.place(x=105, y=40, width=110, height=22.4)

            Label(FrameDadosFIN, text="Valor do Desconto: ", font="Arial 10 bold", bg="#FFF", fg="#000").place(x=235, y=40)
            vValDescVenFIN = Entry(FrameDadosFIN)
            vValDescVenFIN.insert(0, '0')
            vValDescVenFIN.configure(font="arial 11 bold", background="#f2f2f2", foreground="#000")
            vValDescVenFIN.place(x=360, y=40, width=110, height=22.4)

            Label(FrameDadosFIN, text="Valor Total com Desconto: ", font="Arial 10 bold", bg="#FFF", fg="#000").place(x=20, y=70)
            vValorTotaVendFIN = Entry(FrameDadosFIN)
            vValorTotaVendFIN.configure(font="arial 11 bold", background="#f2f2f2", foreground="#000")
            vValorTotaVendFIN.place(x=195, y=70, width=110, height=22.4)

            Label(FrameDadosFIN, text="Data da Venda: ", font="Arial 10 bold", bg="#FFF", fg="#000").place(x=20, y=100)
            vDataVendaFIN = Entry(FrameDadosFIN)
            vDataVendaFIN.configure(font="arial 11 bold", background="#f2f2f2", foreground="#000")
            vDataVendaFIN.place(x=125, y=100, width=90, height=22.4)

            Label(FrameDadosFIN, text="Forma de Pagamento: ", font="Arial 10 bold", bg="#FFF", fg="#000").place(x=225, y=100)
            vFormaPGVendaFIN = Entry(FrameDadosFIN)
            vFormaPGVendaFIN.configure(font="arial 11 bold", background="#f2f2f2", foreground="#000")
            vFormaPGVendaFIN.place(x=375, y=100, width=180, height=22.4)

            # Botão calcular Desconto
            btnCalcular = Button(FrameDadosFIN, text="Calcular", font="Arial 11 bold", bg="yellow", fg="#000", relief="raised", borderwidth='4', command=Valor_Final)
            btnCalcular.place(x=306, y=70, width=80, height=22.4)

            # Botões IMPRIMIR ORÇAMENTO, FINALIZAR VENDA e CANCELAR/SAIR
            btnOrcament = Button(FrameDadosFIN, text="Imprimir Orçamento", background="green", foreground="white", relief="raised", borderwidth='6', command=Gerar_PDF)
            btnOrcament.configure(font="Arial 12 bold")
            btnOrcament.place(x=620, y=1, height=35)

            btnFinalVenda = Button(FrameDadosFIN, text="Finalizar Venda", background="blue", foreground="white", relief="raised", borderwidth='6', command=FinalizarVenda)
            btnFinalVenda.configure(font="Arial 12 bold")
            btnFinalVenda.place(x=620, y=48, width=175, height=35)

            btnCancelVenda = Button(FrameDadosFIN, text="Cancelar/Sair", background="red", foreground="white", relief="raised", borderwidth='6', command=AppVENDA.destroy)
            btnCancelVenda.configure(font="Arial 12 bold")
            btnCancelVenda.place(x=620, y=95, width=175, height=35)

            AppVENDA.transient(appVCU)
            AppVENDA.mainloop()
        except:
            messagebox.showinfo(title=" Atenção!", message="Nenhum item selecionado!")

    def TelaInicial():
        ABA.forget(0)
        ABA.add(abaBemVindo, text="Tela Inicial")
        abaBemVindo.configure(background="white")

    ### Gridview da ABA CONSULTAR VEÍCULO ###
    quadroGrid = LabelFrame(FrameLab4, text="Dados dos Veículos", font="Arial 11", foreground="#f00", relief="flat", background="#e6e6e6")
    quadroGrid.place(x=5, y=20, width=1260, height=760)

    tv = ttk.Treeview(quadroGrid, columns=(
    'Cód. Veículo', 'Cód. Proprietário', 'Marca', 'Modelo', 'Ano de Fabricação', 'Cor', 'Combustivel', 'Placa', 'Renavan', 'qtd Portas', 'Vidro Elétr.',
    'Trava Elétr.', 'Alarme', 'Ar Condic.', 'Som', 'outros', 'Venc. IPVA', 'Valor em Multas', 'Valor FIPE', 'Valor de Venda'), show='headings')
    tv.configure(height=22)
    tv.column('Cód. Veículo', minwidth=50, width=50)
    tv.column('Cód. Proprietário', minwidth=55, width=55)
    tv.column('Marca', minwidth=65, width=65)
    tv.column('Modelo', minwidth=65, width=65)
    tv.column('Ano de Fabricação', minwidth=60, width=60)
    tv.column('Cor', minwidth=60, width=60)
    tv.column('Combustivel', minwidth=75, width=75)
    tv.column('Placa', minwidth=54, width=54)
    tv.column('Renavan', minwidth=60, width=60)
    tv.column('qtd Portas', minwidth=58, width=58)
    tv.column('Vidro Elétr.', minwidth=60, width=60)
    tv.column('Trava Elétr.', minwidth=64, width=64)
    tv.column('Alarme', minwidth=45, width=45)
    tv.column('Ar Condic.', minwidth=60, width=60)
    tv.column('Som', minwidth=40, width=40)
    tv.column('outros', minwidth=60, width=60)
    tv.column('Venc. IPVA', minwidth=70, width=70)
    tv.column('Valor em Multas', minwidth=80, width=80)
    tv.column('Valor FIPE', minwidth=70, width=70)
    tv.column('Valor de Venda', minwidth=80, width=80)

    tv.heading('Cód. Veículo', text="Cód. Veículo")
    tv.heading('Cód. Proprietário', text="Cód. Proprietário")
    tv.heading('Marca', text="Marca")
    tv.heading('Modelo', text="Modelo")
    tv.heading('Ano de Fabricação', text="Ano/Fabricação")
    tv.heading('Cor', text="Cor")
    tv.heading('Combustivel', text="Combustivel")
    tv.heading('Placa', text='Placa')
    tv.heading('Renavan', text='Renavan')
    tv.heading('qtd Portas', text='qtd Portas')
    tv.heading('Vidro Elétr.', text='Vidro Elétr.')
    tv.heading('Trava Elétr.', text='Trava Elétr.')
    tv.heading('Alarme', text='Alarme')
    tv.heading('Ar Condic.', text='Ar Condic.')
    tv.heading('Som', text='Som')
    tv.heading('outros', text='outros')
    tv.heading('Venc. IPVA', text='Venc. IPVA')
    tv.heading('Valor FIPE', text='Valor FIPE')
    tv.heading('Valor em Multas', text='Valor/Multas')
    tv.heading('Valor FIPE', text='Valor/FIPE')
    tv.heading('Valor de Venda', text='Valor/Venda')
    tv.pack(side=LEFT)
    tv.place(x=0, y=0, height=320)

    # Scrollbar Vertical ABA CONSULTAR VEÍCULO
    VScroll = ttk.Scrollbar(quadroGrid, orient="vertical", command=tv.yview)
    VScroll.place(x=1235, y=2, height=320)

    # Scrollbar Vertical ABA CONSULTAR VEÍCULO
    OScroll = ttk.Scrollbar(quadroGrid, orient="horizontal", command=tv.xview)
    OScroll.place(x=0, y=322, width=1235)

    # configurar as Scrolls da ABA CONSULTAR VEÍCULO
    tv.configure(yscrollcommand=VScroll.set, xscrollcommand=OScroll.set)

    ### FRAMES da ABA CONSULTAR VEÍCULOS ###
    # Frame de SELECT
    FrameBusca = LabelFrame(quadroGrid, text="Opções de busca", foreground="#f00", font="Arial 11", relief='raised', borderwidth='2')
    FrameBusca.configure(background="#e6e6e6")
    FrameBusca.place(x=2, y=340, width=1250, height=108)

    FrameAttVE = LabelFrame(quadroGrid, text="Atualizar Registro Selecionado", foreground="#f00", font="Arial 11", relief='raised', borderwidth='2')
    FrameAttVE.configure(background="#e6e6e6")
    FrameAttVE.place(x=30, y=455, width=330, height=75)

    FrameDelVE = LabelFrame(quadroGrid, text="Excluir Registro Selecionado", foreground="#f00", font="Arial 11", relief='raised', borderwidth='2')
    FrameDelVE.configure(background="#e6e6e6")
    FrameDelVE.place(x=450, y=455, width=330, height=75)

    FrameVendaVE = LabelFrame(quadroGrid, text="Realizar Venda do Veículo Selecionado", foreground="#f00", font="Arial 11", relief='raised', borderwidth='2')
    FrameVendaVE.configure(background="#e6e6e6")
    FrameVendaVE.place(x=880, y=455, width=330, height=75)

    ### elementos para quadro de pesquisa na ABA Consultar VEÍCULO ###
    # Busca por MODELO
    LabelPesq = Label(FrameBusca, text="Busca por Modelo:")
    LabelPesq.configure(font="Arial 12", background="#e6e6e6")
    LabelPesq.place(x=10, y=10)

    txtPesqMod = Entry(FrameBusca)
    txtPesqMod.configure(width=22, font="arial 14")
    txtPesqMod.place(x=145, y=10)

    btnPesqMod = Button(FrameBusca, text="Pesquisar", command=PesquisarMODE)
    btnPesqMod.configure(font="arial 10 bold", background="blue", foreground="#fff")
    btnPesqMod.place(x=395, y=10)

    # Busca por Cód. do Proprietário
    LabelPesq1 = Label(FrameBusca, text="Busca/Cód. Proprietário:")
    LabelPesq1.configure(font="Arial 12", background="#e6e6e6")
    LabelPesq1.place(x=10, y=50)

    txtPesqPro = Entry(FrameBusca)
    txtPesqPro.configure(width=18, font="arial 14")
    txtPesqPro.place(x=190, y=50)

    btnPesqCodPro = Button(FrameBusca, text="Pesquisar", command=PesquisarCodPRO)
    btnPesqCodPro.configure(font="arial 10 bold", background="blue", foreground="#fff")
    btnPesqCodPro.place(x=395, y=50)

    # Busca por PLACA
    LabelPesq2 = Label(FrameBusca, text="Busca por Placa:")
    LabelPesq2.configure(font="Arial 12", background="#e6e6e6")
    LabelPesq2.place(x=500, y=10)

    txtPesqPlaca = Entry(FrameBusca)
    txtPesqPlaca.configure(width=20, font="arial 14")
    txtPesqPlaca.place(x=625, y=10)

    btnPesqPlaca = Button(FrameBusca, text="Pesquisar", command=PesquisarPLAC)
    btnPesqPlaca.configure(font="arial 10 bold", background="blue", foreground="#fff")
    btnPesqPlaca.place(x=853, y=10)

    # Busca por Cód. do Veículo
    LabelPesq3 = Label(FrameBusca, text="Busca/Cód. Veículo:")
    LabelPesq3.configure(font="Arial 12", background="#e6e6e6")
    LabelPesq3.place(x=500, y=50)

    txtPesqCodVE = Entry(FrameBusca)
    txtPesqCodVE.configure(width=18, font="arial 14")
    txtPesqCodVE.place(x=645, y=50)

    btnPesqCodVE = Button(FrameBusca, text="Pesquisar", command=PesquisarCodVE)
    btnPesqCodVE.configure(font="arial 10 bold", background="blue", foreground="#fff")
    btnPesqCodVE.place(x=850, y=50)

    # Botão voltar
    btnVoltarVE = Button(FrameLab4, text='Voltar', font='Arial 12 bold', relief='raised', borderwidth='4', command=TelaInicial)
    btnVoltarVE.configure(bg='white', fg='black')
    btnVoltarVE.place(x=1175, y=0, height=30)

    # botao q busca TODOS os registros na ABA Consultar VEÍCULOS
    btnBuscaTudo = Button(FrameBusca, text="Buscar Tudo", command=ListarVeiculos)
    btnBuscaTudo.configure(width=14, height=2, font="arial 11 bold", background="blue", foreground="#fff", relief="raised", borderwidth='6')
    btnBuscaTudo.place(x=1050, y=15)

    # botao Atualizar na ABA Consultar VEICULOS
    btnAttVE = Button(FrameAttVE, text="Atualizar dados do Veículo", command=AtualizarVE)
    btnAttVE.configure(font="arial 12 bold", background="yellow", foreground="#000", relief="raised", borderwidth='6')
    btnAttVE.place(x=50, y=5, width=220, height=40)

    # botao Excluir na ABA Consultar VEICULOS
    btnExcVE = Button(FrameDelVE, text="Excluir dados do Veículo", command=DeletarVE)
    btnExcVE.configure(font="arial 12 bold", background="#f00", foreground="#fff", relief="raised", borderwidth='6')
    btnExcVE.place(x=50, y=5, width=220, height=40)

    # botao Vender na ABA Consultar VEICULOS
    btnVendVE = Button(FrameVendaVE, text="Vender Veículo", command=VenderVE)
    btnVendVE.configure(font="arial 12 bold", background="#0f3", foreground="#000", relief="raised", borderwidth='6')
    btnVendVE.place(x=50, y=5, width=220, height=40)

def Versao():
    AppVersao = Toplevel()
    AppVersao.title(" Detalhes da Versão")
    AppVersao.geometry("400x180")
    AppVersao.resizable(False, False)
    AppVersao.configure(background="#2b2b2b")
    AppVersao.wm_iconbitmap('icon_VCU.ico')
    AppVersao.focus_force()
    AppVersao.grab_set()

    lblVersao = Label(AppVersao, text="Versão: 1.5.5", font="arial 12 italic", bg='#2b2b2b', fg="#fff")
    lblVersao.place(x=153, y=20)

    lvlDatInic = Label(AppVersao, text="Data de Criação: 28/09/2020", font="arial 12 italic", bg='#2b2b2b', fg="#fff")
    lvlDatInic.place(x=110, y=50)

    lvlDesenv = Label(AppVersao, text="Desenvolvedores: Célio Santos Cardoso,", font="arial 12 italic", bg='#2b2b2b', fg="#fff")
    lvlDesenv.place(x=60, y=80)

    lvlDesenv2 = Label(AppVersao, text="Luiz de Paula Martins Filho e", font="arial 12 italic", bg='#2b2b2b', fg="#fff")
    lvlDesenv2.place(x=100, y=110)

    lvlDesenv3 = Label(AppVersao, text="Talita Paes Landim do Nascimento", font="arial 12 italic", bg='#2b2b2b', fg="#fff")
    lvlDesenv3.place(x=80, y=140)

    AppVersao.transient(appVCU)
    AppVersao.mainloop()

#  Criando os menús da tela principal #
barraMenu = Menu(appVCU)

# Menu Gerenciar
menuGerenciar = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Gerenciar", menu=menuGerenciar)
menuGerenciar.add_command(label="Configurações de Vendedores", command=Config_Vendedores)
menuGerenciar.add_separator()
menuGerenciar.add_command(label="Relatório de Vendas", command=Relatorio_Venda)

# Menu do Proprietario
menuPro = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Proprietários", menu=menuPro)
menuPro.add_command(label="Cadastrar Proprietário", command=ABA_CAD_Propri)
menuPro.add_separator()
menuPro.add_command(label="Buscar Proprietário", command=ABA_Consu_Propri)

# Menu do Veículo
menuVeic = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Veículos", menu=menuVeic)
menuVeic.add_command(label="Cadastrar Veículo", command=ABA_CAD_Veic)
menuVeic.add_separator()
menuVeic.add_command(label="Buscar Veículo", command=ABA_Consu_Veic)

# Menu Informações do Software
menuVCU = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Software", menu=menuVCU)
menuVCU.add_command(label="Detalhes da Versão", command=Versao)

# Menu Fechar App
CloseApp = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Sair do App", menu=CloseApp)
CloseApp.add_command(label="Sair", command=quit)

#  executa o programa em loop  #
appVCU.config(menu=barraMenu)
appVCU.mainloop()