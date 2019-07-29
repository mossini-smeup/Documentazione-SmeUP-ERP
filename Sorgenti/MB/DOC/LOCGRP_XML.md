# Descrizione XML servizio
Il componente GRP utilizza un apposito XML.
 T(E' costituito da 4 parti : )
- Setup
- Set di nodi.
-- Nodo :  attributi
--- nodeID :  (univoco) lo identifica nel grafo
--- shape :  specifica la forma del grafo (valori possibili 1,2,3)
--- Label : attributi
---- label :  testo da mostrare nel nodo
---- backColor :  colore sfondo, formato RRGGBB
---- textColor :  colore testo, formato RRGGBB
---- fontSize :  la dimensione del font
--- location :  attributi
---- x :  specifica la coordinata x
---- y :  specifica la coordinata y
---- visibility :  specifica se il nodo è visibilwe
--- Hint :  attributi
---- hint :  il testo da mostrare
---- isHTML :  true se il testo è in formato HTML
---- width :  larghezza finestra suggerimento
---- height :  altezza finestra suggerimento. -1 se si desidera che sia automatico.
- Relazioni :  attributi
-- fromID :  l'id del nodo da cui partire
-- toID :  l'id del nodo su cui andare
-- type :  il tipo (linea ingrossata, freccia, linea semplice, freccia se si posiziona sopra il mouse, linea con freccia finale)
-- length : 
-- visible : 
-- color :  il colore
-- descr :  la descrizione
- Parametri


<?xml version="1.0" encoding="ISO-8859-1"?>
<UiSmeup Testo="Import/Export XML per grafi (oggettizzato) - istruzione demo">
	<Service Titolo1="Import/Export XML per grafi (oggettizzato)" Titolo2="istruzione demo" Funzione="F(GRP;WFSER_06;EXP) 1(F1;;0000002069) 2(;;)" Servizio="WFSER_06"/>
	<Setup>
		<Program>
			<GRP>
				<Gen Locality="" ObjIconType=""/>
			</GRP>
		</Program>
	</Setup>
	<TOUCHGRAPH_LB version="1.20">
		<NODESET>
			<NODE nodeID="L01" shape="3">
				<NODE_LABEL label="L01" backColor="00FF00" textColor="FFFFFF" fontSize="20"/>
				<NODE_LOCATION x="0300" y="0200" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="L02" shape="3">
				<NODE_LABEL label="L02" backColor="000000" textColor="FFFFFF" fontSize="11"/>
				<NODE_LOCATION x="0300" y="0400" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="L97" shape="3">
				<NODE_LABEL label="L97" backColor="000000" textColor="FFFFFF" fontSize="11"/>
				<NODE_LOCATION x="0600" y="0500" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="L03" shape="3">
				<NODE_LABEL label="L03" backColor="000000" textColor="FFFFFF" fontSize="11"/>
				<NODE_LOCATION x="0300" y="0600" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="L06" shape="3">
				<NODE_LABEL label="L06" backColor="000000" textColor="FFFFFF" fontSize="11"/>
				<NODE_LOCATION x="0000" y="0500" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="L05" shape="3">
				<NODE_LABEL label="L05" backColor="00FF00" textColor="FFFFFF" fontSize="11"/>
				<NODE_LOCATION x="0450" y="0900" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="L04" shape="3">
				<NODE_LABEL label="L04" backColor="000000" textColor="FFFFFF" fontSize="11"/>
				<NODE_LOCATION x="0150" y="0800" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="L07" shape="3">
				<NODE_LABEL label="L07" backColor="000000" textColor="FFFFFF" fontSize="11"/>
				<NODE_LOCATION x="0450" y="1100" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="L98" shape="3">
				<NODE_LABEL label="L98" backColor="000000" textColor="FFFFFF" fontSize="11"/>
				<NODE_LOCATION x="0450" y="1300" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="L99" shape="3">
				<NODE_LABEL label="L99" backColor="FF0000" textColor="FFFFFF" fontSize="11"/>
				<NODE_LOCATION x="0450" y="1500" visible="true"/>
				<NODE_HINT hint="" isHTML="true" width="500" height="-1"/>
			</NODE>
			<NODE nodeID="T01" shape="1">
				<NODE_LABEL label="T01 :  Creazione documento - codice balnk " backColor="00FF00" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0300" y="0300" visible="true"/>
				<NODE_HINT hint="<b>Eseguito</b>
Data ultima attivazione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima attivazione :   14 : 40 : 56
Utente ultima esecuzione :  <b>MR             </b>
Data ultima esecuzione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima esecuzione :   14 : 42 : 44
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="F2" Parametro="GEN01" Codice="" Testo="Creazione" Fld="" Leaf=""/>
			</NODE>
			<NODE nodeID="T02" shape="1">
				<NODE_LABEL label="T02 :  Verifica- p e k blank" backColor="00FF00" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0300" y="0500" visible="true"/>
				<NODE_HINT hint="<b>Eseguito</b>
Data ultima attivazione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima attivazione :   14 : 47 : 03
Utente ultima esecuzione :  <b>MR             </b>
Data ultima esecuzione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima esecuzione :   15 : 02 : 07
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="F2" Parametro="" Codice="" Testo="Verifica" Fld="" Leaf=""/>
			</NODE>
			<NODE nodeID="T03" shape="1">
				<NODE_LABEL label="T03 :  Anche approvazione? - T,P e K blank" backColor="00FF00" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0300" y="0700" visible="true"/>
				<NODE_HINT hint="<b>Eseguito</b>
Data ultima attivazione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima attivazione :   15 : 02 : 07
Utente ultima esecuzione :  <b>               </b>
Data ultima esecuzione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima esecuzione :   15 : 02 : 07
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="" Parametro="" Codice="" Testo="Anche approvazione?" Fld="" Leaf=""/>
			</NODE>
			<NODE nodeID="T04" shape="1">
				<NODE_LABEL label="T04 :  Approvazione" backColor="00FF00" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0150" y="0900" visible="true"/>
				<NODE_HINT hint="<b>Eseguito</b>
Data ultima attivazione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima attivazione :   15 : 02 : 07
Utente ultima esecuzione :  <b>MR             </b>
Data ultima esecuzione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima esecuzione :   16 : 00 : 23
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="F2" Parametro="GEN01" Codice="0000010006" Testo="Approvazione" Fld="" Leaf=""/>
			</NODE>
			<NODE nodeID="T05" shape="1">
				<NODE_LABEL label="T05 :  Distribuzione" backColor="0000FF" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0450" y="1000" visible="true"/>
				<NODE_HINT hint="<b>Distribuito</b>
Data ultima attivazione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima attivazione :   16 : 00 : 24
Utente ultima esecuzione :  <b>               </b>
Data ultima esecuzione : 
Ora ultima esecuzione : 
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="F2" Parametro="GEN01" Codice="0000010007" Testo="Distribuzione" Fld="" Leaf=""/>
			</NODE>
			<NODE nodeID="S01" shape="1">
				<NODE_LABEL label="S01 :  Presa visione" backColor="FF0000" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0999" y="0999" visible="true"/>
				<NODE_HINT hint="<b>Pronto</b>
Data ultima attivazione :  Martedì 15 Maggio 2007 / Set 20
Ora ultima attivazione :   11 : 28 : 19
Utente ultima esecuzione :  <b>               </b>
Data ultima esecuzione : 
Ora ultima esecuzione : 
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="F2" Parametro="GEN01" Codice="0000010033" Testo="Presa visione" Fld="" Leaf=""/>
			</NODE>
			<NODE nodeID="T06" shape="1">
				<NODE_LABEL label="T06 :  Revisione" backColor="00FF00" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0000" y="0400" visible="true"/>
				<NODE_HINT hint="<b>Eseguito</b>
Data ultima attivazione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima attivazione :   14 : 45 : 35
Utente ultima esecuzione :  <b>MR             </b>
Data ultima esecuzione :  Lunedì 14 Maggio 2007 / Set 20
Ora ultima esecuzione :   14 : 47 : 03
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="F2" Parametro="GEN01" Codice="0000010008" Testo="Revisione" Fld="" Leaf=""/>
			</NODE>
			<NODE nodeID="T07" shape="1">
				<NODE_LABEL label="T07 :  Pubblicazione" backColor="FF0000" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0450" y="1200" visible="true"/>
				<NODE_HINT hint="<b>Non pronto</b>
Data ultima attivazione : 
Ora ultima attivazione : 
Utente ultima esecuzione :  <b>               </b>
Data ultima esecuzione : 
Ora ultima esecuzione : 
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="F2" Parametro="GEN01" Codice="0000010009" Testo="Pubblicazione" Fld="" Leaf=""/>
			</NODE>
			<NODE nodeID="T98" shape="1">
				<NODE_LABEL label="T98 :  Annulla" backColor="FF0000" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0600" y="0600" visible="true"/>
				<NODE_HINT hint="<b>Non pronto</b>
Data ultima attivazione : 
Ora ultima attivazione : 
Utente ultima esecuzione :  <b>               </b>
Data ultima esecuzione : 
Ora ultima esecuzione : 
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="F2" Parametro="GEN01" Codice="0000010010" Testo="Annulla" Fld="" Leaf=""/>
			</NODE>
			<NODE nodeID="T99" shape="1">
				<NODE_LABEL label="T99 :  Finale" backColor="FF0000" textColor="FFFFFF" fontSize="15"/>
				<NODE_LOCATION x="0450" y="1400" visible="true"/>
				<NODE_HINT hint="<b>Non pronto</b>
Data ultima attivazione : 
Ora ultima attivazione : 
Utente ultima esecuzione :  <b>               </b>
Data ultima esecuzione : 
Ora ultima esecuzione : 
" isHTML="true" width="500" height="-1"/>
				<Oggetto Nome="" Tipo="F2" Parametro="GEN01" Codice="0000010011" Testo="Finale" Fld="" Leaf=""/>
			</NODE>
		</NODESET>
		<EDGESET>
			<EDGE fromID="L01" toID="T01" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T01" toID="L02" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T01" toID="L97" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="L02" toID="T02" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T02" toID="L03" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T02" toID="L06" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T02" toID="L97" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="L03" toID="T03" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T03" toID="L05" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T03" toID="L04" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="L04" toID="T04" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T04" toID="L05" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T04" toID="L06" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="L05" toID="T05" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T05" toID="L07" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="L06" toID="T06" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T06" toID="L02" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T06" toID="L97" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="L07" toID="T07" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T07" toID="L98" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="L97" toID="T98" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T98" toID="L98" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="L98" toID="T99" type="3" length="50" visible="true" color="000000" descr=""/>
			<EDGE fromID="T99" toID="L99" type="3" length="50" visible="true" color="000000" descr=""/>
		</EDGESET>
		<PARAMETERS>
			<PARAM name="offsetX" value="0"/>
			<PARAM name="rotateSB" value="0"/>
			<PARAM name="zoomSB" value="0"/>
			<PARAM name="offsetY" value="0"/>
		</PARAMETERS>
	</TOUCHGRAPH_LB>
</UiSmeup>



