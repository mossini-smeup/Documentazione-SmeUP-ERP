### Insoluti
Nel caso in cui si decida di liquidare le provvigioni anche quando le relative scadenze risultano ancora in rischio e contemporaneamente si vuole gestire il fatto che in caso insoluto la partita venga riaperta e necessario gestire un'azione che a partire dalla contabilità vada a riaprire lo stato della provvigione in modo che questa venga ripresa in considerazione nel calcolo.

Nel caso in cui la contabilità sia Smeup è disponibile un esempio applicato all'exit di inizializzazione delle rate, impostazione tramite la tabella C5E.

 :  : DEC T(ST) P() K(C5D&AZ)
 :  : DEC T(ST) P() K(C5E&AZ)

### Sorgente pgm di esempio
 :  : INI
 :  : CMD CALL B£VED0 PARM('C5C5C0_V' '' '' '' '0')
 :  : FIN

### Impostazione parametri per escludere provvigione in caso di rilevamento perdita
Nel caso in cui si abbia una fattura insoluta che viene chiusa con una causale di rilevazione perdita (e quindi la fattura viene inclusa nei crediti inesigibili) è possibile fare in modo che la provvigione non venga liquidata pur essendo la partita chiusa.
Per fare questo è necessario attivare l'utilizzo delle causali V56 nella tabella V58, attivare l'esclusione degli abbuoni in liquidazione sempre da V58 e compilare la V56. Nella V56 andrà indicata la causale con cui si ha la rilevazione della perdita e flaggato il campo "Causale Credito Inesigibile"
