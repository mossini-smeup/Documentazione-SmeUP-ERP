# A5A - Categoria fiscale cespite
 :  : DEC T(ST) K(A5A)
## OBIETTIVO
Definisce i parametri propri di ogni categoria fiscale, caratterizzazione principale (ed obbligatoria) di ogni cespite aziendale.
## SOTTOSETTORE
Da non impostare.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il codice della categoria fiscale
 :  : FLD T$A5AA **Da non ammortizzare**
È un valore V2 SI/NO :  se impostato, per i cespiti di questa categoria non verrà calcolato l'ammortamento.
Un esempio è dato dai terreni, il cui valore non diminuisce nel tempo, ma è determinato solo da variazione di capitale.
 :  : FLD T$A5AB **Inizializzazione cespite**
È un elemento della tabella A5W. È un valore obbligatorio : 
contiene le informazioni collegate ai cespiti di questa categoria (gruppi flag, categoria parametri, parametri impliciti, contenitori note).
 :  : FLD T$A5AC **Griglia classificazione**
È un elemento della tabella B£G che tipizza i primi tre campi di classificazione dei cespiti di questa categoria.
 :  : FLD T$A5AD **Domande costruzione codice**
È un elemento della tabella B£F :  rappresenta il flusso di domande che sovraintende alla costruzione del codice di un cespite appartenente a questa categoria.
 :  : FLD T$A5AE **Riferimento legislativo**
È un elemento della tabella V§A (fornita da SME_UP) :  rappresenta la corrispondenza, a livello legislativo, della categoria.
 :  : FLD T$A5AG **% Indeducibilità**
Se impostata, definisce la percentuale di ammortamento non deducibile per questa categoria. Essa verrà applicata se, nella linea, è presente la causale di ammortamento indeducibile.
 :  : FLD T$A5AH **Massimo capitale ammortizzabile**
Se impostata, definisce il valore massimo di capitale ammortizzabile per questa categoria. Essa verrà applicata se, nella linea, è presente la causale di capitale non ammortizzabile.
 :  : FLD T$A5AI **Immateriali**
È un valore V2 SI/NO :  se impostato, i cespiti di questa categoria sono beni immateriali.
Pertanto, nel calcolo dell'ammortamento non viene considerata la soglia dei cespiti minori, eventualmente impostata sulla linea per eseguire l'ammortamento istantaneo. Inoltre non viene effettuata la riduzione del primo anno.
 :  : FLD T$A5AF **Griglia classificazione**
È un elemento della tabella B£G che tipizza i secondi tre campi di classificazione dei cespiti di questa categoria.
