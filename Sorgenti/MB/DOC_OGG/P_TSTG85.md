# Funzioni e Metodi
 :  : PAR F(01) L(PUN)
- il metodo POS effettua il posizionamento e la prima lettura del BRESCO;
- il metodo LET effettua le letture successive;


##  ESPLOSIONE : 
   Possibili utilizzi
   Dato un contatto e un tipo indirizzo, ottenere i valori presenti per quel contatto relativi a quel tipo indirizzo.
   In Oggetto 1 (£G85T1,K1) passo il tipo contatto e il codice;
   In Oggetto 2 (£G85T2) passo il tipo indirizzo.

   Dato un contatto ottenere tutti i tipi indirizzo e i relativi valori presenti per quel contatto.
   In Oggetto 1 (£G85T1,K1) passo il tipo contatto e il codice;
   in Oggetto 2 (£G85T2) non passo nulla;

## IMPLOSIONE : 
   Possibili utilizzi
   Dato un tipo indirizzo e un valore, ottenere il tipo e codice contatto cui appartiene.
   In Oggetto 1 (£G85T1,K1) non passo né il tipo contatto né il codice;
   In Oggetto 2 (£G85T2,K2) passo il tipo e il codice indirizzo.

   Dato un tipo indirizzo ottenere tutti i valori di tutti i contatti relativamente a quel tipo indirizzo.
   In Oggetto 1 (£G85T1,K1) non passo né il tipo contatto né il codice;
   in Oggetto 2 (£G85T2) passo il tipo indirizzo.

##  ESPLOSIONE TIPO : 
   Possibili utilizzi
   Dato un contatto ottenere tutti i tipi indirizzo presenti per quel contatto.
   In £G85T1,K1 passo il tipo e il codice contatto;
   in £G85T2,K2 non passo nulla.

##  RICERCA : 
   Possibili utilizzi
   Metodo '   ' :  In base al primo carattere.
   Dato un tipo indirizzo e una richiesta di tipo ricerca per codice (valore preceduto da "!")
   o per descrizione (valore preceduto da "?") ottenere la lista dei valori contenenti quel
   codice o descrizione realtivi al tipo indirizzo passato.
   In £G85T1,K1 non passo nulla;
   in £G85T2 passo il tipo indirizzo, in £G85K2 passo il valore preceduto da "?" o "!".

   Metodo 'COD' :  In base al primo carattere.
   Dato un tipo indirizzo e un valore ottenere la lista dei valori contenenti quel codice.
   In £G85T1,K1 non passo nulla;
   in £G85T2 passo il tipo indirizzo, in £G85K2 passo il valore ricercato.

   Metodo 'DES' :  In base al primo carattere.
   Dato un tipo indirizzo e un valore ottenere la lista dei valori contenenti quella descrizione
   In £G85T1,K1 non passo nulla;
   in £G85T2 passo il tipo indirizzo, in £G85K2 passo il valore ricercato.

##  DECODIFICA : 
   Dato un tipo indirizzo e un valore completo ottenere la decodifica di quel valore, ovvero il
   contatto a cui si riferisce.
   In £G85T1,K1 non passo nulla;
   in £G85T2 passo il tipo indirizzo, in £G85K2 passo il valore da decodificare.
