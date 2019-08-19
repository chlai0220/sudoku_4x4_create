####################################################################################
# Python Version : 3.7.3
# File Name     : 
# Coder            : Weder Lai
# Purpose        : 
####################################################################################
# History: 
#  Ver        Date               Descripition
# -------  ------------  ----------------------------
#  1.0          2019/08/19   * New Issue
####################################################################################
#+--------------------+
#|       MODULE       |     
#+--------------------+
#==================================
import os , sys
import random
import time
import numpy as np
#==================================

#*******************************************#
# FUNCTION 
#*******************************************#
##############################################################################
 
def Exe_Time(t1 , t2):
    #---------------------------------------------------------------------------------------------------------------------------------
    print("啟動時間  : " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t1))  )
    print("結束時間  : " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t2))  )
    print("執行時間  : " + str(round(t2-t1,3))+ "秒")
    #---------------------------------------------------------------------------------------------------------------------------------

class Create_Sudoku:
    #---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self , rows=4 , sudoku_model=None):
        print("Start to Create Sudoku!")
        self.sudoku_model = sudoku_model
        self.rows = rows
        #self.main()

    def main(self):
        row_num = self.rows
        ans1 , ans2 , ans3 = True , True , True
        new_model = np.zeros((row_num,row_num) , np.int)
        if row_num==4:row_num_list = [1,2,3,4]
        if row_num==9:row_num_list = [1,2,3,4,5,6,7,8,9]
        #......................................................................................
        #Row 0
        random.shuffle(row_num_list)
        for i in range(1):
            for j in range(row_num):
                new_model[i][j]=row_num_list[j]
        #......................................................................................
        #Row 1~3 or Row 1~8
        while True:
            for i in range(1,row_num):
                while len(row_num_list)==row_num:
                    for j in range(4):
                        row = (set(row_num_list) - set([new_model[i-1-d][j] for d in range(i)]))
                        row = [x for x in row]
                        if len(row)==0:
                            if row_num==4:row_num_list = [1,2,3,4]
                            if row_num==9:row_num_list = [1,2,3,4,5,6,7,8,9]
                            break
                        num = np.random.choice(row)
                        new_model[i][j]=num
                        row_num_list.remove(num)
                if row_num==4:row_num_list = [1,2,3,4]
                if row_num==9:row_num_list = [1,2,3,4,5,6,7,8,9]
            #......................................................................................     
            ans1 = self.verify1(new_model , row_num)
            ans2 = self.verify2(new_model , row_num)
            ans3 = self.verify3(new_model , row_num)
            #print(ans1 , ans2 , ans3)
            if ans1 and ans2 and ans3:
                print(new_model)
                break
            #......................................................................................
        
    def verify1(self , new_model , row_num):
        if row_num==4:Row_Sum = 10
        if row_num==9:Row_Sum = 45
        new_model_trans = np.transpose(new_model)
        
        for i in range(row_num):
            row_sum = np.sum(new_model_trans[i])
            if not row_sum==Row_Sum:
                print("Verify Rule1 - Fail!")
                print("Create Sudoku Again")
                #print(new_model)
                #self.main()
                return False
        return True
        #print("Verify Rule1 - Pass!")
                
    def verify2(self , new_model , row_num):
        if row_num==4:myRange = [[0,1] , [2,3]]  
        if row_num==9:myRange = [[0,1,2] , [3,4,5] , [6,7,8]]
            
        Row_Sum = int(row_num * (1+row_num)*0.5)    
        check_count = 0
        
        for i in myRange:
            for j in myRange:
                cell_sum = 0
                for ii in i:
                    for jj in j:
                        #print(ii , jj)
                        cell_sum += new_model[ii][jj]
                if cell_sum==10:
                    check_count += 1

        if not check_count==row_num:
            #print("Verify Rule2 - Pass!")
            #print(new_model)
            print("Verify Rule2 - Fail!")
            print("Create Sudoku Again")
            #print(new_model)
            #self.main()
            return False
        return True

    def verify3(self , new_model , row_num):
        if row_num==4:myRange = [[0,1] , [2,3]]   
        if row_num==9:myRange = [[0,1,2] , [3,4,5] , [6,7,8]]
        
        Row_Sum = int(row_num * (1+row_num)*0.5)
        check_count = 0
        
        for i in myRange:
            for j in myRange:
                temp_list = []
                for ii in i:
                    for jj in j:
                        temp_list.append(int(new_model[ii][jj]))
                        
                #Rule3
                temp_list.sort()
                str_num = "".join([str(num) for num in temp_list])
                if str_num=="1234":
                    check_count += 1
                    
        if not check_count==row_num:
            #print("Verify Rule3 - Pass!")
            #print(new_model)
            #sys.exit(0)    
            #else:
            print("Verify Rule3 - Fail!")
            print("Create Sudoku Again")
            #print(new_model)
            #self.main()
            return False
        return True
    #---------------------------------------------------------------------------------------------------------------------------------    

#============================================================================#
if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    time1 = time.time()
    cs = Create_Sudoku()
    cs.main()
    time2 = time.time()
    Exe_Time(time1 , time2)
#============================================================================#

