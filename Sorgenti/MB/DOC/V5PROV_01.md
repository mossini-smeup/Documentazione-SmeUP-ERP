# Note generali
La singola provvigione è rappresentata dall'oggetto PV, che ha un suo identificativo sul file V5PROV0F (P§IDOJ).
L'identificativo del file è dato dall'oggetto PV, il cui numeratore è definito dall'elemento OG.PV della tabella CRNV5. e la cui gestione è affidata alla /COPY £V6B.

# Gestione archivio provvigioni
La manutenzione dei singoli record di provvigione viene fatta mediante gli appositi programmi di gestione del data entry.
Le autorizzazioni sono controllate dalla classe V5PR01 e il contenitore delle note viene specificato sul tipo provvigione (tab V5P) o, per risalita, sulla tabella V58.

 :  : INI Test Gestione provvigioni
 :  : CMD CALL V5PR01G
 :  : FIN

# Ripresa (Estrazione provvigioni da documenti V5)
Il file delle provvigioni può essere popolato lanciando un pgm di caricamento che analizza i dati dei documenti del ciclo attivo in rapporto all'agente (ta AGE) cui risultano associati. Il tipo provvigione con il quale verrano generati i record dipende da quanto definito nella tabella dell'agente, ma c'è la possibilità di determinarla anche tramite un pgm di aggiustamento, la cui esecuzione dipende dall'averne indicata l'intenzione nella tabella V58. E' da tenere presente che per le note d'accredito è necessario creare un tipo provvigioni avente il flag 08 valorizzato (Inversione Valori) nel gruppo flag.

Normalmente le % delle provvigioni sui documenti di ciclo attivo vengono strutturate tramite l'utilizzo dei listini.

# Pgm del flusso
V5PR05G/V  :  Guida
V5PR05CL   :  Seleziona Testate dei documenti da elaborare
V5PR05_XX  :  Pgm di esecuzione (dove ad XX va sostituito il codice dell'ambiente dei documenti)
V5PR05_X   :  Eventuale pgm di exit per la determinazione del tipo provvigione

# Richiamo pgm
 :  : INI Estrazione Provvigioni
 :  : CMD CALL V5PR05G
 :  : FIN

# Tabelle
 :  : DEC T(ST) P() K(V58)
 :  : DEC T(ST) P() K(V5P)
 :  : DEC T(ST) P() K(AGE)
 :  : DEC T(TA) P(CRNV5) K(OG.V5)
