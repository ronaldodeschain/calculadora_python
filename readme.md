# 🧮 Calculadora com Tkinter

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)

## 📝 Descrição do Projeto

Este projeto é uma calculadora funcional e com um design moderno, desenvolvida como parte do meu portfólio para aprimorar e demonstrar minhas habilidades com a biblioteca **Tkinter** do Python. O objetivo foi criar uma aplicação desktop que não apenas realizasse cálculos matemáticos, mas que também oferecesse uma experiência de usuário agradável através de uma interface intuitiva e bem estruturada.

A calculadora foi construída do zero, com foco em boas práticas de programação, organização do código e estilização visual.

---

## ✨ Visualização

A aplicação possui um tema escuro, fontes legíveis e botões coloridos para diferenciar números, operadores e funções especiais.

*(Dica: Substitua a imagem abaixo por uma captura de tela da sua calculadora em execução!)*

![Screenshot da Calculadora](https://i.imgur.com/placeholder.png "Interface da Calculadora")

---

## 🚀 Funcionalidades

A calculadora oferece um conjunto completo de funcionalidades para cálculos diários e científicos.

### Operações Aritméticas Básicas
- ✔️ **Soma** (`+`)
- ✔️ **Subtração** (`-`)
- ✔️ **Multiplicação** (`*`)
- ✔️ **Divisão** (`/`)

### Funções Científicas
- ✔️ **Seno** (`sin`): Calcula o seno de um ângulo em graus.
- ✔️ **Cosseno** (`cos`): Calcula o cosseno de um ângulo em graus.
- ✔️ **Tangente** (`tan`): Calcula a tangente de um ângulo em graus.
- ✔️ **Raiz Quadrada** (`sqrt`): Calcula a raiz quadrada de um número.

### Funções de Memória
- **MC (Memory Clear)**: Limpa o valor armazenado na memória (define como 0).
- **MR (Memory Recall)**: Recupera o valor da memória e o exibe no visor.
- **M+ (Memory Add)**: Adiciona o valor do visor ao valor já existente na memória.

### Controles da Calculadora
- **C (Clear)**: Limpa todo o campo de input.
- **DEL (Delete)**: Apaga o último caractere inserido.
- **= (Igual)**: Avalia a expressão matemática e exibe o resultado.

### Outras Características
- **Suporte ao Teclado**: Utilize os números, operadores, a tecla `Enter` (=) e `Backspace` (DEL) do seu teclado para interagir com a calculadora.
- **Interface Moderna**: Design com tema escuro, botões sem borda e layout organizado para uma melhor experiência de uso.
- **Janela Centralizada**: A aplicação sempre abre no centro da tela para maior conveniência.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal.
- **Tkinter**: Biblioteca padrão do Python para criação de interfaces gráficas (GUI).

---

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para executar a calculadora em seu ambiente local.

### Pré-requisitos

- É necessário ter o **Python 3** instalado em sua máquina.

### Passo a Passo

1.  **Clone o repositório** (ou baixe os arquivos para uma pasta em seu computador):
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2.  **Navegue até o diretório do projeto**:
    ```bash
    cd nome-do-repositorio
    ```

3.  **Execute o script Python**:
    ```bash
    python calculator.py
    ```

> **Nota**: Certifique-se de que o arquivo de ícone `calculator.ico` está na mesma pasta que o script `calculator.py` para que o ícone da janela seja exibido corretamente.

---

## � Gerando um Executável (.exe)

Para facilitar a distribuição e permitir que usuários executem a calculadora sem precisar ter o Python instalado, você pode gerar um arquivo executável `.exe`. Para isso, usaremos a biblioteca `PyInstaller`.

1.  **Instale o PyInstaller**:
    Abra seu terminal ou prompt de comando e execute o seguinte comando:
    ```bash
    pip install pyinstaller
    ```

2.  **Gere o executável**:
    Ainda no terminal, navegue até a pasta do projeto e execute o comando abaixo:
    ```bash
    pyinstaller --onefile -w --icon=calculator.ico calculator.py
    ```
    - `--onefile`: Agrupa tudo em um único arquivo executável.
    - `-w` ou `--windowed`: Impede que uma janela de console (terminal) seja aberta ao executar a aplicação.
    - `--icon=calculator.ico`: Define o ícone da aplicação.

3.  **Encontre o arquivo**:
    Após a conclusão do processo, uma nova pasta chamada `dist` será criada no diretório do seu projeto. Dentro dela, você encontrará o arquivo `calculator.exe`, pronto para ser executado e compartilhado.

---

## �📂 Estrutura do Código

O código-fonte está contido no arquivo `calculator.py` e é estruturado de forma orientada a objetos:

- **`Calculator(tk.Tk)`**: A classe principal que herda de `tk.Tk` e representa a janela da calculadora.
  - **`__init__`**: O construtor, onde toda a interface é montada, os estilos são definidos e os eventos são configurados.
  - **`button_click`, `clear_input`, `delete_char`**: Métodos que controlam a lógica principal dos botões.
  - **`memory_*`**: Métodos que implementam as funcionalidades de memória.
  - **`keyboard_input`**: Método para capturar e processar as entradas do teclado.
  - **`center_and_lock_window`**: Método utilitário para posicionar a janela na tela.

Essa estrutura torna o código modular, legível e fácil de dar manutenção ou expandir com novas funcionalidades.