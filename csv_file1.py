# FOR READ THE CSV FILES
# from csv import reader
# with open('csv1.csv','r') as f:
#       csv_reader = reader(f)
#       for row in csv_reader:
#             print(row)

# from csv import DictReader
# with open('csv1.csv' , 'r') as f:
#       csv_reader = DictReader(f, delimiter = '|')
#       for row in csv_reader:
#             print(row)

# 
# FOR WRITE IN CSV FILES
# 1. writer function
# from csv import writer
# with open('csv2.csv' ,'a', newline = '') as f:
      # csv_writer = writer(f)
      # TWO METHODS FOR WRITING ROWS
      # 1. writerow method
      # csv_writer.writerow(['fname','lname','age'])
      # csv_writer.writerow(['jassi','kaur',22])
      # csv_writer.writerow(['mandeep','singh' , 20])
      # csv_writer.writerow(['jasleen','matharu',27])

      # 2. writerows method
      # csv_writer.writerows([['fname','lname','age'],['jassi','kaur',22],['mandeep','singh',20]])
#    2. DictWriter function 
from csv import DictWriter
with open('output3.csv' , 'a' , newline='') as wf:
      csv_writer = DictWriter(wf , fieldnames = ['fname','lname','age'])
      csv_writer.writeheader()
      # HERE ALSO TWO METHODS TO WRITE
      # csv_writer.writerow({
      #       'fname':'jassi',
      #       'lname':'kaur',
      #       'age':22
      # })

      # csv_writer.writerow({
      #       'fname':'mandeep',
      #       'lname':'singh',
      #       'age':21      })


      csv_writer.writerows([
      {'fname':'jassi','lname':'kaur','age':22},
      {'fname':'mandeep','lname':'singh','age':20}
])
