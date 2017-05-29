import pandas as pd
import csv
import json
import os


def json_to_csv(path):
    commonSufix = '2017_05_'
    currentDay = '0'
    csv_file = open('toDel', 'w+')
    allFiles = []

    for fileName in os.listdir(path):
        if fileName[1:3] != currentDay:
            csv_file.close()
            currentDay = fileName[1:3]
            csvName = '{0}{1}.csv'.format(commonSufix, currentDay)
            allFiles.append(csvName)
            csv_file = open(csvName, 'w+')
            csvWriter = csv.writer(csv_file)
            writeHeader = True
        f = open('{0}{1}'.format(path, fileName))
        result = json.load(f)
        data = result['result']
        f.close()

        for item in data:
            if writeHeader:
                header = item.keys()
                csvWriter.writerow(header)
                writeHeader = False
            csvWriter.writerow(item.values())
    csv_file.close()
    os.remove('toDel')
    return allFiles


path = 'twoja\\wspaniala\\sciezka'
allFiles = json_to_csv(path)
df = pd.read_csv(allFiles[0])
df
