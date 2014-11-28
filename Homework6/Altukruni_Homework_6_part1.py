from wsgiref.simple_server import make_server
import psutil,datetime

def health_server(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    message = "<h1> Welcome to the Health Server Monitor </h1>"
    message +="<table style=\"width:150%\">"
    message += "<tr>"
    message +="<td style=\"background-color:Gray\"><strong>BOOT TIME:</strong></td>"
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    message +="<td style=\"background-color:Gray\">"+str(boot_time)+"</td>"
    message +="</tr>"
    cpu_util = psutil.cpu_percent(interval=1, percpu=True)
    message += "<tr><th rowspan=\"4\"><strong>CPU UTILIZATION</strong></th>"
    
    i=1
    
    for cpu in cpu_util:
        if cpu < 20:
             message += "<td style=\"background-color:Yellow\">"
        else:
            message += "<td style=\"background-color:green\">"
            
        message += "CPU {} : {}%".format(i, cpu)
        
        i+=1
        message += "</tr>"

    

    mem = psutil.virtual_memory()
    THRESHOLD = 100 * 1024 * 1024  
    message += "<tr>"
    message +="<td style=\"background-color:Gray\"><strong>AVAILABLE MEMORY:</strong></td>"
    message +="<td style=\"background-color:Gray\">"+str(mem.available)+"</td>"
    message += "<tr>"
    message +="<td style=\"background-color:Gray\"><strong>USE PERCANTAGE:</strong></td>"
    message +="<td style=\"background-color:Gray\">"+str(mem.percent)+"</td>"
    #message +="</tr>"
    message += "<tr>"
    message += "<tr><th rowspan=\"4\"><strong>USED MEMORY</strong></th>"
    message +="<td>"+str(mem.used)+"</td>"
 #   message +="</tr>"
    message +="</tr>"
    message +="</tr>"
    message +="</tr>"

    return[bytes(message,'utf-8')]

httpd = make_server('', 8000,health_server)
print("Serving on port 8000...")


httpd.serve_forever()
