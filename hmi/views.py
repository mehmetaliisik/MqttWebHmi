from django.shortcuts import render
from hmi import MQTT as mqtt

p1 = "False"
p2 = "False"
stop = "False"
pause = "False"
runTime = 1
overRide = 50
pauseButtonValue = "Pause"
#run = mqtt.getRuns
def index(request):
    global p1
    global p2
    global runTime
    global stop
    global pause
    global overRide
    global pauseButtonValue
    if request.method == 'POST':
        if 'program1' in request.POST:
            p1 = "True"
            p2 = "False"
            stop = "False"
            if request.POST["runTime1"]:
                runTime = request.POST["runTime1"]
            else:
                runTime = 1
            mqtt.sendData("Roboter/Anzahl",runTime)
            mqtt.sendData("Roboter/Program1",p1)
        elif 'program2' in request.POST:
            p2 = "True"
            p1 = "False"
            stop = "False"
            if request.POST["runTime2"]:
                runTime = request.POST["runTime2"]
            else:
                runTime = 1
            mqtt.sendData("Roboter/Anzahl",runTime)
            mqtt.sendData("Roboter/Program2",p2)
        elif 'stop' in request.POST:
            stop = "True"
            runTime = 1
            mqtt.sendData("Roboter/Stop",stop)
        elif 'pause' in request.POST:
            if pause == "False":
                pause = "True"
                mqtt.sendData("Roboter/Pause",pause)
                pauseButtonValue = "Continue"
            else:
                pause = "False"
                pauseButtonValue = "Pause"
                mqtt.sendData("Roboter/Pause",pause)
        elif 'override' in request.POST:
            overRide = request.POST["overRide"]
        myDict = {
            'p1': p1,
            'p2': p2,
            'stop': stop,
            'runTime': runTime,
            'pause': pause,
            'overRide': overRide,
            'pauseButtonValue': pauseButtonValue,
            #'runs': run
        }
        return render(request, "index.html", myDict)
    else:
        myDict = {
            'p1': p1,
            'p2': p2,
            'stop': stop,
            'runTime': runTime,
            'pause': pause,
            'overRide': overRide,
            'pauseButtonValue': pauseButtonValue,
            #'runs': run
        }
        return render(request, "index.html", myDict)

