from dataclasses import dataclass
from tkinter import E
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from ScrappingPageResponsive_GUI import Ui_ScrappingWindow 
import pandas as pd
import sys
import numpy as np
import time
import csv
from csv import writer
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class artPieces:

        def __init__(self, Name, Width, Height, Depth, Artist, Country, Price, Category):
                self.Name = Name
                self.Width = Width
                self.Height = Height
                self.Depth = Depth
                self.Artist = Artist
                self.Country = Country
                self.Price = Price 
                self.Category = Category


class Ui_MainWindow(object):

    dataList = []
    searchList = []

    def openScrappingWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ScrappingWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def importData(self):
        self.dataList.clear()
        df = pd.read_csv(r'C:\Users\amnai\Documents\GitHub\cs261f22pid40\BackEndCode\Scrapping\DigitalsData.csv')

        df.fillna('', inplace = True)
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)

        # for row in df.iterrows():
        #         values = row[1]
        #         for col, value in enumerate(values):
        #                 # if isinstance(value, (float, int)):
        #                 #         value = '{0:0,.0f}'.format(value)
        #                 tableItem = QTableWidgetItem(str(value))
        #                 self.table.setItem(row[0], col, tableItem)

        List = df.values.tolist()
        for i in range(0, len(List)):
                s = List[i][6].replace("$", "")
                s = s.replace(",", "")
                s = s.replace(".", "")
                x = int(s)
                self.dataList.append(artPieces(List[i][0], List[i][1], List[i][2], List[i][3], List[i][4], List[i][5], x, List[i][7]))


        self.reloadSortedListIntoTable()

        # for i in range(len(self.dataList)):
        #         print(type(self.dataList[i].Heigth))


    def reloadSortedListIntoTable(self):
        List = [[0 for i in range(8)] for j in range(len(self.dataList))]

        for i in range(0, len(self.dataList)):
                List[i][0] = self.dataList[i].Name
                List[i][1] = self.dataList[i].Width
                List[i][2] = self.dataList[i].Height
                List[i][3] = self.dataList[i].Depth
                List[i][4] = self.dataList[i].Artist
                List[i][5] = self.dataList[i].Country
                List[i][6] = self.dataList[i].Price
                List[i][7] = self.dataList[i].Category

        self.table.setRowCount(len(List))
        self.table.setColumnCount(len(List[0]))

        for row in range(len(List)):
                for col in range(len(List[0])):
                        tableItem = QTableWidgetItem(str(List[row][col]))
                        self.table.setItem(row, col, tableItem)

    def reloadSearchList(self):
        
        List = [[0 for i in range(8)] for j in range(len(self.searchList))]

        for i in range(0, len(self.searchList)):
                List[i][0] = self.searchList[i].Name
                List[i][1] = self.searchList[i].Width
                List[i][2] = self.searchList[i].Height
                List[i][3] = self.searchList[i].Depth
                List[i][4] = self.searchList[i].Artist
                List[i][5] = self.searchList[i].Country
                List[i][6] = self.searchList[i].Price
                List[i][7] = self.searchList[i].Category

        self.table.setRowCount(len(List))
        self.table.setColumnCount(len(List[0]))

        for row in range(len(List)):
                for col in range(len(List[0])):
                        tableItem = QTableWidgetItem(str(List[row][col]))
                        self.table.setItem(row, col, tableItem)


    def doSorting(self):
        algorithm = self.comboBoxSorting.currentText()
        column = self.comboBoxSortingColumn.currentText()

        if(algorithm == "Insertion Sort"): 
                start_time = time.time()
                self.InsertionSort(1, len(self.dataList), column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Merge Sort"): #setattr
                start_time = time.time()
                self.MergeSort(0, len(self.dataList) - 1, column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Selection Sort"):
                start_time = time.time()
                self.SelectionSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Bubble Sort"):
                start_time = time.time()
                self.BubbleSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Heap Sort"):
                start_time = time.time()
                self.HeapSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Quick Sort"):
                start_time = time.time()
                self.QuickSort(0, len(self.dataList) - 1, column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Genome Sort"):
                start_time = time.time()
                self.GenomeSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Cocktail Sort"):
                start_time = time.time()
                self.CocktailSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Shell Sort"): #setattr
                start_time = time.time()
                self.ShellSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Tim Sort"): #insertion and merge
                start_time = time.time()
                self.TimSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))
        
        elif(algorithm == "Counting Sort"):
                B = [0 for i in range(len(self.dataList))]
                max = getattr(self.dataList[0], column)

                for i in range (len(self.dataList)):
                        if getattr(self.dataList[i], column) > max:
                                max = getattr(self.dataList[i], column) + 1 

                start_time = time.time()
                self.CountingSort(B, max, column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Bucket Sort"):
                start_time = time.time()
                self.BucketSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.BucketSort(column)
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "Radix Sort"):
                start_time = time.time()
                self.RadixSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.RadixSort(column)
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))

        elif(algorithm == "PigeonHole Sort"): 
                start_time = time.time()
                self.PigeonHoleSort(column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSortedListIntoTable()
                self.txtTime.setText(str(run_time))


    def Search(self):
        #self.searchList.clear()
        search = self.txtSearch.text()
        column = self.comboBoxSearchingColumn.currentText()
        searchAlgorithm = self.comboBoxSearching.currentText()

        if (searchAlgorithm == "Linear Search"):
                start_time = time.time()
                self.LinearSearch(search, column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSearchList()
                self.txtTime.setText(str(run_time))

        if (searchAlgorithm == "Starting Letter"):
                start_time = time.time()
                self.StartLetterSeacrh(search, column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSearchList()
                self.txtTime.setText(str(run_time))

        if (searchAlgorithm == "Middle Words"):
                start_time = time.time()
                self.MiddleWordsSearch(search, column)
                end_time = time.time()
                run_time = end_time - start_time
                self.reloadSearchList()
                self.txtTime.setText(str(run_time))
        

    def InsertionSort(self, p, r, column):
        i = 0
        key = 0

        for j in range(p, r):
                key = getattr(self.dataList[j], column)
                temp = self.dataList[j]
                i = j - 1
                
                while i >= 0 and getattr(self.dataList[i], column) > key:
                        temp = self.dataList[i + 1]
                        self.dataList[i + 1] = self.dataList[i]
                        i = i - 1 
                        self.dataList[i + 1] = temp


    def MergeSort(self, p, r, column):
        
        if p < r:
                q = int((p + r) / 2)
                self.MergeSort(p, q, column)
                self.MergeSort(q + 1, r, column)
                self.Merge(p, q, r, column)
    
    
    def Merge(self, p, q, r, column):
        n1 = q - p + 1
        n2 = r - q

        left_array = []
        right_array = []
        
        for i in range(n1):
                left_array.append(self.dataList[p + i])

        for j in range(n2):
                right_array.append(self.dataList[q + j + 1])

        x = artPieces(sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize)
        left_array.append(x)
        right_array.append(x)
        
        i = 0
        j = 0
        
        for k in range (p, r + 1):
                if getattr(left_array[i], column) < getattr(right_array[j], column):
                        self.dataList[k] = left_array[i]
                        i = i + 1
                else:
                        self.dataList[k] = right_array[j]
                        j = j + 1 


    def SelectionSort(self, column):
        start = 0
        end = len(self.dataList) - 1
        length = (end - start) + 1
        
        for i in range(length):
                min = i
                
                for j in range(i + 1, length):
                
                        if getattr(self.dataList[j], column) < getattr(self.dataList[min], column):
                                min = j
                                
                (self.dataList[i], self.dataList[min]) = (self.dataList[min], self.dataList[i])


    def BubbleSort(self, column):
        start = 0
        end = len(self.dataList) - 1
    
        for i in range(start, end):
                
                for j in range(start, end):
                
                        if getattr(self.dataList[j], column) > getattr(self.dataList[j + 1], column):
                                (self.dataList[j], self.dataList[j + 1]) = (self.dataList[j + 1], self.dataList[j])

    def maxHeapify(self, length, i, column):

        largest = i
        l = (2 * i) + 1
        r = (2 * i) + 2

        if l < length and getattr(self.dataList[l], column) > getattr(self.dataList[i], column):
                largest = l

        if r < length and getattr(self.dataList[r], column) > getattr(self.dataList[largest], column):
                largest = r

        if largest != i:
                (self.dataList[i], self.dataList[largest]) = (self.dataList[largest], self.dataList[i])
                self.maxHeapify(length, largest, column)

    def buildMaxHeapify(self, length, column):

        for i in range(length // 2, -1, -1):
                self.maxHeapify(length, i, column)

    def HeapSort(self, column):

        length = len(self.dataList)
        self.buildMaxHeapify(length, column)

        for i in range(length - 1, 0, -1):
                (self.dataList[i], self.dataList[0]) = (self.dataList[0], self.dataList[i])
                length = length - 1
                self.maxHeapify(i, 0, column)


    def partition(self, p, r, column):
        x = getattr(self.dataList[r], column)
        i = p - 1

        for j in range(p, r):
                if getattr(self.dataList[j], column) <= x:
                        i = i + 1
                        (self.dataList[i], self.dataList[j]) = (self.dataList[j], self.dataList[i])
        
        (self.dataList[i + 1], self.dataList[r]) = (self.dataList[r], self.dataList[i + 1])
        return i + 1


    def QuickSort(self, p, r, column):
        if p < r:
                q = self.partition(p, r, column)
                self.QuickSort(p, q - 1, column)
                self.QuickSort(q + 1, r, column)


    def GenomeSort(self, column):
        length = len(self.dataList)
        idx = 0 

        while idx < length:

                if idx == 0 or getattr(self.dataList[idx], column) >= getattr(self.dataList[idx - 1], column):
                        idx = idx + 1

                else:
                        (self.dataList[idx], self.dataList[idx - 1]) = (self.dataList[idx - 1], self.dataList[idx])
                        idx = idx - 1


    def CocktailSort(self, column):
        length = len(self.dataList)

        for i in range(length - 1, 0, -1):

                for j in range(i):
                        if getattr(self.dataList[j], column) > getattr(self.dataList[j + 1], column):
                                (self.dataList[j], self.dataList[j + 1]) = (self.dataList[j + 1], self.dataList[j])

                for j in range(i, 0, -1):
                        if getattr(self.dataList[j], column) < getattr(self.dataList[j - 1], column):
                                (self.dataList[j], self.dataList[j - 1]) = (self.dataList[j - 1], self.dataList[j]) 

    
    def ShellSort(self, column):

        gap = len(self.dataList)//2
     
        while gap>0:
                j = gap
                
                while j < len(self.dataList):
                        i = j - gap 
                        
                        while i >= 0:
                                
                                if getattr(self.dataList[i + gap], column) > getattr(self.dataList[i], column):
                                        break
                                else:
                                        self.dataList[i+gap], self.dataList[i] = self.dataList[i], self.dataList[i+gap]
                
                                i = i - gap 

                        j = j + 1
                        
                gap = gap // 2


    def TimSort(self, column):
        length = len(self.dataList)
        minRun = 32

        for p in range(0, length, minRun):
                r = min(p + minRun - 1, length -1)
                self.InsertionSort(p, r, column)

        size = minRun
        while size < length:
                for p in range(0, length, 2 * size):
                        q = min(length - 1, p + size - 1)
                        r = min((p + 2 * size - 1), (length - 1))

                        if q < r:
                                self.Merge(p, q, r, column)        

                size = 2 * size

                
    def CountingSort(self, B, max, column):

        C = []
        Result = []

        for i in range (max):
                C.append(0)

        for j in range (len(self.dataList)):
                C[getattr(self.dataList[j], column)] = C[getattr(self.dataList[j], column)] + 1

        for i in range (1, max):
                C[i] = C[i] + C[i - 1]

        for j in range (len(self.dataList), 0 , -1):
                B[(C[getattr(self.dataList[j-1], column)]) - 1] = self.dataList[j - 1]      
                C[getattr(self.dataList[j - 1], column)] = C[getattr(self.dataList[j - 1], column)] - 1

        for i in range (len(self.dataList)):
                self.dataList[i] = B[i]


    def BucketInsertionSort(self, array):
        i = 0
        key = 0

        for j in range(1, len(array)):
                key = array[j]
                i = j - 1
        
                while i >= 0 and array[i] > key:
                        array[i+1] = array[i]
                        i = i - 1 
                        array[i + 1] = key


    def BucketSort(self, column):
        B = []
        n = 10

        for i in range (n * 1000):
                B.append([])

        for i in range (n):
                B[int(n * getattr(self.dataList[i], column))].append(self.dataList[i])

        for i in range (n):
                B[i] = self.BucketInsertionSort(B[i])

        B = np.concatenate(B)
        return B 


    def RadixCountingSort(self, B, n, column):
        C = [0] * 10

        for j in range (len(self.dataList)):
                temp = getattr(self.dataList[j], column) // n
                C[temp % 10] = C[temp % 10] + 1
        print (C)

        for i in range (1, 10):
                C[i] = C[i] + C[i - 1]

        print (C)

        i = len(self.dataList) - 1
        while (i >= 0):
                temp = getattr(self.dataList[i], column) // n 
                B[C[temp % 10] - 1] = self.dataList[i] # attribute or object??
                C[temp % 10] = C[temp % 10] - 1
                i = i - 1

        for i in range (len(self.dataList)):
                self.dataList[i] = B[i] #attribute or object?
        return self.dataList


    def RadixSort(self, column):
        d = -1

        for i in range(0, len(self.dataList)):
                if d > getattr(self.dataList[i], column):
                        d = getattr(self.dataList[i], column)
                        print (d)

        B = [0 for i in range(len(self.dataList))]
        n = 1
        while (d // n > 0):
                self.dataList = self.RadixCountingSort(B, n, column) # attribute or object??
                n = n * 10


    def PigeonHoleSort(self, column):
        Smallest = 9999999999
        Largest = -1

        for i in range(0, len(self.dataList)):
                if Smallest > getattr(self.dataList[i], column):
                        Smallest = getattr(self.dataList[i], column)

        for i in range(0, len(self.dataList)):
                if Largest < getattr(self.dataList[i], column):
                        Largest = getattr(self.dataList[i], column)

        
        NumberOfHoles = Largest - Smallest + 1
        Holes = []

        for i in range (NumberOfHoles):
                Holes.append(0)

        for j in self.dataList:
                Holes[j - Smallest] = Holes[j - Smallest] + 1

        self.dataList.clear()
        for x in range (NumberOfHoles):
                while (Holes[x] > 0):
                        Holes[x] = Holes[x] - 1
                        self.dataList.append(x + Smallest)


    def LinearSearch(self, search, column):

        if column == "Width" or column == "Height" or column == "Depth":
                search = float(search)

        elif column == "Price":
                search = int(search)

        #if len(self.searchList) == 0:
        for i in range(0, len(self.dataList)):
                        if getattr(self.dataList[i], column) == search:
                                self.searchList.append(self.dataList[i])

        # elif len(self.searchList) != 0:
        #         for i in range(0, len(self.searchList)):
        #                 if getattr(self.searchList[i], column) != search:
        #                         self.searchList.remove(self.searchList[i])


    def StartLetterSeacrh(self, search, column):
        length = len(self.dataList)

        #if len(self.searchList) == 0:
        for i in range(0, length):
                if column == "Width" or column == "Height" or column == "Depth" or column == "Price":
                        attribute = getattr(self.dataList[i], column)
                        attribute = str(attribute)

                else:
                        attribute = getattr(self.dataList[i], column)

                if attribute[0] == search:
                        self.searchList.append(self.dataList[i])

        # elif len(self.searchList) != 0:
        #         for i in range(0, x):
        #                 if column == "Width" or column == "Height" or column == "Depth" or column == "Price":
        #                         attribute = getattr(self.searchList[i], column)
        #                         attribute = str(attribute)

        #                 else:
        #                         attribute = getattr(self.searchList[i], column)

        #                 if attribute[0] != search:
        #                         self.searchList.remove(self.searchList[i])


    def MiddleWordsSearch(self, search, column):

        #if len(self.searchList) == 0:
        for i in range(0, len(self.dataList)):
                
                attribute = getattr(self.dataList[i], column)
                wordList = attribute.split()

                for j in range(0, len(wordList)):
                        if wordList[j] == search:
                                self.searchList.append(self.dataList[i])

        # elif len(self.searchList) != 0:
        #         for i in range(0, len(self.searchList)):
                
        #         attribute = getattr(self.searchList[i], column)
        #         wordList = attribute.split()

        #         for j in range(0, len(wordList)):
        #                 if wordList[j] != search:
        #                         self.searchList.remove(self.searchList[i])


    def SearchPaintingsBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Category == "Paintings":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()


    def SearchPrintsBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Category == "Prints":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()


    def SearchDigitalsBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Category == "Digitals":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()


    def SearchSculpturesBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Category == "Sculptures":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()


    def SearchDrawingsBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Category == "Drawings":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()


    def SearchPhotographyBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Category == "Photography":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchUKBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "United Kingdom":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchCanadaBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Canada":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchUSBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "United States":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchFranceBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "France":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchSwedenBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Sweden":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchNetherlandsBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Netherlands":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchAustraliaBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Australia":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchGreeceBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Greece":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchSwitzerlandBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Switzerland":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchSpainBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Spain":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchMexicoBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Mexico":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchPakistanBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Pakistan":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchSABtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "South Africa":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchItalyBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Italy":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchNZBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "New Zealand":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchGermanyBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "Germany":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchIndiaBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "India":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchChinaBtn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Country == "China":
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchUnder500Btn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Price >= 0 and self.dataList[i].Price < 500:
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def Search500to1000Btn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Price >= 500 and self.dataList[i].Price < 1000:
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def Search1000to2000Btn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Price >= 1000 and self.dataList[i].Price < 2000:
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def Search2000to5000Btn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Price >= 2000 and self.dataList[i].Price < 5000:
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def Search5000to10000Btn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Price >= 5000 and self.dataList[i].Price < 10000:
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def SearchOver10000Btn(self):
                for i in range(0, len(self.dataList)):
                        if self.dataList[i].Price >= 10000:
                                self.searchList.append(self.dataList[i])
                
                self.reloadSearchList()

    def Export(self):
        info = [0] * 7

        List = [[0 for i in range(8)] for j in range(len(self.dataList))]

        for i in range(0, len(self.dataList)):
                List[i][0] = self.dataList[i].Name
                List[i][1] = self.dataList[i].Width
                List[i][2] = self.dataList[i].Height
                List[i][3] = self.dataList[i].Depth
                List[i][4] = self.dataList[i].Artist
                List[i][5] = self.dataList[i].Country
                List[i][6] = self.dataList[i].Price
                List[i][7] = self.dataList[i].Category

        with open('ExportFile.csv', "w", encoding='utf8', newline='') as f:
    
                thewriter =  writer(f)
                header = ['Name', 'Width', 'Height', 'Depth', 'Painter', 'Country','Price', 'Category']
                thewriter.writerow(header)

                for row in range(len(List)):
                        for col in range(len(List[0])):
                                info[col] = QTableWidgetItem(str(List[row][col]))

                        thewriter.writerow(info)
                        info.clear()


        self.dataList.clear()
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 850)
        MainWindow.setMinimumSize(QtCore.QSize(550, 100))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -215, 826, 1412))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 95))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 95))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 71))
        self.label_2.setStyleSheet("background-image:url(:/resource/graphics/Auction.jpg)")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/resource/graphics/Auction.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(110, 10, 441, 41))
        self.label.setStyleSheet("font: 20pt \"MS Reference Sans Serif\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(110, 50, 671, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"color:rgb(217, 145, 0)")
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 31, 31))
        self.pushButton.setStyleSheet("background-image:url(:/newPrefix/Downloads/P19.png)")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Downloads/P19.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 190))
        self.frame_3.setStyleSheet("background-color:rgb(225, 198, 129)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line = QtWidgets.QFrame(self.frame_4)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMinimumSize(QtCore.QSize(190, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(175, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 141, 31))
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setGeometry(QtCore.QRect(40, 50, 141, 16))
        self.label_5.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.label_13 = QtWidgets.QLabel(self.frame_7)
        self.label_13.setGeometry(QtCore.QRect(30, 70, 161, 21))
        self.label_13.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.frame_7)
        self.label_15.setGeometry(QtCore.QRect(20, 90, 171, 21))
        self.label_15.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.label_15.setObjectName("label_15")
        self.btnScrappingWindow = QtWidgets.QPushButton(self.frame_7, clicked = lambda: self.openScrappingWindow())
        self.btnScrappingWindow.setGeometry(QtCore.QRect(20, 120, 151, 31))
        self.btnScrappingWindow.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnScrappingWindow.setFont(font)
        self.btnScrappingWindow.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}")
        self.btnScrappingWindow.setAutoDefault(False)
        self.btnScrappingWindow.setDefault(False)
        self.btnScrappingWindow.setFlat(True)
        self.btnScrappingWindow.setObjectName("btnScrappingWindow")
        self.horizontalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMinimumSize(QtCore.QSize(550, 100))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setStyleSheet("background-image:url(:/resource/graphics/P12.jpg)")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/resource/graphics/P12.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setStyleSheet("background-image:url(:/resource/graphics/P5.jpg)")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/resource/graphics/P5.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        self.label_8.setStyleSheet("background-image:url(:/resource/graphics/P41.jpg)")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/resource/graphics/P41.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        self.label_9.setStyleSheet("background-image:url(:/resource/graphics/P8.jpg)")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/resource/graphics/P8.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_9)
        self.label_10.setStyleSheet("background-image:url(:/resource/graphics/P14.jpg)")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/resource/graphics/P14.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.frame_9)
        self.label_11.setStyleSheet("background-image:url(:/resource/graphics/P11.jpg)")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/resource/graphics/P11.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnPaintings = QtWidgets.QPushButton(self.frame_10, clicked = lambda: self.SearchPaintingsBtn())
        self.btnPaintings.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnPaintings.setFont(font)
        self.btnPaintings.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}")
        self.btnPaintings.setFlat(True)
        self.btnPaintings.setObjectName("btnPaintings")
        self.horizontalLayout_3.addWidget(self.btnPaintings)
        self.btnPrints = QtWidgets.QPushButton(self.frame_10, clicked = lambda: self.SearchPrintsBtn())
        self.btnPrints.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnPrints.setFont(font)
        self.btnPrints.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}")
        self.btnPrints.setFlat(True)
        self.btnPrints.setObjectName("btnPrints")
        self.horizontalLayout_3.addWidget(self.btnPrints)
        self.btnPhotography = QtWidgets.QPushButton(self.frame_10, clicked = lambda: self.SearchPhotographyBtn())
        self.btnPhotography.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnPhotography.setFont(font)
        self.btnPhotography.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}")
        self.btnPhotography.setFlat(True)
        self.btnPhotography.setObjectName("btnPhotography")
        self.horizontalLayout_3.addWidget(self.btnPhotography)
        self.btnDigitals = QtWidgets.QPushButton(self.frame_10, clicked = lambda: self.SearchDigitalsBtn())
        self.btnDigitals.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnDigitals.setFont(font)
        self.btnDigitals.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}")
        self.btnDigitals.setFlat(True)
        self.btnDigitals.setObjectName("btnDigitals")
        self.horizontalLayout_3.addWidget(self.btnDigitals)
        self.btnSculptures = QtWidgets.QPushButton(self.frame_10, clicked = lambda: self.SearchSculpturesBtn())
        self.btnSculptures.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnSculptures.setFont(font)
        self.btnSculptures.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}")
        self.btnSculptures.setFlat(True)
        self.btnSculptures.setObjectName("btnSculptures")
        self.horizontalLayout_3.addWidget(self.btnSculptures)
        self.btnDrawings = QtWidgets.QPushButton(self.frame_10, clicked = lambda: self.SearchDrawingsBtn())
        self.btnDrawings.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnDrawings.setFont(font)
        self.btnDrawings.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}")
        self.btnDrawings.setFlat(True)
        self.btnDrawings.setObjectName("btnDrawings")
        self.horizontalLayout_3.addWidget(self.btnDrawings)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.horizontalLayout.addWidget(self.frame_8)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 40, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_11.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(225, 198, 129);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_13.addWidget(self.label_17)
        self.verticalLayout_7.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_11)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_2 = QtWidgets.QFrame(self.frame_14)
        self.line_2.setMinimumSize(QtCore.QSize(0, 0))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.verticalLayout_7.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_11)
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(225, 198, 129);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_14.addWidget(self.label_14)
        self.verticalLayout_7.addWidget(self.frame_15)
        self.frame_18 = QtWidgets.QFrame(self.frame_11)
        self.frame_18.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btnUnder500 = QtWidgets.QPushButton(self.frame_18, clicked = lambda: self.SearchUnder500Btn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnUnder500.setFont(font)
        self.btnUnder500.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnUnder500.setFlat(True)
        self.btnUnder500.setObjectName("btnUnder500")
        self.verticalLayout_9.addWidget(self.btnUnder500)
        self.btn500to1000 = QtWidgets.QPushButton(self.frame_18, clicked = lambda: self.Search500to1000Btn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btn500to1000.setFont(font)
        self.btn500to1000.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btn500to1000.setFlat(True)
        self.btn500to1000.setObjectName("btn500to1000")
        self.verticalLayout_9.addWidget(self.btn500to1000)
        self.btn1000to2000 = QtWidgets.QPushButton(self.frame_18, clicked = lambda: self.Search1000to2000Btn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btn1000to2000.setFont(font)
        self.btn1000to2000.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btn1000to2000.setFlat(True)
        self.btn1000to2000.setObjectName("btn1000to2000")
        self.verticalLayout_9.addWidget(self.btn1000to2000)
        self.btn2000to5000 = QtWidgets.QPushButton(self.frame_18, clicked = lambda: self.Search2000to5000Btn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btn2000to5000.setFont(font)
        self.btn2000to5000.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btn2000to5000.setFlat(True)
        self.btn2000to5000.setObjectName("btn2000to5000")
        self.verticalLayout_9.addWidget(self.btn2000to5000)
        self.btn5000to10000 = QtWidgets.QPushButton(self.frame_18, clicked = lambda: self.Search2000to5000Btn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btn5000to10000.setFont(font)
        self.btn5000to10000.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btn5000to10000.setFlat(True)
        self.btn5000to10000.setObjectName("btn5000to10000")
        self.verticalLayout_9.addWidget(self.btn5000to10000)
        self.btnOver10000 = QtWidgets.QPushButton(self.frame_18, clicked = lambda: self.SearchOver10000Btn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnOver10000.setFont(font)
        self.btnOver10000.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnOver10000.setFlat(True)
        self.btnOver10000.setObjectName("btnOver10000")
        self.verticalLayout_9.addWidget(self.btnOver10000)
        self.verticalLayout_7.addWidget(self.frame_18)
        self.frame_16 = QtWidgets.QFrame(self.frame_11)
        self.frame_16.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(225, 198, 129);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_15.addWidget(self.label_16)
        self.verticalLayout_7.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_11)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btnUK = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchUKBtn() )
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnUK.setFont(font)
        self.btnUK.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnUK.setFlat(True)
        self.btnUK.setObjectName("btnUK")
        self.verticalLayout_10.addWidget(self.btnUK)
        self.btnCanada = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchCanadaBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnCanada.setFont(font)
        self.btnCanada.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnCanada.setFlat(True)
        self.btnCanada.setObjectName("btnCanada")
        self.verticalLayout_10.addWidget(self.btnCanada)
        self.btnUS = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchUSBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnUS.setFont(font)
        self.btnUS.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnUS.setFlat(True)
        self.btnUS.setObjectName("btnUS")
        self.verticalLayout_10.addWidget(self.btnUS)
        self.btnFrance = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchFranceBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnFrance.setFont(font)
        self.btnFrance.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnFrance.setFlat(True)
        self.btnFrance.setObjectName("btnFrance")
        self.verticalLayout_10.addWidget(self.btnFrance)
        self.btnSweden = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchSwedenBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnSweden.setFont(font)
        self.btnSweden.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnSweden.setFlat(True)
        self.btnSweden.setObjectName("btnSweden")
        self.verticalLayout_10.addWidget(self.btnSweden)
        self.btnNetherlands = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchNetherlandsBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnNetherlands.setFont(font)
        self.btnNetherlands.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnNetherlands.setFlat(True)
        self.btnNetherlands.setObjectName("btnNetherlands")
        self.verticalLayout_10.addWidget(self.btnNetherlands)
        self.btnAustralia = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchAustraliaBtn())
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.btnAustralia.setFont(font)
        self.btnAustralia.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnAustralia.setFlat(True)
        self.btnAustralia.setObjectName("btnAustralia")
        self.verticalLayout_10.addWidget(self.btnAustralia)
        self.btnGreece = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchGreeceBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnGreece.setFont(font)
        self.btnGreece.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnGreece.setFlat(True)
        self.btnGreece.setObjectName("btnGreece")
        self.verticalLayout_10.addWidget(self.btnGreece)
        self.btnSwitzerland = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchSwitzerlandBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnSwitzerland.setFont(font)
        self.btnSwitzerland.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnSwitzerland.setFlat(True)
        self.btnSwitzerland.setObjectName("btnSwitzerland")
        self.verticalLayout_10.addWidget(self.btnSwitzerland)
        self.btnSpain = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchSpainBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnSpain.setFont(font)
        self.btnSpain.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnSpain.setFlat(True)
        self.btnSpain.setObjectName("btnSpain")
        self.verticalLayout_10.addWidget(self.btnSpain)
        self.btnMexico = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchMexicoBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnMexico.setFont(font)
        self.btnMexico.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnMexico.setFlat(True)
        self.btnMexico.setObjectName("btnMexico")
        self.verticalLayout_10.addWidget(self.btnMexico)
        self.btnPakistan = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchPakistanBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnPakistan.setFont(font)
        self.btnPakistan.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnPakistan.setFlat(True)
        self.btnPakistan.setObjectName("btnPakistan")
        self.verticalLayout_10.addWidget(self.btnPakistan)
        self.btnSouthAfrica = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchSABtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnSouthAfrica.setFont(font)
        self.btnSouthAfrica.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnSouthAfrica.setFlat(True)
        self.btnSouthAfrica.setObjectName("btnSouthAfrica")
        self.verticalLayout_10.addWidget(self.btnSouthAfrica)
        self.btnItaly = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchItalyBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnItaly.setFont(font)
        self.btnItaly.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198,129);\n"
"}")
        self.btnItaly.setFlat(True)
        self.btnItaly.setObjectName("btnItaly")
        self.verticalLayout_10.addWidget(self.btnItaly)
        self.btnNZ = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchNZBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnNZ.setFont(font)
        self.btnNZ.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnNZ.setFlat(True)
        self.btnNZ.setObjectName("btnNZ")
        self.verticalLayout_10.addWidget(self.btnNZ)
        self.btnGermany = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchGermanyBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnGermany.setFont(font)
        self.btnGermany.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnGermany.setFlat(True)
        self.btnGermany.setObjectName("btnGermany")
        self.verticalLayout_10.addWidget(self.btnGermany)
        self.btnIndia = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchIndiaBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnIndia.setFont(font)
        self.btnIndia.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnIndia.setFlat(True)
        self.btnIndia.setObjectName("btnIndia")
        self.verticalLayout_10.addWidget(self.btnIndia)
        self.btnChina = QtWidgets.QPushButton(self.frame_17, clicked = lambda: self.SearchChinaBtn())
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnChina.setFont(font)
        self.btnChina.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnChina.setFlat(True)
        self.btnChina.setObjectName("btnChina")
        self.verticalLayout_10.addWidget(self.btnChina)
        self.verticalLayout_7.addWidget(self.frame_17)
        self.horizontalLayout_4.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_19 = QtWidgets.QFrame(self.frame_12)
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_19.setStyleSheet("Qframe_19{\n"
"border-radius: 20px;\n"
"\n"
"}")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.txtSearch = QtWidgets.QLineEdit(self.frame_19)
        self.txtSearch.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.txtSearch.setFont(font)
        self.txtSearch.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(37, 39, 48);\n"
"border-radius: 15px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(217, 145, 0);\n"
"}")
        self.txtSearch.setText("")
        self.txtSearch.setObjectName("txtSearch")
        self.horizontalLayout_8.addWidget(self.txtSearch)
        self.btnSearch = QtWidgets.QPushButton(self.frame_19, clicked = lambda: self.Search())
        self.btnSearch.setAutoFillBackground(False)
        self.btnSearch.setStyleSheet("QPushButton{\n"
"background-image:url(:/resource/graphics/P19.png)\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid rgb(225, 198, 129);\n"
"}")
        self.btnSearch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resource/graphics/P19.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon1)
        self.btnSearch.setFlat(True)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout_8.addWidget(self.btnSearch)
        self.verticalLayout_11.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_12)
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.table = QtWidgets.QTableWidget(self.frame_20)
        self.table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setMidLineWidth(0)
        self.table.setRowCount(0)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.verticalLayout_12.addWidget(self.table)
        self.verticalLayout_11.addWidget(self.frame_20)
        self.frame_23 = QtWidgets.QFrame(self.frame_12)
        self.frame_23.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_33 = QtWidgets.QLabel(self.frame_23)
        self.label_33.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(225, 198, 129);")
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_5.addWidget(self.label_33)
        self.comboBoxSorting = QtWidgets.QComboBox(self.frame_23)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.comboBoxSorting.setFont(font)
        self.comboBoxSorting.setAutoFillBackground(False)
        self.comboBoxSorting.setStyleSheet("QComboBox:focus{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"font: 10pt \"MS Reference Sans Serif\";\n"
"}\n"
"QComboBox:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}\n"
"")
        self.comboBoxSorting.setCurrentText("")
        self.comboBoxSorting.setFrame(True)
        self.comboBoxSorting.setObjectName("comboBoxSorting")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.comboBoxSorting.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBoxSorting)
        self.label_35 = QtWidgets.QLabel(self.frame_23)
        self.label_35.setMinimumSize(QtCore.QSize(0, 0))
        self.label_35.setMaximumSize(QtCore.QSize(85, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(225, 198, 129);")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_5.addWidget(self.label_35)
        self.comboBoxSortingColumn = QtWidgets.QComboBox(self.frame_23)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.comboBoxSortingColumn.setFont(font)
        self.comboBoxSortingColumn.setAutoFillBackground(False)
        self.comboBoxSortingColumn.setStyleSheet("QComboBox:focus{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"font: 10pt \"MS Reference Sans Serif\";\n"
"}\n"
"QComboBox:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}")
        self.comboBoxSortingColumn.setFrame(True)
        self.comboBoxSortingColumn.setObjectName("comboBoxSortingColumn")
        self.comboBoxSortingColumn.addItem("")
        self.comboBoxSortingColumn.addItem("")
        self.comboBoxSortingColumn.addItem("")
        self.comboBoxSortingColumn.addItem("")
        self.comboBoxSortingColumn.addItem("")
        self.comboBoxSortingColumn.addItem("")
        self.comboBoxSortingColumn.addItem("")
        self.comboBoxSortingColumn.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBoxSortingColumn)
        self.btnImport = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.importData())
        self.btnImport.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnImport.setFont(font)
        self.btnImport.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198,129);\n"
