## File J7
I file riconosciuti da Looc.UP sono elencati come oggetti J7.
### Categorie di J7
Tali oggetti J7 hanno i seguenti sottotipi : 

- S00 :  Menù file S00
- S01 :  Menù di tipo S01
- S02 :  Menù di formato SIF
- S05 :  Menù file LTX - Latex
- S06 :  Menù file TXE - Wiki
- S07 :  Menù file XML - Docbook
- S08 :  Menù file DSF
- S09 :  Menù file S09 - Spool iSeries

e, riconosciuti come oggetti VO COD_OGJ7, sono definiti nello script OGJ7 del file DOC_VOC


### Funzioni generali sui J7
Tali file dispongono di funzioni relative al tipo di oggetto, quindi comuni a tutti i J7, alcune funzioni invece specifiche della particolare categoria.

Le funzioni si distinguono per categoria : 

- Interrogazione :  le funzioni di **Gestione** sono contenute nello script J7.G presente nel file SCP_MNU
-- Apri file
-- Copia file
-- Salva con nome
-- Zippa file
-- Cancella
-- Invia allo spool
-- Associa file ad Oggetto
-- Copia in clipboard
- Interrogazione :  le funzioni di **Interrogazione** sono contenute nello script J7.I presente nel file SCP_MNU
-- Visualizzazione
-- Proprietà file
- Interrogazione :  le funzioni di **Cruscotto** sono contenute nello script J7.K presente nel file SCP_MNU
-- Definizione del Cruscotto


### Funzioni specifiche per categoria J7
Oltre alle funzioni standard degli oggetti J7 è possibile definire delle funzioni particolari valide solo per lo specifica tipologia di J7
tali funzioni vanno inserite nel membro J7xxx dove xxx è il parametro dell'oggetto J7
Per i J7 S01 (Xml di una matrice) sono definite le seguenti funzioni specifiche : 

- Sposta in tabella AS400 :  tramite JA_00_39 sposta i dati della matrice in una tabella AS
- Visualizza come matrice :  visualizza la matrice dei dati
- Visualizza come Grafico :  visualizzza il grafico dei dati
- Apri matrice dati :  Apre la matrice dei dati in un'latra finestra
- Apri Grafico dati :  Apre la il grafico dei  dati in un'latra finestra
- Apri Excel dati :  Esporta in Excel
- Apri Openoffice Calc dati :  Esporta in Openoffice
- Apri Cubo dati :  Esporta in Databeacon
- PDF Report dati :  crea il pdf del report dei dati
- PDF Scheda dati :  crea il pdf della scheda dei dati

