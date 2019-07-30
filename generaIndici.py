# -*- coding: utf-8 -*-
# Generazione di indici
# summary all .md files in a folder

import argparse
import os
import re
from AreeApplicative import applicazioni, areeApplicative, nomiAreeApplicative, areeApp, moduli, nomiDOC_SCH, nomiDOC_OGG, nomiDOC_SER, moduliDOC_OPE

def output_markdown(dire, base_dir, output_file, append, oneLevelIndex, iter_depth=0):
    """
    Main iterator for get information from every file/folder

    i: directory, base directory(to calulate relative path), 
       output file name, iter depth.
    p: Judge is directory or is file, then process .md/.markdown files.
    o: write .md information (with indentation) to output_file.
    """
    for filename in sort_dir_file(os.listdir(dire), base_dir): 
        # add list and sort
        #print('Processing ', filename) # output log
        file_or_path = os.path.join(dire, filename)
        if os.path.isdir(file_or_path): #is dir
            
            if mdfile_in_dir(file_or_path): # if there is .md files in the folder
                if filename == 'DOC_APP':
                    output_file.write('  ' * iter_depth + '- [Documentazione Applicativa](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                elif filename == 'DOC_VIS':
                    output_file.write('  ' * iter_depth + '- [Documentazione di Visione](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                elif filename == 'DOC_SCH':
                    output_file.write('  ' * iter_depth + '- [Documentazione Schede](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                elif filename == 'DOC_OGG':
                    output_file.write('  ' * iter_depth + '- [Documentazione per Oggetto](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                elif filename == 'DOC_OPE':
                    output_file.write('  ' * iter_depth + '- [Documentazione Operativa](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                elif filename == 'DOC_SER':
                    output_file.write('  ' * iter_depth + '- [Documentazione dei Servizi](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                elif filename == 'NWS':
                    output_file.write('  ' * iter_depth + '- [News](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                
                elif filename in areeApp: # Se è un'area applicativa
                    if 'DOC_SCH' not in os.path.relpath(file_or_path):
                        output_file.write('  ' * iter_depth + '- [' + areeApp[filename] + '](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                    else:
                        iter_depth = 1

                elif filename in applicazioni: # Se è un'applicazione
                    if 'DOC_VIS' in os.path.relpath(file_or_path):
                        if os.path.exists('Sorgenti/MB/DOC_VIS/' + filename +'.md'):
                            output_file.write('  ' * iter_depth + '- [' + applicazioni[filename] + '](' + "Sorgenti/MB/DOC_VIS/" + filename +'.md)\n')
                    elif 'DOC_SER' in os.path.relpath(file_or_path):
                        applicazioneEsistente = False
                        for singleFile in os.listdir('Sorgenti/MB/DOC_SER'):
                            nomeFile = singleFile.replace(".md","")
                            if filename == singleFile[:2] and applicazioneEsistente == False:
                                output_file.write('  ' * iter_depth + '- [' + applicazioni[filename] + '](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                                applicazioneEsistente = True
                    elif 'DOC_SCH' in os.path.relpath(file_or_path):
                        pathApplicazione = os.path.relpath(file_or_path) + '/_sidebar.md'
                        with open(pathApplicazione, "w", encoding='utf8') as f3:
                            f3.write('# ' + applicazioni[filename] + '\n')
                            for singleFile in os.listdir('Sorgenti/MB/DOC_SCH'):
                                nomeFile = singleFile.replace('.md','')    
                                if filename == singleFile[:2]:
                                    if nomeFile in nomiDOC_SCH and len(nomeFile) == 6 and '_' not in nomeFile:
                                        indiceModulo = 'Sorgenti/MB/DOC_SCH/' + nomeFile + '.md'
                                        f3.write('- [' + nomiDOC_SCH[nomeFile] + '](' + indiceModulo + ')\n')
                    else:
                        output_file.write('  ' * iter_depth + '- [' + applicazioni[filename] + '](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')
                
                elif filename in moduli: # Se è un modulo
                    indiceModulo = os.path.relpath(file_or_path) + '/' + filename + '.md'
                    if os.path.exists(indiceModulo): # Se il modulo non ha il file di indice non viene inserito nell'elenco dei modul
                        output_file.write('  ' * iter_depth + '- [' + moduli[filename] + '](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/' + filename +')\n')
                
                else:
                    if 'DOC_SCH' not in os.path.relpath(file_or_path) and 'DOC_OGG' not in os.path.relpath(file_or_path):
                        output_file.write('  ' * iter_depth + '- [' + filename + '](' + os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20') + '/_sidebar.md)\n')

                if oneLevelIndex == False:
                    output_markdown(file_or_path, base_dir, output_file, append, oneLevelIndex, iter_depth + 1) # iteration

        else: # is file
            if is_markdown_file(filename): 
            # re to find target markdown files, $ for matching end of filename
                if filename != '_sidebar.md':
                    if (filename not in ['_sidebar.md', 
                                        'SUMMARY-GitBook-auto-_sidebar.md'] 
                        or iter_depth != 0): # escape _sidebar.md at base directory
                        output_file.write('  ' * iter_depth + 
                            '- [{}]({})\n'.format(write_md_filename(filename, 
                                                                    append), 
                                os.path.relpath(file_or_path).replace('\\','/').replace(' ','%20')))


                        # iter depth for indent, relpath and join to write link.
                else:
                    if 'DOC_APP' in os.path.relpath(file_or_path):
                        for codice, nome in applicazioni.items():
                            if codice in os.path.relpath(file_or_path):
                                with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f2:
                                    f2.write('# ' + nome + '\n')
                                    for singleFile in os.listdir('Sorgenti/MB/DOC'):
                                        nomeFile = singleFile.replace(".md","")
                                        if codice == singleFile[:2]:
                                            if nomeFile in moduli and '_' not in nomeFile:
                                                indiceModulo = 'Sorgenti/MB/DOC/' + nomeFile + '.md'
                                                if os.path.exists(indiceModulo): # Se il modulo non ha il file di indice non viene inserito nell'elenco dei moduli
                                                    f2.write('- [' + moduli[nomeFile] + '](' + indiceModulo +')\n')
                    elif 'DOC_OPE' in os.path.relpath(file_or_path):
                        for codice, nome in applicazioni.items():
                            if codice in os.path.relpath(file_or_path):
                                with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f2:
                                    f2.write('# ' + nome + '\n')
                                    for singleFile in os.listdir('Sorgenti/MB/DOC_OPE'):
                                        nomeFile = singleFile.replace(".md","")
                                        if codice == singleFile[:2]:
                                            if nomeFile in moduliDOC_OPE and '_' not in nomeFile:
                                                indiceModulo = 'Sorgenti/MB/DOC_OPE/' + nomeFile + '.md'
                                                if os.path.exists(indiceModulo): # Se il modulo non ha il file di indice non viene inserito nell'elenco dei moduli
                                                    f2.write('- [' + moduliDOC_OPE[nomeFile] + '](' + indiceModulo +')\n')
                    elif 'DOC_SER' in os.path.relpath(file_or_path):
                        for codice, nome in applicazioni.items():
                            if codice in os.path.relpath(file_or_path):
                                with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f2:
                                    f2.write('# ' + nome + '\n')
                                    for singleFile in os.listdir('Sorgenti/MB/DOC_SER'):
                                        nomeFile = singleFile.replace(".md","")
                                        if codice == singleFile[:2]:
                                            indiceFile = 'Sorgenti/MB/DOC_SER/' + nomeFile + '.md'
                                            f2.write('- [' + nomiDOC_SER[nomeFile] + '](' + indiceFile +')\n')
                    elif 'DOC_SCH' in os.path.relpath(file_or_path):
                        if '\\Applicazioni\\_sidebar' in os.path.relpath(file_or_path): # Elenca le applicazioni che hanno almeno un documento DOC_SCH
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# Elenco Applicazioni\n')
                                for i in range(len(areeApplicative)):
                                    for j in range(len(areeApplicative[i])):
                                        applicazioneEsistente = False
                                        for codice, nome in areeApp.items(): 
                                            if nome == nomiAreeApplicative[i]:
                                                for singleFile in os.listdir('Sorgenti/MB/DOC_SCH'):
                                                    nomeFile = singleFile.replace('.md','')    
                                                    if areeApplicative[i][j] == singleFile[:2] and nomeFile in nomiDOC_SCH and len(nomeFile) == 6 and '_' not in nomeFile and applicazioneEsistente == False:
                                                        pathApplicazione = 'Documentazione SmeUP/DOC_SCH/Applicazioni/' + codice + '/' + areeApplicative[i][j] + '/_sidebar.md'
                                                        f.write('- [' + applicazioni[areeApplicative[i][j]] + '](' + pathApplicazione.replace(' ', '%20') + ')\n')
                                                        applicazioneEsistente = True
                                            
                        elif '\\Componenti\\_sidebar' in os.path.relpath(file_or_path): # Elenco dei DOC_SCH relativi ai Componenti
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# Schede di Componenti\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_SCH'):
                                    if singleFile[:3] == 'CMP':
                                        nomeFile = singleFile.replace('.md','')
                                        f.write('- [' + nomiDOC_SCH[nomeFile] + '](Sorgenti/MB/DOC_SCH/' + singleFile +')\n')
                        elif '\\UPP\\_sidebar' in os.path.relpath(file_or_path): # Elenco dei DOC_SCH relativi agli UPP
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# Schede di UPP\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_SCH'):
                                    nomeFile = singleFile.replace('.md','')
                                    upp = ""
                                    if '_' in nomeFile:
                                        codice = nomeFile.rsplit('_')[0]
                                        upp = nomeFile.rsplit('_')[1]
                                        if len(upp) == 3 and len(codice) == 2 and codice in applicazioni:
                                            f.write('- [' + nomiDOC_SCH[nomeFile] + '](Sorgenti/MB/DOC_SCH/' + singleFile +')\n')
                        elif '\\Oggetti\\_sidebar' in os.path.relpath(file_or_path): # Elenco dei DOC_SCH relativi agli Oggetti
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# Schede di Oggetti\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_SCH'):
                                    nomeFile = singleFile.replace('.md','')
                                    if '_' in nomeFile:
                                        codice = nomeFile.rsplit('_')[0]
                                        if len(codice) == 2 and codice not in applicazioni:
                                            f.write('- [' + nomiDOC_SCH[nomeFile] + '](Sorgenti/MB/DOC_SCH/' + singleFile +')\n')
                        else:
                            with open('Documentazione SmeUP/DOC_SCH/Altro/_sidebar.md' , "w", encoding='utf8') as f:
                                f.write('# Altre Schede\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_SCH'):
                                    codice = ""
                                    if '_' in singleFile:
                                        codice = singleFile.rsplit('_')[0]
                                    if singleFile[:3] != 'CMP' and singleFile[:2] not in applicazioni and len(codice) != 2:
                                        nomeFile = singleFile.replace('.md','')
                                        f.write('- [' + nomiDOC_SCH[nomeFile] + '](Sorgenti/MB/DOC_SCH/' + singleFile +')\n')
                    elif 'DOC_OGG' in os.path.relpath(file_or_path):
                        if '\\File\\_sidebar' in os.path.relpath(file_or_path): # Elenco dei DOC_OGG relativi ai File
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# File\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_OGG'):
                                    if singleFile[:2] == 'F_':
                                       nomeFile = singleFile.replace('.md','')
                                       f.write('- [' + nomiDOC_OGG[nomeFile] + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n')
                        elif '\\Costruttori\\_sidebar' in os.path.relpath(file_or_path): # Elenco dei DOC_OGG relativi ai Costruttori
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# Costruttori\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_OGG'):
                                    if singleFile[:3] == 'LOA' or singleFile[:7] == 'V2LOCOS':
                                       nomeFile = singleFile.replace('.md','')
                                       f.write('- [' + nomiDOC_OGG[nomeFile] + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n')
                        elif '\\Classi\\_sidebar' in os.path.relpath(file_or_path): # Elenco dei DOC_OGG relativi alle Classi
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# Classi\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_OGG'):
                                    if singleFile[:3] == 'OG_':
                                        nomeFile = singleFile.replace('.md','')
                                        if nomiDOC_OGG[nomeFile] == '':
                                            f.write('- [' + nomeFile + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n')
                                        else:
                                            f.write('- [' + nomiDOC_OGG[nomeFile] + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n')
                        elif '\\Programmi\\_sidebar' in os.path.relpath(file_or_path): # Elenco dei DOC_OGG relativi ai Programmi
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# Programmi\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_OGG'):
                                    if singleFile[:2] == 'P_':
                                        nomeFile = singleFile.replace('.md','')
                                        if nomiDOC_OGG[nomeFile] == '':
                                            f.write('- [' + nomeFile + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n')
                                        else:
                                            f.write('- [' + nomiDOC_OGG[nomeFile] + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n')
                        elif '\\Tabelle\\_sidebar' in os.path.relpath(file_or_path): # Elenco dei DOC_OGG relativi alle Tabelle
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# Tabelle\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_OGG'):
                                    if singleFile[:3] == 'TA_':
                                        nomeFile = singleFile.replace('.md','')
                                        if nomiDOC_OGG[nomeFile] == '':
                                            f.write('- [' + nomeFile + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n')
                                        else:
                                            f.write('- [' + nomiDOC_OGG[nomeFile] + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n') 
                        else:
                            with open('Documentazione SmeUP/DOC_OGG/Altro/_sidebar.md' , "w", encoding='utf8') as f:
                                f.write('# Altri Oggetti\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_OGG'):
                                    if singleFile[:2] != 'F_' and singleFile[:3] != 'LOA' and singleFile[:7] != 'V2LOCOS' and singleFile[:3] != 'OG_' and singleFile[:2] != 'P_' and singleFile[:3] != 'TA_' and singleFile[:2] != 'V3':
                                        nomeFile = singleFile.replace('.md','')
                                        if nomiDOC_OGG[nomeFile] == '':
                                            f.write('- [' + nomeFile + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n')
                                        else:
                                            f.write('- [' + nomiDOC_OGG[nomeFile] + '](Sorgenti/MB/DOC_OGG/' + singleFile +')\n')
                            

def mdfile_in_dir(dire):
    """
    Judge if there is .md file in the directory

    i: input directory
    o: return True if there is .md file, False if not.
    """
    for _, _, files in os.walk(dire):
        for filename in files:
            if re.search('.md$|.markdown$', filename):
                return True
    return False

def is_markdown_file(filename):
    """
    Judge if the filename is a markdown filename

    i: filename
    o: filename without '.md' or '.markdown'
    """
    match = re.search('.md$|.markdown$', filename)
    if not match:
        return False
    elif len(match.group()) is len('.md'):
        return filename[:-3]
    elif len(match.group()) is len('.markdown'):
        return filename[:-9]

def sort_dir_file(listdir, dire):
    # sort dirs and files, first files a-z, then dirs a-z
    list_of_file = []
    list_of_dir = []
    for filename in listdir:
        if os.path.isdir(os.path.join(dire, filename)):
            list_of_dir.append(filename)
        else: 
            list_of_file.append(filename)
    for dire in list_of_dir:
        list_of_file.append(dire)
    return list_of_file  

def write_md_filename(filename, append):
    """
    Write markdown filename

    i: filename and append
    p: if append: find former list name and return
       else: write filename
    """
    if append:
        for line in former_summary_list:
            if re.search(filename, line):
                s = re.search('\[.*\]\(',line)
                return s.group()[1:-2]
        else:
            return is_markdown_file(filename)
    else:
        return is_markdown_file(filename)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--overwrite', 
                        help='overwrite on _sidebar.md', 
                        action="store_true")
    parser.add_argument('-a', '--append', 
                        help='append on _sidebar.md', 
                        action="store_true")
    parser.add_argument('directory', 
                        help='the directory of your GitBook root')
    args = parser.parse_args()
    overwrite = args.overwrite
    append = args.append
    dir_input = args.directory
    
    if append and os.path.exists(os.path.join(dir_input, '_sidebar.md')): 
        #append: read former _sidebar.md
        print('--append', end = ' ')
        global former_summary_list
        with open(os.path.join(dir_input, '_sidebar.md')) as f:
            former_summary_list = f.readlines()
            f.close()

    # output to file
    if (overwrite == False and 
        os.path.exists(os.path.join(dir_input, '_sidebar.md'))):
        # overwrite logic
        filename = '_sidebar.md'
    else:
        filename = '_sidebar.md'
    
    if 'DOC_SCH\\Applicazioni' in os.path.join(dir_input, filename):
        for key in areeApp:
            if key + '\\_sidebar' in os.path.join(dir_input, filename):
                output = open(os.path.join(dir_input, filename), 'w+', encoding='utf8')
            else:
                output = open(os.path.join(dir_input, filename), 'a+', encoding='utf8')
    else:
        output = open(os.path.join(dir_input, filename), 'w+', encoding='utf8')

    # Se è una cartella stampa nel file di indice il titolo ed eventualmente le categorie
    if os.path.isdir(dir_input):
        directoryName = dir_input[dir_input.rfind('/')+1:]
        if directoryName == 'DOC_APP':
            output.write('# Documentazione Applicativa\n')
        elif directoryName == 'DOC_VIS':
            output.write('# Documentazione di Visione\n')
        elif directoryName == 'DOC_SCH':
            output.write('# Documentazione Schede\n')
            output.write('- [Schede di Applicazioni](Documentazione%20SmeUP/DOC_SCH/Applicazioni/_sidebar)\n')
            output.write('- [Schede di Componenti](Documentazione%20SmeUP/DOC_SCH/Componenti/_sidebar)\n')
            output.write('- [Schede di UPP](Documentazione%20SmeUP/DOC_SCH/UPP/_sidebar)\n')
            output.write('- [Schede di Oggetti](Documentazione%20SmeUP/DOC_SCH/Oggetti/_sidebar)\n')
            output.write('- [Altre Schede](Documentazione%20SmeUP/DOC_SCH/Altro/_sidebar)\n')
        elif directoryName == 'DOC_OGG':
            output.write('# Documentazione per Oggetto\n')
            output.write('- [File](Documentazione%20SmeUP/DOC_OGG/File/_sidebar)\n')
            output.write('- [Costruttori](Documentazione%20SmeUP/DOC_OGG/Costruttori/_sidebar)\n')
            output.write('- [Classi](Documentazione%20SmeUP/DOC_OGG/Classi/_sidebar)\n')
            output.write('- [Programmi](Documentazione%20SmeUP/DOC_OGG/Programmi/_sidebar)\n')
            output.write('- [Tabelle](Documentazione%20SmeUP/DOC_OGG/Tabelle/_sidebar)\n')
            output.write('- [Altri Oggetti](Documentazione%20SmeUP/DOC_OGG/Altro/_sidebar)\n')
        elif directoryName == 'DOC_OPE':
            output.write('# Documentazione Operativa\n')
        elif directoryName == 'DOC_SER':
            output.write('# Documentazione dei Servizi\n')
        elif directoryName == 'NWS':
            output.write('# News\n')
        # elif directoryName in applicazioni:
            # output.write('# ' + applicazioni[directoryName] + '\n')
        elif directoryName in areeApp:
            output.write('# ' + areeApp[directoryName] + '\n')
        

    # Se non è l'indice totale, genera indice con un solo livello
    if os.path.relpath(dir_input) == 'Documentazione SmeUP':
        oneLevelIndex = False
    else:
        oneLevelIndex = True

    output_markdown(dir_input, dir_input, output, append, oneLevelIndex)

    return 0

if __name__ == '__main__':
    main()