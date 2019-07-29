Descrivere i controlli necessari per le informazioni riservate, i responsabili

Preparare un PDF che descriva tutta l'organizzazione per la gestione della sicurezza, raccogliendole autorizzazioni di accesso dalle autorizzazioni applicative di Smeup
## Architettura delle informazioni
L'oggetto base a cui si fa riferimento è l'azienda, intesa come oggetto CN di tipo AZI
A questo oggetto vengono relazionati gli enti responsabili per i vari livelli di sicurezza che sono
descritti nei parametri X dell'azienda, ed esattamente : 

- X                 Rappresentante Legale
- X0                Titolare del Trattamento
- X1                Resp. del Trattamento
- X2                Resp. Sic.za sist. informati
- X21               SERVER
- X22               DISPOSITIVI ACCESSO
- X23               ELABORATORI
- X3                Inc. Custodia Parole chiave
- X4                Inc. Trat.Dati sens.li/giud.ri
- X5                Locali trattamento dati
- X6                Fornitori Est.Trattamento Dati
- X9                Data Consolidamento DPPS
- X10              Tempo recupero dati (in gg)
- X11              Costo recupero dati (in euro)
- X12              Costo tempo perso per recupero


I dispositivi fisici sono descritti come cespiti, con una particolare Classe implicita (tabella A5D)
che li identifica come elaboratori, dispositivi di accesso e servers.
