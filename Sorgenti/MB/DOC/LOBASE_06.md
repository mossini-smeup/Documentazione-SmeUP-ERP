# Vecchia gestione immagine (pre giugno 2014)
NOTA la versione precedente è la LOBASE_340
La documentazione del membro LOBASE_340 NON è aggiornata.
Per capire il meccanismo di risalita di ricerca delle immagini è  stato creato l'alias IMG

## Definizioni
Il tema delle immagini di Loocup lo possiamo dividere in 4 aspetti : 
 - Immagini degli oggetti
 - Icone degli oggetti
 - Immagini della documentazione
 - Icone utilizzate da Loocup

In questo documento tratteremo il tema della immagini.
Per distinguere le immagini dalle icone, possiamo dire che le icone : 
 - sono memorizzate nella cartella LOOCUP_ICO
 - sono di tipo gif
 - hanno una dimensione di 16x16 pixel.

La documentazione della gestione delle icone è disponibile nel documento : 
- [Gestione icone](Sorgenti/MB/DOC/LOBASE_07)

Le immagini disponibili in LoocUp possono essere di oggetto o della documentazione.

In questo documento tratteremo solo delle immagini di oggetto.
Le immagini della documentazione, non assimilabili a immagini di oggetto, vengono reperite

## Logica per la ricerca delle immagini
La ricerca delle immagini e delle icone in Looc.up avviene in due fasi distinte.
La prima consiste nel determinare la directory che fisicamente conterrà le immagini.
Una volta che è stata determinata la directory che contiene le immagini, viene fatta al suo interno una ricerca per tipo di file (png, gif, jpg).


Gli schemi che seguono mostrano tutte le fasi.

![LOBASE_117](http://localhost:3000/immagini/LOBASE_06/LOBASE_117.png)ImgRef(Identificazione cartella immagine istanza)

In questo primo schema possiamo vedere le macro fasi della ricerca e le condizioni per cui viene intrapresa una strada piuttosto che un'altra.

Negli schemi che seguono andremo ad analizzare le operazioni più "delicate" ovvero l'identificazione della cartella che contiene l'immagine dell'istanza successivamente l'identificazione della cartella che contiene l'immagine della classe.

![LOBASE_118](http://localhost:3000/immagini/LOBASE_06/LOBASE_118.png)
In questo schema possiamo vedere le cartelle dove vengono cercate le immagini di istanza.

![LOBASE_119](http://localhost:3000/immagini/LOBASE_06/LOBASE_119.png)
La ricerca della cartella delle immagini di istanza e di classe, avviene utilizzando le variabili IMG.003, 002 001 e la cartella di installazione.
Se una o più variabili IMG.nnn nonsono definite la ricerca non verrà effettuata.

Per capire i meccanismi di riaslita utilizzare l'alias IMG

## Immagini profili utente
Le immagini dei profili  utente sono un caso particolare e vanno elencate nella cartella LOOCUP_PRF/USR con codice = al codice utente


- IMAGE_DIR/TIPO/PARAMETRO/CODICE.png
- IMAGE_DIR/TIPO/PARAMETRO/CODICE.jpg
- IMAGE_DIR/TIPO/PARAMETRO/CODICE.gif
- IMAGE_DIR/OG/TIPO/PARAMETRO.png
- IMAGE_DIR/OG/TIPO/PARAMETRO.jpg
- IMAGE_DIR/OG/TIPO/PARAMETRO.gif
- IMAGE_DIR/OG/TIPO.png
- IMAGE_DIR/OG/TIPO.jpg
- IMAGE_DIR/OG/TIPO.gif




## Caratteri non consentiti nel percorso delle immagini
Qualore gli identificativi dell'oggetto di cui si sta ricercando l'immagine contengano catarreti non consentiti in un percorso di file system, tali caratteri andranno sostituiti con il carattere meno (-). Quindi l'immagine dell'oggetto di tipo ** sarà contenuto nella cartella --. Gli oggetti di tipo OJ-*USRPRF avranno le loro immagini nella cartella -USRPRF contenuta nella cartella OJ.


