import sqlite3
from tkinter import *
from tkinter import simpledialog
import tkinter.ttk as ttk
from tkinter import messagebox

class ConectarDB:
    """Classe para criar o banco de dados"""
    def __init__(self):
        """Função que conecta ao banco"""
        self.con = sqlite3.connect('db.sqlite3')
        self.cur = self.con.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        """Função que cria a tabela do banco de dados"""
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS NomeDaTabela (
                nome TEXT,
                telefone TEXT,
                email TEXT)''')
        except Exception as e:
            print('[x] Falha ao criar tabela: %s [x]' % e)
        else:
            print('\n[!] Tabela criada com sucesso [!]\n')

    def inserir_registro(self, nome, telefone, email):
        """Função para inserir um registro na tabela"""
        try:
            self.cur.execute(
                '''INSERT INTO NomeDaTabela VALUES (?, ?, ?)''', (nome, telefone, email,))
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print('[x] Revertendo operação (rollback) %s [x]\n' % e)
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def consultar_registros(self):
        """Função que retorna os registros"""
        return self.cur.execute('SELECT rowid, * FROM NomeDaTabela').fetchall()

    def consultar_ultimo_rowid(self):
        """Função para encontrar o ID do ultimo elemento da tabela"""
        return self.cur.execute('SELECT MAX(rowid) FROM NomeDaTabela').fetchone()

    def remover_registro(self, rowid):
        """Função para remover o registro"""
        try:
            self.cur.execute("DELETE FROM NomeDaTabela WHERE rowid=?", (rowid,))
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print('[x] Revertendo operação (rollback) %s [x]\n' % e)
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')

    def atualizar_registro(self, rowid, nome, telefone, email):
        """Função para atualizar um registro na tabela"""
        try:
            self.cur.execute('''UPDATE NomeDaTabela SET nome=?, telefone=?, email=? WHERE rowid=?''',(nome, telefone, email, rowid,))
        except Exception as e:
            print('\n[x] Falha ao atualizar registro [x]\n')
            print('[x] Revertendo operação (rollback) %s [x]\n' % e)
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro atualizado com sucesso [!]\n')


class Janela(Frame):
    """Classe da janela principal"""

    def __init__(self, master=None):
        """Função construindo a janela"""
        super().__init__(master)

        master.title('Lista telefonica')

        master.geometry('1000x350')

        self.banco = ConectarDB()

        self.pack()

        self.criar_widgets()

    def criar_widgets(self):
        """Função que cria os widgets da janela"""
        frame1 = Frame(self)
        frame1.pack(side=TOP, fill=BOTH, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(fill=BOTH, expand=True)

        frame3 = Frame(self)
        frame3.pack(side=BOTTOM, padx=5)

        label_nome = Label(frame1, text='Nome')
        label_nome.grid(row=0, column=0)

        label_telefone = Label(frame1, text='Telefone')
        label_telefone.grid(row=0, column=1)

        label_email = Label(frame1, text='E-mail')
        label_email.grid(row=0, column=2)

        self.entry_nome = Entry(frame1, width=40)
        self.entry_nome.grid(row=1, column=0)

        self.entry_telefone = Entry(frame1)
        self.entry_telefone.grid(row=1, column=1, padx=10)

        self.entry_email = Entry(frame1)
        self.entry_email.grid(row=1, column=2)

        button_adicionar = Button(frame1, text='Adicionar', bg='blue', fg='white')
        button_adicionar['command'] = self.adicionar_registro
        button_adicionar.grid(row=0, column=3, rowspan=2, padx=10)

        button_buscar = Button(frame1, text='Buscar', bg='green', fg='white')
        button_buscar['command'] = self.procurar_registro
        button_buscar.grid(row=0, column=4, rowspan=2, padx=10)

        button_buscar = Button(frame1, text='Atualizar', bg='green', fg='white')
        button_buscar['command'] = self.atualizar_registro
        button_buscar.grid(row=0, column=5, rowspan=2, padx=10)

        self.treeview = ttk.Treeview(frame2, columns=('Nome', 'Telefone', 'E-mail'))
        self.treeview.heading('#0', text='ID')
        self.treeview.heading('#1', text='Nome')
        self.treeview.heading('#2', text='Telefone')
        self.treeview.heading('#3', text='E-mail')

        for row in self.banco.consultar_registros():
            self.treeview.insert('', 'end', text=row[0], values=(row[1], row[2], row[3]))

        self.treeview.pack(fill=BOTH, expand=True)

        button_excluir = Button(frame3, text='Excluir', bg='red', fg='white')
        button_excluir['command'] = self.excluir_registro
        button_excluir.pack(pady=10)

    def adicionar_registro(self):
        """Função que adiciona um regitro à tabela"""
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()

        self.banco.inserir_registro(nome=nome, telefone=telefone, email=email)

        rowid = self.banco.consultar_ultimo_rowid()[0]

        self.treeview.insert('', 'end', text=rowid, values=(nome, telefone, email))

    def excluir_registro(self):
        """Função que exclui um registro da tabela"""
        if not self.treeview.focus():
            messagebox.showerror('Erro', 'Nenhum item selecionado')
        else:
            item_selecionado = self.treeview.focus()

            rowid = self.treeview.item(item_selecionado)

            self.banco.remover_registro(rowid['text'])

            self.treeview.delete(item_selecionado)

    def procurar_registro(self):
        """Função que procura por um registro na tabela"""
        search = simpledialog.askstring("Buscar", "Digite o nome a ser pesquisado:")
        if search:
            found_items = []
            for item in self.treeview.get_children():
                if search.lower() in self.treeview.item(item)["values"][0].lower():
                    found_items.append(item)
            if found_items:
                self.treeview.selection_set(found_items)
                self.treeview.focus(found_items[0])
                self.treeview.see(found_items[0])
            else:
                messagebox.showinfo("Buscar", "Nenhum item encontrado.")

    def atualizar_registro(self):
        """Função que atualiza um item da tabela"""
        selected_item = self.treeview.focus()
        if selected_item:
            item_values = self.treeview.item(selected_item)
            updated_values = simpledialog.askstring("Atualizar", "Digite os novos valores separados por vírgula:")
            if updated_values:
                updated_values = updated_values.split(',')
                if len(updated_values) == 3:
                    self.banco.atualizar_registro(rowid=item_values['text'], nome=updated_values[0], telefone=updated_values[1], email=updated_values[2])  
                    self.treeview.item(selected_item, values=updated_values)
                    messagebox.showinfo("Atualizar", "Item atualizado com sucesso.")
                else:
                    messagebox.showerror("Atualizar", "Erro: Por favor, insira todos os valores (Nome, Telefone e Email).")  
        else:
            messagebox.showerror("Atualizar", "Nenhum item selecionado.")        

root = Tk()
app = Janela(master=root)
app.mainloop()