"}")
        self.btnImport.setAutoDefault(True)
        self.btnImport.setDefault(False)
        self.btnImport.setFlat(False)
        self.btnImport.setObjectName("btnImport")
        self.horizontalLayout_5.addWidget(self.btnImport)
        self.verticalLayout_11.addWidget(self.frame_23)
        self.frame_21 = QtWidgets.QFrame(self.frame_12)
        self.frame_21.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_34 = QtWidgets.QLabel(self.frame_21)
        self.label_34.setMinimumSize(QtCore.QSize(0, 0))
        self.label_34.setMaximumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(225, 198, 129);")
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_7.addWidget(self.label_34)
        self.comboBoxSearching = QtWidgets.QComboBox(self.frame_21)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.comboBoxSearching.setFont(font)
        self.comboBoxSearching.setAccessibleName("")
        self.comboBoxSearching.setAccessibleDescription("")
        self.comboBoxSearching.setAutoFillBackground(False)
        self.comboBoxSearching.setStyleSheet("QComboBox:focus{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"font: 10pt \"MS Reference Sans Serif\";\n"
"}\n"
"QComboBox:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}\n"
"\n"
"")
        self.comboBoxSearching.setCurrentText("")
        self.comboBoxSearching.setFrame(True)
        self.comboBoxSearching.setObjectName("comboBoxSearching")
        self.comboBoxSearching.addItem("")
        self.comboBoxSearching.addItem("")
        self.comboBoxSearching.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBoxSearching)
        self.label_36 = QtWidgets.QLabel(self.frame_21)
        self.label_36.setMaximumSize(QtCore.QSize(85, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(225, 198, 129);")
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_7.addWidget(self.label_36)
        self.comboBoxSearchingColumn = QtWidgets.QComboBox(self.frame_21)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.comboBoxSearchingColumn.setFont(font)
        self.comboBoxSearchingColumn.setAutoFillBackground(False)
        self.comboBoxSearchingColumn.setStyleSheet("QComboBox:focus{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"font: 10pt \"MS Reference Sans Serif\";\n"
"}\n"
"QComboBox:hover{\n"
"border: 2px solid rgb(217, 145, 48);\n"
"}")
        self.comboBoxSearchingColumn.setFrame(True)
        self.comboBoxSearchingColumn.setObjectName("comboBoxSearchingColumn")
        self.comboBoxSearchingColumn.addItem("")
        self.comboBoxSearchingColumn.addItem("")
        self.comboBoxSearchingColumn.addItem("")
        self.comboBoxSearchingColumn.addItem("")
        self.comboBoxSearchingColumn.addItem("")
        self.comboBoxSearchingColumn.addItem("")
        self.comboBoxSearchingColumn.addItem("")
        self.comboBoxSearchingColumn.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBoxSearchingColumn)
        self.btnSearch_2 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.Export())
        self.btnSearch_2.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.btnSearch_2.setFont(font)
        self.btnSearch_2.setStyleSheet("QPushButton:hover{\n"
"border: 2px solid rgb(225, 198,129);\n"
"}")
        self.btnSearch_2.setAutoDefault(True)
        self.btnSearch_2.setDefault(False)
        self.btnSearch_2.setFlat(False)
        self.btnSearch_2.setObjectName("btnSearch_2")
        self.horizontalLayout_7.addWidget(self.btnSearch_2)
        self.verticalLayout_11.addWidget(self.frame_21)
        self.frame_22 = QtWidgets.QFrame(self.frame_12)
        self.frame_22.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_31 = QtWidgets.QLabel(self.frame_22)
        self.label_31.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_6.addWidget(self.label_31)
        self.txtTime = QtWidgets.QLineEdit(self.frame_22)
        self.txtTime.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.txtTime.setFont(font)
        self.txtTime.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(37, 39, 48);\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(217, 145, 0);\n"
