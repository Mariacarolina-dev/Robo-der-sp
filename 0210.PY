import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading


# --- FUNÇÕES DE AUTOMAÇÃO ---

def executar_der_sp_thread(consultas, tree_resultados):
    """Inicia a execução da automação em uma thread separada para não travar a interface."""
    thread = threading.Thread(target=executar_der_sp, args=(consultas, tree_resultados))
    thread.daemon = True # Garante que a thread feche se o programa principal fechar
    thread.start()


def executar_der_sp(consultas, tree_resultados):
    """Executa o scraping do DER-SP com gerenciamento automático de versão do driver."""
    try:
        chrome_options = Options()
        # O ChromeDriverManager baixa e gerencia a versão correta do driver automaticamente
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        url = "http://www.eindicacao.der.sp.gov.br/der_eindicacao_web/Pesquisa/Placa_AIT"
        driver.get(url)

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "PLACA")))

        resultados = []

        for placa, ait in consultas:
            try:
                # Preenche os campos
                placa_input = driver.find_element(By.ID, "PLACA")
                ait_input = driver.find_element(By.ID, "AIT")
                placa_input.clear()
                ait_input.clear()
                placa_input.send_keys(placa)
                ait_input.send_keys(ait)

                # Clica em pesquisar
                btn_pesquisar = driver.find_element(By.ID, "search")
                btn_pesquisar.click()

                time.sleep(2)

                try:
                    # Espera a tela de resultados
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//span[text()="Retorno Pesquisa Indicação"]'))
                    )

                    # Tenta extrair a situação
                    situacao_elem = driver.find_element(By.ID, "OUT_RESPLIA4_OC_0__OUT_RESPLIA4_OC_SITUACAO")
                    situacao_texto = situacao_elem.get_attribute('value').strip()

                    protocolo = ""
                    if "Indicação de Condutor aceita" in situacao_texto:
                        # Se aceita, tenta pegar o protocolo
                        protocolo_elem = driver.find_element(By.ID, "OUT_RESPLIA4_OC_0__OUT_RESPLIA4_OC_PROTOCOLO")
                        protocolo = protocolo_elem.get_attribute('value').strip()
                    
                    resultados.append((placa, ait, situacao_texto, protocolo))

                    # Clica em 'Nova Pesquisa'
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//input[@value="Nova Pesquisa"]'))
                    ).click()
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "PLACA")))

                except:
                    # Caso não encontre a tela de resultados
                    resultados.append((placa, ait, "Sem resultado", ""))

                    # Tenta fechar a mensagem de erro (se houver)
                    try:
                        WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, '//input[@value="Fechar"]'))
                        ).click()
                    except:
                        pass

                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "PLACA")))

            except Exception as e:
                resultados.append((placa, ait, f"Erro na consulta", ""))
                driver.get(url) 
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "PLACA")))

        # Atualiza a interface (limpa e insere) - usamos root.after para segurança da UI
        for item in tree_resultados.get_children():
            tree_resultados.delete(item)

        for r in resultados:
            tree_resultados.insert("", tk.END, values=r)
            
    except Exception as main_e:
        messagebox.showerror("Erro Geral na Consulta", f"Ocorreu um erro inesperado durante a execução: {main_e}")

    finally:
        if 'driver' in locals() and driver:
            driver.quit()
        messagebox.showinfo("Consulta Concluída", "Todas as verificações foram finalizadas.")


# --- INTERFACE ---

