import requests

chave_api = '17528cca6d733031cd27a0916ee4cde5'
nome_filme = 'thor amor e trõvao'

url_procura_filme = f"https://api.themoviedb.org/3/search/movie?api_key={chave_api}&query={nome_filme}&language=pt-BR"

resposta = requests.get(url_procura_filme)

data = resposta.json()

if resposta.status_code == 200:
    for movie in data['results']:
        print(f'Resultado: {movie['title']}')

else:
    print(f'Erro: {resposta.status_code}' + resposta.text)

def buscar_poster_filme(nome_filme):
    # URL do endpoint de busca de filmes
    url = f'https://api.themoviedb.org/3/search/movie?api_key={chave_api}&query={nome_filme}'

    # Fazendo a requisição
    response = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        
        # Checando se encontrou algum filme
        if data['results']:
            # Pegando o primeiro resultado (mais relevante)
            filme = data['results'][0]
            
            # Montando a URL completa do pôster
            poster_path = filme.get('poster_path')
            if poster_path:
                poster_url = f'https://image.tmdb.org/t/p/w500{poster_path}'
                print(f"Título: {filme['title']}\nPôster: {poster_url}")
            else:
                print(f"O filme '{nome_filme}' não tem um pôster disponível.")
        else:
            print(f"Nenhum filme encontrado com o nome '{nome_filme}'.")
    else:
        print("Erro ao fazer a requisição:", response.status_code)

# Solicita ao usuário que insira o nome do filme
nome_filme = input("Digite o nome do filme: ")

# Chama a função para buscar o filme e exibir o pôster
buscar_poster_filme(nome_filme)