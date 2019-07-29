# Gestione ambienti utente
Con queste funzioni si definiscono :  gli ambienti (sistemi informativi) a cui un utente può accedere, il menù principale utilizzato ed altre impostazioni generali di ambiente (es. Lingua, Coda lavori, Coda di stampa, ecc..). Le attribuzioni possono essere per singolo utente oppure per Gruppo di accesso (consigliata).

## Menù di ingresso
Il programma può essere lanciato dalla riga comandi attraverso il comando breve **UP UT5**, o in alternativa dalle actions del modulo B£AMBI.
![B£UT55_00](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_00.png)
Descriveremo di seguito le funzioni nell'ordine del processo suggerito (creazione ambienti, creazione gruppi, attribuzione gruppi agli utenti).

## Costruzione ambienti applicativi
L'attività utilizza la funzione "Ambienti Applicativi (B£B)" che permette di definire la lista librerie utilizzata da un ambiente, l'impostazione è la stessa utilizzata in precedenza con la tabella B£B (si possono inserire sia librerie che gruppi di librerie, questi ultimi caratterizzati dal prefisso **, anche i gruppi di librerie vengono gestiti con questa stessa funzione) : 
![B£UT55_10](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_10.png)F6 per inserire un nuovo ambiente, per la gestione di un ambiente esistente sono valide le opzioni consuete (02 = Modifica, 03 = Copia, ....) : 
![B£UT55_11](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_11.png)**Nota**; Nella gestione ambienti, oltre alla lista delle librerie e gruppi sono presenti anche 2 campi ulteriori : 
* __Localizzazione__, in questo campo può essere inserito un elemento della tab. A£B dove sono presenti le impostazioni di localizzazione (lingua, separatori decimali, formato data; ...)
* __Encoding__, qui possono essere impostati i parametri di codifica dei dati negli archivi
* __Colore__, qui è possibile indicare il colore di base che dovrà avere Looc.UP in questo ambiente (il colore va indicato nella forma RxxxGyyyBzzz).

## Defninizione gruppi di accesso
I gruppi di accesso vengono usati per attribuire ad un insieme di utenti gli stessi ambienti con le stesse modalità. I gruppi di accesso non vanno confusi con i gruppi utente che invece servono, all'interno di un ambiente, per assegnare a più utenti autorizzazioni comuni.
La funzione permette di gestire la lista dei gruppi di accesso, sono utilizzabili le funzioni di manutenzione consuete, F6 per inserire un nuovo gruppo : 
![B£UT55_09](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_09.png)In creazione o modifica del gruppo si può direttamente gestire gli ambienti associati : 
![B£UT55_14](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_14.png)![B£UT55_15](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_15.png)
## Gestione ingressi utente / Ambiente per utente
La funzione premette di attribuire direttamente gli accessi ad un utente oppure di assegnare un gruppo utente da cui ereditare gli ingressi, oltre a dare la possibilità di impostare per l'utente anche altri default operativi. Con la stessa funzione si possono anche gestire delle impostazioni di natura più sistemistica sul profilo utente, ma queste richiedono un livello di autorizzazioni più elevato (SECADM) e non saranno trattate in questo documento.

Per gestire accessi e impostazioni dell'utente Scegliere "Gestione utente" ed inserire il profilo : 

![B£UT55_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_01.png)
Premendo INVIO il programma mostra la lista degli accessi previsti per l'utente, in cui si possono vedere le varie impostazioni di ambiente già attribuite all'utente direttamente oppure dal suo gruppo di accesso : 
![B£UT55_02](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_02.png)Viene emessa una segnalazione per indicare se l'utente è collegato o meno ad un gruppo accesso.
Con F13 si passa alle impostazioni di default utente, con F14 alla gestione degli accessi utente, con F15 alla gestione degli accessi di gruppo.

## F13 Default utente
Questa funzione permette di attribuire ad un utente il suo gruppo di accesso, oltre che altri parametri di default.
Vedi formato : 
![B£UT55_05](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_05.png)
## F15 Accessi di gruppo
Si può accedere direttamente alla gestione degli accessi del gruppo utente : 
![B£UT55_16](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_16.png)
## F14 Accessi utente
![B£UT55_17](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_17.png)Sono possibili le consuete operazioni di gestione (01 Inserimento, 02 Modifica, 03 Copia, 04 Cancellazione).

## Formato di dettaglio
![B£UT55_03](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_03.png)Descrizione dei campi significativi : 

