from flask import Flask, render_template, request, jsonify

app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # Homepage if get it will show index.html if post it will show result.html
def ui_math():
    if request.method == 'POST':
        operation=request.form['operation'] # Get the operation from the form
        num1=int(request.form['num1'])      # Get the first number from the form
        num2=int(request.form['num2'])      # Get the second number from the form
        if (operation=="add"):              # If the operation is add
            r=num1+num2
            result=f'The sum of {num1} and {num2} is {r}'       
        elif (operation=="subtract"):       # If the operation is subtract
            r=num1-num2
            result=f'The difference of {num1} and {num2} is {r}'
        elif (operation=="multiply"):       # If the operation is multiply
            r=num1*num2
            result=f'The product of {num1} and {num2} is {r}'
        elif (operation=="divide"):         # If the operation is divide
            r=num1/num2
            result=f'The quotient of {num1} and {num2} is {r}'
        else:                               # If the operation is none of the above
            result="Invalid operation !"
        return render_template('result.html', result=result)    # Return the result to the result.html
    else:
        return render_template('index.html')                # Return the index.html if the request is GET



@app.route('/postman', methods=['POST'])        # Postman API
def math_postman():
    if (request.method=="POST"):
        operation=request.json['operation']     # Get the operation from the json
        num1=int(request.json['num1'])          # Get the first number from the json
        num2=int(request.json['num2'])          # Get the second number from the json
        if (operation=="add"):              # If the operation is add
            r=num1+num2
            result=f'The sum of {num1} and {num2} is {r}'
        elif (operation=="subtract"):       # If the operation is subtract
            r=num1-num2
            result=f'The difference of {num1} and {num2} is {r}'
        elif (operation=="multiply"):       # If the operation is multiply
            r=num1*num2
            result=f'The product of {num1} and {num2} is {r}'
        elif (operation=="divide"):         # If the operation is divide
            r=num1/num2
            result=f'The quotient of {num1} and {num2} is {r}'
        else:                               # If the operation is none of the above
            result="Invalid operation !"
        return jsonify(result=result)       # Return the result to the postman in json format



if __name__=="__main__":
    app.run()