# CAratteri non validi nelle password estese

Abilitando la gestione delle password lunghe, parametro QPWDLVL=2, si attiva la possibilità di utilizzare password che sono case sensitive e possono contenere caratteri speciali.

Non tutti i caratteri però risultano ammissibili e su AS400 va specificato che i seguenti caratteri non sono validi : 
 ***'** : apice singolo
 ***"** : apice doppio
 ***<** : minore
 ***>** : maggiore
 ***=** : uguale
 ***&** : e commerciale
 *** ** : spazio
 ***|** : pipe
 ***;** : punto e virgola

