# Gestione Operatori

## Gestione Operatori

In Negoziando è attiva la Gestione degli Operatori. Nei programmi di Gestione della Cassa (Gestione Registratore,Vendite, Chiusure di Cassa, Ricevimento Merce, etc) Negoziando provvederà a chiedere e a memorizzare l'Operatore che ha effettuato l'operazione.

## Tabelle da Configurare

Per abilitare la gestione degli operatori, è opportuno configurare le seguenti Tabelle : 

 :  : R03 Dal Menu>Principale>Anagrafiche di Base>Gestione Tabelle

 * Tabella SOPE - Sigla Operatori Scontrini
 * Tabella SOPR - Ruoli degli Operatori
 * Tabella SOPZ - Eccezioni Definizione Ruoli Operatori

## Definizione Elenco Operatori -  Tabella SOPE

Viene inizialmente presentato l'elenco degli Operatori esistenti. Nella maschera sono a disposizione i normali tasti di Negoziando per Inserimento/Modifica/Annullamento/Duplicazione.
Premendo F6=Inserisci per aggiungere un nuovo Operatore, verranno richieste le seguenti informazioni : 

 * Nome e Cognome
 * Password
 * Codice del Negozio di Riferimento dell'Operatore
 * Ruolo dell'Operatorre
 * Operatore Bloccato : Sì/No
 * Tipo Operatore
 * Livello Autorizzazione
 * Autorizzato al Ricevimento Merce
 * Autorizzato alla Codifica Operatori

La definizione del Tipo Operatore, Livello di Autorizzazione, Autorizzazioni al Ricevimento Merce e alla Codifica Operatori non deve essere effettuata se viene attivata la Gestione dei Ruoli degli Operatori ( scelta consigliata).
 __Il Ruolo Operatore prevale sempre infatti sulle impostazioni locali della tabella SOPE__

