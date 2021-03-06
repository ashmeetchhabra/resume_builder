import webapp2

from google.appengine.ext import ndb

## this is just a skeleton of how your code should be.
## i think you can make changes in this code to suit your requirements


head='''
<head>
<script src= "http://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js"></script>  
<center><h1><p style="color:#6699FF">Welcome</p></h1></center></head>
'''

LoginForm="""
<center>
<form action="/login" method="post">
Login Form
      <table>
      <tr><td>username:</td><td><input type='text' name="username"></td></tr>
      <tr><td>password:</td><td><input type='password' name="password" ></td></tr>
      <tr><td></td><td><input type="reset" value="Reset"><input type="submit" value="Submit"></div>
    </form>
    </center>
"""

SignupForm="""
<center>
<form action="/signup" method="post" ng-app="myApp" ng-controller="validateCtrl" 
name="myForm" novalidate>
Add Details
      <table>
      <tr><td>First Name:</td><td><input type='text' name="firstname" ng-model="user" required></td></tr>
      <span style="color:red" ng-show="myForm.user.$dirty && myForm.user.$invalid">
<span ng-show="myForm.user.$error.required">First Name is required.</span>
</span>
      <tr><td>Last Name:</td><td><input type='text' name="lastname"></td></tr>
      <tr><td>Address:</td><td><input type='text' name="address"></td></tr>
      <tr><td>Objective:</td><td><input type='text' name="objective"></td></tr>
      <tr><td>City:</td><td><input type='text' name="city"></td></tr>
      <tr><td>State:</td><td><input type='text' name="state"></td></tr>
      <tr><td>Pin:</td><td><input type='text' name="pin"></td></tr>
      <tr><td>Email id:</td><td><input type='text' name="email_id"></td></tr>
      <tr><td>Phone no:</td><td><input type='text' name="phno"></td></tr>
      <tr><td>College Name:</td><td><input type='text' name="college_name"></td></tr>
      <tr><td>Affiliated to:</td><td><input type='text' name="affiliated_to"></td></tr>
      <tr><td>Current Average:</td><td><input type='text' name="current_avg"></td></tr>
      <tr><td>Twelth Percentage:</td><td><input type='text' name="twelth_percent"></td></tr>
      <tr><td>Tenth Percentage:</td><td><input type='text' name="tenth_percent"></td></tr>
      <tr><td>Technical Skills:</td><td><input type='text' name="tech_skills"></td></tr>
      <tr><td>Industrial Training-</td></tr>
      <tr><td>Organization:</td><td><input type='text' name="it_organization"></td></tr>
      <tr><td>Description:</td><td><input type='text' name="it_description"></td></tr>
      <tr><td>Duration:</td><td><input type='text' name="it_duration"></td></tr>
      <tr><td>Role:</td><td><input type='text' name="it_role"></td></tr>
      <tr><td>Minor Project-</td></tr>
      <tr><td>Organization:</td><td><input type='text' name="mi_organization"></td></tr>
      <tr><td>Description:</td><td><input type='text' name="mi_description"></td></tr>
      <tr><td>Duration:</td><td><input type='text' name="mi_duration"></td></tr>
      <tr><td>Role:</td><td><input type='text' name="mi_role"></td></tr>
      <tr><td>Major Project-</td></tr>
      <tr><td>Organization:</td><td><input type='text' name="ma_organization"></td></tr>
      <tr><td>Description:</td><td><input type='text' name="ma_description"></td></tr>
      <tr><td>Duration:</td><td><input type='text' name="ma_duration"></td></tr>
      <tr><td>Role:</td><td><input type='text' name="ma_role"></td></tr>

      <tr><td>Extra Curricular Activities:</td><td><input type='text' name="extra_curricular"></td></tr>
      <tr><td>Achievements:</td><td><input type='text' name="achievements"></td></tr>
      <tr><td>Strength:</td><td><input type='text' name="strength"></td></tr>
      <tr><td>Weakness:</td><td><input type='text' name="weakness"></td></tr>
      <tr><td>Hobbies:</td><td><input type='text' name="hobbies"></td></tr>
      <tr><td>Date of Birth:</td><td><input type='text' name="dob"></td></tr>
      <tr><td>Gender:</td><td><input type='text' name="gender"></td></tr>
      <tr><td>Nationality:</td><td><input type='text' name="nationality"></td></tr>
      <tr><td>Marital Status:</td><td><input type='text' name="marital_status"></td></tr>
      <tr><td>Language Known:</td><td><input type='text' name="lang_known"></td></tr>
      <tr><td>Mother Tongue:</td><td><input type='text' name="mother_tongue"></td></tr>
      <tr><td>Father's Name:</td><td><input type='text' name="father_name"></td></tr>
      <tr><td>Head of Department:</td><td><input type='text' name="hod"></td></tr>
      <tr><td>Today's Date:</td><td><input type='text' name="date"></td></tr>
      <tr><td>User Name:</td><td><input type='text' name="username"></td></tr>
      <tr><td>Password:</td><td><input type='password' name="password" ></td></tr>
      <tr><td></td><td><input type="reset" value="Reset"><input type="submit" value="Submit" ng-disabled="myForm.user.$dirty && myForm.user.$invalid "></div>
    </form></center>
<script>
var app = angular.module('myApp', []);
app.controller('validateCtrl', function($scope) {
    $scope.user = 'default_name';
    $scope.email = 'default@gmail.com';
});
</script>
"""

