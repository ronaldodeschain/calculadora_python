import tkinter as tk
import math
from tkinter import font
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- Configurações de Estilo --- #
        # Define as cores da interface
        self.COLOR_BACKGROUND = '#212121'  # Preto fosco
        self.COLOR_INPUT_BG = '#424242'    # Cinza escuro
        self.COLOR_INPUT_FG = '#FFFFFF'    # Branco
        self.COLOR_BTN_NUM_BG = '#616161'   # Cinza para números
        self.COLOR_BTN_OP_BG = '#FF9800'    # Laranja para operadores
        self.COLOR_BTN_FUNC_BG = '#4CAF50'  # Verde para funções
        self.COLOR_BTN_FG = '#FFFFFF'       # Branco para texto do botão

        # Define a cor de fundo da janela principal
        self.configure(bg=self.COLOR_BACKGROUND)

        # Define o ícone da aplicação
        self.iconbitmap('calculator.ico')

        # Define o título da janela
        self.title("Calculadora")

        # --- Campo de Input --- #
        # Define uma fonte maior e em negrito para o campo de input
        input_font = font.Font(size=24, weight='bold')

        # Cria uma variável para armazenar o texto do campo de input
        self.input_text =tk.StringVar()

        # Cria o campo de input (Entry)
        self.input_field = tk.Entry(self,textvariable=self.input_text,
                                    justify='right',
                                    font=input_font,
                                    width=16,
                                    bg=self.COLOR_INPUT_BG,
                                    fg=self.COLOR_INPUT_FG,
                                    bd=0,
                                    relief='flat')

        # Posiciona o campo de input na janela usando o grid layout
        self.input_field.grid(row=0,
                                column=0,
                                columnspan=5,
                                padx=10,
                                pady=20,
                                ipady=10)

        # --- Botões da Calculadora --- #
        # Define os textos dos botões
        buttons = [
            '7','8','9','/','sin',
            '4','5','6','*','cos',
            '1','2','3','-','tan',
            '0','.','=','+','sqrt'
            
        ]

        # Cria os botões e os adiciona ao grid
        row = 1
        col = 0 

        # Define a fonte padrão para os botões
        btn_font = font.Font(size=12)

        # Loop para criar cada botão
        for button in buttons:
            # Define a ação do botão (o que acontece quando é clicado)
            button_action = lambda x=button: self.button_click(x)
            
            # Define a cor de fundo baseada no tipo de botão
            if button in '0123456789.':
                bg_color = self.COLOR_BTN_NUM_BG
            elif button in '/*-+=':
                bg_color = self.COLOR_BTN_OP_BG
            else:
                bg_color = self.COLOR_BTN_FUNC_BG
            
            # Cria o botão com as configurações definidas
            btn = tk.Button(self,
                            text=button,
                            bg=bg_color,
                            fg=self.COLOR_BTN_FG,
                            font=btn_font,
                            width=5,
                            command=button_action,
                            bd=0,
                            relief='flat')
            
            # Adiciona o botão ao grid layout
            btn.grid(row=row,
                    column=col,
                    padx=2,
                    pady=2,
                    sticky='nsew',
                    ipady=10)

            col +=1
            if col > 4:
                col =0
                row +=1

        # --- Botões de Controle e Memória --- #
        # Reorganiza os botões de controle (C, DEL, MC, MR)
        control_buttons = {
            'C': (self.clear_input, 0), 'DEL': (self.delete_char, 1),
            'MC': (self.memory_clear, 2), 'MR': (self.memory_recall, 3)
        }

        # Loop para criar os botões de controle
        for (text, (command, col)) in control_buttons.items():
            tk.Button(self, text=text, bg=self.COLOR_BTN_OP_BG,
                    fg=self.COLOR_BTN_FG, font=btn_font, width=5, 
                    command=command, bd=0, relief='flat').grid(
                        row=6, column=col, padx=2, pady=2, sticky='nsew', ipady=10)

        # Cria o botão de adicionar à memória (M+)
        tk.Button(self, text='M+', bg=self.COLOR_BTN_OP_BG,
                fg=self.COLOR_BTN_FG, font=btn_font, width=5, 
                command=self.memory_add, bd=0, relief='flat').grid(
                    row=6, column=4, padx=2, pady=2, sticky='nsew', ipady=10)

        # --- Eventos do Teclado --- #
        # Permite que a calculadora receba inputs do teclado
        self.bind('<Key>',self.keyboard_input)

        # --- Configurações da Janela --- #
        # Centraliza a janela na tela e impede o redimensionamento
        self.center_and_lock_window()

        # --- Inicialização da Memória --- #
        # Inicializa a memória da calculadora com o valor 0
        self.memory = 0

    def center_and_lock_window(self):
        # Centraliza a janela na tela e impede o redimensionamento
        self.update_idletasks()  # Força a atualização
        
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        self.resizable(False, False) # Impede que a janela seja redimensionada
    
    def button_click(self,button):
        # Manipula os cliques dos botões
        if button == '=':
            # Se o botão clicado for o '=', calcula o resultado
            try:
                # Avalia a expressão no campo de input
                result = eval(self.input_text.get())
                # Define o resultado no campo de input
                self.input_text.set(result)
            except:
                # Se ocorrer um erro, exibe 'ERROR' no campo de input
                self.input_text.set('ERROR')
        elif button == 'C':
            # Se o botão clicado for o 'C', limpa o campo de input
            self.clear_input()
        elif button == 'DEL':
            # Se o botão clicado for o 'DEL', apaga o último caractere
            self.delete_char()
        elif button == 'sin':
            # Se o botão clicado for 'sin', calcula o seno
            self.input_text.set(math.sin(math.radians(float(
                self.input_text.get())))) #type:ignore
        elif button == 'cos':
            # Se o botão clicado for 'cos', calcula o cosseno
            self.input_text.set(math.cos(math.radians(float(
                self.input_text.get())))) #type:ignore
        elif button == 'tan':
            # Se o botão clicado for 'tan', calcula a tangente
            self.input_text.set(math.tan(math.radians(float(
                self.input_text.get())))) #type:ignore
        elif button == 'sqrt':
            # Se o botão clicado for 'sqrt', calcula a raiz quadrada
            self.input_text.set(math.sqrt(float(
                self.input_text.get()))) #type:ignore
        else:
            # Se for um botão normal (número ou operador),
            # adiciona o texto do botão ao campo de input
            current_text = self.input_text.get()
            new_text = current_text + button
            self.input_text.set(new_text)

    def clear_input(self):
        # Limpa o campo de input
        self.input_text.set('')

    def delete_char(self):
        # Apaga o último caractere do campo de input
        current_text = self.input_text.get()
        new_text = current_text[:-1]
        self.input_text.set(new_text)

    def keyboard_input(self,event):
        # Manipula os inputs do teclado
        if event.char in '0123456789-*/.()':
            # Se a tecla pressionada for um número ou operador,
            # simula o clique do botão correspondente
            self.button_click(event.char)
        elif event.keysym == 'Return':
            # Se a tecla pressionada for 'Enter', simula o clique
            # no botão '='
            self.button_click('=')
        elif event.keysym == 'BackSpace':
            # Se a tecla pressionada for 'Backspace', simula o clique
            # no botão 'DEL'
            self.delete_char()

    def memory_add(self):
        # Adiciona o valor atual do campo de input à memória
        current_input = self.input_text.get()
        try:
            # Tenta converter o valor para float
            current_input = float(current_input)
            # Adiciona o valor à memória
            self.memory += current_input
        except:
            # Se não for um número válido, ignora
            pass 
    
    def memory_subtract(self):
        # Subtrai o valor atual do campo de input da memória
        current_input = self.input_text.get()
        try:
            # Tenta converter o valor para float
            current_input = float(current_input)
            # Subtrai o valor da memória
            self.memory -= current_input
        except:
            # Se não for um número válido, ignora
            pass

    def memory_recall(self):
        # Exibe o valor da memória no campo de input
        self.input_text.set(str(self.memory))

    def memory_clear(self):
        # Limpa o valor da memória (define como 0)
        self.memory = 0

calc = Calculator()

calc.mainloop()