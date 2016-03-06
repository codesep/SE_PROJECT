from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.db.models import Q

from .models import *

def home(request):
	if "loggedinuserid" in request.session:
		user = User.objects.get(userID = request.session["loggedinuserid"])
		if(user.role==2):
			return render(request, 'GMS/admin.html', {'user' : user})
		else:
			return render(request, 'GMS/home.html', {'user' : user})
		# return HttpResponse("Hello, " + request.session["loggedinuserid"])
	else:
		return HttpResponseRedirect(reverse('GMS:login'))
def admin(request):
	if "loggedinuserid" in request.session:
		user = User.objects.get(userID = request.session["loggedinuserid"])
		if(user.role==2):
			return render(request, 'GMS/admin.html', {'user' : user})
		else:
			return render(request, 'GMS/home.html', {'user' : user})
	else:
		return HttpResponseRedirect(reverse('GMS:login'))
def addStudent(request):
	if "loggedinuserid" in request.session:
		user = User.objects.get(userID = request.session["loggedinuserid"])
		if(user.role==2):
 			return render(request, 'GMS/addStudent.html', {'user' : user})
		else:
 			return render(request, 'GMS/home.html', {'user' : user})
 	else:
		return HttpResponseRedirect(reverse('GMS:login'))

def addInstructor(request):
	if "loggedinuserid" in request.session:
		user = User.objects.get(userID = request.session["loggedinuserid"])
		if(user.role==2):
 			return render(request, 'GMS/addInstructor.html', {'user' : user})
		else:
 			return render(request, 'GMS/home.html', {'user' : user})
 	else:
		return HttpResponseRedirect(reverse('GMS:login'))

def addCourse(request):
	if "loggedinuserid" in request.session:
		user = User.objects.get(userID = request.session["loggedinuserid"])
		if(user.role==2):
 			return render(request, 'GMS/addCourse.html', {'user' : user})
		else:
 			return render(request, 'GMS/home.html', {'user' : user})
 	else:
		return HttpResponseRedirect(reverse('GMS:login'))

def saveCourse(request):
	name = request.POST.get('name','')
	courseid = request.POST.get('courseid','')
	LTP = request.POST.get('LTP','')
	credit = request.POST.get('credit','')
	courseType = request.POST.get('courseType','')
	userid = request.POST.get('Iuserid','')
	c = {}
	c.update(csrf(request))
	user1 = User.objects.get(userID = request.session["loggedinuserid"])
	if courseid == '':
		return render_to_response('GMS/addCourse.html', c)
	try:
		user = User.objects.get(userID = userid)
	except(KeyError, User.DoesNotExist):
		c.update({ 'error_message':'Invalid Instructor User - ID' })
		return render(request, 'GMS/addCourse.html', c)
	else:
		instructor = Instructor.objects.get(user=user)
		c=Course(instructor=instructor,courseID=courseid,name=name,LTP=LTP,credits=credit,courseType=courseType,gradesUploaded=0)
		c.save()
		if(user1.role==2):
			return render(request, 'GMS/admin.html', {'user' : user1})
		else:
			return render(request, 'GMS/home.html', {'user' : user1})

def saveInstructor(request):
	name = request.POST.get('name','')
	user = request.POST.get('userid','')
	pwd = request.POST.get('password','')
	email=request.POST.get('email','')
	department=request.POST.get('department','')
	contact=request.POST.get('contact','')
	c = {}
	c.update(csrf(request))
	user1 = User.objects.get(userID = request.session["loggedinuserid"])
	if user == '':
		return render_to_response('GMS/addInstructor.html', c)
	u=User(userID=user,password=pwd,name=name,email = email,contact=contact,role=1)
	i=Instructor(user=u,department=department)
	u.save()
	i.save()
	if(user1.role==2):
		return render(request, 'GMS/admin.html', {'user' : user1})
	else:
		return render(request, 'GMS/home.html', {'user' : user1})

