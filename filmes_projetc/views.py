from django.shortcuts import render
import requests
chave_api = '17528cca6d733031cd27a0916ee4cde5'

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    
    if request.method == 'POST':
        pesquisar = request.POST.get('pesquisar')
        if pesquisar:
            # URL do endpoint de busca de filmes
            url = f'https://api.themoviedb.org/3/search/movie?api_key={chave_api}&query={pesquisar}'

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
                    print(f"O filme '{pesquisar}' não tem um pôster disponível.")
            else:
                print(f"Nenhum filme encontrado com o nome '{pesquisar}'.")

            if response.status_code == 200:
                for movie in data['results']:
                    return render(request, 'home.html', {'nome_filme': movie['title'], 'poster_filme': movie['poster_path']})                           
            else:
                return render(request, 'home.html', {'erro': response.status_code + response.text})


        return render(request, 'home.html',)
    
def filme(request):
    if request.method == 'GET':
        return render(request, 'filme.html')
    else:
        return render(request, 'filme.html')
