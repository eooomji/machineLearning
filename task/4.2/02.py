import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

HorsePower = pd.Series([130, 250, 190, 300, 210, 220, 170])
Weight = pd.Series([1900, 2600, 2200, 2900, 2400, 2300, 2100])
Efficiency = pd.Series([16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2])

PCC = pd.DataFrame({'horsePower' : HorsePower, 'weight' : Weight ,'efficiency' : Efficiency})

x = PCC[['horsePower', 'weight']].to_numpy()
y = PCC['efficiency'].to_numpy()

LR = LinearRegression()
result = LR.fit(x,y)
print('계수 :', result.coef_)
print('절편 :', result.intercept_)
print('예측 점수 :', result.score(x,y))

## y = w1*x1 + w2*x2 + b
w1 = result.coef_[0]
w2 = result.coef_[1]
x1 = 270
x2 = 2500
b = result.intercept_

predict_score = w1*x1 + w2*x2 + b

print('270 마력 2500kg 자동차의 예상 연비 : {:.2f}'.format(float(predict_score)), 'km/l')
