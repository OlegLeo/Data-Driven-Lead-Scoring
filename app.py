from flask import Flask, request, render_template, redirect, send_file
from lead_scoring import process_leads
import pandas as pd
from io import BytesIO

app = Flask(__name__)

# Global variables (for memory storage)
scored_leads = None
columns = []
top_rows = []

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global scored_leads, columns, top_rows
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/')
        
        file = request.files['file']
        if file.filename == '':
            return redirect('/')
        
        if file:
            leads = process_leads(file)
            scored_leads = pd.DataFrame(leads, columns=[ 
                "Lead ID", "Job Title", "Company Name", "Industry", "Company Size", "Email", "Location", "Score"
            ])

            # Add a fake column for the ranking
            columns = ["#"] + scored_leads.columns.tolist()
            top_rows = scored_leads.head(10).values.tolist()

            return render_template('index.html', columns=columns, top_rows=top_rows)
    
    return render_template('index.html', columns=None, top_rows=None)



@app.route('/download')
def download_file():
    if scored_leads is not None:
        output = BytesIO()
        scored_leads.to_csv(output, index=False)
        output.seek(0)

        return send_file(
            output,
            mimetype='text/csv',
            as_attachment=True,
            download_name='scored_leads.csv'
        )
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
