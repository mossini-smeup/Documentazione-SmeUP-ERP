# Premessa

I menù standard possono essere modificati solo dall'ambiente MOD della macchina di sviluppo.

La MEA di quest'ambiente (contenuta nella libreria SMEDAT£MO) è quella a partire dalla quale, ogni notte viene costruito lo script B£MNU2_SCP in SCP_MNU.
Questo script è quello attraverso cui viene resa disponibile la ptf di allineamento dei menù standard. La modifica di questa tabella deve quindi essere eseguita con la dovuta attenzione.

Va inoltre sottolineato che strutturalmente tutte le voci di menù vanno attribuite ad un modulo per tale motivo si consiglia di preparare già aperta la scheda di tale modulo, in modo da farsi un'idea della struttura sulla quale si sta andando ad intervenire.

# Passi

Questi i passi operativi consigliati : 
* Collegarsi all'ambiente MOD
* UP TAB
* Settore MEA, sottosettore corrispondente all'applicazione dell'azione che si vuole inserire. Rispetto a tale regola uniche deroghe sono i sottosettori V4 e V6 rappresentati le funzioni delle richieste d'acquisto e delle vendite, che apparterrebbero tutte all'applicazione V5, che in quest'ambito rappresenta esclusivamente le funzioni di acquisto.
* Indicare funzione 01 di inserimento e premere F06 per farsi attribuire il numero sequenziale automatico.
* Valorizzare tutti i campi nel dovuto modo, compilando obbligatoriamente anche il campo modulo.
* A questo punto, a meno di aver attribuito la voce al surf (tramite il corrspondente campo della MEA) va attribuita la posizione nel menù nel file del corrispondente modulo. Per fare questo nell'ambiente MOD, va richiamata la voce del modulo B£MENU, riordina menù di accesso. Tramite essa la voce specifica potrà essere spostata nel punto interessato.
* A conclusione di quest'operazione sarà stato aggiornato il modello. Nel caso si voglia poi attivare tale voce in un altro ambiente si potrà operare attraverso il comando UP FTB. Se l'ambiente di destinazione è l'ambiente di sviluppo, si può utilizzare il comando "MEA ss" (dove ss è il sottosettore della MEA), dall'ambiente modello. Tramite tale comando l'ambiente di sviluppo verrà automaticamente riallineato rispetto a quello dell'ambiente modello.

