 :  : HEA RESP(FP) STAT(80) CLAS(A)
# OBIETTIVO
Riunire le funzioni per l'analisi di uno script di scheda.
Il servizio consente di analizzare la composizione strutturale di uno script di scheda in termini di organizzazione gerarchica di sottoschede/sezioni/subsezioni e di singole istruzioni.
Per ciascuna istruzione è possibile visualizzare in modo dinamico gli attributi, caricati dal membro EDT_SCH del file SCP_CFG.

# FUNZIONI/METODI
## Organizzazione gerarchica

Gruppo di metodi caratterizzati dalla funzione SCH che permettono di analizzare una scheda del punto di vista strutturale, elencando progressivamente
le sottoschede, le sezioni e le subsezioni di uno script, in base all'elemento selezionato : 


- SCH.SCH :  elenca le sottoschede presenti nello script di scheda;
- SCH.SEZ :  elenca le sezioni presenti in una sottoscheda precedentemente selezionata;
- SCH.SUB :  elenca le sottosezioni (i componenti grafici) presenti in una sezione precedentemente selezionata.
- SCH.SCO :  elenca le schede chiamate all'interno dello script in esame. L'identificazione viene effettuata tramite la ricerca delle parole chiave *SCO e JATRE_18. Sono considerate valide per il richiamo le chiamate a funzione che non contengono variabili statiche o dinamiche.
Cliccando due volte sulla riga della matrice, si apre la scheda corrispondente.


## Proprietà generali
Metodi relativi all'analisi di proprietà generali della scheda.


- PRO.HEA :  visualizza tutte le informazioni contenuto nell'istruzione di tipo  :  : HEA, quali ad esempio l'utente di creazione, l'utente di aggiornamento, la data in cui è avvenuto l'aggiornamento.


## Analisi delle istruzioni
In base all'elemento strutturale selezionato, viene visualizzato l'insieme di istruzioni appartenenti a tale elemento con i corrispondenti attributi.


- ELE.SCR :  visualizza tutte le istruzioni dello script;
- ELE.SCH :  visualizza le istruzioni di una sottoscheda precedentemente selezionata;
- ELE.SEZ :  visualizza le istruzioni di una sezione precedentemente selezionata;
- ELE.SUB :  visualizza le istruzioni di una subsezione precedentemente selezionata;
- ELE.COM :  visualizza tutti gli attributi di una istruzione precedentemente selezionata, caricando dinamicamente il nome, il tipo e la descrizione
degli attributi dal membro EDT_SCH del file SCP_CFG e il valore dallo script di scheda;
- ELE.ALL :  visualizza un elenco di istruzioni, e corrispondenti attirbuti, uguali ad una istruzione precedentemente selezionata.


## Analisi istruzioni specifiche
Gruppo di metodi caratterizzati dalla funzione ALT che permettono di analizzare aspetti particolari legati alla struttura di uno script di scheda, quali la presenza di dinamismi, di istruzioni per il controllo del flusso, di variabili, di autorizzazioni e di inclusioni.


- ALT.AUT :  visualizza l'elenco delle istruzioni di tipo S.EXD.AUT;
- ALT.FLU :  visualizza l'elenco delle istruzioni per il controllo del flusso di uno script di scheda (istruzioni di tipo I.IF);
- ALT.DIN :  visualizza l'elenco delle istruzioni di tipo G.DIN, calcolando il numero della riga di script destinataria del dinamismo;
- ALT.VAR :  visualizza l'elenco delle istruzioni che istanziano variabili, sia tramite istruzione diretta di tipo S.VAR.VAL sia tramite l'apposito
attributo all'interno di altre istruzioni (ad esempio dinamismi).
- ALT.INC :  visualizza l'elenco delle istruzioni di tipo I.INC.


## Analisi grafica istruzioni specifiche
Gruppo di metodi per la visualizzazione grafica tramite cruscotto delle istruzioni specifiche descritte al punto precedente.
Il cruscotto è rosso se le istruzioni in esame non sono presenti, è giallo se il numero di istruzioni in esame presenti è compreso tra 1 e 15 ed è verde se il numero di istruzioni in esame presenti è superiore a 15.

- GAU.AUT :  visualizza un cruscotto per istruzioni di tipo S.EXD.AUT;
- GAU.FLU :   visualizza un cruscotto per istruzioni per il controllo del flusso di uno script di scheda (istruzioni di tipo I.IF);
- GAU.DIN :   visualizza un cruscotto per istruzioni di tipo G.DIN;
- GAU.VAR :   visualizza un cruscotto per istruzioni che istanziano variabili, sia tramite istruzione diretta di tipo S.VAR.VAL sia tramite l'apposito
attributo all'interno di altre istruzioni (ad esempio dinamismi);
- GAU.IND :   visualizza l'indice delle istruzioni speciali da analizzare presenti nello script.


## Controllo script di scheda
Funzione incaricata di eseguire il controllo sintattico dello script della scheda. E' individuato dalla funzione CTR e richiede come parametro il riferimento allo script di scheda : 

Prototipo di chiamata : 
 :  : D.FUN.STD F(;LOSER_07;CTR) 1(MB;SCP_SCH;nome_scp)
dove nome_scp deve contenere il nome dello script.

I controlli vengono eseguiti facendo riferimento alle regole sintattiche specificate nel configuratore degli script di scheda :  EDT_SCH nel file SCP_CFG.
I controlli attualmente eseguiti sono i seguenti : 
 :  : PAR L(LET)
