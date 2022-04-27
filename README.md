# Making an API Request using python's urllib package modules
## - request
## - parse
## Also import the json module
# instructions 
- import the request module from the urtllib package
- create a request variable and assign it to the value you get when you invoke the urlopen function of the request module (req=request.urlopen(url)) 
- create another variable and assign it to the value you get when you access the read() function chained to the request variables value ( var= req.read())
- Data received above will be of byte type convert it, to a python dictionary (pass it as a argument to the json.loads() method) (data=json.loads(var))
- use tha value from tha data in any way you wan't in your project