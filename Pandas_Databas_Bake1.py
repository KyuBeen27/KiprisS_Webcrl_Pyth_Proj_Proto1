import pandas as pd
import numpy as np
import warnings
import sys

warnings.filterwarnings('ignore')

datafra = pd.read_csv("./DataBS_For_Training_1/ArtcsE1.csv", encoding='utf-8')

print(datafra)

datafra = datafra.transpose()

datafra.to_csv('./DataBS_For_Training_1/ArtcsE2.csv', encoding='utf-8-sig')

### 30개 단위 데이터 크롤링 후 csv파일로 저장, 행렬전환 완료.
### 파일명 : ArtcsE2.csv

datafra.reset_index(inplace=True)
datafra.columns = ["Patent Summary", "Result"]
print(datafra)
datafra.to_csv('./DataBS_For_Training_1/ArtcsE33.csv', index = False, encoding='utf-8-sig')

### 인덱스 리셋 후 컬럼 인덱스 추가
### 인덱스를 제거해야할 경우 index = False를 to_csv 메서드에 추가하면 된다.



# ### 데이터 라벨링 코드 ### 기호에 따라 사용 ### 010101
# temp_list = ['거절', '등록']
# datafra.insert(2, 'Rslt_Lbl', datafra.Result.map(lambda x: temp_list.index(x)))
# datafra.to_csv('./DataBS_For_Training_1/ArtcsE44.csv', encoding='utf-8-sig')

