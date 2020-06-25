with open('html1.html','r') as rf:
      with open('output.html','a') as wf:
            for line in rf.readlines():
                  if '<a href =' in line:
                        pos = line.find('<a href =')
                        first_quote = line.find('\"' ,pos)
                        last_quote = line.find('\"',first_quote+1)
                        url = line[first_quote+1:last_quote]
                        wf.write(url + '\n')
