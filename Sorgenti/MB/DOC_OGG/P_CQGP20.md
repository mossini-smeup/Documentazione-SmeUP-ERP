# Obiettivo
Immissione, gestione e interrogazione dei valori in dettaglio attribuibili ad ogni dipendente. Il programma inserisce nell'archivio solo le competenze, rispetto alle quali si desidera valutare il dipendente, e che sono ritenute veramente significative per il compito assegnatogli. Ne risulta un quadro di valutazione assolutamente personalizzato e specifico a livello del singolo dipendente.

Una seconda modalità di utilizzo del programma consente di documentare la partecipazione del dipendente al corso in questione, previa, naturalmente la registrazione in anagrafica corsi delle specifiche relative al corso.

## Formato guida attribuzione JNDS a dipendente
![CQ_PERS_12](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP20/CQ_PERS_12.png)
Si immette : 
 * _2_Ente di Riferimento, è un campo tabellato *CNTT
 * _2_Profilo di posizione, è un campo tabellato CQ*DA

Una volta immesso nella maschera di ingresso il codice, il programma propone automaticamente la lista dei fattori e delle competenze legate a quel profilo di posizione registrate in archivio (con la valutazione minima accettabile).

### Formato selezione profili
![CQ_PERS_13](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP20/CQ_PERS_13.png)
Vengono evidenziate solo quelle competenze rispetto alle quali l'Ente responsabile non ha ancora inserito i dati di giudizio per il dipendente in oggetto.

Attivando l'inserimento del JNDS per una delle voci elencate, la volta successiva che si interroga il modulo con quel codice dipendente, non verrà più ripresentata.

### Formato di gestione JNDS
![CQ_PERS_14](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP20/CQ_PERS_14.png)
L'inserimento del valore di JNDS tabellato CRF è  relativo alla specifica combinazione profilo di posizione / subfattore / competenza; il modulo lascia la possibilità di indicare un giudizio sulla posizione iniziale e sulla competenza acquisita :  in genere comunque il modulo viene utilizzato nella fase iniziale della valutazione, quindi il valore dei due campi coincide.

## Formato guida attribuzione corsi
![CQ_PERS_15](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP20/CQ_PERS_15.png)
L'opzione F15 consente di creare un nuovo profilo di posizione secondo le modalità viste nel modulo specifico

### Formato attribuzione enti a corsi
![CQ_PERS_16](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP20/CQ_PERS_16.png)
Vengono visualizzati, con possibilità di modifica, i valori JNDS definiti per l'ente di riferimento in merito al profilo di posizione, ai subfattori e al dettaglio di competenza abbinati all'ente stesso.

## Formato guida gestione profilo dipendente
![CQ_PERS_17](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP20/CQ_PERS_17.png)
### Formato lista gestione profilo dipendente
Lista dei profili attribuiti, della frequenza a corsi, ecc....
![CQ_PERS_19](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP20/CQ_PERS_19.png)
### Formato dettaglio documentazione di un corso
![CQ_PERS_18](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP20/CQ_PERS_18.png)
Viene documentata la partecipazione al corso con tutti i dati relativi (edizione del corso, luogo, docente, tempistica, ecc.).

Si possono inserire delle note

Si possono lanciare delle richieste di intervento (ad esempio per l'acquisto di materiale di sicurezza, di materiale didattico, ecc...).

L'opzione F15 consente di aggiornare le valutazioni. Al termine di un training, nasce la necessità di registrare i risultati conseguiti dal dipendente valutando i miglioramenti (o i peggioramenti) in riferimento all'aspetto del profilo in questione.

### Mappa di gestione valori JNDS
![CQ_PERS_20](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP20/CQ_PERS_20.png)
_2_Nota 1; quando si entra in un documento di frequentazione ad un corso e si modifica il valore del JNDS acquisito, il programma aggiorna il dato solo nel documento del profilo generale non legato a nessun corso lasciando (inserito dal modulo "Attribuzione JNDS Ente Riferimento" o altrimenti in ingresso ad "Attribuzione corsi dipendente") inalterato il valore negli altri documenti.

_2_Nota 2; è importante sottolineare il fatto che il programma archivia per ognuna delle competenze inserite (e non dei documenti presenti) un valore del JNDS. Ciascuno di questi singoli valori ("JNDS Competenza Acquisita") viene pesato in funzione dell'importanza attribuita alla competenza, dalla cui media deriva il valore del profilo relativo al dipendente.
