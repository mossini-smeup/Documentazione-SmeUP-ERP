# V62 - Impostazioni aggiuntive TradUP
 :  : DEC T(ST) K(V62)

## OBIETTIVO
Definisce i parametri aggiuntivi relativi alla gestione documenti.

## CONTENUTO CAMPI
 :  : FLD T$ELEM Elemento
È un elemento fisso.
 :  : FLD T$DESC Note
 :  : FLD T$V62A **Controllo Dichiarazioni di Intento**
* "1"=Automatico :  in fase di fatturazione si attiverà il programma di calcolo e controllo delle esenzioni da applicare sulla base di dichiarazioni di intento per importo.
* "2"=Manuale :  in fase di fatturazione, solo in pre-stampa viene data indicazione, della presenza di dichiarazioni di intento per importo non esaurite. A questo punto il collegamento va fatto manualmente da scheda.
* "3"=Solo controllo :  in fase di fatturazione, solo in pre-stampa viene data indicazione, della presenza di dichiarazioni di intento per importo. A questo punto sui documenti dove si vuole applicare l'esenzione, l'assoggettamento andrà modificato manualmente ed i riferimenti delle dichiarazioni andranno riportati nelle note.
* " "=Nessun controllo
Per maggior dettaglio si veda la documentazione applicativa specifica del modulo V5SPRID.

 :  : FLD T$V62B **Inizio Validità Dichiarazione di Intento**
Permette di indicare quale data prendere in considerazione come data inizio validità della dichiarazione.
* "1"=Data protocollo :  coincide con la data in cui la dichiarazione viene registrata nel sistema, quindi con la data in cui è stata effettivamente verificata la validità della dichiarazione.
* " "=Data acquisizione agenzia :  coincide con la data cui la data in cui la dichiarazione è stata acquisita dall'agenzia.

 :  : FLD T$V62C **Applicazione Dichiarazione solo se applicabile a totale documento**
Se impostato questo campo l'applicazione della dichiarazione verrà effettuata solo se applicabile all'intero documento.
Si sottolinea che l'applicazione parziale può avvenire per differenti casistiche : 
* Se la fattura è composta da bolle che sono state spedite sia prima che dopo la data di inizio validità della dichiarazione
* Se la fattura ha un importo superiore al residuo della dichiarazione, ma l'esenzione può essere applicata ad alcune delle righe che lo compongono

 :  : FLD T$V62D **Ambiente Di contabilizzione assunto da Azienda**
Se impostato il campo a '1', qualora non venga impostato il campo T$V51F (Ambiente di
contabilizzazione) della tabella V51, viene impostato automaticamente con l'azienda.
Questa opzione è importante per le installazioni multi azienda per le quali non si
ha la necessità di cambiare altri dati della tabella V51 e quindi si può tenere la
tabella stessa tra le tabelle di gruppo

 :  : FLD T$V62E **Suff.ctr fatture em.**
E' possibile attivare un programma di controllo alla 'STAMPA' della fattura. Per impedire la
generazione della fattura in determinate condizioni specifiche dell'azienda.
Il campo è il suffisso del programma V5FA01C_x  è lanciato dal programma V5FA01S in modalità stampa
dopo il reperimento del numeratore.
Come esempio è presente la exit standard V5FA01C_1
