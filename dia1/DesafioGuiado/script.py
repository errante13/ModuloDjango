"""
    #instalar virtualenvwrapper 
    
    pip install virtualenvwrapper-win
    
    mkvirtualenv ferreteria
    pip install django==3.2.4
    cd c:\Users\luis\Envs\ferreteria
    pip freeze > requirements-ferreteria.txt
    
    mkvirtualenv laesquina
    pip install django<3 (no encuentra el archivo)
    cd c:\Users\luis\Envs\laesquina
    pip freeze > requirements-laesquina.txt
    
    
    mkvirtualenv onlyflans
    pip install django==3.2 
    cd c:\Users\luis\Envs\onlyflans
    pip freeze > requirements-onlyflans.txt
    
    
    mkvirtualenv prestobar
    pip install django==3.2
    pip install astral 
    cd c:\Users\luis\Envs\prestobar
    pip freeze > requirements-prestobar.txt
    
    mkvirtualenv taller
    pip install django==3.2
    pip install pytz==2019.3 
    cd c:\Users\luis\Envs\taller
    pip freeze > requirements-taller.txt
    
    mkvirtualenv calendariolunar
    pip install -r (nombre-archivo)
    pip freeze > requirements-taller.txt
 """