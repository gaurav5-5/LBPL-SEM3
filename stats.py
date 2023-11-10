import numpy as np
import pandas as pd

class statistical_data:
    '''Class for returning statistical data when required'''

    __data : pd.core.frame.DataFrame
    
    def __init__(self, dataset):
        self.__data = dataset.copy()

    def mean(self, x:str='', f:str='') -> float:
        
        ret:float = 0.0
        
        if x and f:
            ret = np.sum(np.multiply(self.__data[x], self.__data[f]))/np.sum(self.__data[f])
        elif x:
            ret = np.sum(self.__data[x])/len(self.__data[x])

        return ret

    def std_deviation(self, x:str, f:str='', n:int=-1) -> float:
        ret = 0.0
        df = pd.DataFrame()

        if n < 0 and f:
            df = self.__data[[x,f]].copy()
            n = np.sum(df[f])
            x_mean = self.mean(x, f)
        else:
            df = self.__data[[x]].copy()
            x_mean = self.mean(x)
            if n < 0:
                n = len(df[x])

        df['x_mean'] = df[x].apply(lambda x: (x-x_mean)*(x-x_mean))
        ret = np.sqrt([(1.0/n) * np.sum(df['x_mean'])])[0]
        return ret

    def cov(self, x:str, y:str, n:int=-1, fx:str='', fy:str='') -> float:
        df = self.__data[[x,f]].copy()

        if not (fx and fy) and n > 0:
            x_mean = self.mean(x)
            y_mean = self.mean(y)
        elif fx and fy:
            x_mean = self.mean(x, fx)
            y_mean = self.mean(y, fy)

        
        
            
class_test = statistical_data(pd.DataFrame({'a' : [1,2,3,4,5], 'b': [6,7,8,9,0]}))
print(class_test.mean('a', 'b'))
print(class_test.std_deviation('a', 'b'))