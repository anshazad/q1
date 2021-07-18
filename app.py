import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    maximum = int(jsonObj[" Please Enter the Maximum Value : "])
     
    Oddtotal = 0

    for number in range(1, maximum+1):
      if(number % 2 != 0):
          if(number % 5  != 0):
          
           Oddtotal = Oddtotal + number

    
    response+="<b> The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))  + "</b><br>"
   
   
        
    	    
    return response
    
     
if __name__ == "__main__":
    app.run(debug=True)
    
    
