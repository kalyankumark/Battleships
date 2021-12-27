d = { "apples" : 5, "beets" : 2, "lemons" : 1 }
keys=d.keys()
values=d.values()
# print("keys:" ,keys)
# print(values)
temp = 1
for i in d:
    temp = temp * d[i]
    print(d[i])
print(temp)
# print(sum(values))


# import operator
# def mostCommonFirstLetter(string):
#     fstd = {} # for i in string:
#     name = string.split(" ") 
#     print(name) 
#     new = [] 
#     for x in name: 
#         new.append(x[0]) 
#     print(new)
#     for i in new:
#         fstd[i]=new.count(i) 
#     print(fstd)
#     sorted_dict = dict(sorted( fstd.items(),key=operator.itemgetter(1),reverse=True))
#     print('Sorted Dictionary: ', sorted_dict)            
#     # return  list(sorted_dict.keys())[0]
#     for key, value in sorted_dict.items():
#         return key
# print(mostCommonFirstLetter("do you have a voting plan for the election happening next month?"))


# import tkinter as tk
# def draw(canvas):
#     pass
# def makeCanvas(w, h):
#     root=tk.Tk()
#     canvas=tk.Canvas(root,width=w,height=h)
#     canvas.configure(bd=0,highlightthicknes=0)
#     # canvas.create_rectangle(40,40,80,140,width=5,fill="red")
#     # canvas.create_oval(30, 80, 150, 200,width=20, fill="#FF69B4")
#     # canvas.create_rectangle(90, 70, 180, 120,width=0, fill="palegreen")
#     # canvas.create_line(200, 300, 400, 350)
#     # canvas.create_line(20, 100, 90, 300, fill="green")
#     # canvas.create_line(100, 100, 300, 300, width=5)
#     canvas.create_text(200, 200, text="Hello World!", font="Arial") 
#     canvas.create_text(100, 100, text="This is fun!", font="Times 30") 
#     canvas.create_text(300, 300, text="weewooweewoo", font="Courier 10 italic")
#     canvas.pack()
#     draw(canvas)
#     root.mainloop()
# makeCanvas(400,400)
