from csv import DictReader , DictWriter
with open('file_csv1.csv' , 'r') as rf:
      with open('output_csv2.csv' , 'w' , newline='') as wf:
            csv_reader = DictReader(rf)
            csv_writer = DictWriter(wf , fieldnames=['firstname','lastname','age'])
            csv_writer.writeheader()
            for row in csv_reader:
                  f1 , l1 , a1 = row['firstname'] ,row['lastname'] , row['age']

                  csv_writer.writerow(
                  {'firstname' :f1.upper(),
                  'lastname' :l1.upper(),
                  'age' :a1})