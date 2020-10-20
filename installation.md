# Installation

Nous allons utiliser Python Numpy et Pandas dans le cours Data.

- Python est un langage de script multi-paradigmes.

- Numpy est un module basé sur Python et qui permet d'optimiser les calculs sur des collections de données importantes.

- Notebooks est un outil de Jupyter pour coder facilement du Python. Il est basé sur un navigateur Web.

Récupérez la structure du cours dans le dossier TEMPLATE, puis renommez ce dossier en DataAnalyse.

```txt
TEMPLATE/
    00_Docs
    01_Python/
        Notebooks
        Exercices
    02_Numpy/
        Notebooks/
        Exercices/
    03_Pandas/
        Notebooks/
        Exercices/
    installation.md
    .gitignore
```

Installation de Python, notebook, Jupyter et Pandas.

1. Une solution simple c'est d'installation **Anaconda** (que nous allons pour ce cours préférer).

Allez sur le site officiel : [anaconda](https://www.anaconda.com/products/individual) et télécharger la version qui vous convient.

C'est une installation libre et open source des langages Python et R, cette distribution est orienté scicence des données.

2. Solution installation des modules (à la main ...)

Insallez Python dans un premier temps : 

[python](https://www.python.org/download/releases/3.0/)

Installez également pip :

[pip](https://pip.pypa.io/en/stable/installing/)

Puis en ligne de commande dans un terminal tapez les lignes suivantes :

```bash
pip install jupyter
pip install numpy
pip install pandas
```

Pour lancer un notebook dans la console tapez la ligne de commande suivante :

```bash
jupyter notebook
```