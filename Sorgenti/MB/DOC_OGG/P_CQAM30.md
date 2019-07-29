# Formato di gestione
![QA_ENLO014](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO014.png)
_1_Nota, in fase di inserimento dichiarazione di collaudo il sistema controlla : 
 *  _3_abilitazione del fornitore alla fornitura di un articolo di quella classe funzionale. Con il comando funzione F6 l'operatore può forzare la dichiarazione del collaudo anche per un fornitore non abilitato alla classe funzionale dell'articolo, il programma assegnerà il piano di campionamento rinforzato impostato in tabella;
 * _3_presenza di un documento rilasciato ad un livello di modifica superiore a quello del lotto. Con il comando funzione F6 F6 l'operatore può forzare la dichiarazione del collaudo anche se sono stati rilasciati documenti a livello di modifica superiore.

I campi da gestire sono : 
 *  _2_ente di controllo, è un campo che identifica il responsabile del controllo
 *  _2_esito controllo, è un campo (Tab. CQB) che identifica l'esito del controllo (deroga interna, consegna regolare, reso da cliente non conforme, ecc...)
 *  _2_quantità rilevata, è un campo numerico che identifica la quantità effettivamente rilevata al controllo
 *  _2_certificato qualità, è un campo in cui l'operatore può immettere il riferimento al certificato di qualità del fornitore ad esempio il certificato di colata dell'acciaio della fornitura
 *  _2_azioni sulla prossima consegna, è un campo (Tab. CQA) che permette di specificare quali azioni fare sulla prossima consegna articolo/fornitore, ad esempio un audit di controllo sull'articolo, collaudo completo articolo, ecc...
 *  _2_note, è un campo in cui vengono visualizzate le scelte fatte nel campo azioni sulla prossima consegna del lotto

## Sviluppi
La dichiarazione di collaudo può avere gli sviluppi seguenti identificati dai campi di selezione posti in basso al formato di dettaglio : 
![QA_ENLO015](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO015.png)
### Tempi e costi
Permette di specificare tempi e costi a preventivo e a consuntivo
![QA_ENLO016](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO016.png)
### Registrazione valori in archivio
Questa registrazione può essere specificata obbligatoria in funzione dell'esito del controllo (Tab. CQB).
_2_Formato registrazione tempi e costi :  permette di specificare tempi e costi a preventivo e a consuntivo
![QA_ENLO018](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO018.png)
_2_Formato gestione registrazione rilievi
![QA_ENLO021](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO021.png)Se 'n' sono le fasi di collaudo che sono state immesse nel ciclo di collaudo il collaudatore può generare 'n' documenti di questo tipo in cui alcune informazioni relative ai documenti a cui è legato come il codice dell'articolo, i valori a specifica, vengono riportate dal programma, mentre l'ente rilevatore deve essere specificato.

_2_Formato immissione  controllata dei rilievi
Il collaudatore a questo punto può o riportare direttamente i risultati finali del collaudo (media, varianza etc..)
![QA_ENLO019](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO019.png)oppure immettere tramite il campo valori rilevati le 'n' rilevazioni lasciando al programma il calcolo di media, varianza etc..

![QA_ENLO020](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO020.png)
### Azioni lotto
Permette di impostare l'esclusione  del lotto dalle statistiche e/o dal Vendor Rating del fornitore (cfr. modulo VEND)
![QA_ENLO017](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO017.png)
### Verbali scarto non conformità
Effettua il collegamento con il modulo delle non conformità per la loro registrazione. Questa registrazione può essere specificata obbligatoria in funzione dell'esito del controllo (tabella CQB). Quando il collaudatore esce da questo modulo di gestione delle non conformità il programma, sulla base dei risultati della gestione delle non conformità obbliga a cambiare l'esito del controllo; ad esempio se prima della richiesta di deroga il lotto era stato definito in attesa di deroga dopo potrebbe essere definito di scarto, accettato in deroga, etc..
![QA_ENLO022](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO022.png)
## Movimentazione
Alla conclusione della dichiarazione, in funzione degli esiti e delle quantità inserite, il programma emette il formato seguente in cui sintetizza le varie quantità che saranno utilizzate dal sistema per eseguire la movimentazione di magazzino (es. trasferimento giacenza da area accettazione a area di magazzino oppure a area scarti) : 
![QA_ENLO023](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM30/QA_ENLO023.png)le quantità possono anche essere cambiate dall'operatore purchè il tutto si bilanci con la quantità rilevata, F6 per confermare la dichiarazione.
