Prerequisiti
Alla base di tale gestione va attivata o completata una serie di tabelle od elementi di esse, al fin
e di codificare alcuni parametri del funzionamento o certi valori di default : 

Di seguito una breve panoramica di quelle fondamentali : 

CRN, creare un sottosettore GA per definire il numeratore delle richieste di acquisto, nonchè il sot
tosettore V5 per definire (se inesistenti) i numeratori degli ordini fornitori e delle bolle di entr
ata merce;
V5D, se necessario, codificare due nuovi tipi di documento per ordini di acquisto e bolle di entrata
merce, altrimenti si possono utilizzare quelli già in uso per la gestione ordini fornitori;
V5A, creare due sottosettori per ordini fornitori e bolle di entrata merce, a cui associare un model
lo per ognuno dei due documenti;
V5B, codificare due sottosettori per ordini fornitori e bolle entrata merce, da associare alla V5A;
GAR, codificare due elementi per ordini di acquisto articoli e generici;
GA1, di personalizzazione ambiente, per codificare come default le tre informazioni precedenti nei c
ampi 'Num.richieste assun.', 'Tipo richiesta assu.', 'Tipo doc.ordine acq.';
GAB, per codificare gli utenti che gestiranno l'applicazione;
GAU, per associare l'utente codificato nella precedente ad un centro di costo, che diventa il richie
