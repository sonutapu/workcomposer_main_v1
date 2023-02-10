# import email
import django

django.setup()
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import user_table
from .models import master_table
from .models import Logtable_time
from .models import project_table
from .forms import empforms
from django.db import connection
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from workcomposer import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
# from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
from .models import team_table
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
import time
import cv2 as cv
import pyautogui
from datetime import datetime
import os
import pyscreenshot
import cv2
# import ctypes
# import csv
# from pywinauto import application

# from apscheduler.schedulers.background import BackgroundScheduler
import multiprocessing
from app.jobs.job import schedule_api, schedule_api2, schedule_api3, schedule_api4


def components(request):
    return render(request, 'blog/components.html')


def forms(request):
    return render(request, 'blog/forms.html')


def tables(request):
    return render(request, 'blog/tables.html')


def notifications(request):
    return render(request, 'blog/notifications.html')


def typography(request):
    return render(request, 'blog/typography.html')


# def myprofile(request):
#     return render(request,'blog/myprofile.html')

def editprofile(request):
    return render(request, 'blog/editprofile.html')


def settingprofile(request):
    return render(request, 'blog/settingprofile.html')


########ADD SCREEN PART################
def screen_capture(request):
    return render(request, 'blog/screen_capture.html')


################################lets try  to send html temp through mail

def index(request):
    if request.method == "POST":

        email = request.POST['email']
        isactive = 1
        if user_table.objects.filter(email=email, isactive=1).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('index')
        else:
            user = user_table(email=email, isactive=isactive)
            user.save()
            html_template = 'blog/register_email.html'
            html_message = render_to_string(html_template)
            subject = 'Wellcome to Surya Internationals'
            reipient_list = [email]
            message = EmailMessage(
                subject, html_message, settings.EMAIL_HOST_USER, reipient_list)

            message.content_subtype = 'html'
            message.send()

            return render(request, "blog/index.html")
    else:
        return render(request, "blog/index.html")


# success view
def success(request):
    return render(request, 'blog/success.html')


# #app tracking
# def get_foreground_window_title():
#     title = ctypes.c_wchar_p("".ljust(100))
#     hwnd = ctypes.windll.user32.GetForegroundWindow()
#     length = ctypes.windll.user32.GetWindowTextW(hwnd, title, 100)
#     return title.value

# def log_session(start_time, end_time, app_name):
#     duration = end_time - start_time

#     try:
#         with open("computer_usage.csv", "a",encoding="utf-8") as file:
#             writer = csv.writer(file)
#             writer.writerow([start_time, end_time, app_name, duration])
#     except PermissionError:
#         print("Error: Could not open file for writing")


# def track_computer_usage():
#     start_time = time.time()
#     app_name = get_foreground_window_title()
#     prev_app_name = app_name

#     while True:
#         time.sleep(1)
#         app_name = get_foreground_window_title()

#         if app_name != prev_app_name:
#             end_time = time.time()
#             log_session(start_time, end_time, prev_app_name)
#             start_time = end_time
#             prev_app_name = app_name

#         try:
#             app = application.Application().connect(title_re="Google Chrome")
#             chrome_title = app.window(title_re="Google Chrome").WindowText()
#             if chrome_title:
#                 app_name = chrome_title
#                 if app_name != prev_app_name:
#                     end_time = time.time()
#                     log_session(start_time, end_time, prev_app_name)
#                     start_time = end_time
#                     prev_app_name = app_name
#         except Exception:
#             pass


# this function will take the face recognition when user is loged in and further
capture = cv.VideoCapture(0)  # to open Camera
# accessing pretrained model
pretrained_model = cv.CascadeClassifier("faceed.xml")


def facercgn():
    while True:
        boolean, frame = capture.read()
        if boolean == True:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            coordinate_list = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
            if len(coordinate_list) == 0:
                print("NO FACE DETECTED")

    capture.release()
    cv.destroyAllWindows()


########### this function will take the screen short when user is loged in and further
def take_screenshots():
    while True:
        datetimeNow = datetime.now()
        datetimeString = datetimeNow.strftime("%d-%m-%Y %H-%M-%S")
        save_path = "app/static/screenshots/"
        fileName = os.path.join(save_path, f"screenshort-{datetimeString}.png")
        image = pyscreenshot.grab()
        image.save(fileName)
        image = ""
        datetimeString = ""
        time.sleep(3)