N.B.All'attivazione della funzione di Gestione della Tabella SOPE potrà essere richiesto il Codice Operatore e la relativa Password che deve effettuare le modifiche agli altri Operatori.
Questa richiesta viene attivata se nella definizione degli Operatori ne esiste anche uno solo che abbia impostata a SI la richiesta Autorizzato alla Codifica Operatori (o direttamente nella
definizione delle informazioni di SOPE o nella definizione delle Autorizzazioni dei Ruoli

## Definizione Ruoli Operatori - Tabella SOPR

Viene inizialmente presentato l'elenco dei Ruoli Operatore esistenti
Nella maschera sono a disposizione i normali tasti di Negoziando per Inserimento/Modifica/Annullamento/Duplicazione
Premendo F6=Inserisci per aggiungere un nuovo Ruolo, verranno richieste le seguenti informazioni : 

 * Descrizione
 * Livello di Gerarchia :  questa impostazione permette di definire fino a che livello l'Operatore potrà effettuare modifiche alle informazioni di altri Operatori. I valori ammessi vanno da 001 a 999, dove 999 rappresenta il massimo grado di gerarchia. Consigliamo di creare ruoli con numerazioni tipo 10-20-30-etc oppure 100-200-300-etc, in modo da poter avere valori intermedi disponibili per inserimenti di ruoli futuri.
Es. Un Operatore con un ruolo di gerarchia pari a 60 potrà effettuare modifiche solo alle informazioni di Operatori con un Livello di Gerarchia inferiore (quindi dal 50 in giu) e non agli Operatori che abbiano un ruolo uguale o superiore. In fase di modifica degli altri Operatori questo Operatore non potrà assegnare Ruoli con Livello di gerarchia uguale o superiore al proprio.

 * Dopo la definizione del Livello di Gerarchia occorre definire le singole Autorizzazioni del Ruolo, impostando Sì/No : 
 **  Autorizzato alla Vendita
 ** Autorizzato all'Utilizzo della Cassa
 ** Autorizzato al Ricevimento Merce
 ** Autorizzato alla Codifica Operatori
 ** Autorizzato ai Prelievi per Cassaforte
 ** Autorizzato alle Chiusure di Fine Giornata
 ** Autorizzato al Controllo Cassaforte
 ** Autorizzato al Versamento in Banca
 ** Autorizzato allo Sblocco di Cassa
 ** Autorizzato al Controllo Versamenti in Banca
 ** Autorizzato Registrazione Movimenti
 ** Autorizzato al Ricevimento delle Proposte
 ** Autorizzato alla Gestione dei Documenti
 ** Autorizzato all'Assoziazione Scontrino/Tessera
 ** Autorizzato alla Modifica Incassi Scontrini
 ** Autorizzato alla Gestione del Conto Riparazione
 * Cambio Password Obbligatorio (se Modifica da Sede) :  indicare se in occasione del cambio di Password di un Operatore (effettuata mediante la Gestione della Tabella SOPE) appartenente al Ruolo che si sta gestendo, dovrà essere richiesto obligatoriamente di modificare la propria password al primo accesso ai programmi di Negoziando.
 * Livello di Autorizzazione :  questo Livello di Autorizzazione viene utilizzato sui Bottoni di Cassa per consentire l'utilizzo di alcune funzionalità in funzione del Livello Operatore
 * Codice Ruolo Secondario : è possibile infine indicare il Ruolo che l'Operatore avrà nel caso stia lavorando in un Negozio diverso da quello di riferimento.

## Definizione Eccezioni ai Ruoli degli Operatori - Tabella SOPZ

Con questa tabella, nel caso la definizione del Ruolo Secondario della Tabella dei Ruoli (SOPR) non sia sufficiente, è possibile definire il Ruolo Specifico di un Operatore nel caso di utilizzo nel Negozio specificato.
Nella maschera occorre definire : 

 * Operatore
 * Codice Negozio
 * Descrizione
 * Nuovo Ruolo :  ruolo che l'Operatore deve assumere nel Negozio specificato

## Stampa Operatori su Scontrino

Nel programma di cassa è stata aggiunta la possibilità di stampare il codice e il nome dell'Operatore di Vendita della riga scontrino solo negli scontrini non fiscali.
Questa opzione è attiva se in configurazione è impostata la richiesta dell'operatore di vendita per ogni riga scontrino.

 :  : R03 Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa - Slave>Gestione Operatori
Impostare come Obbligatorio per ogni Riga Scontrino la Richiesta Indica Operatore di Vendita
(Le variabili da utilizzare nella tabella PRTDR01F sono le seguenti OpVCode = Codice OpVName =Nome Operatore)

E' stata aggiunta inoltre la possibilità di stampare anche l'Operatore di Vendita dello scontrino sia sugli scontrini fiscali che non fiscali impostandolo nei commenti
 :  : R03 Dal Menu>Principale>Anagrafiche di Base>Gestione Commenti (inserire le seguenti variabili  %OPVCODE% = Codice %OPVNAME% = Nome Operatore)
Questa opzione è attiva se in configurazione è impostata la richiesta dell'Operatore di Vendita per ogni Scontrino.

 :  : R03 Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa - Slave>Gestione Operatori
Impostare come Obbligatorio per ogni Scontrino la Richiesta Indica Operatore di Vendita

## Configurazione Applicativa

Per l'utilizzo in cassa della Gestione Operatori è opportuno impostare determinati parametri in Configurazione

 :  : R03 Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa - Slave>Gestione Operatori

Vengono richiesti : 

 * Indica Operatore di Cassa
 ** Obbligatorio. In questo caso verrà richiesto di indicare l'operatore che sta avviando il programma di Cassa
 ** Facoltativo. L'operatore non verrà richiesto
 * Indica Operatore di Vendita
 ** Facoltativo. Se selezionata questa opzione, non verrà richiesto l'operatore di Vendita, ma sarà comunque possibile bipparlo durante la vendita
 ** Obbligatorio per Ogni Scontrino. Ad ogni scontrino si è obbligati ad indicare l'operatore che sta effettuando la Vendita
 ** Obbligatorio per Ogni Riga Scontrino. Per ogni articolo bippato è obbligatorio indicare l'Operatore
 * Usa Operatore di Vendita Originario nel Reso da Scontrino. Se impostato a Sì, alla selezione in cassa del tasto Reso da Scontrino non verrà richiesto l'operatore, ma in automatico il sistema imposterà il codice dell'operatore che ha effettuato la vendita originale
 * Proponi Ultimo Operatore di Vendita. Se impostato a Sì, alla vendita successiva si aprirà la finestra di richiesta dell'Operatore, ma sarà già indicato l'ultimo Operatore di Vendita inserito. Confermare oppure cambiare Codice Operatore
 * Usa Operatore di Vendita Originario nel Ritiro Prenotazioni. Se impostato a Sì, nel Ritiro Prenotazioni non verrà richiesto nessun Operatore, ma il sistema in automatico memorizzerà l'operatore della Prenotazione originale
 * Richiedi Operatore Autorizzato nella Modifica Incassi. Se impostato a Sì, quando si cerca di modificare l'incasso di uno scontrino emesso (vedi Visualizza Incassi Casse), verrà richiesto un Operatore abilitato per Modifica Incasso Scontrino
 * Richiedi Operatore di Vendita con PopUp. Se impostato a Sì, la richiesta dell'Operatore di Vendita avverrà tramite un PopUp che riporta i nominativi dei vari Operatori e basta selezionare quello desisderato. Nel caso in cui l'Operatore non sia presente all'interno di questo elenco (magari perchè non lavora in quel negozio,ma è li solo in prestito), basterà premere Esc per passare alla normale selezione degli Operatori. A quel punto basterà premere F1 per visualizzare l'elenco degli Operatori e col tasto F9=Visualizza Tutti sarà possibile vedere anche quelli degli altri negozi.
Nel Plates va inserito il seguente codice per poter far funzionare il PopUp
               <Plate Title="POPUPOPERATORI" Width="15" Height="10" BWidth="15" BHeight="15" Type="POPUP" Id="1">
      <Functions>
        <Function Title="" Top="1" Left="1" Height="3" Width="11" Style="GenCMDred" KeyCode="-0" FCode="" FAttr="" FAutLevel="" AutoWrap="True"/>
      </Functions>
                </Plate>

 * Blocco Tastiera dopo xx Secondi di Inattività. E' possibile impostare un blocco automatico del programma di cassa, dopo tot. secondi di inattività. Ovviamente, il blocco funziona solo se si gestisce l'indicazione obbligatoria dell'Operatore di Cassa. Basta premere il tasto di sblocco ed indicare nuovamente il Codice Operatore con la relativa Password
 * Livello Operatore per Scontrini Negativi. Si può attribuire un livello minimo a partire dal quale è possibile emettere Scontrini Negativi. I livelli sono quelli definiti nella Tabella SOPR - Ruoli degli Operatori
 * Tipo Stampa Distinte di Cassa
 ** Stampa Scontrino NON Fiscale
 ** Stampa Modulo
 ** Stampa Scontrino NON Fiscale e Modulo
 ** Nessuna Stampa

