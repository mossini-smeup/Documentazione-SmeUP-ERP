from AreeApplicative import areeApplicative, nomiAreeApplicative, areeApp
import re
import os

def traduciTabella(riga):
    riga = riga.replace("::TAB\n", '::TAB')
    riga = riga.replace("\n", ' |\n| ')
    riga = riga.replace("::TAB", '\n| ')
    
    numeroColonne = riga.count('|')
    if righeTabella == 2:
        riga = riga + "---" + "|----"*(numeroColonne-2) + "|\n| "
    return riga

basepath = './'
for fileTxt in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, fileTxt)) and fileTxt.endswith(")"):

        with open(fileTxt, encoding='utf8') as f:
            tabella = False
            righeTabella = 0
            filemd = fileTxt + ".md"
            with open(filemd, "w", encoding='utf8') as f1:
                titoloFile = filemd.replace('.md','')
                
                if len(titoloFile) == 6: # Se è un file di indice del modulo scrivi il nome del modulo in testa
                    f1.write('# ' + titoloFile + '\n')
                for line in f:
                    if '::I.INC.MBR Fil(DOC) Mem(' in line: # Inclusione di altri documenti
                        fileName = line.rsplit('Mem(')[1]
                        fileName = fileName.rsplit(')')[0]
                        for i in range(len(areeApplicative)):
                            for j in range(len(areeApplicative[i])):
                                if areeApplicative[i][j] == fileName[:2]:
                                    for codice, nome in areeApp.items(): 
                                        if nome == nomiAreeApplicative[i]:
                                            pathApplicazione = "Aree Applicative/" + codice + "/" + areeApplicative[i][j]
                                            pathModulo = pathApplicazione + "/" + fileName[:6]
                                            pathfile = pathModulo + "/" + fileName + ".md"
                                    if os.path.exists(pathfile):
                                        with open(pathfile, "r", encoding='utf8') as f2:
                                            for l in f2:
                                                f1.write(l)
                        line = ''
                    if 'http' in line and 'K(' in line: # Conversione link esterni
                        fileName = line.rsplit('K(')[1]
                        fileName = fileName.rsplit(')')[0]
                        line = '[' + fileName + '](' + fileName + ')\n'
                    if '::DEC' in line and 'P(' in line: # Conversione link interni tipo DOC
                        tipo = line.rsplit('T(')[1]
                        tipo = tipo.rsplit(')')[0]
                        parametro = line.rsplit('P(')[1]
                        parametro = parametro.rsplit(')')[0]
                        codice = line.rsplit('K(')[1]
                        codice = codice.rsplit(')')[0]
                        #line = line.replace('::DEC T(MB) P(DOC) K(','')
                        #fileName = line[line.find('K(')+1 : line.find(')')]

                        pathParametro = "Sorgenti/" + tipo + "/" + parametro
                        path = pathParametro  + "/" + codice

                        for linkedFile in os.listdir(pathParametro):
                            
                            if codice in linkedFile and '(' in linkedFile: # Se il nome del file contiene la descrizione
                                descrizione = linkedFile[linkedFile.find('(')+1 : linkedFile.find(')')]

                                line = '- [' + descrizione + '](' + path + ')\n'

                        '''for i in range(len(areeApplicative)):
                            for j in range(len(areeApplicative[i])):
                                if areeApplicative[i][j] == fileName[:2]:
                                    for codice, nome in areeApp.items(): 
                                        if nome == nomiAreeApplicative[i]:
                                            pathApplicazione = "Aree Applicative/" + codice + "/" + areeApplicative[i][j]
                                            pathModulo = pathApplicazione + "/" + fileName[:6]
                                            line = '- [' + fileName + '](' + pathModulo.replace(' ', '%20') + '/' +  fileName + ')\n'
                                    if os.path.exists(pathModulo):  
                                        for linkedFile in os.listdir(pathModulo):
                                            if fileName in linkedFile and '-' in linkedFile and len(fileName) != 6: # Se il nome del file contiene la descrizione
                                                descrizione = linkedFile[linkedFile.find('-')+1 : linkedFile.find('.md')]
                                                print(fileName)
                                                print(descrizione)
                                                print(linkedFile)
                                                line = '- [' + descrizione + '](' + pathModulo.replace(' ', '%20') + '/' +  fileName + ')\n'
                                                os.rename(pathModulo + '/' +  linkedFile, pathModulo + '/' +  fileName + '.md')
                    '''
                    if '::FIG' in line and 'P(' in line: # Conversione immagini  
                        img = line.rsplit('P(')[1]
                        img = img.rsplit(')')[0]
                        pathImmagine = 'http://localhost:3000/immagini/' + titoloFile + '/' + img.replace('£','X') + '.png'
                        line = '![' + img + '](' + pathImmagine + ')'
                        line = line.replace('\n','')

                    if line.endswith('+\n'):
                        line = line.replace('+\n','')

                    if "::TAB" in line: # Conversione Tabella
                        tabella = True
                    if "::TAB.END" in line:
                        righeTabella = 0
                        tabella = False

                    if tabella:
                        righeTabella += 1
                        line = traduciTabella(line)
                    
                    
                    line = line.replace('::TAB.END', '\n')
                    line = line.replace('::PAR F(02)\n', '>')
                    line = line.replace('::PAR F(02)', '>')
                    line = line.replace('::PAR.END','')
                    line = line.replace('::PAR L(NUM)', '')
                    line = line.replace('::PAR L(PUN)', '')
                    

                    if '_h_' in line: # Conversione grassetto
                        line = line.replace('_h_ ','**')
                        line = line.replace(' _n_','**')
                        line = line.replace('_h_','**')
                        line = line.replace('_n_','**')
                    if '_i_' in line: # Conversione corsivo
                        line = line.replace('_i_','_')
                        line = line.replace('_n_','_')    
                    if '_u_' in line: # Conversione sottolineato
                        line = line.replace('_u_','__')
                        line = line.replace('_n_','__')
                    if '_8_' in line: # Conversione citazione/comando
                        line = line.replace('_8_','>')
                        line = line.replace('_n_','')

                    line = line.replace('_n_','')
                    line = line.replace('#', '-') # Conversione elenco puntato
                    line = line.replace('::T01', '#') # Conversione titoli                             
                    line = line.replace('::T02', '##')
                    line = line.replace('::T03', '###')
                    
                    if 'http' not in line:
                        line = line.replace(':', ' : ')

                    f1.write(line)
            newName = filemd.rsplit(' (')[0] + ".md"
            os.rename(filemd, newName)
        os.remove(fileTxt)

