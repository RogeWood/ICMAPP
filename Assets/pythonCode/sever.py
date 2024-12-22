from flask import Flask, jsonify, request
from code1_kappa import kappa_main
from code2_minimize import minimize_main
from code3_QRfactor import QRfactor_main
from code5_fixed_solve import fixed_solve_main
from code6_secent_method import secent_method_main

app = Flask(__name__)

@app.route('/run_python_code', methods=['GET'])
def run_python_code():
    # Your Python logic goes here
    result = {"message": "Hello from Python!"}
    return jsonify(result)

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

# code5
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
