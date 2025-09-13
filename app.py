from flask import Flask, render_template, request, send_file
import pikepdf
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get uploaded PDF and password from form
        pdf_file = request.files['pdf']
        password = request.form['password']
        
        if pdf_file and password:
            try:
                # Open the PDF with the provided password
                pdf = pikepdf.open(pdf_file, password=password)
                
                # Create an in-memory buffer for the unlocked PDF
                unlocked_buffer = BytesIO()
                
                # Save without encryption (removes password)
                pdf.save(unlocked_buffer)
                
                # Reset buffer position for reading
                unlocked_buffer.seek(0)
                
                # Send the unlocked PDF as a downloadable file
                return send_file(
                    unlocked_buffer,
                    as_attachment=True,
                    download_name='unlocked_' + pdf_file.filename,
                    mimetype='application/pdf'
                )
            except pikepdf.PasswordError:
                return "Incorrect password. Please try again.", 400
            except Exception as e:
                return f"Error processing PDF: {str(e)}", 500
    
    # Render the form on GET
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)