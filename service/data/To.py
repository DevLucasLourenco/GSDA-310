import locale
import pandas as pd
from typing import Literal
from datetime import datetime


class To:
    """Once changed, you cannot change the same Key"""
    
    LANG:str=''
    
    @staticmethod
    def languageTo(langTo:Literal['pt_BR', 'es_ES', 'en_US', 'fr_FR']):
        To.LANG = langTo
    
    @staticmethod
    def __applyLang():
        if To.LANG:
            locale.setlocale(locale.LC_TIME, To.LANG)
    
    @staticmethod
    def Date():
        To.__applyLang()
        return _Date()
    
    @staticmethod    
    def Hour():
        To.__applyLang()
        return _Hour()
    
    @staticmethod
    def Money():
        To.__applyLang()
        return _Money()



class _Date():
    
    @staticmethod
    def to_dd_mm(OBJECT:pd.Timestamp):
        'dd/m'
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%d/%m')  
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")
    
    @staticmethod
    def to_dd_MM(OBJECT:pd.Timestamp):
        'dd/M'
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%d/%B')  
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")
    
    @staticmethod
    def to_MM_yy(OBJECT:pd.Timestamp):
        'MM/y'  
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%B/%y')  
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")
    
    @staticmethod
    def to_MM_yyyy(OBJECT:pd.Timestamp):
        'MM/Y'  
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%B/%Y')  
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")
    
    @staticmethod
    def to_dd_mm_yy(OBJECT:pd.Timestamp):
        'dd/mm/yy'
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%d/%m/%y')
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")
    
    @staticmethod
    def to_dd_MM_yyyy(OBJECT:pd.Timestamp):
        'dd/MM/yyyy'
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%d/%B/%Y')
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")

    @staticmethod
    def to_dd_mm_yyyy(OBJECT:pd.Timestamp):
        'dd/mm/yyyy'
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%d/%m/%Y')
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")

    @staticmethod
    def to_mm_dd_yyyy(OBJECT:pd.Timestamp):
        'mm/dd/yyyy'
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%m/%d/%Y')
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")

    @staticmethod
    def to_yyyy_mm_dd(OBJECT:pd.Timestamp):
        'yyyy-mm-dd'
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%Y-%m-%d')
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")

    @staticmethod
    def to_full_date(OBJECT:pd.Timestamp):
        "Full Date - DayWeek, Day Month Year"
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%A, %d %B %Y').title()
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")

    @staticmethod
    def to_dd_MM_yyyy_in_full(OBJECT:pd.Timestamp):
        "dd MM yyyy"
        if isinstance(OBJECT, pd.Timestamp):
            return OBJECT.strftime('%d %B %Y').title()
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")

    @staticmethod
    def to_personalizedFormat(OBJECT:pd.Timestamp, formatPersonalized:str):
        """Personalized\n\nUse Datetime format. (e.g.: '%d/%B/%Y')\n\nTo use this feature, you must have to follow this logic, e.g.:\n\n
        handler = DataHandler (r'example.xlsx')\n
        handler.getArchive().changeType(keyColumn="NAME", funcProvided=lambda x: To.Date().to_personalizedFormat(x, '%d de %B de %Y'))"""
        
        if isinstance(OBJECT, pd.Timestamp):
            if isinstance(formatPersonalized, str):
                return OBJECT.strftime(formatPersonalized)
            else:
                raise TypeError("Only str is allowed.")
        raise TypeError("Type Non Allowed. Only pd.Timestamp (e.g.: Timestamp('2024-01-01 00:00:00'))")
        
    
class _Hour:
    
    @staticmethod
    def to_hh_mm_ss(OBJECT:datetime):
        'HH:MM:SS'
        try:
           return OBJECT.strftime('%H:%M:%S')
        except Exception as e:
            raise TypeError("Type Non Allowed. Only datetime (e.g.: datetime.time(11, 30))")

    @staticmethod
    def to_hh_mm(OBJECT:datetime):
        'HH:MM'
        try:
           return OBJECT.strftime('%H:%M')
        except Exception as e:
            raise TypeError("Type Non Allowed. Only datetime (e.g.: datetime.time(11, 30))")

    @staticmethod
    def to_12_hour_format(OBJECT:datetime):
        'HH:MM AM/PM'
        try:
           return OBJECT.strftime('%I:%M %p')
        except Exception as e:
            raise TypeError("Type Non Allowed. Only datetime (e.g.: datetime.time(11, 30))")

    @staticmethod
    def to_24_hour_format(OBJECT:datetime):
        'HH:MM'
        try:
           return OBJECT.strftime('%H:%M')
        except Exception as e:
            raise TypeError("Type Non Allowed. Only datetime (e.g.: datetime.time(11, 30))")



class _Money:
    
    @staticmethod
    def to_dollars(OBJECT:float):
        if isinstance(OBJECT, float) or isinstance(OBJECT, int): 
            return f"$ {float(OBJECT):,.2f}"
        raise TypeError("Type Non Allowed. Only float or int")
    
    @staticmethod
    def to_euros(OBJECT:float):
        if isinstance(OBJECT, float) or isinstance(OBJECT, int): 
            return f"€ {float(OBJECT):_.2f}".replace('.',',').replace("_",".")
        raise TypeError("Type Non Allowed. Only float or int")
    
    @staticmethod
    def to_pounds(OBJECT:float):
        if isinstance(OBJECT, float) or isinstance(OBJECT, int): 
            return f"£ {float(OBJECT):,.2f}"
        raise TypeError("Type Non Allowed. Only float or int")

    @staticmethod
    def to_brl(OBJECT:float):
        if isinstance(OBJECT, float) or isinstance(OBJECT, int): 
            return f"R$ {float(OBJECT):_.2f}".replace('.',',').replace("_",".")
        raise TypeError("Type Non Allowed. Only float or int")
