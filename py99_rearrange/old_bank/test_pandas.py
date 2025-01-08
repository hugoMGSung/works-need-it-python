'''
판다스 예제 소스
1. 필요라이브러리 설치
pip install pandas

'''
import pandas as pd

def azureml_main(dataframe1 = None, dataframe2 = None):

    # Execution logic goes here
    print('Input pandas.DataFrame #1:\r\n\r\n{0}'.format(dataframe1))

    windowSize = 120    # 표준분포 데이터 샘플크기
    multiplier = 3      # 3배의 sigma
    rollingstd = pd.r
    rollingstd = pd.rolling_std(dataframe1.Temperature, window=windowSize) # 주어진 샘플을 바탕으로 분산 계산
    rollingmean = pd.rolling_mean(dataframe1.Temperature, windows=windowSize)  # 기대값 계산
    
    ucl = rollingmean + multiplier*rollingstd
    lcl = rollingmean - multiplier*rollingstd  # 이상 온도 구간이 아닌 부분을 계산
    
    # 온도의 이상여부 표기
    dataframe1["Alert"] = (dataframe1.Temperature > ucl) | (dataframe1.Temperature < lcl) 
    
    return dataframe1,