class LoginDB(ndb.Model):
    first_name=ndb.StringProperty()
    last_name=ndb.StringProperty()
    user_addr=ndb.StringProperty()
    user_obj=ndb.StringProperty()
    user_city=ndb.StringProperty()
    user_state=ndb.StringProperty()
    user_pin=ndb.StringProperty()
    user_email=ndb.StringProperty()
    user_phno=ndb.StringProperty()
    user_clgname=ndb.StringProperty()
    user_affiliated_to=ndb.StringProperty()
    user_current_avg=ndb.StringProperty()
    user_twelthpercent=ndb.StringProperty()
    user_tenthpercent=ndb.StringProperty()
    user_tech_skills=ndb.StringProperty()
    user_it_organization=ndb.StringProperty()
    user_it_description=ndb.StringProperty()
    user_it_duration=ndb.StringProperty()
    user_it_role=ndb.StringProperty()
    user_mi_organization=ndb.StringProperty()
    user_mi_description=ndb.StringProperty()
    user_mi_duration=ndb.StringProperty()
    user_mi_role=ndb.StringProperty()
    user_ma_organization=ndb.StringProperty()
    user_ma_description=ndb.StringProperty()
    user_ma_duration=ndb.StringProperty()
    user_ma_role=ndb.StringProperty()
    user_extra_curri=ndb.StringProperty()
    user_achievements=ndb.StringProperty()
    user_strength=ndb.StringProperty()
    user_weakness=ndb.StringProperty()
    user_hobbies=ndb.StringProperty()
    user_dob=ndb.StringProperty()
    user_gender=ndb.StringProperty()
    user_nationality=ndb.StringProperty()
    user_marital_status=ndb.StringProperty()
    user_lang_known=ndb.StringProperty()
    user_mother_tongue=ndb.StringProperty()
    user_father_name=ndb.StringProperty()
    user_hod=ndb.StringProperty()
    user_date=ndb.StringProperty()

    
    user_name=ndb.StringProperty()
    user_pwd=ndb.StringProperty()

