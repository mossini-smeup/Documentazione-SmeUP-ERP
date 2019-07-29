## Metafonti
Una metafonte è una fonte che ha, tra i suoi parametri di caratterizzazione, un gruppo fonti.
Essa scandisce la disponibilità dell'articolo ricevuto con questo gruppo fonti, esegue delle elaborazioni specifiche sui suoi risultati, e ritorna, in scansione, una serie di quantità e date.

Le metafonti impostate attualmente sono : 

la fonte bilanciata
- [&-x2a; M5F - BL - Bilanciata](Sorgenti/MB/DOC_OGG/TA_M5F_BL)
che esegue il programma
 :  : DEC T(OJ) P(*PGM) K(M5M5D6G)

la disponibilità libera
- [&-x2a; M5F - DL - Disponib.libera](Sorgenti/MB/DOC_OGG/TA_M5F_DL)
che esegue i programmi
 :  : DEC T(OJ) P(*PGM) K(M5M5D1G)
 :  : DEC T(OJ) P(*PGM) K(M5M5D2G)

il fabbisogno giornaliero
- [&-x2a; M5F - FG - Fabbisogno giornaliero](Sorgenti/MB/DOC_OGG/TA_M5F_FG)
che esegue il programma
 :  : DEC T(OJ) P(*PGM) K(M5M5D6G)

Nel creare nuove metafonti bisogna prestare attenzione a due ordini di problemi : 
la ricorsione (problema tecnico)
il gruppo plant (problema applicativo)

## Ricorsione
La scansione disponibilità (M5M5D0GA) lancia il programma di metafonte al suo stesso livello (es : M5M5D6GA). Quest'ultimo deve eseguire un'analisi disponibilità ad un livello superiore. Per far questo si estrae il suffisso del suo nome, e imposta il livello di chiamata della scansione disponibilità £M5DLC immediatamente successivo ('A' --> 'B'). Per problemi di prestazioni, questa catena è cablata all'interno dei programmi di metafonti, invece di chiedere alla routine opportuna (£CRI) il livello successivo.

## Gruppo plant
Tra i parametri di caratterizzazione della metafonte c'è il gruppo fonti, che contiene al suo interno il gruppo plant in modo fisso, indipendentemente dal gruppo plant del gruppo fonti di lancio della disponibilità di partenza.
E' quindi necessario prevedere, tra i parametri di caratterizzazione, anche un flag che specifica se il gruppo plant viene assunto dal gruppo fonti della metafonte, oppure (impostazione più probabile) se viene ereditato da quello della scansione disponibilità che la ha lanciata.

Ricordo che la exit di definizione fonte UT/AP
 :  : DEC T(MB) P(M5SRC) K(XXM5E0)
tra i suoi parametri riceve il gruppo plant originale, quindi è in grado di implementare quanto sopra descritto.



