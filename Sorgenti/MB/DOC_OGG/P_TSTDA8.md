# Azioni sulle date
## Introduzione
Tutte le azioni che si possono eseguire sulle date sono eseguite nella routine £DA8, che svolge le seguenti funzioni : 

- Elaborazioni su una data (controllo, editazione, trasformazione)
- Ritorno informazioni
- Spostamento date (incrementi, decrementi, ...)
- Forzatura date (giorno della set.,giorno del mese, ...)
- Azioni interattive (visibilità calendario, spostamenti a video ...)


### Controllo/Trasformazione
La tabella *CND4 contiene le azioni che sono possibili su un campo di tipo data grazie alla funzione specifica.

### Controlli formali
La data è fisicamente salvata in un campo di 8 caratteri, ma per quanto riguarda l'input e l'output della stessa viene accettata a 6 caratteri.
Ciò si rivela molto importante per la gestione delle date e della problematica riguardante l'anno 2000, infatti permette l'immissione di date con o senza il secolo che viene  comunque assunto in automatico. In particolare viene assunto in automatico il secolo 1900 dall'anno 30,  il secolo 2000 fino all'anno 29.

Esempio
> 07/08/96  07/08/1996
 09/10/28  09/10/2028


### Controllo correttezza formale
Le tabelle *CND1 e *CND3 contengono rispettivamente i formati accettabili per la data e per il separatore.

I formati accettabili per la data sono : 
> *CYMD        SAAMMGG           :  s=0/s=1 se <1999/>2000
 *DMY         GGMMAA
 *DMYY        GGMMAAAA
 *JOB         Formato del JOB
 *JULY        AAGGG             :  Giuliano
 *JULYY       AAAAGGG           :  Giuliano
 *MDY         MMGGAA
 *MDYY        MMGGAAAA
 *SYSVAL      Formato del sistema
 *YMD         AAMMGG
 *YYMD        AAAAMMGG
 IBM          Formato IBM

I formati accettabili per i separatori sono invece : 
> Separatore "."
 *JOB            Vedi attributo lavoro DATSEP
 *SYSVAL         Vedi attributo lavoro DATSEP
 -               Separatore "-"
 /               Separatore "/"
 ,               Separatore ","
 _               Separatore "_"
  :                Separatore " : "

Si definiscono i formati della data di input e di output e viene eseguita la trasformazione della data numerica di input nella data numerica di output, con aggiunta e soppressione del secolo.

###Ritorno Informazioni
Informazioni caratteristiche
> giorno
 settimana
 mese


### Calcoli

- Giorno da inizio anno, restituisce il progressivo del giorno dall'inizio dell'anno
- Giorno del mese, restituisce il progressivo del giorno dall'inizio del mese
- Giorno della settimana, restituisce il progressivo del giorno dall'inizio della settimana
- Mese nell'anno, restituisce il progressivo del mese dall'inizio dell'anno
- Settimana nell'anno, restituisce il progressivo della settimana dall'inizio dell'anno
- Progressivo dal 01.01.1960, restituisce il progressivo del giorno dalla data 01/01/1960 che è stata cablata all'interno del programma.


### Sfasamenti
Lo spostamento di una data
È possibile spostare una data nei seguenti modi : 

- spostamento in mesi, incrementa o decrementa la data del numero di mesi specificati in input
- spostamento in giorni, incrementa o decrementa la data del numero di giorni specificati in input


La forzatura di una data
È possibile forzare una data nei seguenti modi

- Forzatura al giorno della settimana, la data viene forzata al giorno della settimana definito in input.
- Forzatura al giorno del mese, la data viene forzata al giorno del mese definito in input
- Forzatura al giorno della settimana relativa del mese, la data viene forzata al giorno della settimana del mese  definito in input
- Forzatura al giorno della settimana completa del mese, la data viene forzata al giorno della settimana partendo dalla prima settimana completa del mese definito in input


### Esempio Interrogazione Data
Vengono ritornate  le informazioni relative alla data numerica di input. Ad esempio se in input mettiamo la data 01/01/97 con formato GGMMAA il programma mi ritorna i seguenti dati : 

_2_Figura 1 - Richiesta Controllo/Trasformazione/Editazione, informazioni su data

![B£BASE_01](http://localhost:3000/immagini/MBDOC_OGG-P_TSTDA8/BXBASE_01.png)
_2_Figura 2 - Output richiesto

![B£BASE_02](http://localhost:3000/immagini/MBDOC_OGG-P_TSTDA8/BXBASE_02.png)
È interessante notare che il numero progressivo dal 1904 mi permette di calcolare i giorni di intervallo tra due date.

Ponendo il carattere "?" nel campo data alfanumerica mi si apre una schermata dove posso accedere ad un calendario dove posso scegliere in maniera posizionale la data di cui ottenere le informazioni o su cui operare le azioni volute.
