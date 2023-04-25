# Arquivo Makefile para rodar os comandos de padronização e formatação de código.
#Escreve o comando: make <comando>
instalar_mysql:
	 pip install mysql-connector

instalar_django:
	pip install django

#cria_requeremento:
	#@echo 'Criando ou Atualizando Arquivo de Requerimento.'
	#@pip freeze > requerimentos.txt


#instala_requerimento:
#	pip install -r requerimentos.txt

#instala_mkdoc:
#	pip install mkdocs

#executa_mkdoc:
#	mkdocs new .



versao_django:
	python -m django version

#inicia_mysite: #Cria a pasta MySite na raiz do projeto, sem subpasta. Só faz uma vez na criação da App Principal (Config).
#	django-admin startproject siteconfig .

#inicia_siteXXApp: #Cria a pasta do App para o Django
#	python manage.py startapp XXApp
#	python manage.py startapp apiXXApp

#migra_projeto:
	#cd mysite
	#python manage.py migrate (Não precisa, apenas se usar Banco local e queira usar o admin user).

#roda_migrations
	#python manage.py makemigrations

#super_usuario
	#python manage.py createsuperuser

#instala_swagger
#pip install -U drf-yasg

roda_django:
	python manage.py runserver

instala_api_rest:
	pip install djangorestframework;
	pip install markdown;
	pip install django-filter;



#Esconde Chave secreta do Django ou outros códigos sensiveis.
instala_python_dotenv:
	pip install python-dotenv

format:
	isort .
	blue .
	echo "Codigo Formatado!"

check:
	@echo 'Checando Codigo com o Blue..'
	blue .
	@echo 'Checando Codigo com o Isort..'
	isort .

test:
	pytest -v

security:
	@echo 'Realizando auditoria em seu Projeto.'
	@pip-audit .

lista_pacotes:
	@echo 'Listando dependencias instaladas.'
	pip freeze
