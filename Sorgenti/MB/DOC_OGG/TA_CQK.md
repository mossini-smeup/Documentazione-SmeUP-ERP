# CQK - Definizione dei rilievi
 :  : DEC T(ST) K(CQK)
## OBIETTIVO
Definire gli algoritmi di calcolo per il trattamento dei rilievi analitici, eseguiti sulle caratteristiche di un oggetto, (albero a gomito, pistone, scheda elettronica, etc.) facente parte di un lotto di collaudo o di produzione.
## CONTENUTO DEI CAMPI
 :  : FLD T$TPRI **Tipo rilievo**
Campo controllato dalla tabella 'CQ*TM' (Tipo misura). Esso serve principalmente a differenziare, nelle caratteristiche di un oggetto, le misure per 'Attributi' (aspetto superficiale, ammaccature, etc.), da quelle per 'Variabili' (lunghezza, peso, etc.).
 :  : FLD T$CAMP **Campo numerico**
Questo campo viene utilizzato per differenziare, nelle caratteristiche di un oggetto, le misure Descrittive (Osservazioni) da quelle Numeriche 'Valori'. Il campo può assumere i valori : 
- ' '  La caratteristica da misurare si intende descrittiva, (Attributo).
- 'X'  La caratteristica da misurare si intende numerica, (Variabile numerica). In questo caso, nella fase di dichiarazione dei valori nel modulo 'Rilievi Controlli e Collaudi', permette l'inserimento dei singoli valori misurati.
 :  : FLD T$ASSO **Valore relativo**
Questo campo viene utilizzato per differenziare, nel campo delle caratteristiche per 'Variabili', le misure o le tolleranze 'Assolute' da quelle 'Relative'. Il campo può assumere i valori : 
- ' '  Il valore, che sarà attribuito alla caratteristica nel ciclo di collaudo, si intende 'assoluto'.
- 'X'  Il valore, che sarà attribuito alla caratteristica nel ciclo di collaudo, si intende 'relativo'. In questo caso, sarà necessario dichiarare a quale Dimensione o 'Variabile' nominale la misura stessa si dovrà riferire.
 :  : FLD T$RELA **Rif.valore assoluto**
Campo controllato dalla tabella 'CQK' (Definizione dei rilievi). Serve per indicare al programma a quale 'Variabile' o Dimensione Nominale ci si deve riferire per poter calcolare i valori Massimo e Minimo Assoluti della Variabile stessa. Questo campo deve essere dichiarato solo se il flag 'Valore relativo' è posto a 'X'.
 :  : FLD T$TOLL **Campo tolleranza**
Questo campo viene utilizzato per indicare che il valore attribuito alla caratteristica è una tolleranza. (ad es. sarà
una tolleranza 'Relativa' se il flag 'Valore relativo' è posto a 'X', mentre sarà 'Assoluta se il Flag e posto ' ').
Il campo può assumere i valori : 
- ' '  Il valore attribuito non definisce un campo di tolleranza.
- 'X'  Il valore attribuito alla caratteristica descrive un campo di Tolleranza.
 :  : FLD T$SUPE **Tolleranza Superiore**
Questo campo viene utilizzato per indicare se il valore attribuito alla caratteristica è una tolleranza superire rispetto alla dimensione nominale. Il campo può assumere i valori : 
- ' '  Il valore attribuito non è una tolleranza superiore.
- 'X'  Il valore attribuito è una tolleranza superiore.
 :  : FLD T$INFE **Tolleranza Inferiore**
Questo campo viene utilizzato per indicare se il valore attribuito alla caratteristica è una tolleranza inferiore rispetto alla dimensione nominale. Il campo può assumere i valori : 
- ' '  Il valore attribuito non è una tolleranza inferiore.
- 'X'  Il valore attribuito è una tolleranza inferiore.
 :  : FLD T$RFTL **Rif. Tolleranza opposto**
Campo controllato dalla tabella 'CQK' (Definizione dei rilievi). Esso serve per indicare al programma il nome del campo simmetricamente opposto al campo tolleranza assegnato, (Ad esempio se si sta descrivendo una 'Tolleranza inferiore', in questo campo andrà inserita la 'Tolleranza superiore).
 :  : FLD T$PROG **Programma di calcolo**
Serve per indicare il programma di calcolo che deve essere richiamato per eseguire la sintesi dei valori inseriti nel File dei 'Rilievi Controlli Collaudi). (es. per il calcolo della Media di una popolazione di misure indicherò il programma 'MEDIA' etc.).
 :  : FLD T$TIPC **Oggetto di controllo/parametro di controllo**
Nel caso il rilievo sia per attributi, è possibile associare il rilievo ad un oggetto di controllo (tipicamente una tabella).
_9_Esempio :  se consideriamo come elemento il COLORE, possiamo decidere di creare la tabella colori; scriveremo allora nel tipo TA e nel parametro la tabella colori.
È consigliabile utilizzare come oggetto di controllo un sottosettore della tabella CQE, poichè in questa tabella è possibile decidere se il rilievo è positivo o negativo, condizionando così il risultato immesso.
_9_Esempio : 
Elemento Colore Acqua; tabella di controllo CQECA (colore acqua); nella tabella CQECA scriveremo che il colore trasparente è positivo mentre il colore nero è negativo; quando si effettueranno i rilievi con elemento colore acqua, se la scelta è per NERO allora il valore non rispetta il risultato previsto (è negativo) e questo verrà evidenziato nella registrazione del rilievo (programma CQRM10).
 :  : FLD T$PARC.T$TIPC **Oggetto di controllo/parametro di controllo**
 :  : FLD T$CQKB **Rif. Risposte multiple**
Se impostato, questo flag indica che la caratteristica che si sta rilevando può avere risposte multiple. Tali risposte vengono registrate come parametri multipli della registrazione (oggetto H2).

 :  : FLD T$CQKC **Rif. Dichiara strumento di misura
Attraverso questo flag si decide se l'operatore che registra i controlli debba dichiarare o meno lo strumento di misura che ha utilizzato per i rilievi.
Questo flag ha effetto solo se si sceglie di adottare la gestione dei rilievi tramite scheda.

 :  : FLD T$CQKD **Rif. Tipo forzatura campione
Attraverso questo flag è possibile autorizzare l'operatore a inserire i rilievi per un campione che è numericamente diverso da quello che è stato calcolato tramite il piano di campionamento.
Questo flag ha effetto solo se si sceglie di adottare la gestione dei rilievi tramite scheda.
