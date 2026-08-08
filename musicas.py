import os
import re

PASTA_NAO_IDENTIFICADAS = r"c:\Users\Leonardo\Downloads\musicas_nao_identificadas"

def extrair_data_e_organizar(pasta):
    print("Iniciando a padronização segura dos arquivos...\n")
    
    if not os.path.exists(pasta):
        print("Pasta de destino não encontrada.")
        return

    arquivos = os.listdir(pasta)
    contador_sucesso = 0
    
    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta, arquivo)
        
        if os.path.isfile(caminho_completo) and "whatsapp" in arquivo.lower():
            # Extrai data e hora
            padrao_data = re.search(r"\d{4}-\d{2}-\d{2}", arquivo)
            padrao_hora = re.search(r"at \d{2}\.\d{2}\.\d{2}", arquivo)
            
            data_str = padrao_data.group(0) if padrao_data else "Data-Desconhecida"
            # CORREÇÃO: Trocado o ":" por "." para o Windows aceitar o nome
            hora_str = padrao_hora.group(0).replace("at ", "").replace(".", "-") if padrao_hora else "Hora-Desconhecida"
            
            # Captura o número da cópia para manter a organização
            padrao_copia = re.search(r"\(\d+\)", arquivo)
            copia_str = f" {padrao_copia.group(0)}" if padrao_copia else ""
            
            # Monta o nome final seguro para o Windows
            novo_nome_base = f"Freestyle Track - Recebida em {data_str} às {hora_str}{copia_str}"
            
            _, extensao = os.path.splitext(arquivo)
            novo_nome_completo = f"{novo_nome_base}{extensao}"
            caminho_novo = os.path.join(pasta, novo_nome_completo)
            
            # Evita conflitos de arquivos duplicados
            sufixo = 1
            while os.path.exists(caminho_novo):
                caminho_novo = os.path.join(pasta, f"{novo_nome_base}_{sufixo}{extensao}")
                sufixo += 1
                
            try:
                os.rename(caminho_completo, caminho_novo)
                print(f"Sucesso: {os.path.basename(caminho_novo)}")
                contador_sucesso += 1
            except Exception as e:
                print(f"Erro ao renomear {arquivo}: {e}")

    print(f"\nProcesso concluído! {contador_sucesso} arquivos foram padronizados com sucesso.")

extrair_data_e_organizar(PASTA_NAO_IDENTIFICADAS)
