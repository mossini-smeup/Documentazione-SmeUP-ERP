# Esempio Injection Servizio MUJ03_SE
@Program(name = "MUJ03_SE", text = "Database Service")
public class MUJ03_SE extends MUJXX_SE {

 @Inject
 private QLibraryManager libraryManager;

 @Inject
 private QJobLogManager jobLogManager;

 @Inject
 private QQueryParserRegistry queryParserRegistry;

 @DataDef(dimension = 1000, length = 100)
 public QArray<QCharacter> swk001;

 protected void main() {

  if (£uib.£uibds.£uibme.eq("LIS.SCH"))
   schemaList();
  else if (£uib.£uibds.£uibme.eq("LIS.TAB"))
   tableList();
  else if (£uib.£uibds.£uibme.eq("LIS.VIE"))
   viewList();
  else if (£uib.£uibds.£uibme.eq("LIS.COL"))
   columnList();
  else if (£uib.£uibds.£uibme.eq("LIS.IND"))
   indexList();
  else if (£uib.£uibds.£uibme.eq("SEL.ROW"))
   rowSelect();
  else if (£uib.£uibds.£uibme.eq("EXE.STM"))
   executeStatement(£uib.£uibds.£uibd1.trimR());
  else if (£uib.£uibds.£uibme.eq("ANA.STM"))
   analyzeStatement(£uib.£uibds.£uibd1.trimR());
 }
}
