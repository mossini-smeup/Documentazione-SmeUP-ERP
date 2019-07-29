# Prerequisiti
Se non è stato attivato Sme.UP dal programma di installazione bisogna eseguire il programma di creazione B£UT11B
 :  : INI **Vuoi lanciare il programma di creazione ambiente base Sme.up?
 :  : CMD CALL B£UT11B
 :  : FIN

# Attivazione
## Tabella V51
E' la tabella di personalizzazione della applicazione V5
 :  : DEC T(TA) P(V51) K(*) I(**Impostazione tabella V51)
### Alla tabella sono collegate le seguenti tabelle :  
 :  : DEC T(ST) K(BRE) I(**Tabella BRE per Clienti e Fornitori)
 :  : DEC T(ST) K(V5S) I(**Tabella V5S per Sconto pagamento e incasso)
 :  : DEC T(ST) K(IVA) I(**Tabella IVA per assoggettamento STD)

## Tabella V5D tipo documento
La tabella V5D identifica i tipo documenti che verranno gestiti. Per impostare la tabella V5D bisogna avere identificato e creato : 
 * sottosettore della tabella V5A ed eventualmente l'elemento std
 * Tipo ente :  intestatario,di spedizione e di fatturazione
 * Categoria listini associati al documento (C£*CL)
 * gruppi flag standard per le testate e per le righe
  :  : DEC T(ST) K(V5D) I(**Impostazione tabella V5D)

## Tabella V5A tipo modello
Dopo aver impostato la tabella V5D bisogna creare la tabelle V5Axx (xx è il sottosettore indicato nella tabella V5D relativa)
Per impostare la tabella V5Axx bisogna avere identificato e creato : 
 * sottosettore della tabella V5B ed eventualmente l'elemento std
 * contenitore (tab. NSC) delle note
 * Categoria listini associati al documento (C£*CL)
  :  : DEC T(ST) K(V5A) I(**Impostazione tabella V5A)

## Tabella V5B tipo riga
Dopo aver impostato la tabella V5Axx bisogna creare la tabelle V5Bxx (xx è il sottosettore indicato nella tabella V5A relativa)
 :  : DEC T(ST) K(V5B) I(**Impostazione tabella V5B)

## Classi autorizzazioni da impostare
Per la gestione delle autorizzazioni sono interessate le seguenti classi di autorizzazione
 :  : DEC T(TA) P(B£P) K(V5DO01)
 :  : DEC T(TA) P(B£P) K(V5DO01D)
 :  : DEC T(TA) P(B£P) K(V5DO01M)
 :  : DEC T(TA) P(B£P) K(V5DO05)
 :  : DEC T(TA) P(B£P) K(V5DO05D)
 :  : DEC T(TA) P(B£P) K(V5DO05M)
 :  : DEC T(TA) P(B£P) K(ABILITA)
 :  : INI _3_ Gestione autorizzazioni 
 :  : CMD UP AUT
 :  : FIN

### Protezione campi
Per attivare la protezione dei singoli campi dopo aver abilitato la gestione totale in tabella B£2 bisogna gestire le seguenti classi di autorizzazione
 :  : DEC T(TA) P(B£2) K(*) I(**Tabella personalizzazione)
 :  : DEC T(TA) P(B£P) K(PLC-)
 :  : DEC T(TA) P(B£P) K(PLC-V5TDOC)
 :  : DEC T(TA) P(B£P) K(PLC-V5RDOC)

**Sottosettori della tabella B£S interessati
 :  : DEC T(ST) K(B£SGD)
 :  : DEC T(ST) K(B£SV5)
 :  : DEC T(ST) K(B£SAZ)
