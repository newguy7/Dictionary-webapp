import inspect
import justpy as jp

from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
from webapp import page

## Automate the creation of jp.Route(Home.path, Home.serve).....
imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

#instantiate the class only when user go to the domain base_url/about or /home   
# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)


jp.justpy(port=8001)