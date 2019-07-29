# Obiettivo
Gestire e presentare l'algoritmo di attribuzione di un PIANO DI CAMPIONAMENTO ad un lotto ricevuto in funzione dell'ente responsabile e dell'articolo cui il lotto appartiene.

## Formato di lancio
![CQ_PDCA_07](http://localhost:3000/immagini/MBDOC_OGG-P_CQAR20/CQ_PDCA_07.png)
## Risultato
![CQ_PDCA_08](http://localhost:3000/immagini/MBDOC_OGG-P_CQAR20/CQ_PDCA_08.png)
## Caratteristiche
Abitualmente questo programma viene richiamato dalle funzioni di ricevimento e generazione del lotto. Il programma video serve al solo scopo di evidenziare l'algoritmo di calcolo affinchè l'utente possa eseguire tutte le necessarie verifiche qualora vengano modificate le tabelle (Es. regole di commutazione)

## Algoritmo di calcolo
Le tabelle utilizzate dall'algoritmo di determinazione del piano di campionamento sono : 
 * CQ1 (Tabella di personalizzazione) determina : 
 ** Il piano di campionamento ed il livello di collaudo assunti per default
 ** Il piano di campionamento ed il livello di cllaudo per un lotto in prima fornitura
 ** Il piano di campionamento ed il livello di collaudo per un lotto ricevuro da un fornitore non omologato o non abilitato alla fornitura di quel particolare
 ** I programmi da utilizzare per la determinazione della classe funzionale dell'articolo e della classe di abilitazione del fornitore.
 * CQV (Classe di abilitazione del fornitore) determina : 
 ** La classe funzionale massima per cui il fornitore è abilitato (vedi esempio successivo)
 ** La classe funzionale massima dell'articolo fornito che può essere collaudato in FREE PASS
 * CQQ (Classe funzionale del prodotto) determina : 
 ** Il piano di campionamento ed il livello di collaudo assunti per l'articolo (se non specificato viene utilizzato quello presente in CQ1)
 ** Il piano di campionamento ed il livello di collaudo di prima fornitura per l'articolo (se non specificato viene utilizzato quello presente in CQ1)
 ** Il piano di campionamento ed il livello di collaudo da utilizzare nel caso di fornitore non omologato o non abilitato (se non specificato viene utilizzato quello presente in CQ1) piano di campionamento e/o del livello di collaudo tramite questo algoritmo
 ** Abilitazione od interdizione al collaudo in FREE PASS
 ** Il piano di campionamento ed il livello di collaudo da utilizzare nonchè della frequenza del collaudo nel caso di lotti in FREE PASS (per esempio collaudare il lotto con il piano U3B al livello II dopo 10 lotti consecutivi collaudati in FREE PASS
 * CQB (Esito controllo collaudo) determina : 
 ** L'obbligatorietà al declassamento del piano di campionamento
 ** L'obbligatorietà al declassamento del livello di collaudo
 * CQR (Regole di commutazione P.d.C.) determina : 
 ** La regola che determina il passaggio ad un piano di campionamento o ad un livello di collaudo più leggeri (per esempio per il piano di campionamento U2B si potrebbe specificare il passaggio al piano U2A nel caso in cui l'esito del collaudo sia stato conforme per gli ultimi 5 lotti consecutivi)
 ** La regola che determina il passaggio ad un piano di campionamento o ad un livello di collaudo più pesanti (per esempio per il piano di campionamento U2A si potrebbe specificare il passaggio al piano U2B nel caso in cui l'esito del collaudo sia stato non conforme per 2 degli ultimi 5 lotti ricevuti)

Esempio di Classe Funzionale Classe di Abilitazione
>CLASSE FUNZIONALE PRODOTTO
CF-0   CF-1   CF-2    ...    CF-5
Scala import.            01     02     03     ...     06
PdC assunto              U2A   U2A    U2A     ...    U2A
Livello assunto          III    II      I     ...    S-2
PdC 1 Fornit.            U2B   U2B    U2B     ...    U2B
Livello 1 For.           III    II      I     ...    S-2
Calcolo autom. PdC               X      X     ...      X
Calcolo autom. Liv.              X      X     ...      X
Free Pass consentito             X      X     ...      X
Massimo n. Free Pass             5     10     ...     20
PdC ogni n. Free Pass          U2C    U2C     ...    U2C
Livello ogni n. F.P.           S-1    S-1     ...    S-1
Critico  ------------------>  Secondario
CLASSE DI ABILITAZIONE FORNITORE
AB-9   AB-8   AB-7    ...    AB-3
Abilit. a cl. Funz.     CF-0   CF-0   CF-1    ...    CF-5
Abilit. per F.P.        CF-1   CF-2   CF-3    ...    CF-5
Affidabile  ------------------->   Inaffidabile


alla classe di abilitazione AB-7 può fornire prodotti con classe funzionale la cui scala d'importanza sia maggiore od uguale a 02 (ovvero l'importanza della classe funzionale CF-1). In questo caso verrà applicato il piano di campionamento U2A con livello I (a meno che si tratti di prima fornitura o che le regole di commutazione determini l'uso di un altro piano o di un altro livello). Tale fornitore potrà inoltre fornire prodotti che verranno collaudati in FREE PASS solo se appartenenti ad una classe funzionale maggiore ofd uguale a CF-3.

Esaminiamo i casi che si possono presentare per un lotto arrivato al collaudo :  (con il termine lotto precedente si intende un lotto dello stesso prodotto proveniente dello stesso ente di riferimento)
>ESISTONO LOTTI PRECEDENTI
ESISTE CLASSE FUNZIONALE ARTICOLO
ENTE ABILITATO
Procedura UC1
ENTE NON ABILITATO
Procedura UC2
CLASSE ABILITAZIONE NON ESISTENTE
Procedura UC1
NON ESISTE CLASSE FUNZIONALE ARTICOLO
Procedura UC1
NON ESISTONO LOTTI PRECEDENTI
ESISTE CLASSE FUNZIONALE
ENTE ABILITATO
Procedura PC1
ENTE NON ABILITATO
Procedura PC2
NON ESISTE CLASSE DI ABILITAZIONE
Procedura PC1
NON ESISTE CLASSE FUNZIONALE
Procedura PC1


### PROCEDURA UC1 (ultimo controllo 1)
Assumere piano di campionamento e livello di collaudo dell'ultimo lotto Verificare l'esito dell'ultimo collaudo nella tabella CQB Se esito indica declassamento Leggere da CQR il PdC ed il livello Se esiste tabella CQQ Se è prevista variazione automatica del PdC e del livello Leggere CQR e calcolare il PdC ed il livello altrimenti Assumere il PdC ed il livello dalla voce "assunti" di CQQ
finese
finese
finese
### PROCEDURA UC2 (ultimo controllo 2)
Assumere piano di campionamento e livello di collaudo dell'ultimo lotto Verificare l'esito dell'ultimo collaudo nella tabella CQB Se esito indica declassamento Leggere da CQR il PdC ed il livello altrimenti
Se esiste tabella CQQ Se è prevista variazione automatica del PdC e del livello Leggere CQR e calcolare il PdC ed il livello altrimenti Assumere il PdC ed il livello dalla voce "non omologato" di CQQ
finese
finese
finese
### PROCEDURA PC1 (primo controllo 1)
Se esiste tabella CQQ Leggi dalla tabella CQQ il PdC ed il livello relativo a "I consegna" altrimenti Leggi dala tabella CQ1 il PdC ed il livello relativo a "I consegna"
finese
### PROCEDURA PC2 (primo controllo 2)
Se esiste tabella CQQ Leggi dalla tabella CQQ il PdC ed il livello relativo a "non omologato" altrimenti Leggi dala tabella CQ1 il PdC ed il livello relativo a "non omologato"
finese
