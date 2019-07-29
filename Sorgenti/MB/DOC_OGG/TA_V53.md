# V53 - Parametri autofatturazione
 :  : DEC T(ST) K(V53)
## OBIETTIVO
Definisce le modalità con cui si creano le AUTOFATTURE.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È un tipo modello da cui saranno estratte le righe omaggio per l'autofattura.
 :  : FLD T$V531 **Cliente intestatario**
È il codice cliente che identifica l'azienda e sarà anche il codice intestatario del documento di autofattura, generato dal programma.
 :  : FLD T$V532 **Tipo documento**
È il tipo documento (tabella V5D) che verrà generato.
 :  : FLD T$V534 **S/S Modello Dest.**
È un sottosettore della tabella V5A.
 :  : FLD T$V535 **Modello destinazione**
È il modello documento che verrà generato ed è un elemento della tabella V5Axx (dove xx è il sottosettore specificato nel campo precedente).
 :  : FLD T$V537 **S/S Riga Destinaz.**
È un sottosettore della tabella V5B.
 :  : FLD T$V538 **Tipo riga destinaz.**
È il tipo riga con cui verranno generate le righe del documento ed è un elemento della tabella V5Bxx (dove xx è il sottosettore specificato nel campo precedente).
 :  : FLD T$V539 **Tipo costo**
È un elemento della tabella TCO. Si può indicare un tipo costo che verrà utilizzato per recuperare il costo dell'articolo, specificato nella riga in autofattura. Questa funzione serve per non obbligare ad inserire un prezzo anche nelle righe omaggio; lasciando il campo in bianco verrà utilizzato (sempre) il valore inserito nella riga.
 :  : FLD T$V530 **Livello costo**
È il livello del costo specificato precedentemente.
 :  : FLD T$V53A **Codice pagamento**
Se specificato imposta questo codice pagamento nella testata del documento autofattura
 :  : FLD T$V53B **Codice listino**
Se specificato imposta questo codice listino nella testata del documento autofattura
 :  : FLD T$V53C **Raggruppamento documenti**
Se specificato imposta questo codice di raggruppamento documenti nella testata del documento autofattura
 :  : FLD T$V53D **Magazzino assunto**
Se specificato ed in ambiente multimagazzino, è il magazzino che viene impostato in testata del documento
autofattura, se questo non è impostato dalla routine V5Y.
