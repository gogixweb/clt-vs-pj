<h1>clt-vs-pj</h1>

<h2>Configurando o projeto:</h2>

<p>
Para esse projeto é necessario ter instalado o python a partir da versão <a href="https://www.python.org/downloads/">3.8</a> e o <a href= "https://pypi.org/project/pip/">pip 3</a>
</p>

<h3>Primeiro passo</h3>

<p>
Nós recomendamos o uso de um <i>virtual enviroment</i>, para envitar conflitos com as versões das bibliotecas utilizadas. Você pode utilizar essa <a href="https://docs.python.org/3/library/venv.html">biblioteca</a> para criar o seu <i>enviroment</i>.

</br>
Usando o venv, você pode usar o seguinte comando na raiz do projeto:
<blockquote>python -m venv venv</blockquote>
</p>

<h3>Segundo passo</h3>

<p>
Neste passo você pode ativar o seu <i>virtual env</i> e executar o comando abaixo para instalar todas as dependencias necessarias
<blockquote>
pip install -r requirements.txt
</blockquote>
</p>

<h3>Terceiro passo</h3>

Você precisa rodar o comando de migração para criar as tabelas no banco de dados

<blockquote>
python manage.py migrate
</blockquote>

Execute o comando para iniciar o servidor web no localhost:
<blockquote>
python manage.py runserver
</blockquote>
