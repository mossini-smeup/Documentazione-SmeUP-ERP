## Obiettivo
* Il prototipo è un oggetto che restituisce un XML simulando una funzione ma senza il bisogno di scrivere codice. Ciò al fine di permettere il disegno di una applicazione o funzione applicativa che potrà essere validata dall'utente, testata ecc. in tempi molto ridotti.
* I dati devono avere il più possibile un contenuto congruente con l'ambiente che stiamo utilizzando. Per farmi capire se parlo di clienti deve presentare clienti di quell'azienda.

## Gestione di un prototipo
I prototipi vengono definiti in membri di SCP_SET.
Appartengano a un modulo, quindi la nomenclatura è : 

SCP_SET/<Modulo>_PRO

Un modulo può avere più prototipi.
Un prototipo è un oggetto
V3 P.<Modulo> <Nome prototipo>

## Sintassi degli script

### Testata
TBL
* Nam="<nome propotipo>"
* Tit="<titolo>"
* Rip="OPZIONALE :  <numero ripetizioni riga>"
* Mod="OPZIONALE :  <se RND i dati vengono generati random in base all'oggetto della colonna>"
* Com="Componente ammesso (Albero/Matrice)

### Colonne di matrice
Per la comprensione fare riferimento agli attributi di colonna nell'XML standard di Smeup

### Dati
Per la comprensione fare riferimento agli attributi di colonna nell'XML standard di Smeup
Inoltre abbiamo che per un albero posso indicare con l'attributo Tre="<Open> oppure <Close>"
e possiamo definire le proprietà oggetto di una foglia mediante Tip=" Par="" Cod=""
Questo è un modo alternativo all'XML. E' particolarmente utile quando

### Setup
Coincidono con i setup dei componenti abilitati quindi matrici, alberi ecc.

### Defizinizione di un albero

 :  : TBL Nam="<nome propotipo>" Tit="<titolo>" Com="TRE"
-- griglia
    :  : COL Cod="<codice colonna>" Txt="<titolo colonna>" Tip="" Lun="01" IO="B" Ogg="<oggetto>" Dpy="" Aut="" Fill=""
-- dati
  -- oggetto
   :  : DAT Tip="TA" Par="B£A" Cod="BR" Txt=""
  -- oggetto
   :  : DAT Tip="TA" Par="B£A" Cod="CQ" Txt=""
-- apertura sottonodi
   :  : DAT Tip="TA" Par="B£A" Cod="B£"   Tre="Open"
-- sottonodo
        :  : DAT Tip="TA" Par="B£AMO" Cod="A£BASE" Fun="F(TRE;*LAP;)"  Txt=""
 -- sottonodo
        :  : DAT Tip="TA" Par="B£AMO" Cod="A5BASE" Fun="F(TRE;*LOG;)"
 -- chiusuta sottonodi
   :  : DAT Tre="Close"


## Richiamo di un prototipo

I prototipi sono letti dal B£SER_46 e utilizzando la Funzione.Medodo WRK.SCP viene letto lo script (Oggetto 1) e la sezione (Oggetto 2) : 
F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;A£LABS_PRO) 2(;;MAT_001)

E' sufficiente richamare questa fun ovunque serva un xml di matrice o di albero : 
- Griglie
- Alberi
- Accordion
- IML
- Grafici
- Grafici SPC
- Input Panel (solo definizione formato, non aggiornamento)


## Come uso un protitipo

1. Creo un membro di scp_set che chiamo <modulo>_pro
2. Definisco una matrice o un albero secondo la sintassi dello script
3. Inserisco nella scheda che sto creando la fun che richiama il prototipo

