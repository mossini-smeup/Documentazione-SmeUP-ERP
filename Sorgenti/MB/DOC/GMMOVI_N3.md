# Revisione movimenti di magazzino
La revisione viene eseguita dal programma di lista movimenti :  GMMO01G > GMMO01L

Se il guida è lanciato con il parametro "1" si predispone alla revisione, altrimenti è solo interrogazione :  in questo modo si può sia fare un'azione di menù, sia impostare un passo di flusso di selezione B£J impostando un valore qualsiasi nel parametro 1 di tabella (in questo modo la B£GFP10 esegue un lancio con un parametro).

La variazione / annullamento è possibile solo se la causale ha una forma di presentazione.
Viene poi eseguito un controllo di autorizzazione (anche in inserimento) : 
 * classe **Abilita**
 * funzione **MOVMAGx**, dove x è il gruppo abilitazione impostato nella causale (GMC)

In variazione si può cambiare anche la causale :  devono essere verificate però entrambe queste condizioni : 
 * le 2 causali (vechcia e nuova) devono avere la stessa forma di presentazione
 * l'utente deve essere abilitato alla variazione anche della nuova causale
