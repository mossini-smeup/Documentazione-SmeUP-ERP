Per tenere ordinato l'AS400 di sviluppo installato in SME.up, abbiamo definito le seguenti convenzioni sulle librerie (nomi e descrizioni) : 

Librerie dati di clienti (NON salvate) : 
 * Nome :  UP_xxx dove xxx è la sigla del cliente
 * Descrizione :  yy (sigla dell'utente Sme.up responsabile) yyyy (versione Sme.up) zzz...  (descrizione in esteso del cliente, con eventuale segnalazione se è una libreria di gruppo)
In caso sia necessario avere più librerie dati per lo stesso cliente, aggiungere semplicemente dei suffissi. Quindi UP_xxx01, oppure UP_xxxGRP, ecc.

Librerie programmi di clienti : 
 * Nome XPER_xxx (se non da salvare) PER_xxx (se da salvare) dove xxx è la sigla del cliente
 * Descrizione :  stesse convenzioni delle librerie dati
In caso sia necessario avere più librerie dati per lo stesso cliente, aggiungere semplicemente dei suffissi. Quindi PER_xxx01, oppure XPER_xxx02, ecc.

Librerie di progetti (salvate) : 
 * Nome P_xx dove xx è la sigla del progetto
 * Descrizione :  yy (sigla del responsabile del progetto) zzzz (descrizione del progetto)

Librerie di sviluppo degli UPP
 * Nome UPP_xxxxxx dove xxxxxx è il nome dell'UPP.
 * Descrizione :  yy (sigla del responsabile dell'UPP) zzzz (descrizione dell'UPP)

Le librerie W_xx sono da usare unicamente come librerie personali degli utenti.
