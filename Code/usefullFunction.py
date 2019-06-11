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
    final = open("./Dataset/datasetTXT/labeledData.txt", "w")

    activityADict = loadFileInDictionary(activityA)
    actionADict = loadFileInDictionary(actionA)

    coupled = False
    out = False
    skip = False

    # print(len(activityADict))
    # print(len(actionADict))

    start = 0
    end = 0

    actionIndex = 0

    for nActivity in range(0, 11):
        if nActivity == 0:
            line = "{:<17}{:<10}{:<10}{:<10}".format("ACTIVITY", "LOCATION", "TYPE", "PLACE")
            final.write(line)
            final.write("\n")
        print("ACTIVITY: ", activityADict[nActivity])
        out = False
        while actionIndex < 28 and not out == True:
            coupled = False
            skip = False
            # print(activityADict[nActivity])
            # print(actionADict[nAction])
            print("ACTION: ", actionADict[actionIndex])

            ###### MONTH 
            startMonthActivity = activityADict[nActivity][0][5:7]
            endMonthActivity = activityADict[nActivity][2][5:7]
            startMonthAction = actionADict[actionIndex][0][5:7]
            endMonthAction = actionADict[actionIndex][2][5:7]

            ###### DAY
            startDayActivity = activityADict[nActivity][0][8:]
            endDayActivity = activityADict[nActivity][2][8:]
            startDayAction = actionADict[actionIndex][0][8:]
            endDayAction = actionADict[actionIndex][2][8:]   

            ##### HOUR
            startHourActivity = activityADict[nActivity][1][:2]
            endHourActivity = activityADict[nActivity][3][:2]
            startHourAction = actionADict[actionIndex][1][:2]
            endHourAction = actionADict[actionIndex][3][:2]

            ##### MINUTE
            startMinuteActivity = activityADict[nActivity][1][3:5]
            endMinuteActivity = activityADict[nActivity][3][3:5]
            startMinuteAction = actionADict[actionIndex][1][3:5]
            endMinuteAction = actionADict[actionIndex][3][3:5]

            ##### SECOND
            startSecondActivity = activityADict[nActivity][1][6:]
            endSecondActivity = activityADict[nActivity][3][6:]
            startSecondAction = actionADict[actionIndex][1][6:]
            endSecondAction = actionADict[actionIndex][3][6:]

            # print("START DAY ACTIVTIY: ", startDayActivity)
            # print("START DAY ACTION: ", startDayAction)

            if int(startMonthAction) >= int(startMonthActivity) and int(endMonthAction) <= int(endMonthActivity):
                print("INSIDE MONTH", end =" ")
                if int(startDayAction) >= int(startDayActivity) and int(endDayAction) <= int(endDayActivity):
                    print("INSIDE DAY", end=" ")
                    if int(startHourAction) >= int(startHourActivity) and int(endHourAction) <= int(endHourActivity):
                        print("INSIDE HOUR", end=" ")
                        if int(startMinuteAction) >= int(startMinuteActivity) and int(endMinuteAction) <= int(endMinuteActivity):
                            print("INSIDE MINUTE", end=" ")
                            if int(startSecondAction) >= int(startSecondActivity) or int(endSecondAction) <= int(endSecondActivity):
                                print("INSIDE SECOND 1", end = " ")
                                print("")
                                coupled = True
                            elif int(endMinuteAction) <= int(endMinuteActivity):
                                coupled = True
                        elif int(startMinuteAction) < int(startMinuteActivity):
                            if int(endMinuteAction) == int(startMinuteActivity):
                                skip = True

                #if int(endDayActivity) < int(endDayAction):
                #    out = True
                #   break
            print("")
                                
            
            if coupled == True:
                end += 1
                actionIndex += 1
                print("I MOVED END, NOW IS: ", end + 3)
            elif skip == True:
                start += 1
                end += 1
                actionIndex += 1
            else:
                print("START ACTION: ", start + 3)
                print("END ACTION: ", end + 3)
                print("I USE THIS ACTIVITY: ", activityADict[nActivity][4])
                for i in range(start, end):
                    line = "{:<17}{:<10}{:<10}{:<10}".format(activityADict[nActivity][4], actionADict[i][4],
                    actionADict[i][5], actionADict[i][6])
                    print("I ADDED THIS LINE: ", line)
                    final.write(line)
                    final.write("\n")

                print("")
                start = end 
                out = True

    


'''def addLabelToAction():

    activityA = open("./Dataset/datasetTXT/OrdonezA_ADLs.txt", "r")
    actionA = open("./Dataset/datasetTXT/OrdonezA_Sensors.txt", "r")
    final = open("./Dataset/datasetTXT/labeledData.txt", "a+")

    activityADict = loadFileInDictionary(activityA)
    actionADict = loadFileInDictionary(actionA)

    coupled = False

    # print(len(activityADict))
    # print(len(actionADict))

    start = 0
    end = 1

    actionIndex = 0

    for nActivity in activityADict:
        while end < len(actionADict):
            coupled = False
            # print(activityADict[nActivity])
            # print(actionADict[nAction])
            startMonthActivity = activityADict[nActivity][0][5:8]
            startMonthAction = actionADict[actionIndex][0][5:8]

            startDayActivity = activityADict[nActivity][0][8:]
            endDayActivity = activityADict[nActivity][2][8:]

            startDayAction = actionADict[actionIndex][0][8:]
            endDayAction = actionADict[actionIndex][2][8:]   

            startHourActivity = activityADict[nActivity][1][:2]
            endHourActivity = activityADict[nActivity][3][:2]
            startHourAction = actionADict[actionIndex][1][:2]
            endHourAction = actionADict[actionIndex][3][:2]

            startMinuteActivity = activityADict[nActivity][1][3:5]
            endMinuteActivity = activityADict[nActivity][3][3:5]
            startMinuteAction = actionADict[actionIndex][1][3:5]
            endMinuteAction = actionADict[actionIndex][3][3:5]

            startSecondActivity = activityADict[nActivity][1][6:]
            endSecondActivity = activityADict[nActivity][3][6:]
            startSecondAction = actionADict[actionIndex][1][6:]
            endSecondAction = actionADict[actionIndex][3][6:]

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
                final.write("\n")'''