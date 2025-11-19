from tkinter import *
import time

root = Tk()
root.title("Quicksort Visualizer")
root.geometry("650x500")
canvas = Canvas(root, width=560, height=300, bg="white")
canvas.pack(pady=20)
def draw_bars(data, colorArray):
    canvas.delete("all")
    c_height = 300
    c_width = 560
    margin = 20
    bar_width = (c_width - 2 * margin) / len(data)
    max_val = max(data)
    for i, val in enumerate(data):
        x0 = margin + i * bar_width
        y0 = c_height - (val / max_val) * (c_height - 20)
        x1 = margin + (i + 1) * bar_width - 2
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 3, y0 - 10, anchor=NW, text=str(val), font=("Arial", 9), fill="black")
    root.update()
speed = 0.2
data = []
def animate(arr, pivot_index=None, i_index=None, j_index=None, final=False):
    colors = []
    for k in range(len(arr)):
        if final:
            colors.append("green")
        elif k == pivot_index:
            colors.append("orange")
        elif k == i_index or k == j_index:
            colors.append("red")
        else:
            colors.append("gray")
    draw_bars(arr, colors)
    time.sleep(speed)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    animate(arr, pivot_index=high)
    for j in range(low, high):
        animate(arr, pivot_index=high, j_index=j)
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            animate(arr, pivot_index=high, i_index=i, j_index=j)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    animate(arr, pivot_index=i + 1)
    return i + 1
def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)
def take_input():
    global data
    text = entry.get().strip()
    if not text:
        return
    try:
        data = list(map(int, text.split()))
    except:
        entry.delete(0, END)
        entry.insert(0, "Invalid input")
        return
    draw_bars(data, ["gray"] * len(data))
def start_sort():
    global data
    if len(data) == 0:
        entry.delete(0, END)
        entry.insert(0, "Enter numbers first!")
        return
    arr_copy = data.copy    ()  
    quicksort(arr_copy, 0, len(arr_copy) - 1)
    animate(arr_copy, final=True)
input_frame = Frame(root)
input_frame.pack()
Label(input_frame, text="Enter numbers (space-separated):", font=("Arial", 12)).pack()
entry = Entry(input_frame, font=("Arial", 14), width=40)
entry.pack(pady=5)
button_frame = Frame(root)
button_frame.pack(pady=10)
Button(button_frame, text="Draw", font=("Arial", 12), command=take_input).pack(side=LEFT, padx=10)
Button(button_frame, text="Start Sort", font=("Arial", 12), command=start_sort).pack(side=LEFT, padx=10)
root.mainloop()
