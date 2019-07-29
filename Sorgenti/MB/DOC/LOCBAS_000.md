# Descrizione del componente base
Il componente base è quella parte dell'applicativo che si occupa delle funzioni base sia lato client sia lato server. E' uno strato intermedio di funzionalità che si occupa tra le altre cose di gestire la comunicazione client-server, di fornire funzionalità comuni a tutti i componenti client, di fornire interfaccie verso i vari moduli server Sme.up.
**N.B.
Il componente base è costituito da due parti, una su AS400 e una nel client.

Alcune funzionalità offerte da questo componente lato client sono : 
 :  : PAR F(01) L(PUN)
- Comunicazione su code e su programcall
- Gestione delle finestre e dello stack
- Gestione funzioni di base comuni :  carrello, preferiti, cronologia
- Gestione di eventuali Loocup Client
- Gestione di Loocup Server
- Gestione della business continuity

