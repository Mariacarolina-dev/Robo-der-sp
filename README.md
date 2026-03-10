# 🤖 Robô de Consulta DER-SP (Placa/AIT)

Este projeto é uma ferramenta de automação (RPA) desenvolvida em **Python** para realizar consultas em lote no portal do **DER-SP**. Ele utiliza **Selenium** para navegação web e **Tkinter** para oferecer uma interface gráfica amigável, permitindo que usuários sem conhecimento em programação utilizem o robô.

---

## 🚀 Funcionalidades
- **Consulta em Lote:** Processa múltiplas placas e AITs simultaneamente.
- **Interface Intuitiva:** Campos de texto simples para colar dados e tabela de resultados (Treeview).
- **Multithreading:** A interface permanece responsiva e não trava durante a execução do robô.
- **Gestão Automática de Driver:** Utiliza `webdriver-manager` para configurar o Chrome automaticamente, eliminando a necessidade de baixar o `chromedriver.exe` manualmente.
- **Exportação Rápida:** Menu de contexto (botão direito) para copiar os resultados diretamente para a área de transferência.

---

## 🛠️ Tecnologias e Requisitos
- **Linguagem:** [Python 3.13+](https://www.python.org/)
- **Bibliotecas Principais:** `selenium`, `webdriver-manager`, `tkinter`, `threading`.
- **Navegador:** Google Chrome instalado e atualizado.

---

## 💻 Como Rodar (Para Desenvolvedores)

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Mariacarolina-dev/Robo-der-sp.git](https://github.com/Mariacarolina-dev/Robo-der-sp.git)
   cd Robo-der-sp

```

2. **Instale as dependências:**
```bash
pip install selenium webdriver-manager

```


3. **Execute o script:**
```bash
python 0210.PY

```



---

## 📦 Como Gerar e Usar o Executável (.exe)

Se você deseja transformar este script em um programa independente para usuários que não possuem Python instalado:

1. **Instale o PyInstaller:**
```bash
pip install pyinstaller

```


2. **Gere o arquivo:**
```bash
pyinstaller --noconsole --onefile --name "Consulta_DER_SP" 0210.PY

```


*O arquivo final será gerado na pasta `dist/`.*

### 📖 Guia de Uso para o Usuário Final

1. Abra o arquivo `Consulta_DER_SP.exe`.
2. Na coluna da **Esquerda**, cole as **Placas** (uma por linha).
3. Na coluna da **Direita**, cole os números de **AIT** (na mesma ordem das placas).
4. Clique em **Consultar**. O robô abrirá o Chrome e preencherá os dados sozinho.
5. **Atenção:** Não feche a janela do navegador enquanto o robô estiver trabalhando.
6. Ao final, os resultados aparecerão na tabela. Clique com o botão direito para copiar.

---

## ⚠️ Observações e FAQ

* **Erro de Conexão:** Se o site do DER estiver instável, o robô pode falhar em carregar os elementos. Reinicie a consulta se necessário.
* **Antivírus:** O Windows pode sinalizar o `.exe` como desconhecido. Clique em "Mais informações" > "Executar assim mesmo".
* **Privacidade:** Certifique-se de não subir arquivos de configuração pessoal (`config.json`) para repositórios públicos.

---

**Desenvolvido por [Maria Carolina](https://www.google.com/search?q=https://github.com/Mariacarolina-dev) ✨**
