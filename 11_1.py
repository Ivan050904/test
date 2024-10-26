import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import numpy as np


labels = ['Category A', 'Category B', 'Category C']
values = [30, 15, 45]

plt.bar(labels, values, color=['blue', 'green', 'red'])
plt.title('Sample Data Visualization')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()


img = Image.open("ball.jpg")

img_resized = img.resize((200, 200))

# эффект размытия
img_blurred = img_resized.filter(ImageFilter.GaussianBlur(5))
img_blurred.save("balll.png")
print('картинка изменилась')

arr = np.arange(1, 11)

sum_arr = np.sum(arr)           
mean_arr = np.mean(arr)         
squared_arr = np.square(arr)    
sqrt_arr = np.sqrt(arr)         


print("Оригинальный массив:", arr)
print("Сумма элементов:", sum_arr)
print("Среднее значение:", mean_arr)
print("Массив после возведения в квадрат:", squared_arr)
print("Квадратный корень элементов массива:", sqrt_arr)

