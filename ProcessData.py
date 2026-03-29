#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #header
  outFile.write("LastName,FirstName,UserID,Major-Year\n")

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data [5]
    major = " ".join(data[6:])

    #print(data)
    student_id = makeID(first, last, idNum)
    major_year = makeMajorYear(major, year)

    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)


    #outFile.write()

    #print(student_id)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen =len(idNum)


  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]

  

  #print(id)
  return id.lower()

def makeMajorYear(major, year):
  major_code = major[:3] .upper()

  year_map = {
    "Freshman": "FR",
    "Sophomore": "SO",
    "Junior": "JR",
    "Senior": "SR"
  }

  year_code = year_map.get(year, "NA")

  return major_code + "-" + year_code

if __name__ == '__main__':
  main()
