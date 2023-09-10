import justpy as jp

from webapp.about import About
from webapp.home import Home

#instantiate the class only when user go to the domain base_url/about or /home   
jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)


jp.justpy(port=8001)