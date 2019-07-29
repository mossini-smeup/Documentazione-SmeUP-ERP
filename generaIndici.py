# -*- coding: utf-8 -*-
# Generazione di indici
# summary all .md files in a folder

import argparse
import os
import re
from AreeApplicative import applicazioni, areeApplicative, nomiAreeApplicative, areeApp, moduli, nomiDOC_SCH, moduliDOC_OPE

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
                    if 'DOC_SCH' not in os.path.relpath(file_or_path):
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
                    elif 'DOC_SCH' in os.path.relpath(file_or_path): # Elenca le applicazioni che hanno almeno un documento DOC_SCH
                        if '\\Applicazioni\\_sidebar' in os.path.relpath(file_or_path):
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
                                            
                        elif '\\Componenti\\_sidebar' in os.path.relpath(file_or_path): # Elenco dei DOC_SCH relativi ai componenti
                            with open(os.path.relpath(file_or_path), "w", encoding='utf8') as f:
                                f.write('# Schede di Componenti\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_SCH'):
                                    if singleFile[:3] == 'CMP':
                                        nomeFile = singleFile.replace('.md','')
                                        f.write('- [' + nomiDOC_SCH[nomeFile] + '](Sorgenti/MB/DOC_SCH/' + singleFile +')\n')
                        else:
                            with open('Documentazione SmeUP/DOC_SCH/Altro/_sidebar.md' , "w", encoding='utf8') as f:
                                f.write('# Altre Schede\n')
                                for singleFile in os.listdir('Sorgenti/MB/DOC_SCH'):
                                    if singleFile[:3] != 'CMP' and singleFile[:2] not in applicazioni:
                                        nomeFile = singleFile.replace('.md','')
                                        f.write('- [' + nomiDOC_SCH[nomeFile] + '](Sorgenti/MB/DOC_SCH/' + singleFile +')\n')
                            

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
        print(os.path.join(dir_input, filename))
        output = open(os.path.join(dir_input, filename), 'a+', encoding='utf8')
    else:
        output = open(os.path.join(dir_input, filename), 'w+', encoding='utf8')

    # Se è una cartella stampa nel file di indice il titolo
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
            output.write('- [Altre Schede](Documentazione%20SmeUP/DOC_SCH/Altro/_sidebar)\n')
        elif directoryName == 'DOC_OGG':
            output.write('# Documentazione per Oggetto\n')
        elif directoryName == 'DOC_OPE':
            output.write('# Documentazione Operativa\n')
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