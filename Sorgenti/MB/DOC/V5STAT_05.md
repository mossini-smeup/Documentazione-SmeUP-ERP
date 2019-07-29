# Personalizzazione campi file V5STAT0F

## Programma B£EQRY_AOX
Il file V5STAT0F ha una set di campi che sono liberi, personalizzabili dal cliente.

In particolare ci sono : 
 * 10 Codici Liberi
 * 10 Numeri Liberi
 * 05 Date Libere

Dei 20 flag presenti sul file, gli ultimi 10 sono personalizzabili dal cliente attraverso il pgm flaggatore V5STAT0F_F.

Per  gestire i campi liberi, è necessario implementare il pgm B£EQRY_AOX  come personalizzazione cliente. Un prototipo del programma si trova in SMESRC/SMEDEV : 

B£EQRY_AOX     RPGLE_ES        EQRY             Assegnazione oggetto di un campo - prototipo

Nella schiera che si trova in fondo nel sorgente, è necessario inserire i campi che si vogliono personalizzare, specificando il file V5STAT0F, il nome del campo, il nuovo tipo oggetto, la nuova descrizione.
Esempio : 
>.      Pgm    Campo    Oggetto KyOCAuT   Descrizione
. V5STAT0F    D6COD1   CNCOL             Classificazione Interna Articolo


Con la stessa modalità è possibile sovrascrivere un qualsiasi campo del file, cambiandone di fatto il significato rispetto allo standard SME-UP.
La gestione del valore dei campi liberi o la gestione particolare del valore dei campi standard, è poi possibile gestirla attraverso il programma di EXIT utente, richiamato dal programma di creazione della statistica V5STA05.

Alcuni campi liberi sono già stati utilizzati dai pgm standard. In particolare : 
**D6NUM0** - Valore escluso da statistica
Questo campo rappresenta il valore della riga escluso da statistica in forza dei flag statistici del documento origine.

**D6DT01** - Data consegna ordine
Rappresenta la data di consegna dell'ordine, utilizzata nella ripresa dell'ordinato.