def abrir_interface():
    root = tk.Tk()
    root.title("Consulta DER-SP (Placa/AIT)")
    root.geometry("800x600")
    
    # Cores na Interface
    BG_COLOR = root["bg"] 
    TEXT_COLOR = "gray"

    # Frame principal
    frame_text = tk.Frame(root)
    frame_text.pack(pady=10)

    # Coluna para Placas
    tk.Label(frame_text, text="Cole aqui as Placas (linha por linha):").grid(row=0, column=0, padx=10, sticky="w")
    text_placas = tk.Text(frame_text, width=30, height=10)
    text_placas.grid(row=1, column=0, padx=10)

    # Coluna para AITs
    tk.Label(frame_text, text="Cole aqui as AITs (linha por linha):").grid(row=0, column=1, padx=10, sticky="w")
    text_aits = tk.Text(frame_text, width=30, height=10)
    text_aits.grid(row=1, column=1, padx=10)

    def iniciar_consulta():
        """Prepara os dados e dispara a automação em thread."""
        placas = [p.strip().upper() for p in text_placas.get("1.0", tk.END).strip().splitlines() if p.strip()]
        aits = [a.strip() for a in text_aits.get("1.0", tk.END).strip().splitlines() if a.strip()]

        if not placas or not aits:
            messagebox.showwarning("Aviso", "As listas de Placas e AITs não podem estar vazias.")
            return

        if len(placas) != len(aits):
            messagebox.showwarning("Aviso", "A quantidade de Placas e AITs deve ser igual.")
            return

        consultas = list(zip(placas, aits))
        # Agora chamamos a função de thread para evitar NameError e travamento da UI
        executar_der_sp_thread(consultas, tree_resultados)

    def limpar_campos_e_tabela():
        """Limpa campos de texto e a tabela."""
        text_placas.delete("1.0", tk.END)
        text_aits.delete("1.0", tk.END)
        for item in tree_resultados.get_children():
            tree_resultados.delete(item)
        messagebox.showinfo("Limpeza", "Campos e resultados limpos.")

    # Botões
    tk.Button(frame_text, text="Consultar", command=iniciar_consulta, width=20, bg="green", fg="white").grid(row=2, column=0, pady=10, padx=10, sticky="n")
    tk.Button(frame_text, text="Limpar", command=limpar_campos_e_tabela, width=20, bg="red", fg="white").grid(row=2, column=1, pady=10, padx=10, sticky="n")
    
    # Tabela de Resultados
    tree_resultados = ttk.Treeview(
        root,
        columns=("Placa", "AIT", "Situação", "Protocolo"),
        show="headings",
        height=15
    )
    tree_resultados.heading("Placa", text="Placa", anchor=tk.CENTER)
    tree_resultados.heading("AIT", text="AIT", anchor=tk.CENTER)
    tree_resultados.heading("Situação", text="Situação", anchor=tk.W)
    tree_resultados.heading("Protocolo", text="Protocolo", anchor=tk.CENTER)
    
    tree_resultados.column("Placa", width=80, anchor=tk.CENTER)
    tree_resultados.column("AIT", width=120, anchor=tk.CENTER)
    tree_resultados.column("Situação", width=350, anchor=tk.W)
    tree_resultados.column("Protocolo", width=120, anchor=tk.CENTER)
    
    tree_resultados.pack(fill="x", padx=10, pady=10)

    # --- LÓGICA DE CÓPIA ---
    def copiar_selecao(event=None):
        item_id = tree_resultados.selection()
        if item_id:
            valores = tree_resultados.item(item_id, 'values')
            texto = "\t".join(valores)
            root.clipboard_clear()
            root.clipboard_append(texto)
            root.update()

    def menu_popup(event):
        item_id = tree_resultados.identify_row(event.y)
        if item_id:
            tree_resultados.selection_set(item_id)
            menu_contexto.post(event.x_root, event.y_root)

    menu_contexto = tk.Menu(root, tearoff=0)
    menu_contexto.add_command(label="Copiar Linha (Ctrl+C)", command=copiar_selecao)
    
    tree_resultados.bind("<Control-c>", copiar_selecao)
    tree_resultados.bind("<Button-3>", menu_popup)

    # Rodapé
    footer_label = tk.Label(root, text="Copyright © 2025 Maria Carolina | Desenvolvido com Python/Tkinter e Selenium", font=("Arial", 8, "italic"), bg=BG_COLOR, fg=TEXT_COLOR)
    footer_label.pack(side="bottom", fill="x", pady=5)

    root.mainloop()


if __name__ == "__main__":
    abrir_interface()