def saveStudent(request):
	name = request.POST.get('name','')
	user = request.POST.get('userid','')
	pwd = request.POST.get('password','')
	email=request.POST.get('email','')
	branch=request.POST.get('branch','')
	batch=request.POST.get('batch','')
	year=request.POST.get('year','')
	contact=request.POST.get('contact','')
	c = {}
	c.update(csrf(request))
	if user == '':
		return render_to_response('GMS/addStudent.html', c)
	u=User(userID=user,password=pwd,name=name,email = email,contact=contact,role=0)
	s=Student(user=u,branch=branch,batch=batch,year=year)
	u.save()
	s.save()
	user1 = User.objects.get(userID = request.session["loggedinuserid"])
	if(user1.role==2):
		user = User.objects.get(userID = request.session["loggedinuserid"])
		return render(request, 'GMS/admin.html', {'user' : user})
	else:
		return render(request, 'GMS/home.html', {'user' : user})


def login(request):
	if "loggedinuserid" in request.session:
		user = User.objects.get(userID = request.session["loggedinuserid"])
		if(user.role==2):
			return render(request, 'GMS/admin.html', {'user' : user})
		else:
			return render(request, 'GMS/home.html', {'user' : user})
	
	userid = request.POST.get('username', '')
	pwd = request.POST.get('password', '')

	c = {}
	c.update(csrf(request))

	if userid == '':
		return render(request, 'GMS/login.html', c)

	try:
		user = User.objects.get(userID = userid)
	except(KeyError, User.DoesNotExist):
		c.update({ 'error_message':'1. Incorrect username or password' })
		return render(request, 'GMS/login.html', c)
	else:
		if pwd != user.password :
			c.update({ 'error_message':'2. Incorrect username or password' })
			return render_to_response('GMS/login.html', c)
		else :
			request.session["loggedinuserid"] = userid
		if(user.role==2):
			return render(request, 'GMS/admin.html', {'user' : user})
		else:
			return render(request, 'GMS/home.html', {'user' : user})


def logout(request):
	if "loggedinuserid" in request.session:
		try:
			del request.session["loggedinuserid"]
		except(KeyError):
			return HttpResponseRedirect(reverse('GMS:home'))
		
		return render(request, 'GMS/loggedout.html')
	else:
		return HttpResponseRedirect(reverse('GMS:login'))

def giveGrade(request, course_id=''):
	# print("Course ID :" + str(course_id))
	if "loggedinuserid" in request.session:
		user = User.objects.get(userID = request.session["loggedinuserid"])

		if user.role == 1 :
			instr = Instructor.objects.get(user = user)
			courses = instr.course_set.all()
			if course_id == '':
				return render(request, 'GMS/giveGrade.html', {'giveGrade' : 0, 'user' : user, 'courses' : courses})
			else:
				try:
					course = courses.get(courseID = course_id)
				except (KeyError, Course.DoesNotExist):
					return HttpResponseRedirect(reverse('GMS:giveGrade'))
				else:
					students = Student.objects.filter(allCourses = course)
					if request.method == 'POST':
						for s in students:
							try:
								g_set = s.grade_set.get(course = course)
							except (KeyError, Grade.DoesNotExist):
								g_set = Grade(student = s, course = course, grade = request.POST.get(s.user.userID, 'U'))
							else:
								g_set.grade = request.POST.get(s.user.userID, 'U')
							g_set.save()
						if course.gradesUploaded == False:
							course.gradesUploaded = True
							course.save()

						return HttpResponseRedirect(reverse('GMS:giveGrade'))
					else:
						grades = []
						for s in students:
							grade = ''
							try:
								g_set = s.grade_set.get(course = course)
							except (KeyError, Grade.DoesNotExist):
								grade = 'U'
							else:
								grade = g_set.grade
							grades.append(grade)

						return render(request, 'GMS/giveGrade.html', {'giveGrade' : 1, 
																	  'user' : user,
																	  'students' : students,
																	  'course' : course,
																	  'grades' : grades,
																	  'std_grd_zipped' : zip(students, grades)})
				
		else :
			return HttpResponseRedirect(reverse('GMS:home'))
	else:
		return HttpResponseRedirect(reverse('GMS:login'))


# Function to get Grade points
def getGradePoints(grade):
	return {
		'A' : 10,
		'B' : 8,
		'C' : 6,
		'D' : 4,
		'F' : 0,
	}.get(grade, 0)


