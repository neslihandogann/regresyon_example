# -*- coding: utf-8 -*-
"""lineerregresyon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o-ME2xKxfc_W_s-BetvkKp5Qyp8YWHU-

**Veri Seti Adı**

**STUDY HOURS ***

Link :https://www.kaggle.com/datasets/himanshunakrani/student-study-hours?resource=download

***PROBLEM VE ÇÖZÜM***

Study Hours Veri seti, öğrencinin çalıştığı saat sayısı ve aldığı notlar olmak üzere iki sütun içerir. Öğrencinin çalışma saati sayısı verilen notlarını tahmin etmek için basit doğrusal regresyon uygulayacağız.
Amaç, bir öğrencinin ders çalışma saatlerine göre puanını tahmin etmektir.

**Kütüphaneler**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np # matematiksel işlemler (lineer cebir vs)
import pandas as pd # veriyi işlemede, CSV dosyası için (e.g. pd.read_csv)
import matplotlib.pyplot as plt # veriyi görselleştirme
import seaborn as sns # veriyi görselleştirme

# Sklearn  kütüphaneleri
import sklearn.model_selection
import sklearn.linear_model
import sklearn.metrics
# %matplotlib inline

import warnings
warnings.filterwarnings('ignore')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv('score.csv')#veri setini ekleme işleme yapıldı

df.head()#her zaman il beş değeri gösterir

df.isnull().sum()

df.shape #df’in satır ve sütun sayısını öğrenemek için kullanılır

df.info()#Bu yöntem, dizin türü ve sütunlar, boş olmayan değerler ve bellek kullanımı dahil olmak üzere bir DataFrame hakkında bilgi yazdırır.

df.describe().transpose() #describe() metodu sayısal verilere sahip olan sütunların max, min , std vb gibi istatiksel değerlerini döndürür.

"""

```
# count - Boş olmayan değerlerin sayısı.
ortalama - Ortalama (ortalama) değer.
std - Standart sapma.
min - minimum değer.
%25 - %25 yüzdelik dilimi*.
%50 - %50 yüzdelik dilimi*.
%75 - %75 yüzdelik dilimi*.
max - maksimum değer.
```


"""

plt.figure(figsize = (12, 6))
sns.set_style("dark")
sns.scatterplot(x = df['Hours'], y = df['Scores'], color = "blue")
plt.xlabel("Ders saatleri")
plt.ylabel("Ogrenci notlari")
plt.title("ders saatleri ve ogrenci notlari")

plt.show()

sns.pairplot(df)
plt.show() #Pair Plot. pairplot(), tüm veri çerçevesi boyunca, sayısal sütunlar için çift yönlü ilişkiler çizer.

korolesyon = df.corr()
sns.heatmap(korolesyon,annot=True)
plt.title("Değişkenler Arası Korelasyon")

x = df["Hours"]
y = df["Scores"]

x.head()

y.head()

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y,train_size=0.8,random_state =42)
print(x_train.head())

x

y

print(y_train.head())

model=LinearRegression()

help(model.fit)

print('x_train.shape:',x_train.shape)
print('y_train.shape: ',y_train.shape)

model.fit(x_train, y_train)

model.fit(x_train.values.reshape(-1,1), y_train.values.reshape(-1,1))

print("modelin katsayısı: ",model.coef_)
print("modelin kesişimi: ", model.intercept_)

model.coef_,model.intercept_ #beta1,beta0 ,x in baş katsayılarını dizi türünde gösterimini sağlar

print("kurulan regresyon modeli Y={} + {}*x".format(model.intercept_[0].round(2),model.coef_[0][0].round(2)))
#temel mantık aslında y=b+ax o da şu şekilde y = beta0 + beta1* x

# Model Optimizasyonu yani tahmini
y_pred = model.predict(x_test)

print(y_pred)

x_test

for i in range(len(y_test)):
    print("gerçek değer:", float(y_test.values[i]), "- tahmini değer:", float(y_pred[i]))

plt.scatter(x_train, y_train, color = "red")
plt.plot(x_train, model.predict(x_train), color = "blue")
plt.title("Study Hours")
plt.xlabel("ders saatleri")
plt.ylabel("öğrenci notları")
plt.show()

y_pred = model.predict(x.values.reshape(-1,1))

r2_score(y,y_pred)

df=pd.DataFrame({'y':y.values.flatten(),'y_pred':y_pred.flatten()})

mean_squared_error(y,y_pred,squared=False)

mean_absolute_error(y,y_pred)

pred_dict = {"Linear": y_pred, }
print(pred_dict)

b0=model.intercept_[0].round(2)
b1=model.coef_[0][0].round(2)

random_x=np.array([0,1])
plt.plot(random_x,b0+b1*random_x, color='red' ,label='lineer regresyon')
plt.scatter(x.values,y.values)
plt.legend()
plt.xlabel("ders saatleri")
plt.ylabel("öğrenci notları")
plt.title("ders saatleri ve öğrenci notları arasındaki regresyon")