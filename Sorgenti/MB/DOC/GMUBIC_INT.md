# Generalità
Le ubicazioni sono partizioni fisiche/logiche del magazzino (es. scaffali) e sono caratterizzate da : 
 * _2_una tipologia;
 * _2_una gestione;
 * _2_delle dimensioni.

Solitamente appartengono ad un'area (Tabella GMR) che, se unica, viene definita nel tipo ubicazione.
# Gestione
Per creare delle ubicazioni è necessario definire il_B_TIPO UBICAZIONE(Tab._R_GMU) a cui si legano principalmente : 
 * l'oggetto gestito (solitamente l'articolo, oggetto_R_AR)
 * le dimensioni (se sono uguali per tutte le ubicazioni della tipologia)
 * l'area di appartenenza se unica
 * le categorie di parametri, impliciti (Tab._R_C£I), espliciti (Tab._R_C£E)
Il tipo ubicazione è un'informazione che nasce con l'ubicazione e non può essere modificata successivamente.

Se si desiderano evidenziare comportamenti diversi nella gestione delle ubicazioni, che possono cambiare nel tempo, si può utilizzare il_B_TIPO GESTIONE (Tabella_R_GMG).

Un altro elemento importante, nella definizione di alcuni particolari tipi di  ubicazione, sono le_B_DIMENSIONI; esse sono definibili sia sul Tipo ubicazione che direttamante sull'anagrafica delle ubicazioni.

### Costruzione codice
La costruzione del codice di una ubicazione può essere guidata tramite un flusso di costruzione
Esempio
>Tabella costruttore
 :  : DEC T(TA) P(B£F) K(OG_UB)
 :  : DEC T(ST) K(B£CUB)
