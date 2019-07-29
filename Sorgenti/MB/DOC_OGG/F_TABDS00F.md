# TABDS00F  Definizioni settori tabelle
Informazioni relative alla definizione delle tabelle.
In questo file risiedono due oggetti :  il settore e il subesettore

## Legenda
xxx :  settore della tabella
yy :   subsettore della tabella

## Codice Oggetto (in TA/*CNTT)
'ST' Settore                       £FUNT1
'SS' Subsettore                    £FUNT1

## Chiave primaria
Per 'ST'
Elemento xxx                       £FUNK1

Per 'SS'
Elemento xxx                       £FUNP1
Elemento yy                        £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
N.A.

## Autorizzazioni
Autorizzazioni gestione definizioni tabelle,  Classe = GEDETA, Funzione = B£DT10.

## Note strutturate (Tabella NSC)
Il contenitore è B£S.
Chiave 1  :  Settore
Chiave 2  :  Subsettore (se oggetto SS), altrimenti blank
Chiave 3  :  N.A.

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
N.A.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
N.A.

## /COPY
Interfaccia settori e subsettori (£RITSS)
In alcuni programmi sono amcora utilizzate le precedenti interfacce
Interfaccia subsettori (£RISBS)
Interfaccia settori (£RISET)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI
