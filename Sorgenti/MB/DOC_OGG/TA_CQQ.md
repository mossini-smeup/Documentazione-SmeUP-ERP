# CQQ - Classi funzionali del prodotto
 :  : DEC T(ST) K(CQQ)
## OBIETTIVO
Controllare le classi funzionali dei prodotti ripresi dal DATABASE aziendale mediante il programma definito nella tabella di personalizzazione CQ1. Ad ogni articolo deve essere assegnata la classe funzionale, che rappresenta l'importanza dell'articolo, riferita all'utilizzo dello stesso. (Es. Un articolo di sicurezza avrà classe funzionale 'Critica' etc.).
In questa tabella deve obbligatoriamente essere presente l'elemento '**' generico.
## CONTENUTO DEI CAMPI
 :  : FLD T$CLAS **Classifica Scala Importanza**
Scala di importanza della classe funzionale. Questo valore è controllato dalla tabella 'CQ*IM' (Classifica import.classe funz.). Valori più bassi indicano classi funzionali più importanti (ovvero riferite a prodotti con caratteristiche di sicurezza)
 :  : FLD T$PDCI **P.d.C. assunto**
Piano di campionamento assunto. Campo controllato dalla tabella 'CQP' (Piano controllo qualità). Piano di campionamento utilizzato per il collaudo di prodotti appartenenti alla classe funzionale, qualora nell'archivio di gestione del legame 'ENTE FORNITORE-ARTICOLO' non sia presente il legame stesso (significa che tale articolo non è ancora stato gestito dal Sistema Qualità).
 :  : FLD T$LPDI **Livello campionamento assunto**
Livello di Campionamento assunto. Campo controllato nella tabella 'CQ*SE' (Tipo piano di campionamento). Livello del piano di campionamento utilizzato per il collaudo di prodotti appartenenti alla classe funzionale, qualora nell'archivio di gestione del legame 'ENTE FORNITORE-ARTICOLO' non sia presente il legame stesso (significa che tale articolo non è ancora stato gestito dal Sistema Qualità).
 :  : FLD T$PDCF **P.d.C. prima fornitura**
Piano di campionamento per consegne in 'prima fornitura'. Campo controllato dalla tabella 'CQP' (Piano controllo qualità).
Piano di campionamento utilizzato per il collaudo di prodotti appartenenti alla classe funzionale, qualora nell'archivio di gestione del legame 'ENTE FORNITORE-ARTICOLO' sia stato attivato il Flag di consegna in '1a fornitura'. Tale Flag può essere mantenuto attivo per un numero 'n' di consegne oppure fino ad una 'data' temporale prefissata.
 :  : FLD T$LPDM **Liv. campionamento prima fornitura**
Livello di campionamento per consegne in 'prima fornitura'.
Campo controllato nella tabella 'CQ*SE' (Tipo piano di campionamento). Livello del piano di campionamento utilizzato per il collaudo di prodotti appartenenti alla classe funzionale, qualora nell'archivio di gestione del legame 'ENTE FORNITORE-ARTICOLO' sia stato attivato il Flag di consegna in 1a fornitura. Tale Flag può essere mantenuto attivo per un numero 'n' di consegne oppure fino ad una 'data' temporale prefissata.
 :  : FLD T$PDCN **P.d.C. For. non Abilit.**
Piano di campionamento per consegne con 'ENTE-FORNITORE' non abilitato alla CLALSE FUNZIONALE dell'articolo. Campo controllato dalla tabella 'CQP' (Piano controllo qualità).
Piano di campionamento utilizzato per il collaudo di prodotti appartenenti alla classe funzionale, qualora nell'archivio di gestione del legame 'ENTE FORNITORE-ARTICOLO' risulti che L'ENTE-FORNITORE non è abilitato alla classe funzionale dell'articolo in consegna. Se nell'archivio di gestione del
legame 'ENTE FORNITORE-ARTICOLO' è attivato il FLAG di forzatura dell'abilitazione (la cui durata può essere fissata per 'n' consegne o per limite 'data' temporale), il programma seguirà l'algoritmo di calcolo per FORNITORE-ABILITATO.
 :  : FLD T$LPDN **Liv. Campionamento For. non Om.**
Livello di campionamento per consegne con 'ENTE-FORNITORE' non abilitato alla CALSSE FUNZIONALE dell'articolo. Campo controllato nella tabella 'CQ*SE' (Tipo piano di campionamento). Livello del piano di campionamento utilizzato per il collaudo di prodotti appartenenti alla classe funzionale, qualora nell'archivio di gestione del legame 'ENTE FORNITORE-ARTICOLO' risulti che L'ENTE-FORNITORE  non è abilitato alla classe funzionale dell'articolo in consegna. Se nell'archivio di gestione del legame 'ENTE FORNITORE-ARTICOLO' è attivato il FLAG di forzatura dell'abilitazione (la cui durata può essere fissata per 'n' consegne o per limite 'data' temporale), il programma seguirà l'algoritmo di calcolo per FORNITORE-ABILITATO.
 :  : FLD T$VAPD **Calcolo Autom. P.d.C.**
I valori possibili sono : 
- ' '  Non permette la variazione del piano di campionamento del lotto con classe funzionale dell'articolo uguale a quella assegnata.
- 'X'  Permette la variazione automatica del piano di campionamento del lotto seguendo le indicazioni riportate nella tabella 'CQR' (Regole di commutazione P.d.C.).
 :  : FLD T$CQQC **Gestione matricole**
Se impostato questo campo, gli articoli appartenenti a questa classe funzionale saranno gestiti a matricola.
 :  : FLD T$OBBL **Obbl.Registr.Rilievi**
I valori possibili sono : 
- ' '  Rende facoltativa la registrazione dei rilievi di Controllo e Collaudo effettuati sul lotto in esame, durante la fase di dichiarazione di conformità o non conformità del lotto.
- 'X'  Rende obbligatoria la registrazione dei rilievi di Controllo e Collaudo effettuati sul lotto in esame, durante la fase di dichiarazione di conformità o non conformità del lotto.
 :  : FLD T$CERT **Obbl.Reg.Cert.Conf.**
I valori possibili sono : 
- ' '  Rende facoltativa la registrazione del 'Certificato di Conformità' dell'Ente-Fornitore durante la fase di dichiarazione di conformità o non conformità del lotto.
- 'X'  Rende obbligatoria la registrazione del 'Certificato di Conformità' dell'Ente-fornitore durante la fase di dichiarazione di conformità o non conformità del lotto.
 :  : FLD T$TRAC **Obbl.Reg.Lotto Der.**
I valori possibili sono : 
- ' '  Rende facoltativa la registrazione del 'Lotto di Derivazione' dell'Ente-fornitore durante la fase di dichiarazione di conformità o non conformità del lotto (es. Certificato di Colata del materiale).
- 'X'  Rende obbligatoria la registrazione del 'Lotto di Derivazione' dell'Ente-fornitore durante la fase di dichiarazione di conformità o non conformità del lotto.
 :  : FLD T$LTFO **Obbl.Reg.Lotto Forn.**
I valori possibili sono : 
- ' '  Rende facoltativa la registrazione del 'Numero del Lotto Fornitore' dell'Ente-fornitore durante la fase di dichiarazione di conformità o non conformità del lotto.
- 'X'  Rende obbligatoria la registrazione del 'Numero del Lotto Fornitore' dell'Ente-fornitore durante la fase di dichiarazione di conformità o non conformità del lotto.
 :  : FLD T$CQQB **Non movimenta a lotti**
È un elemento V2 SI/NO :  se impostato nella movimentazione non sarà trattato il lotto.
 :  : FLD T$CLQA **L.Q.A. classe funzionale**
Livello di qualità, assegnato alla classe funzionale dell'articolo, necessario per la determinazione del numero di accettazione e/o di rifiuto del lotto in collaudo. È un campo numerico. Questo valore viene assunto per il lotto, qualora non sia definito il ciclo di collaudo.
 :  : FLD T$FREE **Free-pass consentito**
I valori possibili sono : 
- ' '  Impedisce per tutti gli articoli con quella classe funzionale, l'attivazione della gestione in FREE-PASS del lotto in entrata. Questo controllo è prioritario rispetto al Flag di gestione in FREE-PASS, riportato nella gestione 'ENTE FORNITORE-ARTICOLO'.
- 'X'  Permette, per tutti gli articoli con quella classe funzionale, l'attivazione della gestione in FREE-PASS del lotto in entrata. In questo caso se risulta attivato il Flag di FREE-PASS nella gestione 'ENTE FORNITORE-ARTICOLO', il programma seguirà le indicazioni della gestione FREE-PASS.
 :  : FLD T$NRFR **Numero free-pass consecutivi**
Numero di consegne consecutive in FREE-PASS oltre le quali scatta un controllo sul lotto. È un campo numerico. Il programma controlla, dapprima, se nella gestione 'ENTE FORNITORE-ARTICOLO' è attivato il Flag del FREE-PASS, poi controlla, sempre in tale gestione, se è definito il campo 'Numero Consegne Successive'. Se tale campo non è definito oppure se il valore ivi riportato è maggiore di quello riportato in tabella per la classe funzionale, il programma assumerà per default quest'ultimo.
 :  : FLD T$PDNF **P.d.C.ogni N° Free-pass**
Piano di campionamento assunto dal sistema per eseguire il controllo sul lotto dopo le 'N' consegne successive in FREE-PASS. Campo controllato dalla tabella 'CQP' (Piano controllo qualità).
 :  : FLD T$LCNF **Liv.Camp.ogni N° Free-pass**
Livello di Campionamento assunto dal sistema per eseguire il controllo sul lotto dopo le 'N' consegne successive in FREE-PASS. Campo controllato nella tabella 'CQ*SE' (Tipo piano di campionamento).
 :  : FLD T$CQQA **Giorni max free pass**
Se impostato stabilisce il numero massimo di giorni dall'ultimo collaudo (non free pass). Se tale limite è superato, viene applicato il piano di definito nei due precedenti campi. Questa forzatura comanda su tutte le altre impostazioni (anche quelle a livello di fornitore/articolo).
