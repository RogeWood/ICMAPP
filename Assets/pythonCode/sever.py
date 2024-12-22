from flask import Flask, jsonify, request, send_file
from code1_kappa import kappa_main
from code2_minimize import minimize_main
from code3_QRfactor import QRfactor_main
from code4_fixed_iteration import fixed_iteration_main
from code5_fixed_solve import fixed_solve_main
from code6_secent_method import secent_method_main

app = Flask(__name__)

@app.route('/run_python_code', methods=['GET'])
def run_python_code():
    # Your Python logic goes here
    result = "run success"
    return result

# code1
@app.route('/kappa', methods=['GET'])
def kappa():
    # Get the string input from the URL query parameter
    input_string = request.args.get('input_string', '')  # Default to empty string if not provided
    
    # Process the input string (for example, convert to uppercase)
    result = input_string.upper()
    result = kappa_main(result)
    # Return the result as a JSON response
    return result

# code2
@app.route('/minimize', methods=['GET'])
def minimize():
    # Get the string input from the URL query parameter
    input_string = request.args.get('input_string', '')  # Default to empty string if not provided
    
    # Process the input string (for example, convert to uppercase)
    result = input_string.upper()
    result = minimize_main(result)
    # Return the result as a JSON response
    return result

# code3
@app.route('/qrfactor', methods=['GET'])
def qrfactor():
    # Get the string input from the URL query parameter
    input_string = request.args.get('input_string', '')  # Default to empty string if not provided
    
    # Process the input string (for example, convert to uppercase)
    result = input_string.upper()
    result = QRfactor_main(result)
    # Return the result as a JSON response
    return result

# code4
@app.route('/fixedIteration', methods=['GET'])
def fixedIteration():
    # Get the string input from the URL query parameter
    input_string = request.args.get('input_string', '')  # Default to empty string if not provided
    
    # Process the input string (for example, convert to uppercase)
    result = input_string.upper()
    result = fixed_iteration_main(result)
    # Return the result as a JSON response
    result = send_file("fixed_point_iterations.png", mimetype='image/png')
    return result

# code5
@app.route('/fixedSolve', methods=['GET'])
def fixedSolve():
    # Get the string input from the URL query parameter
    input_string = request.args.get('input_string', '')  # Default to empty string if not provided
    
    # Process the input string (for example, convert to uppercase)
    result = input_string.upper()
    result = fixed_solve_main(result)
    # Return the result as a JSON response
    return result

# code6
@app.route('/secentMethod', methods=['GET'])
def secentMethod():
    # Get the string input from the URL query parameter
    input_string = request.args.get('input_string', '')  # Default to empty string if not provided
    
    # Process the input string (for example, convert to uppercase)
    result = input_string.upper()
    result = secent_method_main(result)
    # Return the result as a JSON response
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
