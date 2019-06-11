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
            startMonthActivity = int(activityADict[nActivity][0][5:7])
            endMonthActivity = int(activityADict[nActivity][2][5:7])
            startMonthAction = int(actionADict[actionIndex][0][5:7])
            endMonthAction = int(actionADict[actionIndex][2][5:7])

            ###### DAY
            startDayActivity = int(activityADict[nActivity][0][8:])
            endDayActivity = int(activityADict[nActivity][2][8:])
            startDayAction = int(actionADict[actionIndex][0][8:])
            endDayAction = int(actionADict[actionIndex][2][8:])   

            ##### HOUR
            startHourActivity = int(activityADict[nActivity][1][:2])
            endHourActivity = int(activityADict[nActivity][3][:2])
            startHourAction = int(actionADict[actionIndex][1][:2])
            endHourAction = int(actionADict[actionIndex][3][:2])

            ##### MINUTE
            startMinuteActivity = int(activityADict[nActivity][1][3:5])
            endMinuteActivity = int(activityADict[nActivity][3][3:5])
            startMinuteAction = int(actionADict[actionIndex][1][3:5])
            endMinuteAction = int(actionADict[actionIndex][3][3:5])

            ##### SECOND
            startSecondActivity = int(activityADict[nActivity][1][6:])
            endSecondActivity = int(activityADict[nActivity][3][6:])
            startSecondAction = int(actionADict[actionIndex][1][6:])
            endSecondAction = int(actionADict[actionIndex][3][6:])

            ##### TIME
            startTimeActivity = startHourActivity * 3600 + startHourActivity * 60 + startSecondActivity
            endTimeActivity = endHourActivity * 3600 + endHourActivity * 60 + endSecondActivity
            startTimeAction = startHourAction * 3600 + startHourAction * 60 + startSecondAction
            endTimeAction = endHourAction * 3600 + endHourAction * 60 + endSecondAction

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