# start recording
def start_recording(img=None):
    video_file = "app/static/recording/screen_recording.avi"
    screen_size = (pyautogui.size())
    fps = 15.0

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(video_file, fourcc, fps, screen_size)
    frame = np.array(img)
    start_time = time.time()
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if cv2.waitKey(1) == ord("q"):
            break
    out.release()
    cv2.destroyAllWindows()


#  start_recording_speci_time
def record_exact_time(duration, img=None):
    video_file = "app/static/exact_time_recording/record_exact_time.avi"
    duration = duration * 60  # in seconds
    screen_size = (pyautogui.size())
    fps = 15.0
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(video_file, fourcc, fps, screen_size)
    frame = np.array(img)
    start_time = time.time()
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if (time.time() - start_time) == duration:
            break
        if cv2.waitKey(1) == ord("q"):
            break
    out.release()
    cv2.destroyAllWindows()


# livescreening of the user
# def livescreening(request):
#      # 'DJI_0209.MP4'

#     # create a videoCapture Object (this allow to read frames one by one)
#     video = cv2.VideoCapture("app/static/recording/screen_recording.avi")
#     # check it's ok
#     if video.isOpened():
#         print('Video Successfully opened')
#     else:
#         print('Something went wrong check if the video name and path is correct')

#     # define a scale lvl for visualization
#     scaleLevel = 2 # it means reduce the size to 2**(scaleLevel-1)

#     windowName = 'Live Video screening'
#     cv2.namedWindow(windowName)
#     # let's reproduce the video
#     xy = []
#     while True:
#         ret, frame = video.read()  # read a single frame
#         if not ret:  # this mean it could not read the frame
#             print("Could not read the frame")
#             cv2.destroyWindow(windowName)
#             continue

#         reescaled_frame = frame
#         for i in range(scaleLevel - 1):
#             reescaled_frame = cv2.pyrDown(reescaled_frame)

#         cv2.imshow(windowName, reescaled_frame)
#         # xy.append(x)

#         waitKey = (cv2.waitKey(1) & 0xFF)
#         if waitKey == ord('q'):  # if Q pressed you could do something else with other keypress
#             print("closing video and exiting")
#             cv2.destroyWindow(windowName)
#             video.release()
#             break
#         # context = {'xy':xy}
#         # return render(request, 'livescreening.html', context=context)


# for signup(registration page)below code written
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        teamname = request.POST['teamname']
        now = datetime.now()
        user_id = now.strftime("%Y%m%d%H%M%S")
        empid = now.strftime("%Y%m%d%H%M%S")
        created_on = datetime.now()
        isactive = 1
        if user_table.objects.filter(email=email, isactive=1).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('index')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('index')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('index')

        user_table(username=username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2,
                   teamname=teamname, isactive=isactive, emp_id=empid, user_id=user_id, created_on=created_on).save()
        messages.success(request, "Your account hasbeen successfully created!")

        email = EmailMessage(
            'Welcome to Everyone',
            'Hello Everyone, \n Welcome',
            settings.EMAIL_HOST_USER,
            [email],
        )
        email.fail_silently = False
        email.send()
        return render(request, "blog/login.html")
    else:
        return render(request, "blog/signup.html")


import csv