- Esistenza dell'istruzione;
- Controllo annidamenti di istruzioni;
- Controllo chiusura istruzioni che lo richiedono;
- Controlli per istruzioni specifiche : 
  - G.SUB necessita di un terzo parametro;
  - I.IF.ELS usato correttamente.


Restano da implementare : 
 :  : PAR L(LET)
- Il controllo degli attributi e della loro obbligatorietà;
- Presenza di sottoschede "orfane";
- Presenza del "main";
- Controllo in massa di più script.


# Sviluppi previsti
 :  : PAR L(LET)
- Esaminare la possibilità di rappresentare graficamente la struttura della scheda utilizzando una "scheda in miniatura", eliminando dallo script tutte le istruzioni che non sono relative alla rappresentaizone strutturale della scheda.
- Utilizzare la funzionalità di drag&drop per generare automaticamente il codice per la struttura di una scheda.
- Modifica dei valori degli attributi di un'istruzione, magari scegliendo i valori possibili da un menù a tendina tramite servizio di aggiornamento.


 :  : PRO.SER Cod="SCH.SCH.1" Tit="Struttura scheda. Sottoschede" Fun="F(EXB;LOSER_07;SCH.SCH)"

 :  : PRO.SER Cod="SCH.SEZ.2" Tit="Struttura scheda. Sezioni" Fun="F(EXB;LOSER_07;SCH.SEZ) 2(NR;;-(F;;NR;RIGA))"

 :  : PRO.SER Cod="SCH.SUB.3" Tit="Struttura scheda. Subsezioni" Fun="F(EXB;LOSER_07;SCH.SUB)" Ref="SCH.SEZ.2"

 :  : PRO.SER Cod="SCH.SCO.4" Tit="Struttura scheda. Schede correlate" Fun="F(EXB;LOSER_07;SCH.SCO)" Ref="SCH.SEZ.2"

 :  : PRO.SER Cod="PRO.HEA.5" Tit="Proprietà generali. Gestione header" Fun="F(EXB;LOSER_07;PRO.HEA)"

 :  : PRO.SER Cod="ELE.SCR.6" Tit="Elenco istruzioni. Script" Fun="F(EXB;LOSER_07;ELE.SCR)"

 :  : PRO.SER Cod="ELE.SCH.7" Tit="Elenco istruzioni. Sottoscheda" Fun="F(EXB;LOSER_07;ELE.SCH)" Ref="SCH.SEZ.2"

 :  : PRO.SER Cod="ELE.SEZ.8" Tit="Elenco istruzioni. Sezione" Fun="F(EXB;LOSER_07;ELE.SEZ)" Ref="SCH.SEZ.2"

 :  : PRO.SER Cod="ELE.SUB.9" Tit="Elenco istruzioni. Sottosezione" Fun="F(EXB;LOSER_07;ELE.SUB)" Ref="SCH.SEZ.2"

 :  : PRO.SER Cod="ELE.COM.10" Tit="Elenco istruzioni. Attributi istruzione" Fun="F(EXB;LOSER_07;ELE.COM) 2(NR;;-(O;;NR;RIGA/ISTRUZIONE))"

 :  : PRO.SER Cod="ELE.SUB.11" Tit="Elenco istruzioni. Attributi istruzioni uguali" Fun="F(EXB;LOSER_07;ELE.SUB)" Ref="ELE.COM.10"

 :  : PRO.SER Cod="ALT.AUT.12" Tit="Funzionalità alternative. Autorizzazioni" Fun="F(EXB;LOSER_07;ALT.AUT)"

 :  : PRO.SER Cod="ALT.DIN.13" Tit="Funzionalità alternative. Dinamismi" Fun="F(EXB;LOSER_07;ALT.DIN)"

 :  : PRO.SER Cod="ALT.VAR.14" Tit="Funzionalità alternative. Variabili" Fun="F(EXB;LOSER_07;ALT.VAR)"

 :  : PRO.SER Cod="ALT.FLU.15" Tit="Funzionalità alternative. Controllo di flusso" Fun="F(EXB;LOSER_07;ALT.FLU)"

 :  : PRO.SER Cod="ALT.INC.16" Tit="Funzionalità alternative. Inclusioni" Fun="F(TRE;LOSER_07;ALT.INC)"

 :  : PRO.SER Cod="ALT.IND.17" Tit="Funzionalità alternative. Indice" Fun="F(EXB;LOSER_07;ALT.IND)"

 :  : PRO.SER Cod="GAU.AUT.18" Tit="Gestione cruscotto. Autorizzazioni" Fun="F(GAU;LOSER_07;GAU.AUT)"

 :  : PRO.SER Cod="GAU.DIN.19" Tit="Gestione cruscotto. Dinamismi" Fun="F(GAU;LOSER_07;GAU.DIN)"

 :  : PRO.SER Cod="GAU.VAR.20" Tit="Gestione cruscotto. Variabili" Fun="F(GAU;LOSER_07;GAU.VAR)"

 :  : PRO.SER Cod="GAU.FLU.21" Tit="Gestione cruscotto. Controllo di flusso" Fun="F(GAU;LOSER_07;GAU.FLU)"

 :  : PRO.SER Cod="GAU.INC.22" Tit="Gestione cruscotto. Inclusioni" Fun="F(GAU;LOSER_07;GAU.INC)"

