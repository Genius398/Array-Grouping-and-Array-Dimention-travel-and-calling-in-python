 from tkinter import *
 root=Tk()
 root.title("Array Dimentions")
 
 root.geometry("400x400")
 label = Label(root)
 
 
 
 
 OneDimentionArray = ["John","Johnson","Edison"]
 print(OneDimentionArray[0])

 TwoDimentionArray = [["John","A"] , ["Johnson","B"] , ["Edison" , "C"]]
 print(TwoDimentionArray[0][1])
 
 ThreeDimentionArray = [[["John", "A+", "Excellent"],["James","A","Very Good"],["Thomson","B","Good"]]]
 print(ThreeDimentionArray[0][0][2])
 
 