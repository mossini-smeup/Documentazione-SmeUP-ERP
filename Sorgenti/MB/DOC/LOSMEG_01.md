
# Sme.Up GO
Dopo l'installazione di Looc.Up sul PC viene creato sul desktop un link che punta all'eseguibile Smeupgo.exe presente nella cartella di installazione Looc.Up.

## A cosa serve
Sme.Up GO è un applicativo che ha lo scopo di fornire all'utente finale del client grafico Looc.Up un sistema grafico con delle funzionalità per l'interazione con il sistema Sme.UP.

 T(Lo Sme.Up GO)
- fornisce un sistema per la selezione e gestione delle connessioni
- gestisce gli aggiornamenti di Looc.Up tramite SmeuUp Provider
- fornisce una serie di utilità aggiuntive

![LOSMEG_012](http://localhost:3000/immagini/LOSMEG_01/LOSMEG_012.png)
## Gestione connessioni
L'avvio di Looc.Up può avvenire tramite l'invocazione dell'eseguibile dello Sme.Up GO con parametri passati a linea di comando.
**Questa pratica è però sconsigliata** in quanto : 

- Sme.Up GO migliora l'interazione con il sistema fornendo una sistema grafico dove è possibile gestire e lanciare diverse configurazioni di connessioni personali e/o condivise a livello aziendale.
- Sme.Up GO gestisce gli aggiornamenti di Looc.Up, cosa che non avviene avviando Looc.Up direttamente!
- è possibile configurare una o più connessioni affinchè vengano eseguite automaticamente all'avvio di Sme.Up GO

Per maggiori informazioni sulle connessioni si rimanda alla sezione apposita : 
- [Gestore connessioni](Sorgenti/MB/DOC/LOSMEG_02)

## Update tramite Sme.Up Provider
Se configurato opportunamente Sme.Up GO è in grado di gestire gli upgrade di Looc.Up interfacciandosi come client ad un server Sme.Up provider.

Per maggiori informazioni si rimanda alla sezione apposita : 
- [Updater lato client](Sorgenti/MB/DOC/LOSMEG_03)

## Funzionalità avanzate
In un apposita sezione lo Sme.Up GO fornisce una serie di funzionalità aggiuntive raggruppate in aree di competenza (Strumenti, Cartelle, Sistema).

![LOSMEG_008](http://localhost:3000/immagini/LOSMEG_01/LOSMEG_008.png)

|  Nam="Adv_fun" |
| 
| .COL Txt="**Funzione**" Lun="0" A="L" |
| ---|----|
| 
| .COL Txt="**Descrizione** " Lun="0" A="L" LunAut="1" |
| Chiusura connessioni Sme.UP|Vengono chiuse tutte le connessioni pendenti di Looc.Up |
| Assistenza remota|Serve per ottenere assistenza remota con i tecnici Sme.Up |
| Forza download completo|Nel caso Sme.Up GO sia configurato per gestire gli aggiornamenti, consente di ottenere l'ultima versione completa della versione in uso di Looc.Up (Per maggiori informazioni vedere la sezione apposita di questa documentazione |
| Recupero Log|Consente la raccolta dei log |
| Apertura cartelle|Fornisce dei comodi collegamenti alle cartelle utilizzate dal sistema |
| Verifica sistema|Esegue una verifica di compatibilità dal sistema con Looc.Up |
| Gestione configurazione|Consente la modifica dei file di configurazione |
| 


### Il file di configurazione
Smeup GO prevede più file di configurazione.

- **SmeAgg.xml**  :  configurazione parametri relativi all'aggiornamento tramite Sme.Up Provider
- **smeupgo<VersionNumber>.xml**  :  (es :  smeupgoV4R1M150315.xml) configurazione per il funzionamento di Sme.Up GO

Tali file vingono cercati in
- cartella di installazione di Looc.UP
- %appdata%/SmeupGo

Di default i file vengono creati in %appdata%. I file in locale hanno però la precedenza e il loro utilizzo può servire per : 
- distribuzione di una configurazione comune da parte dell'amministratore
- nel caso debbano essere gestite più installazioni di Looc.Up, in quanto i file in %appdata% sono comuni a tutte i Looc.Up installati su una macchina

E' possibile gestire questi file in_ Funzioni Avanzate_ -> _Gestione Configurazione_

![LOSMEG_013](http://localhost:3000/immagini/LOSMEG_01/LOSMEG_013.png)
La finestra indica la posizione dei file di configurazione :  (Local) o (Appdata).
Con un doppio click è possibile modificare ogni parametro, tramite l'apposita maschera di modifica che viene presentata.

