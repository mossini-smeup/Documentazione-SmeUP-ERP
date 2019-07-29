# encoding: utf-8 
from AreeApplicative import nomiAreeApplicative, areeApplicative, areeApp
import os
import shutil

def creaCartelle():
    for i in range(len(areeApplicative)):
        for codice, nome in areeApp.items(): 
            if nome == nomiAreeApplicative[i]:
                dirName = codice
                if not os.path.exists('Documentazione SmeUP/DOC_APP/' + dirName):
                    os.mkdir('Documentazione SmeUP/DOC_APP/' + dirName)
                if not os.path.exists('Documentazione SmeUP/DOC_VIS/' + dirName):
                    os.mkdir('Documentazione SmeUP/DOC_VIS/' + dirName)
                if not os.path.exists('Documentazione SmeUP/DOC_OPE/' + dirName):
                    os.mkdir('Documentazione SmeUP/DOC_OPE/' + dirName)
                if not os.path.exists('Documentazione SmeUP/DOC_SCH/Applicazioni'):
                    os.mkdir('Documentazione SmeUP/DOC_SCH/Applicazioni')
                if not os.path.exists('Documentazione SmeUP/DOC_SCH/Componenti'):
                    os.mkdir('Documentazione SmeUP/DOC_SCH/Componenti')
                if not os.path.exists('Documentazione SmeUP/DOC_SCH/Altro'):
                    os.mkdir('Documentazione SmeUP/DOC_SCH/Altro')
                if not os.path.exists('Documentazione SmeUP/DOC_SCH/Applicazioni/' + dirName):
                    os.mkdir('Documentazione SmeUP/DOC_SCH/Applicazioni/' + dirName)
                for j in range(len(areeApplicative[i])):
                    # print(areeApplicative[i][j])
                    dirName = areeApplicative[i][j]
                    pathApplicazione = 'Documentazione SmeUP/DOC_APP/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'Documentazione SmeUP/DOC_VIS/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'Documentazione SmeUP/DOC_OPE/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)
                    pathApplicazione = 'Documentazione SmeUP/DOC_SCH/Applicazioni/' + codice + '/' + dirName
                    if not os.path.exists(pathApplicazione):
                        os.mkdir(pathApplicazione)


def organizzaFile():
    basepath = './'
    for singleFile in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, singleFile)) and singleFile.endswith('.md') and singleFile != 'README.md' and singleFile != 'notFoundPage.md':
            print(singleFile[:2])

            for i in range(len(areeApplicative)):
                for j in range(len(areeApplicative[i])):
                    if areeApplicative[i][j] == singleFile[:2]:
                        for codice, nome in areeApp.items(): 
                            if nome == nomiAreeApplicative[i]:
                                pathApplicazione = 'Documentazione SmeUP/' + codice + '/' + areeApplicative[i][j]
                                pathModulo = pathApplicazione + '/' + singleFile[:6]
                                #print(pathModulo)
                                if not os.path.exists(pathModulo):
                                    os.mkdir(pathModulo)
                            
                        shutil.copy(singleFile, pathModulo)
                        os.remove(singleFile)

    '''for singleFile in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, singleFile)) and singleFile.endswith(".md") and singleFile != "README.md":
            if not os.path.exists("Documentazione/" + singleFile):
                print(singleFile)
                shutil.move(os.path.abspath(singleFile), "Documentazione")'''


def generaIndici():
    basepath = './'
    pathGeneraIndice = os.path.abspath('generaIndici.py')
    for dirname, dirnames, filenames in os.walk(basepath):
        if 'immagini' in dirnames: 
            dirnames.remove('immagini') # Esclude la cartella immagini dal controllo
        if '.git' in dirnames: 
            dirnames.remove('.git') # Esclude la cartella immagini dal controllo
        if 'Sorgenti' in dirnames: 
            dirnames.remove('Sorgenti') # Esclude la cartella immagini dal controllo
        if '__pycache__' in dirnames: 
            dirnames.remove('__pycache__') # Esclude la cartella immagini dal controllo
        for subdirname in dirnames:
            if subdirname != '__pycache__': 
                if len(subdirname) != 6 or subdirname in areeApp: # Se subdirname in moduli, non creo l'indice perchè esiste già
                    os.system(pathGeneraIndice + " \"" + os.path.abspath(dirname) + "/" + subdirname + "\" -o")


creaCartelle()
#organizzaFile()
generaIndici()     

sidebar = os.path.abspath('Documentazione SmeUP/_sidebar.md')
basepath = 'Sorgenti'
with open(sidebar, "a+",  encoding='utf8') as f:
    f.write('- [](.)\n')
    f.write('<trick>\n')
    f.write('\n')
    for dirname, dirnames, filenames in os.walk(basepath):
        for singleFile in filenames:
            f.write('  - [' + singleFile + '](' + dirname.replace('\\','/').replace(' ','%20')  + '/' + singleFile +  ')\n')
    f.write('</trick>')
