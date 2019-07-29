## Contenuto
Dati pianificazione PLANT / Articolo.

## Codice Oggetto (in TA/*CNTT)
N.A.

## Chiave primaria
N.A.

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
Chiave primaria individuata dai campi U§LIVE **Livello**, U§CDMG **Codice**, U§CODI **Codice**, U§TIOG **Tipo**, U§PAOG **Parametro**, U§OGRF **Oggetto riferimento**.

## Tabelle guida
La struttura di questo archivio è definita nell'elemento 'ART_MAT' della tabella C£F.
La risalita viene parcheggiata nell'elemento di C£G definito in C£F (consigliato AR_MT).
Il modo di suddivisione della risalita è definito in tabella M51.

## Autorizzazioni
N.A.

## Note strutturate (Tabella NSC)
Contenitore :  'M05' fisso.
Chiave 1 :  Livello di risalita
Chiave 2 :  Codice 1
Chiave 3 :  Codice 2

## Parametri (Tabella C£E)
La categoria si assume dalla tabella C£F (elemento ART_MAT).
Le chiavi sono i codici 1 e 2 dell'archivio.
Particolare cura deve essere prestata nelle omonimie, essendo la categoria indipendente dal livello di risalita :  oggetti diversi con lo stesso nome puntano agli stessi parametri.

## Flussi (Tabella B£H)
N.A.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo

## /COPY
Lettura archivio con risalita (£M5A) : 
 :  : DEC T(MB) P(QILEGEN) K(£M5A)

Livello di risalita (£GRI) : 
 :  : DEC T(MB) P(QILEGEN) K(£GRI)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
N.A.
