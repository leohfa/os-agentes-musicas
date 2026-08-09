import os
import acoustid

# CONFIGURAÇÕES DEFINIDAS PARA O SEU PC
PASTA_MUSICAS = r"C:\Users\Leonardo\Downloads\todas_as_musicas"
API_KEY = "8XaBELgH8O" 

def identificar_musica(caminho_arquivo):
    try:
        # Analisa o áudio e busca no banco de dados do AcoustID
        resultados = acoustid.match(API_KEY, caminho_arquivo)
        for score, recording_id, title, artist in resultados:
            if title and artist:
                return title, artist
    except acoustid.NoMatchesError:
        return None, None
    except Exception as e:
        print(f"Erro ao processar {os.path.basename(caminho_arquivo)}: {e}")
        return None, None
    return None, None

def limpar_nome_arquivo(nome):
    """Remove caracteres proibidos pelo Windows em nomes de arquivos."""
    caracteres_invalidos = '<>:"/\\|?*'
    for char in caracteres_invalidos:
        nome = nome.replace(char, '')
    return nome.strip()

def analisar_diretorio(diretorio):
    print("🚀 Iniciando a identificação e renomeação das músicas...\n")
    
    # Adicionado .mpeg na lista de formatos suportados
    formatos_suportados = ('.mp3', '.wav', '.flac', '.m4a', '.mpeg', '.mpg')
    
    for arquivo in os.listdir(diretorio):
        if arquivo.lower().endswith(formatos_suportados):
            caminho_completo = os.path.join(diretorio, arquivo)
            print(f"Analisando áudio de: {arquivo}...")
            
            titulo, artista = identificar_musica(caminho_completo)
            
            if titulo and artista:
                # Limpa os nomes para evitar erros no Windows
                artista_limpo = limpar_nome_arquivo(artista)
                titulo_limpo = limpar_nome_arquivo(titulo)
                
                # Define o novo nome e a extensão original
                _, extensao = os.path.splitext(arquivo)
                novo_nome = f"{artista_limpo} - {titulo_limpo}{extensao}"
                novo_caminho = os.path.join(diretorio, novo_nome)
                
                try:
                    # Renomeia o arquivo fisicamente
                    os.rename(caminho_completo, novo_caminho)
                    print(f"✨ RENOMEADO PARA: {novo_name}")
                except Exception as e:
                    print(f"⚠️ Identificado como '{artista} - {titulo}', mas não pôde renomear: {e}")
                print("-" * 60)
            else:
                print("❌ Não foi possível identificar esta música por áudio.")
                print("-" * 60)

if __name__ == "__main__":
    if os.path.exists(PASTA_MUSICAS):
        analisar_diretorio(PASTA_MUSICAS)
    else:
        print("Erro: A pasta especificada não foi encontrada.")
