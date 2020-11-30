# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:19:30 2020

@author: tanta
"""

#1.Numpy:
    
  #- Tạo ma trận:
import numpy as np
a = np.array(([(2,3,4,5), (4,6,4,8)],
              [(2,4,6,2), (3,6,7,2)],
              [(4,6,3,2), (4,7,9,0,)]), dtype = int)
print("Ma trận A= ",a)

  #- Tính tổng 2 ma trận:
import numpy as np
a = np.array(([(2,3,5,6), (2,7,8,4)]), dtype = int)
b = np.array(([(2,9,0,1), (7,4,7,8)]), dtype = int)
print("ma trận A= ",a)
print("ma Trận B= ",b)
print("ma trận A+B= ", a+b)
  
  #- Tính tích 2 ma trận:
import numpy as np
a = np.array(([((6,8),(3,9)), ((6,3),(8,3))]), dtype = int)
b = np.array(([(5,7,3,7), (6,2,7,2)]), dtype = int)
print("ma trận C= ",a)
print("ma trận D= ",b)
print("ma trận C*D= ", a @ b)      
  
  #- tính chuyển vị ma trận:
import numpy as np
a = np.array(([(4,6,8,2),(6,3,7,2)]), dtype = int)
b = np.transpose(a)   
print("ma trận A= ", a)
print("ma trận chuyển vị of A", b)   

#2. Matplotlib:
    
  #- Đồ thị hình column:
import matplotlib.pyplot as plt 
import numpy as np  
divisions = ["Banana", "Apple", "grapes", "oranges","Dragon Fruit"]
divisions_average_marks = [80,63,72,67,90]
plt.bar(divisions, divisions_average_marks, color = 'blue')
plt.title("Trung bình mỗi người ăn hoa quả trong 1 năm")
plt.xlabel("Name hoa quả")
plt.ylabel("%")
plt.show()
  
  #- Đồ thị hình bar
import matplotlib.pyplot as plt
import numpy as np
divisions = ["iphone 12", "iphone 12 pro max", "iphone 11", "iphone 6", "iphone 5"]
division_average_marks = [70,50,60,80,40]
boys_average_marks = [60,30,59,38,56]

index = np.arange(5)
width = 0.20

plt.bar(index, division_average_marks, width, color= 'green', label= 'Việt Nam')
plt.bar(index+ width, boys_average_marks, width, color = 'red', label= 'Mỹ')
plt.ylabel("%")
plt.xlabel("Các loại iphone")
plt.xticks(index+ width/2, divisions)        
plt.legend(loc = 'best') 
plt.show()
          
  #- Đồ thị line:
import matplotlib.pyplot as plt
import numpy as np
plt.plot([3,2,3,6],[3,4,2,30])
plt.title("Biểu đồ đường")
plt.xlabel("Tỉ trọng")
plt.ylabel("Tỉ lệ %")
plt.show()

  #- Đồ thị box plot:
u = u"""index,location,price
    Apr 25,ASHEVILLE,15.0
    Apr 25,ASHEVILLE,45.0
    Apr 25,ASHEVILLE,50.0
    Apr 25,ASHEVILLE,120.0
    Apr 25,ASHEVILLE,300.0"""

import io
import pandas as pd
import matplotlib.pyplot as plt

data = io.StringIO(u)

df = pd.read_csv(data, sep=",", index_col=0)

plt.boxplot(df["price"])
plt.show()

      

      
       
      