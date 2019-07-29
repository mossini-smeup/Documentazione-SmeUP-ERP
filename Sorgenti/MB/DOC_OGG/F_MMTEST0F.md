## Contenuto
Dati descrittivi e classificazioni dell'impianto.

## Codice Oggetto (in TA/*CNTT)
 'IM'                               £FUNT1

## Chiave primaria
Codice impianto           (IM)   £FUNK1

## Altri condizionamenti facoltativi in ricerca
Tipo impianto             (TA/MMT)     £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle MMT : 
 :  : DEC T(ST) K(MMT)

## Autorizzazioni
La classe di autorizzazione è MMAM10.

La funzione di autorizzazione è il programma in cui si esegue il controllo : 
 * MMAM01G   -    Formato guida
 * MMAM01L   -    Lista richiamata dal formato guida

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella MMT (tipo impianto), se non inserito si assume MMT.
 Chiave 1 'IM'
 Chiave 2 N.A.
 Chiave 3 N.A.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella MMT.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-IMyyy, dove yyy è il tipo impianto; se assente viene associato il flusso x-IM.

## Costruzione automatica campi (tabella B£C)
La struttura della matrice risultante quando è attivata la funzione di costruzione campo è la seguente : 
>Descrizione                    Riga £SC Da  A
Codice Impianto                    1    01  15
Tipologia                          2    01  03
Descrizione impianto               3    01  50
Stato                              4    01  03
Codice Appartenenza                4    04  18
Codice Cespite                     4    19  33
Costruttore                        5    01  30
Fornitore                          5    31  60
Anno costruzione                   6    01  04
Data installazione                 6    05  12
Data ultima manutenzione           6    13  20
Matricola interna                  7    01  15
Matricola fornitore                7    16  30
Posto di Lavoro                    8    01  06
Centro di costo                    8    07  12
Peso in Kg                         9    01  07
Altezza mm                         9    08  12
Larghezza mm                       9    13  17
Lunghezza mm                       9    18  22


## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
N.A.

## /COPY
Interfaccia impianti (£IFMM0) : 
 :  : DEC T(MB) P(QILEGEN) K(£IFMM0)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD T$CODI **Codice impianto**
E' tipizzabile dal tipo e parametro omonimi di tabella M5T.
In questo modo l'impianto può essere un altro oggetto.

 :  : FLD T$COAP **Codice appartenenza**
E' tipizzato dal tipo e parametro omonimi di tabella M5T.
