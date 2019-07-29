## Contenuto
Informazioni aggiuntive legate ad un oggetto o a una coppia di oggetti.

## Codice Oggetto (in TA/*CNTT)
N.A.

## Chiave primaria
N.A.

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
C£TPRC - Categoria parametri
C£CD01 - Codice 1
C£CD02 - Codice 2
C£NUMP - Codice parametro
C£CDVA - Codice valore
C£VALO - Valore
C£DTIN - Data inizio validità

## Tabella guida
Le impostazioni sono derivate dalla tabella C£E (categoria parametri) e B£N (parametri variabili).

## Autorizzazioni
Classe autorizzazione C£CR01 con Funzione = Categoria parametri.

## Note strutturate (Tabella NSC)
Si possono impostare note per i codici guida (oggetto 1 e oggetto 2).
Il contenitore va impostato in tabella C£E.
Le tre chiavi delle note sono : 
Chiave 1 - Codice 1
Chiave 2 - Codice 2
Chiave 3 - N.A.

Si possono impostare note per il singolo parametro.
Il contenitore va impostato in tabella B£N.
Le tre chiavi delle note sono : 
Chiave 1 - Codice 1
Chiave 2 - Codice 2
Chiave 3 - Codice parametro

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
N.A.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
Nella tabella C£E è possibile specificare un programma specifico di visualizzazione ed uno di controllo.

## /COPY
Funzioni sui parametri (C£6) : 
 :  : DEC T(MB) P(QILEGEN) K(£C£6)

Funzioni archivio parametri (C£E) : 
 :  : DEC T(MB) P(QILEGEN) K(£C£E)

Funzioni parametri (C£R) : 
 :  : DEC T(MB) P(QILEGEN) K(£C£R)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
E' possibile specificare, in tabella C£E, il file di appartenenza dei parametri della categoria.
 :  : DEC T(CS) P(T/C£E) K(T$C£EE) R(1)

## CONTENUTO DEI CAMPI