def login(request):
    global funloginTime, funloginDate, thread
    # take global varible to logintime and logindate so that we can use its value to other function also
    if request.method == 'POST':

        def funloginTime():
            return loginTime

        def funloginDate():
            return loginDate

        try:
            Userdetails = user_table.objects.get(username=request.POST['username'], pass1=request.POST['pass1'])
            request.session["username"] = Userdetails.username
            request.session["useremail"] = Userdetails.email
            request.session["status"] = Userdetails.isactive
            request.session["id"] = Userdetails.id
            request.session["sesuserid"] = Userdetails.user_id

            # Inserting Login time of an user
            loginDate = datetime.now()
            loginTime = datetime.now().strftime("%H:%M:%S")
            global proc1, proc2, proc3, proc4, proc5, proc6, proc7, proc8
            proc1 = multiprocessing.Process(target=schedule_api, args=())
            proc2 = multiprocessing.Process(target=schedule_api2, args=())
            proc3 = multiprocessing.Process(target=schedule_api3, args=())
            proc4 = multiprocessing.Process(target=schedule_api4, args=())
            proc5 = multiprocessing.Process(target=start_recording, args=())
            duration = 1
            proc6 = multiprocessing.Process(target=record_exact_time, args=(duration,))
            proc7 = multiprocessing.Process(target=take_screenshots, args=())
            proc8 = multiprocessing.Process(target=facercgn, args=())
            # proc9= multiprocessing.Process(target=livescreening, args=())
            # proc10= multiprocessing.Process(target=track_computer_usage, args=())

            proc1.start()
            proc2.start()
            proc3.start()
            proc4.start()
            proc5.start()
            proc6.start()
            proc7.start()
            proc8.start()
            # proc9.start()
            # proc10.start()

            ennn = Logtable_time(master_id=request.session["id"], login_time=loginTime,
                                 user_id=request.session["sesuserid"], Date=loginDate)
            ennn.save()
            return redirect('index')

        except user_table.DoesNotExist as e:
            messages.error(request, "Invallid Credentials!")
        return redirect('index')
    else:
        return render(request, "blog/login.html")


########################### for logout page below code written
def signout(request):
    if 'username' in request.session:
        masterid = request.session["id"]
        userid = request.session["sesuserid"]
        loginTime = funloginTime()
        loginDate = funloginDate()
        logout(request)
        logouttime = datetime.now().strftime("%H:%M:%S")
        print(logouttime)
        # workduration = logouttime-logintime

        proc1.terminate()
        proc2.terminate()
        proc3.terminate()
        proc4.terminate()
        proc5.terminate()
        proc6.terminate()
        proc7.terminate()
        proc8.terminate()
        # proc9.terminate()
        # proc10.terminate()

        file = open('mouseidle.csv', 'r')
        x = file.read()
        print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", x)
        # for update the logout after login use this method in the logtable database
        Logtable_time.objects.filter(user_id=userid, master_id=masterid, Date=loginDate, login_time=loginTime).update(
            logout_time=logouttime, idle_time=x)
        # settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        # request.session.get_expire_at_browser_close()

        return render(request, "blog/login.html")

    else:
        return HttpResponse("Your Session has Expired....Please Login again..")


####################### change a login user his password
def passwordchange(request):
    email = request.POST.get('email')
    pwd = request.POST.get('txtpwd')
    confpwd = request.POST.get('txtconfpwd')
    if pwd != confpwd:
        messages.error(request, "Passwords and Confirm Password didn't matched")
        return render(request, "blog/passwordchange.html")
    else:
        # messages.success(request, "Passwords updated successfully.")
        user_table.objects.filter(email=email).update(pass1=pwd, pass2=confpwd)

    return render(request, "blog/passwordchange.html")


def demo(request):
    return render(request, "blog/demo.html")


def productivity(request):
    getdata1 = user_table.objects.all()
    data1 = {
        "getdata1": getdata1
    }
    return render(request, "blog/productivity.html", data1)


def attendance(request):
    getdata1 = user_table.objects.all()

    curtime = datetime.now()
    logintime = datetime(2022, 11, 14, 10, 00, 00)
    workingtime = curtime - logintime

    data1 = {"getdata1": getdata1, 'workedtime': workingtime}

    return render(request, "blog/attendance.html", data1)


def screenshots(request):
    getdata1 = user_table.objects.all()
    data1 = {
        "getdata1": getdata1
    }
    return render(request, "blog/screenshots.html", data1)


def appusage(request):
    getdata1 = user_table.objects.all()
    data1 = {
        "getdata1": getdata1
    }
    return render(request, "blog/appusage.html", data1)


# def dashboard(request):
#     return render(request, "authentication/dashboard.html")

# To get all the signup data in frontend
def User(request):
    getdata1 = user_table.objects.all()
    data1 = {
        "getdata1": getdata1
    }
    return render(request, "blog/User.html", data1)


# def passwordchange(request):
#     return render(request, "authentication/passwordchange.html")

