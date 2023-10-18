import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

datafra = pd.read_csv("./DataBS_For_Training_1/ArtcsE1.csv", encoding='utf-8')

print(datafra)

datafra = datafra.transpose()

datafra.to_csv('./DataBS_For_Training_1/ArtcsE2.csv', encoding='utf-8-sig')

### 30개 단위 데이터 크롤링 후 csv파일로 저장.
### 파일명 : ArtcsE2.csv

