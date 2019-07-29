# Lancio BCD in modalità cieca
Per eseguire un flusso BCD in modalità cieca si devono codificare : 

- L'elemento di tabella B§G. E' del tutto simile ad un elemento di lancio interattivo, ad eccezione dei seguenti campi
-- Forza interattivo, che va impostato a ' '
-- Forza emulazione, che va impostato a '1'
Non è necessario intervenire sullo script BCD, posto che esso preveda anche la modalità cieca :  non deve emettere, in questo caso, formati o schede.
Lo script standard di Fine.Up, ad esempio, è già predisposto in questo modo.
- La memorizzazione dei parametri di lancio
Per impostare i parametri di lancio va utilizzato il seguente procedimento.
Si entra nel lancio interattivo, in modalità 5250, con l'elemento B§G definito in precedenza, e si impostano i campi di lancio.
Si copia quindi questa memorizzazione (con UP MDV), dall'utente che ha eseguito la memorizzazione, e dall'ambiente individuato dall'elemento B§G, nello stesso ambiente, ed in un utente inesistente (si consiglia di farlo iniziare con un numero, in modo che non potrà coincidere con utenti futuri).
Questo nuovo utente costituisce la memorizzazione dei parametri di lancio.
Il motivo della laboriosità di questa operazione sta nella differenza di memorizzazione tra £G11 (non compattata) e £G30 (compattata).


# Lancio BCD da menu
Si lancia il programma B£BCD06 con i seguenti parametri : 
- L'elemento di tabella B§G (15 caratteri)
- La memorizzazione dei parametri di lancio (8 caratteri)
# Lancio BCD da passo di flusso
Si codifica una B£J con il programma B£BCD07, e con la £FUNPS impostata nel seguete modo : 
- L'elemento di tabella B§G  :  Posizioni 1 - 15
- La memorizzazione dei parametri di lancio  :  Posizioni 16 - 23
