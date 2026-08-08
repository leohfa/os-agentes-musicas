from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random
import os

def carregar_lista_medicamentos() -> list:
    """Lê os nomes dos medicamentos do arquivo de texto externo."""
    nome_arquivo = 'lista_medicamentos.txt'
    if not os.path.exists(nome_arquivo):
        print(f"Aviso: Arquivo '{nome_arquivo}' não encontrado. Usando modelo básico...")
        return ["Dipirona", "Paracetamol", "Ibuprofeno", "Omeprazol"]
        
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return [linha.strip() for bundle, linha in enumerate(f.readlines()) if linha.strip()]

def main() -> None:
    medicamentos_alvo = carregar_lista_medicamentos()
    print(f"Total de medicamentos carregados para busca: {len(medicamentos_alvo)}")
    
    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--start-maximized")
    opcoes.add_argument("--disable-blink-features=AutomationControlled")
    opcoes.add_experimental_option("excludeSwitches", ["enable-automation"])
    opcoes.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=opcoes)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    
    nome_planilha = 'medicamentos.csv'
    with open(nome_planilha, mode='w', newline='', encoding='utf-8-sig') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow(['Pesquisa Original', 'Nome Comercial / Produto', 'Preço'])

    try:
        driver.get("https://drogaraia.com.br")
        wait = WebDriverWait(driver, 15)
        
        for indice, medicamento in enumerate(medicamentos_alvo, start=1):
            print(f"[{indice}/{len(medicamentos_alvo)}] Buscando por: {medicamento}...")
            
            try:
                search_box = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//input[@type='search' or contains(@placeholder, 'Buscar')]"))
                )
                
                search_box.clear()
                search_box.send_keys(medicamento)
                search_box.send_keys(Keys.ENTER)
                
                # Pausa para renderização do conteúdo assíncrono
                time.sleep(random.uniform(5.0, 7.0))
                
                # Localização ampla de contêineres usando múltiplos padrões do e-commerce da Raia
                produtos = driver.find_elements(By.XPATH, "//article | //div[contains(@data-testid, 'product-card') or contains(@class, 'productCard')]")
                
                dados_desse_medicamento = []
                contador_por_medicamento = 0
                
                for produto in produtos:
                    if contador_por_medicamento >= 3:
                        break
                        
                    try:
                        # Extração inteligente via quebra de blocos textuais visíveis
                        texto_bloco = produto.text.strip()
                        if not texto_bloco or "R$" not in texto_bloco:
                            continue
                            
                        linhas = [l.strip() for l in texto_bloco.split("\n") if l.strip()]
                        
                        # Ignora blocos institucionais, banners ou cabeçalhos do site
                        if len(linhas) < 2 or "compre" in linhas[0].lower() or "buscar" in linhas[0].lower():
                            continue
                            
                        nome_comercial = linhas[0]
                        preco_final = "Não encontrado"
                        
                        # Varre de baixo para cima para achar o preço de venda real ativo
                        for linha in reversed(linhas):
                            if "R$" in linha and "por" not in linha.lower() and "cada" not in linha.lower() and linha != "R$ 0,00":
                                preco_final = linha
                                break
                                
                        if preco_final == "Não encontrado":
                            for linha in reversed(linhas):
                                if "R$" in linha and linha != "R$ 0,00":
                                    preco_final = linha
                                    break

                        if nome_comercial and preco_final != "Não encontrado" and len(nome_comercial) > 4:
                            # Evita salvar nomes duplicados seguidos no mesmo laço
                            if not any(item[1] == nome_comercial for item in dados_desse_medicamento):
                                dados_desse_medicamento.append([medicamento, nome_comercial, preco_final])
                                contador_por_medicamento += 1
                            
                    except Exception:
                        continue
                
                if dados_desse_medicamento:
                    with open(nome_planilha, mode='a', newline='', encoding='utf-8-sig') as arquivo:
                        escritor = csv.writer(arquivo, delimiter=';')
                        escritor.writerows(dados_desse_medicamento)
                    print(f"   -> Sucesso: {contador_por_medicamento} marcas gravadas.")
                else:
                    print("   -> Nenhum resultado capturado para este termo.")
                    
                time.sleep(random.uniform(2.0, 3.0))
                
            except Exception as erro_busca:
                print(f"   -> Erro ao pesquisar '{medicamento}': {erro_busca}")
                driver.get("https://drogaraia.com.br")
                time.sleep(5)
                continue
                
        print(f"\n Processo finalizado com sucesso!")
                
    except Exception as e:
        print(f"Ocorreu um erro geral: {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