def transcript(request, student_id = ''):
	if "loggedinuserid" in request.session:
		user = User.objects.get(userID = request.session["loggedinuserid"])
		
		# Check if user is Instructor
		if user.role == 1:
			students = Student.objects.all()
			if student_id == '':
				return render(request, 'GMS/transcript.html', {'user' : user, 'students' : students, 'student_selected' : 0})
		
		# Generating transcript for selected student
		if student_id == '':
			student = Student.objects.get(user = user)
		else:
			# Generate transcript of selected student (if user = instructor)
			if user.role == 1:
				try:
					user_selected = User.objects.get(userID = student_id)
				except (KeyError, User.DoesNotExist):
					return HttpResponseRedirect(reverse('GMS:transcript'))
				student = Student.objects.get(user = user_selected)
			else:
				return HttpResponseRedirect(reverse('GMS:transcript'))

		# All assigned grades of selected student
		grades = student.grade_set.all()

		# Current year of selected student
		curr_year = "1"
		sem_of_curr_year = "1"

		# Array of 8 semesters' grades
		all_sem_grades = [[], [], [], [], [], [], [], []]

		# Iterate all grades
		for g in grades:
			course = g.course 
			cID = course.courseID
			grade = g.grade
			year = cID[2]
			acad_year = str(int(float(student.year)) + int(float(year)) - 1)
			acad_year_plus_one = str(int(float(acad_year)) + 1)
			acad_year = acad_year + "-" + acad_year_plus_one			# e.g. : "2014-2015"
			sem_curr_year =  cID[3]										# Semester no. of current year
			sem = (int(float(year))-1) * 2 + int(float(sem_curr_year))	# Overall semester no.

			# Add grades of current course in 'all_sem_grades' list
			all_sem_grades[sem - 1].append({'course' : course, 'grade' : grade, 'acad_year' : acad_year, 'sem_curr_year' : sem_curr_year})

			# Update current year of selected student
			if curr_year < year:
				curr_year = year
				if sem_of_curr_year < sem_curr_year:
					sem_of_curr_year = sem_curr_year

		# Total semesters count of selected student (till now)
		total_sems = (int(float(curr_year))-1) * 2 + int(float(sem_of_curr_year))

		# Calculating SPIs and CPIs
		cpi = 0
		total_points = 0
		points = 0
		for sem_grades in all_sem_grades:
			total_sem_points = 0
			sem_points = 0
			if sem_grades.__len__():
				for g in sem_grades:
					total_sem_points += g['course'].credits * 10
					# sem_points += g.get['course'].credits * getGradePoints(g['grade'])
					gradePoints = ({ 'A' : 10, 'B' : 8, 'C' : 6, 'D' : 4, 'F' : 0 }.get(g['grade'], 0))
					sem_points += g['course'].credits * gradePoints
				
				total_points += total_sem_points
				points += sem_points
				
				spi = sem_points / total_sem_points * 10
				spi = float("{0:.2f}".format(spi))	# limit to 2 decimal places

				cpi = points / total_points * 10
				cpi = float("{0:.2f}".format(cpi))	# limit to 2 decimal places

				for g in sem_grades:
					g.update({'spi' : spi, 'cpi' : cpi})

		
		return render(request, 'GMS/transcript.html', {'user' : user, 
													   'student' : student, 
													   'total_sems' : total_sems, 
													   'all_sem_grades' : all_sem_grades,
													   'student_selected' : 1})
	else:
		return HttpResponseRedirect(reverse('GMS:login'))


def search(request):
	if "loggedinuserid" in request.session:
		user = User.objects.get(userID = request.session["loggedinuserid"])

		if user.role == 1:
			if request.method == 'POST':
				query = request.POST.get('search', '')
				if query != '':
					result = User.objects.filter(Q(userID__contains = query) | Q(name__contains = query))
					result = result.filter(role = 0)

					return render(request, 'GMS/transcript.html', {'user' : user, 'students' : result, 'student_selected' : 0, 'searched' : 1})
				else:
					return HttpResponseRedirect(reverse('GMS:transcript'))
			else:
				return HttpResponseRedirect(reverse('GMS:transcript'))
		else:
			return HttpResponseRedirect(reverse('GMS:transcript'))
	else:
		return HttpResponseRedirect(reverse('GMS:login'))