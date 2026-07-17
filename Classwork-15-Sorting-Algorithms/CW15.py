import random
import stddraw
from color import Color

def bubble_sort(numbers):
    n = len(numbers)
    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            if numbers[pair] > numbers[pair+1]:
                numbers[pair], numbers[pair + 1] = numbers[pair+1], numbers[pair]

def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

def draw_bars(numbers, selected=()):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n
    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(100)

def bubble_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    for sweep in range(n):
        swapped = False  
        for pair in range(0, n - 1 - sweep):
            draw_bars(numbers, selected=(pair, pair+1))
            if numbers[pair] > numbers[pair+1]:
                numbers[pair], numbers[pair + 1] = numbers[pair+1], numbers[pair]
                swapped = True 
            draw_bars(numbers, selected=(pair, pair+1))
        if not swapped:
            break  
    draw_bars(numbers)
    stddraw.show()

def insertion_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            draw_bars(numbers, selected=(j, j+1))
            numbers[j + 1] = numbers[j]
            draw_bars(numbers, selected=(j, j+1))
            j -= 1 
        numbers[j + 1] = key    
    draw_bars(numbers)
    stddraw.show()
    
def selection_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_bars(numbers, selected=(min_idx, j))
            if numbers[j] < numbers[min_idx]:
                min_idx = j  
        if min_idx != i:
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]      
    draw_bars(numbers)
    stddraw.show()
    
numbers = [random.randint(5, 95) for _ in range(15)]
print(f"Original: {numbers}")

#Seleccion  de animaccion
#selection_sort_animated(numbers)
#insertion_sort_animated(numbers)
bubble_sort_animated(numbers)