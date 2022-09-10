# PersonalCarros
 Criação de um app,  respeito de uma concessionária

- [X] Criar o arquivo index.html
    - Dentro da pasta receitas(app), crie a pasta `templates`
    - Dentro da pasta `templates` crie seus arquivos HTML começando pelo `index.html`
    - No arquivo `views.py` que está dentro da pasta do app faça a seguinte alteração de código:
    ```python
    from django.shortcuts import render

    def index(request):
        return render(request,'index.html')
    ```
- [X] Integrar arquivos estáticos (CSS, JS, IMG)
    - Dentro da pasta do projeto (PersonalCarros), criar a pasta `static`
    - Dentro da pasta static, colocar as imagens, os arquivos css e os arquivos js que for utilizar.
    - No arquivo `settings.py`:
        - Realize a importação da biblioteca `os` através do comando `import os`
        -  Na linha ~58 adicione o caminho dos templates da seguinte forma:
        ```python
        'DIRS': [os.path.join(BASE_DIR, 'receitas/templates')],
        ```
        - No final do arquivo, após a linha `STATIC_URL` na linha ~121 insira o seguinte código:
        ```python
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'PersonalCarros/static')
    ]
    ```
- `STATIC_URL`: é a configuração da rota através do qual os arquivos estáticos seram servidos. 
- `STATIC_ROOT`: configuração da pasta de saída (destino) dos arquivos estáticos.
- `STATICFILES_DIRS`: configuração da(s) pasta de origem dos arquivos estáticos.
- Após realizar essas configurações execute, no terminal, o comando `python manage.py collectstatic`.

- [ ] Utilizando links
    - 

- [ ] Criando o base.html
- [ ] Separando em partials
- [ ] Renderizando dados dinamicamente
- [ ] Criando um dicionario com as receitas
- [ ] Criando o banco de dados(MySQL/MariaDB)
- [ ] Instalando o conector do bando de dados MySQL
- [ ] Criando o modelo da receita
- [ ] Criando a migration (mapeamento)
- [ ] Realizando a migration
- [ ] Registrando um modelo no admin
- [ ] Criando um usuário para o ambiente administrativo