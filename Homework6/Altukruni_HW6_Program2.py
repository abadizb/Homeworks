from wsgiref.simple_server import make_server
import sqlite3
conn = sqlite3.connect("zoo.sqlite")
cursor = conn.cursor()


def Value(post_str):
	form = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	return form

def Animal_DB(environ, start_response):      
        message=""
        status = '200 OK'
        headers = [('Content-type', 'html; charset=utf-8')]
        start_response(status, headers)
        if(environ['REQUEST_METHOD'] == 'POST'):
                message += "<br>Your data has been recieved:"
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
                form = Value(request_body)
                
                for item in form.keys():
                        message += "<br/>"+item + " = " + form[item]
                        if item == "animal":
                                a = form[item]
                        elif item == "count":
                                b = form[item]
                        else:
                                continue
                animal = [(a,b)]
                cursor.executemany("insert into animal_count(name,count) values(?,?)", animal)
                result = cursor.execute("select * from animal_count")
                conn.commit()
                conn.close()
        message += "<h1>Welcome to the Zoo</h1>"
        message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
        message += "<br><br>Count:<input type=text name='count'>"
        message += "<br><br><input type='submit' name='Submit' ></form>"
        return[bytes(message,'utf-8')]

httpd = make_server('', 8000, Animal_DB)
print("Serving on port 8000...")


httpd.serve_forever()
