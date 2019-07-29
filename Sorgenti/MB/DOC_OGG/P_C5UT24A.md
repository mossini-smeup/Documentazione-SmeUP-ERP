# OBIETTIVO

Eliminare Fisicamente dai file della contabilità i dati degli esercizi che si ritengono non più rilevanti.

Quando un esercizio viene eliminato vengono cancellate tutte le registrazioni ed i dati correllati ad eccezione delle registrazioni che contengono partite clienti/fornitori che ancora alla fine dell'esercizio sino a cui si vuole eseguire l'eliminazione risultano aperte.

L'elaborazione va effettuata in due fasi : 
* La prima serve per controllare e definire quali dati vadano cancellati e quali è necessario,  che permangano. La cosa si traduce nell'aggiornamento fisico dei file nel flag 40 dove viene memorizzata una "D" qual'ora il dato debba essere cancellato.
* La seconda eseguita obbligatoriamente dopo la prima, applica quando elaborato dalla fase precedente cancellando o meno i dati.

# PARAMETRI

* Azienda :  azienda di riferimento
* Esercizio :  l'esercizio, non indica un singolo esercizio, ma l'esercizio sino al quale si vuole che evenga effettuata la cancellazione (es. se indico 2010, verranno cancellati tutti gli esercizi fino al 2010 compreso)
* Stampa Log :  condizioa il fatto di voler anche o solo produrre una stampa di log dell'elaborazione* Tipo di Elaborazione :  definisce la fase di elaborazione che voglio eseguire.
* Crea file di Backup :  se valorizzato, verranno creati nella libreria indicata (o nella libreria in cui si trovano i file effettivi) i file C5TREG_OL, C5RREG_OL, C5RATE_OL, C5RITE_OL, C5MOAN_OL, C5SOLL_OL. Se questi al momento del lancio esistono già verra prima richiesta la conferma della loro cancellazione.

# CONSIGLI PRATICI

* E' opportuno che nessuno lavori nell'ambiente mentre si sta eseguendo la funzione, al fine che i file non vengano allocato. In particolar modo quando si vuole anche eseguire il backup dei file.
* Possibile, eseguire prima l'eliminazione in un ambiente di test
* L'unico effetto che l'eliminazione può avere sugli esercizi che vogliono essere mantenuti, è un'errata gestione dell'eliminazione delle partite (es. partite che si aprono o partite aperte che vengono erronamente cancellate). Per verificare il suddetto aspetto si consiglia di operare nel seguente modo : 
** stampare gli scadenzari clienti/fornitori (se si ha tempo di fine anno di tutti gli esercizi successivi a quelli che verranno eliminati, o solo dell'anno corrente se si dispone di meno tempo)
** identificare, se esistono, le partite aperte registrate negli esercizi che verranno cancellati
** lanciare l'elaborazione per rendere eliminabile un esercizio con stampa di log e : 
*** verificare che le partite controllate al punto precedente vengano correttamente mantenute
*** verificare a campione se esistono altre registrazioni al di fuori di quelle che ci si aspetta ad essere mantenute. NOTA BENE :  nella stampa di log le registrazioni che verranno mantenute sono identificabili dal fatto che nello spool il primo carattere di stampa è "U".
** una volta eseguite le sopracitate verificare eseguire l'eliminazione e riverificare che il totale degli scadenziari non sia mutato.

