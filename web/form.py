# Import modules for CGI handling
import cgi, cgitb
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
#first_name = form.getvalue('first_name')
#last_name = form.getvalue('last_name')
month = form.getvalue('Month') #use these in the python functions
day = form.getvalue('day')
time = form.getvalue('time')
year = form.getvalue('Year')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Month is %s %s</h2>" % (month))
print ("<h2>Day is %s %s</h2>" % (day))
print ("<h2>Time is %s %s</h2>" % (time))
print ("<h2>Year is %s %s</h2>" % (year))
print ("</body>")
print ("</html>")