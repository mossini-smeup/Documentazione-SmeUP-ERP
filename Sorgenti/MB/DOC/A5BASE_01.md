_B_Struttura del codice - primo esempio

 Supponiamo si voglia ottenere un codice così formato : 

   - codice azienda 2 caratteri
   - gruppo/conto   4 caratteri
   - progressivo    5 caratteri

_B_Cosa settare
## Tabelle da impostare
   - B£C :  definire un sottosettore 'CE', quindi codificare tre elementi
     che conterranno le regole di costruzione (ad es. CE001-2-3);
   - B£F :  codificato un nuovo elemento 'CE', contenente il sottosettore
     della B£C ('CE' nel nostro esempio) da cui prendere la domanda ini-
     ziale (CE001) che avvia la costruzione;
   - A5A :  sulle categorie fiscali definire se utilizzare la costruzione
     del codice, inserendo 'CE' nel campo 'Domande Costr.Codice'.

_B_Tabella B£C - Dettaglio elementi

 Elemento**CE001
   Descrizione      :   Azienda
   Programma/Metodo :   *DOI
   Parametro        :   ** /2/01/05
   Azione 1         :   101   2  101
   Azione 2         :   103   3  107

   Passo succ.-Subsett. CE
               Elemen.  CE002

 Elemento**CE002
   Descrizione      :   Gruppo/Conto
   Programma/Metodo :   *CAR
   Parametro        :   COxxyy
   Azione 1         :   101   4  103
   Azione 2         : 

   Passo succ.-Subsett. CE
               Elemen.  CE003

 Elemento**CE003
   Descrizione      :   Progressivo scheda
   Programma/Metodo :   *PRGOG
   Parametro        :   CE/C/101/09/05/N
   Azione 1         :   101  14  101
   Azione 2         : 

   Passo succ.-Subsett.
               Elemen.



_B_Struttura del codice - secondo esempio

 Supponiamo si voglia ottenere un codice così formato : 

   - anno acquisto  4 caratteri
   - progressivo    5 caratteri

 Posto che i passi da seguire sono gli stessi, la codifica dei due ele-
 menti della tabella B£C è la seguente : 

 Elemento**CE001
   Descrizione      :   Anno
   Programma/Metodo :   *OGG
   Obbligatorio     :   1
   Parametro        :   P8A
   Azione 1         :   101   4  101
   Azione 2         : 

   Passo succ.-Subsett. CE
               Elemen.  CE002

 Elemento**CE002
   Descrizione      :   Progressivo
   Programma/Metodo :   *PRGOG
   Parametro        :   CE/C/101/04/05/N
   Azione 1         :   101  14  101
   Azione 2         : 

   Passo succ.-Subsett.
               Elemen.



_B_Struttura del codice - terzo esempio

 Supponiamo si voglia ottenere un codice così formato : 

   - azienda        2 caratteri
   - anno acquisto  2 caratteri (es.2005 --> 05)
   - cat.cespite    3 caratteri
   - progressivo    4 caratteri

 Posto che i passi da seguire sono gli stessi, la codifica dei quattro
 elementi della tabella B£C è la seguente : 

 Elemento**CE001
   Descrizione      :   Azienda
   Programma/Metodo :   *OGG
   Parametro        :   AZ
   Obbligatorio     :   1
   Azione 1         :   101   2  101
   Azione 2         : 

   Passo succ.-Subsett. CE
               Elemen.  CE002

 Elemento**CE002
   Descrizione      :   Anno
   Programma/Metodo :   *OGG
   Parametro        :   P8A
   Obbligatorio     :   1
   Azione 1         :   103   2  103
   Azione 2         : 

   Passo succ.-Subsett. CE
               Elemen.  CE003

 Elemento**CE003
   Descrizione      :   Categoria cespite
   Programma/Metodo :   *OGG
   Parametro        :   TAA5A
   Obbligatorio     :   1
   Azione 1         :   101   3  105
   Azione 2         : 

   Passo succ.-Subsett. CE
               Elemen.  CE004

 Elemento**CE004
   Descrizione      :   Progressivo
   Programma/Metodo :   *PRGOG
   Parametro        :   CE/C/101/08/04/N
   Obbligatorio     : 
   Azione 1         :   101  14  101
   Azione 2         : 

   Passo succ.-Subsett.
               Elemen.
