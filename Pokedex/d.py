import requests 
import json 
from django.shortcuts import render
from django.http import HttpResponse
import requests
from PIL import Image
from io import BytesIO

def habidades(poke):
   for i in poke['abilities']:
      print(i['ability']['name'])

pokemon = str(input("pokémon: "))
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
response = requests.get(url
                                )
if response.status_code == 200:
            poke = response.json()
            habidades(poke)




<div>
        <footer class="footer">
            <p class="footer__text">desenvolvido por <a href="#"> ewerson2022</a></p>
        </footer>
    </div>


.footer{
    background-color: var(--gray-900);
    color: var(--white-900);
    height: 100px;
}
    
   