- **Tipo accesso**,  definisce la modalità con cui ci si collega all'ambiente, la ricerca presenta i tipi accesso previsti, in particolare : 
-- S = Menù Sme.UP
-- P = Menù Sme.UP con richiesta parametri
-- G = Menù Sme.UP con autorizzazioni a parametri autorizzati per gruppo utente
- **Ambiente / Sistema informativo**, dove è definita la lista librerie del sistema informativo
- **Menù**, sottosettore della tabella MEA che rappresenta il menù di ingresso (attivo per i tipi accesso S, P, G)
- **Stringa comando**,  comando server da lanciare con accesso = C
- **Piattaforma esecuzione**,  permette di definire se l'ambiente è valido solo per emulazione 5250 (client access), solo per LoocUP o per entrambi
- **Colore**,  permette di definire il colore di base che dovrà avere Looc.UP in questo ingresso utente (il colore va indicato nella forma RxxxGyyyBzzz)


## Funzioni particolari
Con il programma di gestione accessi si possono anche lanciare funzioni particolari

### Gruppo di Accesso di Default
Permette di definire un gruppo di default, se è presente il gruppo di default, quando un utente non ha una propria lista di ambienti nè è associato a nessun gruppo di accesso assume il gruppo di default.

### Gruppo Azioni collegati a "ESC"
Permette di gestire il gruppo della azioni attivabili con "Attn/Esc", questo gruppo azioni può essere associato ad un utente in fase di impostazione del default utente, in mancanza di una precisa assegnazione il sistema utilizza il gruppo **$$****.

![B£UT55_06](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_06.png)
## Librerie di Sistema
Permette di impostare o modificare le librerie di sistema utilizzate da Sme.UP.
E' possibile impostare tali librerie mediante due metodologie. Quella "Normale" (F06) e quella "Speciale" (F07).
Tali funzioni sono eseguibili solo dall'emulazione 5250 in quanto si appoggiano a comandi di sistema operativo.

### Impostazione "normale" (F06)
L'impostazione "normale" si basa sulla modifica del valore di sistema QSYSLIBL.
Aggiungendo in questo elenco le librerie di sistema Sme.UP (solitamente SMESYS), ogni job eseguito sul server avrà in lista (parte "di sistema") queste librerie.
L'inserimento in lista è assicurato dal sistema operativo, però in questo modo **ogni JOB** alloca tali librerie.

### Impostazione "speciale" (F07)
Per avere un'installazione meno invasiva (per quanto riguarda la SMESYS) è possibile utilizzare la gestione speciale.
Con questa scelta il sistema richiede quali siano le librerie di sistema Sme.UP. I programmi di inizializzazione di Sme.UP si preoccupano poi di metterle in linea.
Questa è un'installazione meno invasiva. E' però necessario utilizzare alcune accortezze.
* Tutte le JOBD utilizzate da job Sme.UP devono contenere la libreria di sistema
* I lavori schedulati devono tassativamente essere eseguiti con impostazione "schedulazione Sme.UP" (che incapsula il comando effettivamente schedulato nel comando B£QQ01).
* Tutti i SBMJOB devono essere eseguiti con il comando B£QQ01 oppure vanno incapsulati nel comando B£QQ02.
Tecnicamente l'informazione di quali siano le librerie da mettere in linea viene salvata in una variabile di ambiente (SMESYSLIBL) con visibilità di sistema.

In caso di necessità è anche possibile utilizzare una gestione mista :  alcune librerie possono essere messe in QSYSLIBL (gestione normale) e altre in SMESYSLIBL (gestione speciale).

### Parametri di encoding e Tabella localizzazione linguistica
Queste voci sono relative all'impostazioni di ambienti in lingua non italiana.

![B£UT55_12](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_12.png)
![B£UT55_13](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT55/BXUT55_13.png)
### Menù a Parametri per gruppo utente
Abbiamo tenuto per ultima questa funzione perchè a partire dalla relase 4.1 non è più attiva essendo stata sostituita dalla gestione del modulo B£MENU.
Con le release precedenti questa funzione si occupava delle impostazioni delle autorizzazioni, sui menù e sulle azioni di menù, per gruppo utente attraverso il programma B£UT54.
 :  : INI Menù a parametri per gruppo utente
 :  : CMD CALL B£UT54
 :  : FIN
Per la spiegazione del funzionamento vedi il documento specifico.
