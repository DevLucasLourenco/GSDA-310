import pandas as pd

from service.data.archive import Archive


class DataDeal: # fazer teste de quando nao estiver a mesma quantidade nas colunas do excel o que vai acontecer 
    TYPE_DATA_ALLOWED:dict
    
    def __init__(self, fileReceived) -> None:
        DataDeal.TYPE_DATA_ALLOWED = {'csv':self.__caseCSV,
                                      'xlsx':self.__caseXLSX,
                                      'json':self.__caseJSON}
        self.__fileReceived = Archive(fileReceived)
        self.__dtypeToPD:dict={}


    def readFile(self):
        typeOf = self.__fileReceived.getFileType()
        
        if typeOf in DataDeal.TYPE_DATA_ALLOWED.keys():
            self.__fileReceived.setDataframe(
                DataDeal.TYPE_DATA_ALLOWED[typeOf](
                    self.__fileReceived.getDesignatedFile()
                    )
                )
            
        elif typeOf not in DataDeal.TYPE_DATA_ALLOWED.keys():
            raise KeyError('Non Allowed Extension')

    
    def __caseCSV(self, file):
        return pd.read_csv(file, dtype=self.__dtypeToPD, sep='\t') ## fazer possíveis escolhas para separador.


    def __caseXLSX(self, file):
        return pd.read_excel(file, dtype=self.__dtypeToPD)


    def __caseJSON(self, file):
        return pd.read_json(file, dtype=self.__dtypeToPD)
    
        
    def getArchive(self) -> Archive:
        return self.__fileReceived
    
    
    def setDtype(self, dtype:dict):
        self.__dtypeToPD = dtype

    