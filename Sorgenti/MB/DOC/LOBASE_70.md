## Definizione Help Wizard di script
In questo documento si vogliono definire le modalità per agganciare l'help dei wizard di script.

## Definizione Help Wizard di script
Un wizard di script è composto da famiglie dii tag. Ogni tag a sua volta è composto da un insieme di attributi ed ogni attributo può avere dei valori predefiniti.

## Famiglie di tag per wizard di tipo EDT

 - SEZ definisce i tag dello script e il formato delle risposte
 - RIG definisce gli attributi dei tag
 - LIS definisce i possibili valori degli attributi dei tag


## Famiglie di tag per wizard di tipo generico

 - KEY definisce le chiavi di salvataggio della configurazione
 - BOT pulsanti attivi
 - POP popup
 - RIG definisce le domande di ogni sezione
 - LIS definisce i possibili valori delle domande


# La soluzione immaginata
Per mantenere puliti i membri di wizard, si è pensato di raggruppare i membri di help in un file apposito (EDT_HLP). Il nome del membro di Help sarà lo stesso del membro di wizard.
Il membro di help verrà creato in automatico partendo dal mebro di wizard ed avrà la seguente struttura : 

_2_T(tipo_elemento) P(parametro elemento) K(codice elemento), Tutto il testo che segue il tag HLP fino al successivo (se presente) tag HLP è l'help dell'elemento in questione. Il formato del testo compreso tra i due tag seguirebbe la sintassi dei comuni membri di documentazione.


|  Nam="Esempio" |
| 
| .COL Txt="**T**" Lun="0" A="L" |
| ---|----|
| 
| .COL Txt="**P** " Lun="0" A="L" |
| 
| .COL Txt="**K**" Lun="0" A="L" |
| 
| .COL Txt="**descrizione**" Lun="0" LunAut="1" |
|  - FAM| |SEZ|Help della famiglia SEZ |
|  - FAM| |RIG|Help della famiglia RIG |
|  - SEZ| |G.SET.MAT|Help del tag G.SET.MAT |
|  - RIG|G.SET.MAT|ShowTotals|Help dell'attributo ShowTotals del tag G.SET.MAT |
| 


Nota :  Gli eventuali valori dell'attributo ShowTotals sono indicati e esplicati nell'help dell'attributo stesso.

## Sviluppi futuri
- Il programma che crea i membri di help provvede ad agganciare la documentazione scritta per la matrice scheda, evitando la replica delle informazioni.
- gestione della risalita :  se ad esempio non trovo l'help per il tag G.SET.MAT cerco l'help del tag G.SET.
