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

def loadFileInDictionary(file):

    fileDict = dict()
    nLine = 0

    skipLine = 2

    for line in file:
        if skipLine > 0:
            skipLine -= 1
            continue
        line = line.split()
        fileDict[nLine] = line
        nLine += 1

    return fileDict




def addLabelToAction():

    activityA = open("./Dataset/datasetTXT/OrdonezA_ADLs.txt", "r")
    actionA = open("./Dataset/datasetTXT/OrdonezA_Sensors.txt", "r")
    final = open("./Dataset/datasetTXT/labeledData.txt", "a+")

    activityADict = loadFileInDictionary(activityA)
    actionADict = loadFileInDictionary(actionA)

    coupled = False

    # print(len(activityADict))
    # print(len(actionADict))

    for nActivity in activityADict:
        for nAction in actionADict:
            coupled = False
            # print(activityADict[nActivity])
            # print(actionADict[nAction])
            startMonthActivity = activityADict[nActivity][0][5:8]
            startMonthAction = actionADict[nAction][0][5:8]

            startDayActivity = activityADict[nActivity][0][8:]
            endDayActivity = activityADict[nActivity][2][8:]
            startDayAction = actionADict[nAction][0][8:]
            endDayAction = actionADict[nAction][2][8:]   

            startHourActivity = activityADict[nActivity][1][:2]
            endHourActivity = activityADict[nActivity][3][:2]
            startHourAction = actionADict[nAction][1][:2]
            endHourAction = actionADict[nAction][3][:2]

            startMinuteActivity = activityADict[nActivity][1][3:5]
            endMinuteActivity = activityADict[nActivity][3][3:5]
            startMinuteAction = actionADict[nAction][1][3:5]
            endMinuteAction = actionADict[nAction][3][3:5]

            startSecondActivity = activityADict[nActivity][1][6:]
            endSecondActivity = activityADict[nActivity][3][6:]
            startSecondAction = actionADict[nAction][1][6:]
            endSecondAction = actionADict[nAction][3][6:]

            if startMonthActivity == startMonthAction:

                if startDayActivity == startDayAction:

                    if endDayActivity == endDayAction:

                        if startHourActivity == startHourAction:

                            if endHourActivity == endHourAction:

                                if startMinuteActivity == startMinuteAction:

                                    if endMinuteActivity == endMinuteAction:

                                        if startSecondActivity == startSecondAction:

                                            if endSecondActivity == endSecondAction:
                                                coupled = True
                                            elif int(endSecondAction) <= int(endSecondActivity) + 50 or int(endSecondAction) >= int(endSecondActivity) - 50:
                                                coupled = True
                                            elif int(endSecondAction) <= int(endSecondActivity):
                                                coupled = True
                                        
                                        elif int(startSecondAction) <= int(startSecondActivity) + 50 or int(startSecondAction) >= int(startSecondActivity) - 50:
                                            coupled = True
                                        elif int(startSecondAction) <= int(endSecondActivity):
                                            coupled = True

                                    elif int(endMinuteActivity) > int(endMinuteAction):
                                        coupled = True

                                    elif int(endHourActivity) > int(endHourAction):
                                        coupled = True

                                elif int(startMinuteActivity) <= int(startMinuteAction):

                                    if int(endMinuteActivity) > int(endMinuteAction):
                                        coupled = True

                            elif int(endHourActivity) == int(endHourAction) + 1:
                                if startMinuteActivity == startMinuteAction:

                                    if endMinuteActivity == endMinuteAction:

                                        if startSecondActivity == startSecondAction:

                                            if endSecondActivity == endSecondAction:
                                                coupled = True
                                            elif int(endSecondAction) <= int(endSecondActivity) + 50 or int(endSecondAction) >= int(endSecondActivity) - 50:
                                                coupled = True
                                            elif int(endSecondAction) <= int(endSecondActivity):
                                                coupled = True
                                        
                                        elif int(startSecondAction) <= int(startSecondActivity) + 50 or int(startSecondAction) >= int(startSecondActivity) - 50:
                                            coupled = True
                                        elif int(startSecondAction) <= int(endSecondActivity):
                                            coupled = True

                                    elif int(endMinuteActivity) > int(endMinuteAction):
                                        coupled = True

                                    elif int(endHourActivity) > int(endHourAction):
                                        coupled = True

                                elif int(startMinuteActivity) <= int(startMinuteAction):
                                    coupled = True   
                                    
            if coupled:
                if nActivity == 0:
                    line = "{:<17}{:<10}{:<10}{:<10}".format("ACTIVITY", "LOCATION", "TYPE", "PLACE")
                    final.write(line)
                    final.write("\n")

                line = "{:<17}{:<10}{:<10}{:<10}".format(activityADict[nActivity][4], actionADict[nAction][4], 
                                                    actionADict[nAction][5], actionADict[nAction][6])
                final.write(line)
                final.write("\n")



    


