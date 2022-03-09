import csv

Player=[]
Points=[]


def ReadScore():
    with open('scores.txt') as csvDataFile:
        csvReader = csv.DictReader(csvDataFile,delimiter=',',quotechar='"', escapechar=' ')
        for row in csvReader:
            Player.append(row["name"])
            Points.append(row["point"])

    csvDataFile.close()
    return (Player)

def SaveScore():
    with open('scores.txt','w') as csvDataFile2:
        fieldnames=['name','point']
        csvWriter = csv.DictWriter(csvDataFile2, fieldnames=fieldnames)
        a=0
        csvWriter.writeheader()
        for player in Player:
            csvWriter.writerow({'name':Player[a], 'point':Points[a]})
            a+=1
    csvDataFile2.close()

def main():

    #CsvReader()
    print(ReadScore())
    SaveScore()

if __name__ == '__main__':
    main()