"}")
        self.txtTime.setReadOnly(True)
        self.txtTime.setPlaceholderText("")
        self.txtTime.setObjectName("txtTime")
        self.horizontalLayout_6.addWidget(self.txtTime)
        self.verticalLayout_11.addWidget(self.frame_22)
        self.horizontalLayout_4.addWidget(self.frame_12)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBoxSorting.setCurrentIndex(-1)
        self.comboBoxSortingColumn.setCurrentIndex(0)
        self.comboBoxSearching.setCurrentIndex(-1)
        self.comboBoxSearchingColumn.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBoxSorting.activated.connect(self.doSorting)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mystical Creations"))
        self.label.setText(_translate("MainWindow", "MYSTICAL CREATIONS"))
        self.label_3.setText(_translate("MainWindow", "WORLD\'S VERY FIRST ART EXHIBIT WITH THE FINEST PAINTINGS FROM AROUND THE GLOBE"))
        self.label_4.setText(_translate("MainWindow", "ARTWORKS"))
        self.label_5.setText(_translate("MainWindow", "  Art Collections"))
        self.label_13.setToolTip(_translate("MainWindow", "<html><head/><body><p>Over more than 136,000 </p><p>original art pieces available</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Over more than 136,000"))
        self.label_15.setToolTip(_translate("MainWindow", "<html><head/><body><p>Over more than 136,000 </p><p>original art pieces available</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "original art pieces available"))
        self.btnScrappingWindow.setText(_translate("MainWindow", "Scrapping Window"))
        self.btnPaintings.setText(_translate("MainWindow", "Paintings"))
        self.btnPrints.setText(_translate("MainWindow", "Prints"))
        self.btnPhotography.setText(_translate("MainWindow", "Photography"))
        self.btnDigitals.setText(_translate("MainWindow", "Digitals"))
        self.btnSculptures.setText(_translate("MainWindow", "Sculptures"))
        self.btnDrawings.setText(_translate("MainWindow", "Drawings"))
        self.label_17.setText(_translate("MainWindow", "           FILTERS"))
        self.label_14.setText(_translate("MainWindow", "                PRICE "))
        self.btnUnder500.setText(_translate("MainWindow", "Under $500 "))
        self.btn500to1000.setText(_translate("MainWindow", "$500 - $1,000"))
        self.btn1000to2000.setText(_translate("MainWindow", "$1,000 - $2,000"))
        self.btn2000to5000.setText(_translate("MainWindow", "$2,000 - $5,000"))
        self.btn5000to10000.setText(_translate("MainWindow", "$5,000 - $10,000"))
        self.btnOver10000.setText(_translate("MainWindow", "Over $10,000"))
        self.label_16.setText(_translate("MainWindow", "             COUNTRY"))
        self.btnUK.setText(_translate("MainWindow", "United Kingdom"))
        self.btnCanada.setText(_translate("MainWindow", "Canada"))
        self.btnUS.setText(_translate("MainWindow", " United States "))
        self.btnFrance.setText(_translate("MainWindow", "France"))
        self.btnSweden.setText(_translate("MainWindow", "Sweden"))
        self.btnNetherlands.setText(_translate("MainWindow", "Netherlands"))
        self.btnAustralia.setText(_translate("MainWindow", "Australia"))
        self.btnGreece.setText(_translate("MainWindow", "Greece"))
        self.btnSwitzerland.setText(_translate("MainWindow", "Switzerland"))
        self.btnSpain.setText(_translate("MainWindow", "Spain"))
        self.btnMexico.setText(_translate("MainWindow", "Mexico"))
        self.btnPakistan.setText(_translate("MainWindow", "Pakistan"))
        self.btnSouthAfrica.setText(_translate("MainWindow", "South Africa"))
        self.btnItaly.setText(_translate("MainWindow", "Italy"))
        self.btnNZ.setText(_translate("MainWindow", "New Zealand"))
        self.btnGermany.setText(_translate("MainWindow", "Germany"))
        self.btnIndia.setText(_translate("MainWindow", "India"))
        self.btnChina.setText(_translate("MainWindow", "China"))
        self.txtSearch.setPlaceholderText(_translate("MainWindow", "Search out your Heart "))
        self.label_33.setText(_translate("MainWindow", "Sorting Algorithms"))
        self.comboBoxSorting.setItemText(0, _translate("MainWindow", "Insertion Sort"))
        self.comboBoxSorting.setItemText(1, _translate("MainWindow", "Merge Sort"))
        self.comboBoxSorting.setItemText(2, _translate("MainWindow", "Bubble Sort"))
        self.comboBoxSorting.setItemText(3, _translate("MainWindow", "Selection Sort"))
        self.comboBoxSorting.setItemText(4, _translate("MainWindow", "Quick Sort"))
        self.comboBoxSorting.setItemText(5, _translate("MainWindow", "Heap Sort"))
        self.comboBoxSorting.setItemText(6, _translate("MainWindow", "Tim Sort"))
        self.comboBoxSorting.setItemText(7, _translate("MainWindow", "Shell Sort"))
        self.comboBoxSorting.setItemText(8, _translate("MainWindow", "Cocktail Sort"))
        self.comboBoxSorting.setItemText(9, _translate("MainWindow", "Counting Sort"))
        self.comboBoxSorting.setItemText(10, _translate("MainWindow", "Bucket Sort"))
        self.comboBoxSorting.setItemText(11, _translate("MainWindow", "Radix Sort"))
        self.comboBoxSorting.setItemText(12, _translate("MainWindow", "Genome Sort"))
        self.comboBoxSorting.setItemText(13, _translate("MainWindow", "PigeonHole Sort"))
        self.label_35.setText(_translate("MainWindow", "Select Column"))
        self.comboBoxSortingColumn.setCurrentText(_translate("MainWindow", "Name"))
        self.comboBoxSortingColumn.setItemText(0, _translate("MainWindow", "Name"))
        self.comboBoxSortingColumn.setItemText(1, _translate("MainWindow", "Width"))
        self.comboBoxSortingColumn.setItemText(2, _translate("MainWindow", "Height"))
        self.comboBoxSortingColumn.setItemText(3, _translate("MainWindow", "Depth"))
        self.comboBoxSortingColumn.setItemText(4, _translate("MainWindow", "Price"))
        self.comboBoxSortingColumn.setItemText(5, _translate("MainWindow", "Category"))
        self.comboBoxSortingColumn.setItemText(6, _translate("MainWindow", "Artist"))
        self.comboBoxSortingColumn.setItemText(7, _translate("MainWindow", "Country"))
        self.btnImport.setText(_translate("MainWindow", "Import"))
        self.label_34.setText(_translate("MainWindow", "Searching Algorithms"))
        self.comboBoxSearching.setItemText(0, _translate("MainWindow", "Linear Search"))
        self.comboBoxSearching.setItemText(1, _translate("MainWindow", "Starting Letter"))
        self.comboBoxSearching.setItemText(2, _translate("MainWindow", "Middle Words"))
        self.label_36.setText(_translate("MainWindow", "Select Column"))
        self.comboBoxSearchingColumn.setCurrentText(_translate("MainWindow", "Name"))
        self.comboBoxSearchingColumn.setItemText(0, _translate("MainWindow", "Name"))
        self.comboBoxSearchingColumn.setItemText(1, _translate("MainWindow", "Width"))
        self.comboBoxSearchingColumn.setItemText(2, _translate("MainWindow", "Height"))
        self.comboBoxSearchingColumn.setItemText(3, _translate("MainWindow", "Depth"))
        self.comboBoxSearchingColumn.setItemText(4, _translate("MainWindow", "Price"))
        self.comboBoxSearchingColumn.setItemText(5, _translate("MainWindow", "Category"))
        self.comboBoxSearchingColumn.setItemText(6, _translate("MainWindow", "Artist"))
        self.comboBoxSearchingColumn.setItemText(7, _translate("MainWindow", "Country"))
        self.btnSearch_2.setText(_translate("MainWindow", "Export"))
        self.label_31.setText(_translate("MainWindow", "Time Taken By Selected Algorithm in seconds :")) 
import project_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