def AddNewUser(request):
    return render(request, "blog/AddNewUser.html")


def SendInvitation(request):
    return render(request, "blog/index.html")


def Userdetails(request):
    return render(request, "blog/Userdetails.html")


# for getting data in the frontend addusertype created
def AddUserType(request):
    if 'username' in request.session:
        getuserdata = master_table.objects.all()
        data = {'getuserdata': getuserdata}
        if request.method == "POST":
            User_Type = request.POST['usertype']
            usertype = User_Type.upper()
            status = request.POST['status']
            en = master_table(User_Type=usertype, is_active=status)
            en.save()
            messages.success(request, "Your account hasbeen successfully created!")
            # return redirect('signup')
            return render(request, "blog/AddUserType.html", data)
        else:
            return render(request, "blog/AddUserType.html", data)
    else:
        return HttpResponse("Your Session has Expired......")


# for update data editdata created
def editdata(request, id):
    editdata = master_table.objects.get(id=id)
    context = {"editdata": editdata}
    return render(request, "blog/edit.html", context)


# for updatedata forms.py created
def updatedata(request, id):
    # updatedata=master_table.objects.get(id=id)
    # form=empforms(request.POST,instance=updatedata)
    # if form.is_valid:
    #     form.save()   
    #     messages.success(request,"Your Record hasbeen updated successfully")
    # return render(request,"blog/edit.html")

    id = int(id)
    try:
        updatedata = master_table.objects.filter(id=id)
    except team_table.DoesNotExist:
        return redirect('AddUserType')

    contex = request.POST['is_active']
    updatedata.update(id=id, is_active=contex)
    messages.success(request, "Your Record hasbeen updated successfully")
    # return redirect('/editteam')
    return render(request, "blog/edit.html")


# for delete data below code written
def deletedata(request, id):
    deletedata = master_table.objects.filter(id=id)
    deletedata.delete()
    messages.success(request, "Your Record hasbeen deleted successfully")
    return render(request, "blog/index.html")


# for create team
def createteam(request):
    if 'username' in request.session:
        getdata = team_table.objects.all()
        data = {'getdata': getdata}

        if request.method == "POST":
            Team_Name = request.POST['teamname']
            teamname = Team_Name.upper()
            status = request.POST['status']
            # createdate=request.POST['createon']
            createdate = datetime.now()
            # cc = datetime.now()
            # createdate = cc.strftime("%Y%M%D%H%M%S")         
            en = team_table(Team_Name=teamname, Is_Active=status, Create_on=createdate)
            en.save()
            messages.success(request, "Your team hasbeen successfully created!")
            # return redirect('signup')
            return render(request, "blog/createteam.html", data)
        else:
            return render(request, "blog/createteam.html", data)
    else:
        return HttpResponse("Your Session has Expired......")


def editteam(request, id):
    editteam = team_table.objects.get(id=id)
    context = {"editteam": editteam}
    return render(request, "blog/editteam.html", context)


def updateteam(request, id):
    id = int(id)
    try:
        updateteam = team_table.objects.filter(id=id)
    except team_table.DoesNotExist:
        return redirect('createteam')

    data = request.POST['Is _Active']
    updateteam.update(id=id, Is_Active=data)
    messages.success(request, "Your Record hasbeen updated successfully")
    # return redirect('/editteam')
    return render(request, "blog/editteam.html")


def deleteteam(request, id):
    deletedata = team_table.objects.filter(id=id)
    deletedata.delete()
    # messages.success(request,"Your Record hasbeen deleted successfully")
    return render(request, "blog/index.html")


# , \n http://127.0.0.1:8000/AddNewUser/


def createproject(request):
    service = team_table.objects.all()
    data = {'service': service}
    if request.method == 'POST':
        if request.POST.get('Assigned_Team') and request.POST.get('Project_Name'):
            savedata = project_table()
            savedata.Project_Name = request.POST.get('Project_Name')
            savedata.Assigned_Team = request.POST.get('Assigned_Team')
            savedata.Create_on = datetime.now()
            savedata.Created_by = request.session["id"]
            savedata.save()
            return render(request, "blog/createproject.html")
    else:

        return render(request, "blog/createproject.html", data)