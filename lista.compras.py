import tkinter as tk
from tkinter import ttk, messagebox
import os

# ===========================================
# LISTA DE COMPRAS - Aplicativo em Tkinter
# ===========================================

ARQUIVO = "lista_compras.txt" 

class ListaComprasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Lista de Compras")
        self.root.geometry("750x550")
        self.root.configure(bg="#f0f4f8")

        # Dados em memória
        self.itens = []
        self.item_selecionado = None
        
        self.criar_widgets()
        self.carregar_do_arquivo()
        self.atualizar_lista()

        def criar_widgets(self):
            # ========= TÍTULO =========
            ibl_título = tk.Label(
                self.root,
                text="🛒 LISTA DE COMPRAS",
                font=("Arial", 20, "bold"),
                bg= "#f0f4f8",
                fg= "#1a5276"
            )
            ibl_título.pack(pady=10)


            # ========= FRAME DE ENTRADA =========
            frame_entrada = tk.Frame(self.root, bg= "#f0f4f8")
            frame_entrada.pack(pady=10, padx=20, fill= "x")

            # Descrição
            tk.Label(frame_entrada, text="descrição:", font=("Arial", 11), bg= "#f0f4f8", fg= "#2c3e50").grid(row=0, column=0, padx=5, pady=5, sticky="e") 
            self.txt_descricao = tk.Entry(frame_entrada, font=("Arial", 11)), width=30, relief="solid", bd=1 )
            self.txt_descricao.grild(row=0, column=1, padx=5, pady=5)

            # Quantidade
            tk.Label(frame_entrada, text="descrição:", font=("Arial", 11), bg= "#f0f4f8", fg= "#2c3e50").grid(row=0, column=0, padx=5, pady=5, sticky="e") 
            self.txt_descricao = tk.Entry(frame_entrada, font=("Arial", 11)), width=30, relief="solid", bd=1 )
            self.txt_descricao.grild(row=0, column=1, padx=5, pady=5)

            # Preço
            tk.Label(frame_entrada, text="descrição:", font=("Arial", 11), bg= "#f0f4f8", fg= "#2c3e50").grid(row=0, column=0, padx=5, pady=5, sticky="e") 
            self.txt_descricao = tk.Entry(frame_entrada, font=("Arial", 11)), width=30, relief="solid", bd=1 )
            self.txt_descricao.grild(row=0, column=1, padx=5, pady=5)

            # ============== FRAME DE BOTÕES ==============
            rame_botoes = tk.frame(self.root, bg"#f0f4f8")
            rame_botoes.pack(pady=10)

            #Botão inserir 
            self.btn_inserir = tk.Button(
                 frame_botoes,
                 text"➕inserir",
                 font= ("Arial", 11, "bola"),
                 bg="#27ae60", fg="white",
                 width=12, cursor="hand2",
                 relief="flat",
                 command=self.inserir
    )
            self.btn_inserir.pack(side="left", padx=5)
            # Botão Editar
             self.btn_botoes,
             text"- Editar", 
            font=("Arial", 11, "bold"),
            bg="#f39c12, fg= "white",
            width=12, cursor= "hand2",
            relief="flat",
            comand-self.editar
        )
        self.btn_editar.pack(side= "left",padx=5)

       # Botão Deletar
         self.btn_deletar = tk.Button(
             frame_botões,
             text"🥤Deletar",
             font=
            