class SignupHandler(webapp2.RequestHandler):
    def post(self):
        login_details=LoginDB(first_name=self.request.get('firstname'),
                              last_name=self.request.get('lastname'),
                              user_addr=self.request.get('address'),
                              
                              user_obj=self.request.get('objective'),
                              user_city=self.request.get('city'),
                              user_state=self.request.get('state'),
                              user_pin=self.request.get('pin'),
                              user_email=self.request.get('email_id'),
                              user_phno=self.request.get('phno'),
                              user_clgname=self.request.get('college_name'),
                              user_affiliated_to=self.request.get('affiliated_to'),
                              user_current_avg=self.request.get('current_avg'),
                              user_twelthpercent=self.request.get('twelth_percent'),
                              user_tenthpercent=self.request.get('tenth_percent'),
                              user_tech_skills=self.request.get('tech_skills'),
                              user_it_organization=self.request.get('it_organization'),
                              user_it_description=self.request.get('it_description'),
                              user_it_duration=self.request.get('it_duration'),
                              user_it_role=self.request.get('it_role'),
                              user_mi_organization=self.request.get('mi_organization'),
                              user_mi_description=self.request.get('mi_description'),
                              user_mi_duration=self.request.get('mi_duration'),
                              user_mi_role=self.request.get('mi_role'),
                              user_ma_organization=self.request.get('ma_organization'),
                              user_ma_description=self.request.get('ma_description'),
                              user_ma_duration=self.request.get('ma_duration'),
                              user_ma_role=self.request.get('ma_role'),
                              user_extra_curri=self.request.get('extra_curricular'),
                              user_achievements=self.request.get('achievements'),
                              user_strength=self.request.get('strength'),
                              user_weakness=self.request.get('weakness'),
                              user_hobbies=self.request.get('hobbies'),
                              user_dob=self.request.get('dob'),
                              user_gender=self.request.get('gender'),
                              user_nationality=self.request.get('nationality'),
                              user_marital_status=self.request.get('marital_status'),
                              user_lang_known=self.request.get('lang_known'),
                              user_mother_tongue=self.request.get('mother_tongue'),
                              user_father_name=self.request.get('father_name'),
                              user_hod=self.request.get('hod'),
                              user_date=self.request.get('date'),
                              user_name=self.request.get('username'),
                              user_pwd=self.request.get('password'))
        login_details.put()
        self.response.write('database updated')


