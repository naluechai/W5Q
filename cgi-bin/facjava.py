#!/usr/bin/python3
print("Content-type: text/html\r\n\r\n")
print('<html><head>')
print('<script type = "text/javascript">')
print('function fac(){var i=0,f=1,n=document.getElementById("num").value;')
print('for (i;i<n;i++){f *= (i+1);}document.write(f);}')
print('</script><input type="text" id="num">')
print('<input type="button" onclick="fac()" value="enter">')
print('</head></html>')