---
title: |
  "Introduction to Python modules."
date: May, 2022
lang: en-EN
urlcolor: blue
geometry: "left=2.5cm,right=2.5cm,top=3cm,bottom=3cm"
documentclass: article
fontfamily: Alegreya
header-includes: |
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhf{}
    \rhead{Dakar Institute of Technology}
    \lhead{Mouhamed KONTE}
    \rfoot{Page \thepage}
    \hypersetup{pdftex,
            pdfauthor={Mouhamed KONTE},
            pdftitle={Typage en python},
            pdfsubject={Python : Type Hint},
            pdfkeywords={Python, Programming,tpye hint,hint,type,typage},
            pdfproducer={Emacs, Pandoc, Latex, Markdown},
            pdfcreator={Emacs, Pandoc, Latex, Markdown}}
    
---

# <center>Python : Type Hint</center>
<p align="center">
  <img width="" height="" src="https://njqdev.gallerycdn.vsassets.io/extensions/njqdev/vscode-python-typehint/1.4.1/1603040363664/Microsoft.VisualStudio.Services.Icons.Default">
</p>

# <center>Introduction</center>
Python est un langage de programmation puissant et facile à apprendre. Il dispose de structures de données de haut niveau et permet une approche simple mais efficace de la programmation orientée objet. Parce que sa syntaxe est élégante, que son typage est dynamique et qu'il est interprété, Python est un langage idéal pour l'écriture de scripts et le développement rapide d'applications dans de nombreux domaines et sur la plupart des plateformes.

L'interpréteur Python et sa vaste bibliothèque standard sont disponibles librement, sous forme de sources ou de binaires, pour toutes les plateformes majeures depuis le site Internet https://www.python.org/ et peuvent être librement redistribués. 

# <center>Type Hints in Python</center>
L’un des points positifs du langage est le gain en productivité pendant le développement d’applications web par rapport à d’autres langages à typage statique comme Java ou C++. Par conséquent, un gain de temps précieux pour les entreprises qui font de plus en plus le choix de Python.

Paradoxalement, la simplicité de Python peut devenir problématique. Les applications sont plus rapidement en production mais elles peuvent également contenir plus de bugs. L’une des critiques souvent évoquées sur Python est son typage dynamique. En effet, le type de variables est assigné lors de la déclaration et il peut être modifié pendant l’interprétation du code.

Pour pallier cette problématique, Python 3.5 a introduit le « type hinting » (PEP484: Type Hints). 
Python est un langage à typage dynamique, ce qui signifie que vous n'avez jamais à indiquer explicitement le type de type de variable. Mais dans certains cas, le typage dynamique peut entraîner des bogues très difficiles à déboguer et dans ces cas, les conseils de type ou le typage statique peuvent être pratiques.

Python supporte des annotations de type (ou type hints) optionnelles.

Ces annotations de type constituent une syntaxe spéciale qui permet de déclarer le type d'une variable.

En déclarant les types de vos variables, cela permet aux différents outils comme les éditeurs de texte d'offrir un meilleur support.

## La syntaxe
Prenons un exemple simple :
```python
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("Amadou", "Ndiaye"))
```
Exécuter ce programe affiche :
```python
Amadou Ndiaye
```

Modifions une seule ligne de la version précédente.

Nous allons changer seulement cet extrait, les paramètres de la fonction, de :
Exécuter ce programe affiche :
```python
first_name, last_name
```
à :
```python
first_name: str, last_name: str
```
Ce sont des annotations de types :
```python
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("Fatou", "Thiva"))

# Affichage
Fatou Thiva
```
Le typage se fait grâce aux annotations. Elles permettent d’associer un type donné (`List, bool, etc`) aux arguments et aux retours des fonctions.

Les types primitifs sont les plus récurrents et utilisés : `bool, int, str, float`. Il peuvent être utilisés pour typer les arguments ainsi que les retours des fonctions.

Prenons un autre exemple, une fonction qui prend en entrée un parèmetre de type `float`et la réponse est de type `float`:
```python
import math

def circle_surface(radius: float) -> float:
    return 3.141516 * math.sqrt(radius)

circle = circle_surface(3.65)

print(circle) //6.001857890739701
```
Dans l’exemple ci-dessus, la fonction `circle_surface` prend en argument le rayon du cercle (le `radius`) et calcule la surface de ce cercle. Cet argument est de type `float` (indiqué après le `:` suivant le nom de l’argument) et la réponse est elle aussi de type `float` (le type de retour est indiqué après la flèche `->`).



- first time
* salut
* dijf
  * fff
[this is the description](https://google.com)
this variable has some `variable` inline codee

```python
# module foo.py

a = 42

def bar(x):
    print(x)
```
