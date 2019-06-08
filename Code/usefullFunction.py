import csv

def writeTxtToCsv():
    txtActivityA = open("./Dataset/datasetTXT/OrdonezA_ADLs.txt", "r")
    txtSensorA = open("./Dataset/datasetTXT/OrdonezA_Sensors.txt", "r")
    skipLine = 2
    nLine = 1

    with open('./Dataset/datasetCSV/ActivityA.csv', mode='w') as activityA:
        activity_writer = csv.writer(activityA, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        activity_writer.writerow(['Number', 'Start_Time', 'End_Time', 'Activity'])

        for line in txtActivityA:
            if skipLine > 0:
                skipLine -= 1
                continue
            line = line.split()
            
            activity_writer.writerow([nLine, str(line[0]) +" "+ str(line[1]), str(line[2]) +" "+ str(line[3]), str(line[4])])
            nLine += 1

    skipLine = 2
    nLine = 1

    with open('./Dataset/datasetCSV/SensorsA.csv', mode='w') as sensorA:
        sensor_writer = csv.writer(sensorA, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        sensor_writer.writerow(['Number', 'Start_Time', 'End_Time',  'Location', 'Type', 'Place'])

        for line in txtSensorA:
            if skipLine > 0:
                skipLine -= 1
                continue
            line = line.split()
            
            sensor_writer.writerow([nLine, str(line[0]) +" "+ str(line[1]), str(line[2]) +" "+ str(line[3]), str(line[4]), 
                                            str(line[5]), str(line[6])])
            nLine += 1 