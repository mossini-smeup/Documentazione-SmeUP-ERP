## Fasatura dei requisiti esterni

I requisiti esterni vengono calcolati ad ogni allineamento per tutti gli impegni i cui requisiti sui luoghi sono soddisfatti, attivandoli/disattivandoli.
La dichiarazione di ogni impegno è preceduta da un allineamento, quindi l'ordine è sempre fasato rispetto ai requisiti esterni cambiati durante l'avanzamento.
Per requisiti che possono variare fuori dall'avanzamento del workflow è necessario schedulare dei riallineamenti esterni dei relativi ordini di workflow.

## Attività collegate

L'attivazione di un impegno con requisito esterno è una normale attivazione (flaggata con F4FL10='1'), avviene quando sia i requisiti sui luoghi che quelli esterni sono soddisfatti.
La disattivazione può essere : 
 * Una normale disattivazione, quando vengono rimossi token dai luoghi in entrata, per cui i requisiti sui luoghi non sono più soddisfatti (F4AZIO='5').
 * Una disattivazione dei requisiti esterni (F4AZIO='9').

## Requisiti esterni e presa in carico

Gli impegni presi in carico non vengono più disattivati da eventuali requisiti esterni :  l'esecuzione è già cominciata, non può essere più interrotta.

Se un requisito esterno dovesse eventualmente interrompere tra presa in carico e dichiarazione lo stesso effetto può essere ottenuto scomponendo la transizione in due transizioni consecutive, la prima rappresenta la presa in carico e la seconda la dichiarazione (vincolo :  la seconda deve avere lo stesso utente di esecuzione della prima)

## Requisiti esterni e file WFHIST0F

Pre 26/10/2012 : 
 * Lo stato dei requisiti esterni veniva salvato sul file WFHIST0F.
 * Era presente un vincolo per cui non potevano essere utilizzati requisiti esterni su transizioni iniziali.
Post 26/10/2012 : 
 * Il file WFHIST0F non viene più usato per la storicizzazione dei requisiti esterni :  l'evoluzione dei requisiti esterni viene calcolata scandendo le attività nel WFATTI0F.
 * Il vincolo sulle transizioni iniziali è stato rimosso.
