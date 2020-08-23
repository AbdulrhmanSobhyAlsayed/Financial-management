import os
class FinancialManagement:
     def __init__(self):
         self.name="null"
         self.basicSalary=dict({"null":"0"})
         self.expenses=dict({"null":"0"})
         self.balance=0.0
         self.extraIncome=dict({"null":"0"})
         self.taker=dict({"null":"0"})
         self.giver=dict({"null":"0"})
         
     def setName(self,name):
         self.name=name
     def getName(self):
          return (self.name)
        
     def setBasicSalary(self,typeOfSalary,valueOfSalary):
        self.basicSalary.update({typeOfSalary:valueOfSalary})
     def getBasicSalary(self):
         return ( sum(self.basicSalary.values()))
         
     def setExpenses(self,typeOfExpense,valueOfExpense):
        self.expenses.update({typeOfExpense:valueOfExpense})
     def getExpenses(self):
         return (sum(self.expenses.values()))

     def getBalance(self):
         return (self.getBasicSalary()+self.getGiver()+self.getExtraIncome()-self.getExpenses()-self.getTaker())

     def setExtraIncome(self,typeOfIncome,valueOfIncome):
         self.extraIncome.update({typeOfIncome:valueOfIncome})
     def getExtraIncome(self):
         return (sum(self.extraIncome.values()))
        
     def setTaker(self,person, value):
         self.taker.update({person:value})
     def getTaker(self):
         return (sum(self.taker.values()))

     def setGiver(self,person, value):
         self.giver.update({person:value})
     def getGiver(self):
         return (sum(self.giver.values()))

     def toString(self):
         return str("Your Name Is :%s\nYour Basic Salary Is : %f \nYour Extra Income Is : %f \nYour Expenses Is : %f \nYour Debit That You Will Have : %f \nYour Debit That You Will pay : %f \nYour Balance Is:%f\n" % (self.getName(),self.getBasicSalary(),self.getExtraIncome(),self.getExpenses(),self.getGiver(),self.getTaker(),self.getBalance()))

    
    
        

