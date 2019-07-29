# Flussi di esecuzione workflow

Per "flusso di esecuzione workflow" si intende l'esecuzione in sequenza, da parte di un utente, di più impegni dello stesso ordine.
Il motore di workflow, dopo la creazione di un ordine (se impostato il modo di creazione opportuno in tabella WFA) o dopo l'esecuzione di un impegno da parte di un utente, verifica se ci sono altri impegni eseguibili da parte dello stesso utente, e : 
 * se trova un solo impegno eseguibile dallo stesso utente lo propone immediatamente;
 * se sono presenti più impegni presenta una worklist (limitata all'ordine in esame) per scegliere come proseguire.

## Impostazione dei flussi

Il fatto che il motore di workflow proponga automaticamente l'esecuzione di passi successivi è automatico. È possibile impostare dei vincoli su quali impegni NON debbano essere presentati agendo sull'attributo di transizione Sfl (salta in flussi di esecuzione).

## Interazione con l'attributo Nwl (no worklist)

Gli attributi Nwl e Sfl sono abbastanza correlati, nel senso che combinazioni diverse dei loro valori danno luogo a comportamenti più o meno tipici.
Combinazioni utili sono : 
 * Nwl='1', Sfl='1' :  utile per impegni totalmente opzionali, per i quali non si vuole nè che venga proposta l'esecuzione in un flusso di esecuzione wf, nè che venga ricordata la loro presenza in worklist. Un esempio potrebbe essere un impegno di annullamento all'interno di un flusso di oggetto, accessibile solo da pop.up di oggetto qualora necessario.
 * Nwl='1', Sfl='2' :  come il caso precedente, l'impegno non viene presentato in worklist nè presentato nei flussi. Unica eccezione :  alla creazione del workflow l'impegno, primo passo, viene proposto ed eseguito immediatamente. Questo è utile per impegni di gestione di un oggetto in processi di gestione "paracadute", per i quali la creazione del workflow è contestuale all'esecuzione dell'impegno.
 * Nwl=' ', Sfl='1' :  si usa per impegni di completamento di un altro impegno sullo stesso utente. Eseguito l'impegno 1, l'utente attiva l'impegno 2 per completare in un secondo tempo il lavoro; a questo punto l'impegno 2 non deve essere presentato immediatamente per l'esecuzione, ma viene messo in worklist per un'esecuzione successiva.