class LoginHandler(webapp2.RequestHandler):
    def post(self):
        global given_user_name
        global given_first_name
        global given_last_name
        global given_user_addr

        global given_user_obj
        global given_user_city
        global given_user_state
        global given_user_pin
        global given_user_email
        global given_user_phno
        global given_user_clgname
        global given_user_affiliated_to
        global given_user_current_avg
        global given_user_twelthpercent
        global given_user_tenthpercent
        global given_user_tech_skills
        global given_user_it_organization
        global given_user_it_description
        global given_user_it_duration
        global given_user_it_role
        global given_user_mi_organization
        global given_user_mi_description
        global given_user_mi_duration
        global given_user_mi_role
        global given_user_ma_organization
        global given_user_ma_description
        global given_user_ma_duration
        global given_user_ma_role
        global given_user_extra_curri
        global given_user_achievements
        global given_user_strength
        global given_user_weakness
        global given_user_hobbies
        global given_user_dob
        global given_user_gender
        global given_user_nationality
        global given_user_marital_status
        global given_user_lang_known
        global given_user_mother_tongue
        global given_user_father_name
        global given_user_hod
        global given_user_date
        
        given_user_name=self.request.get('username')
       
        
        #self.response.headers['Content-Type'] = 'text/html'
        #self.response.write('<html><h1><center>Resume</center></h1><body style="color:#000000" vlink="#6699FF"><hr><div align="right">'+a+b+'<br></div>')
        given_user_pwd=self.request.get('password')
 
       
 
        q=LoginDB.query(LoginDB.user_name==given_user_name)
        self.response.write('<br>')
        self.response.write('<br>')
        
        x=q.fetch()
        if len(x)==0:
            self.response.write('please sign up')
        else:
            
            for i in x:
                y=i.user_pwd
                a=i.first_name
                b=i.last_name
                c=i.user_addr
                d=i.user_obj
                e=i.user_city
                f=i.user_state
                g=i.user_pin
                h=i.user_email
                j=i.user_phno
                k=i.user_clgname
                l=i.user_affiliated_to
                m=i.user_current_avg
                n=i.user_twelthpercent
                o=i.user_tenthpercent 
                p=i.user_tech_skills
                q=i.user_it_organization
                r=i.user_it_description
                s=i.user_it_duration
                t=i.user_it_role
                u=i.user_mi_organization
                v=i.user_mi_description
                w=i.user_mi_duration
                cz=i.user_mi_role
                cx=i.user_ma_organization
                z=i.user_ma_description
                ab=i.user_ma_duration
                bc=i.user_ma_role
                cd=i.user_extra_curri
                ef=i.user_achievements
                gh=i.user_strength
                ij=i.user_weakness
                kl=i.user_hobbies
                mn=i.user_dob
                op=i.user_gender
                qr=i.user_nationality
                st=i.user_marital_status
                uv=i.user_lang_known
                wx=i.user_mother_tongue
                yz=i.user_father_name
                az=i.user_hod
                bx=i.user_date

               
                self.response.write(' ')
                self.response.write('<br>')
            if y==given_user_pwd:
                self.response.write('<html><font size="2"><div align="left">'+a+' '+b+'<br>Address:'+c+'<br>Phone No.:'+j+'<br>Email id:'+h+'</div></font><hr>')
                self.response.write('<font size="3">'
                                    '<b>Career Objective:</b>'+d+
                                    '<br><br><b>Academic Record:</b><ul><li><b>Profesional Qualification:</b></li></ul><ul style="list-style-type:circle"><li>Pursuing Bachelor of Engineering from '+k+','+e+' '+f+' affiliated to '+l+' with specialization in Computer Science(2012-2016)(Current Average-'+m+' CGPA)<br><br></li></ul>'
                                    '<ul><li><b>Educational Qualification:</li></b></ul><ul style="list-style-type:circle"><li>Senior Secondary School Certificate (10+2) from Board of Secondary Education Bhopal M.P. with' +n+'%</li></ul>'
'<ul style="list-style-type:circle"><li>Higher School Certificate (10th) from Board of Secondary Education Bhopal M.P. with' +o+'%</li></ul>'
'<br><b>IT Skills:</b>'+p+
'<br><br><b>Training:</b><br><ul><li><b>Industrial Training:</b></li>Organization:'+q+
'<br>Description:'+r+
'<br>Duration:'+s+
'<br>Role:'+t+
'<br><br><li><b>Minor Project:</b></li>Organization:'+u+
'<br>Description:'+v+
'<br>Duration:'+w+
'<br>Role:'+cz+
'<br><br><li><b>Major Project:</b></li>Organization:'+cx+
'<br>Description:'+z+
'<br>Duration:'+ab+
'<br>Role:'+bc+'/ul>'   
'<br><br><b>Extra Curricular Activities:</b>'+cd+
'<br><br><b>Achievements:</b>'+ef+
'<br><br><b>Strengths:</b>'+gh+
'<br><br><b>Weakness:</b>'+ij+
'<br><br><b>Hobbies:</b>'+kl+
'<br><br><b>Personal Details:</b><br>Date Of Birth     :'+mn+
'<br>Gender            :'+op+
'<br>Nationality       :'+qr+
'<br>Marital Status    :'+st+
'<br>Language Known    :'+uv+
'<br>Mother Tongue     :'+wx+
'<br>Fathers Name      :'+yz+
'<br><br><b>References:</b><br>Prof. '+az+' (HOD,'+k+')<br><br><b>Declaration:</b>I here by declare that the information furnished above is true to the best of my knowledge.<br>Date:'
+bx+'<br>Place:'+e+'<div align="center">'+a+' '+b+'</div><br><br></font>')
            else:
                self.response.write('password does not match')
class Welcome(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html>'+head+'<body>'+LoginForm+'<br>'+SignupForm+'</body></html>')

app = webapp2.WSGIApplication([
    ('/', Welcome),('/login',LoginHandler),('/signup',SignupHandler)], debug=True)

