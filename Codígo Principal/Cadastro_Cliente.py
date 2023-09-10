import customtkinter
import customtkinter as ctk
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x800")
        self.title("Cadastro de Clientes TermoFibra")
        
        # Criar Titulo principal de canto
        self.titulo = customtkinter.CTkLabel(self, text='Cadastro de Clientes', font=customtkinter.CTkFont(size=20, weight="bold"), bg_color="transparent")
        self.titulo.grid(row=0, column=0, padx=10, pady=(10))


        # Criar Rótulos e campos de entrada
        self.label_nome = ctk.CTkLabel(self, text="Nome Completo:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_nome.grid(row=2, column=2, padx=10, pady=10)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_nome.grid(row=2, column=3, padx=10, pady=10)

        self.label_email = ctk.CTkLabel(self, text="Email:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_email.grid(row=3, column=2, padx=10, pady=10)
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_email.grid(row=3, column=3, padx=10, pady=10)
    
        self.label_N_Telefone = ctk.CTkLabel(self, text="Numero com DDD:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_N_Telefone.grid(row=4, column=2, padx=10, pady=10)
        self.entry_N_Telefone = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_N_Telefone.grid(row=4, column=3, padx=10, pady=10)
        
        self.label_CPF = ctk.CTkLabel(self, text="CPF:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_CPF.grid(row=5, column=2, padx=10, pady=10)
        self.entry_CPF = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_CPF.grid(row=5, column=3, padx=10, pady=10)
        
        self.label_RG = ctk.CTkLabel(self, text="RG:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_RG.grid(row=6, column=2, padx=10, pady=10)
        self.entry_RG = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_RG.grid(row=6, column=3, padx=10, pady=10)
        
        self.label_CNPJ = ctk.CTkLabel(self, text="CNPJ:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_CNPJ.grid(row=7, column=2, padx=10, pady=10)
        self.entry_CNPJ = ctk.CTkEntry(self, placeholder_text="Não Obrigatório", width=380)
        self.entry_CNPJ.grid(row=7, column=3, padx=10, pady=10)
        
        self.label_D_Nascimento = ctk.CTkLabel(self, text="Data de Nascimento:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_D_Nascimento.grid(row=8, column=2, padx=10, pady=10)
        self.entry_D_Nascimento = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_D_Nascimento.grid(row=8, column=3, padx=10, pady=10)
    
        self.label_Carro = ctk.CTkLabel(self, text="Carro:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_Carro.grid(row=9, column=2, padx=10, pady=10)
        self.entry_Carro = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_Carro.grid(row=9, column=3, padx=10, pady=10)
    
        self.label_Placa = ctk.CTkLabel(self, text="N da PLaca:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_Placa.grid(row=10, column=2, padx=10, pady=10)
        self.entry_Placa = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_Placa.grid(row=10, column=3, padx=10, pady=10)

        # Criar Botão para cadastrar cliente
        btn_cadastrar = ctk.CTkButton(self, text="Cadastrar Cliente", command=self.cadastrar_cliente)
        btn_cadastrar.grid(row=850, column=3, padx=0, pady=30)
        
        # Criar Label para identificar o menu de opções de zoom
        self.label_zoom = ctk.CTkLabel(self, text="Zoom:", bg_color="transparent")
        self.label_zoom.grid( row=899, column=0, padx=20, pady=(10, 20))
        self.fonte = customtkinter.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"], command=self.tamanho_fonte)
        self.fonte.grid( row=900, column=0)
        
        # Criar botão para menu de opções de temas
        self.label_tema = ctk.CTkLabel(self, text="Temas:", bg_color="transparent")
        self.label_tema.grid(row=897, column=0, padx=20, pady=(10, 10))
        self.opcaomenu = customtkinter.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                                       command=self.modo_aparencia)
        self.opcaomenu.grid(row=898, column=0, padx=20, pady=(10, 10))
        
    # Criar Funções para os botões
        # Botão de tamanho das fontos
    def tamanho_fonte(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        
        # Botão de aparência
    def modo_aparencia(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    # Cadastrar clientes
    def cadastrar_cliente(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        N_Telefone = self.entry_N_Telefone.get()
        CPF = self.entry_CPF.get()
        RG = self.entry_RG.get()
        CNPJ = self.entry_CNPJ.get()
        D_Nascimento = self.entry_D_Nascimento.get()
        Carro = self.entry_Carro.get()
        Placa = self.entry_Placa.get()

        if nome.strip() == '' or email.strip() == '' or N_Telefone.strip() == '' or CPF.strip() == '' or RG.strip() == '' or D_Nascimento.strip() == '' or Carro.strip() == '' or Placa.strip() == '':
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        else:
            # Salvar os dados em algum lugar (por exemplo, em um arquivo .txt ou banco de dados)
            with open('clientes.txt', 'a') as file:
                file.write(f"Nome: {nome}, Email: {email}, Numero com DDD: {N_Telefone}, CPF: {CPF}, RG: {RG}, CNPJ: {CNPJ}, D_Nascimento: {D_Nascimento},Carro: {Carro}, N da PLaca: {Placa}\n")
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
