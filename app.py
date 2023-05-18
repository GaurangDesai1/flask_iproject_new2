from flask import Flask, render_template
import os

app = Flask(__name__)

theses = [
    {'id': '147', 'title': 'Thesis 1', 'subchapter': 'Subchapter 1'},
    {'id': '148', 'title': 'Thesis 2', 'subchapter': 'Subchapter 2'},
    # ...add more thesis data...
]

@app.route('/')
def index():
    return render_template('index.html', theses=theses)

@app.route('/THESIS/<thesis_id>')
def view_thesis(thesis_id):
    # Retrieve the thesis information based on the ID
    thesis = next((t for t in theses if t['id'] == thesis_id), None)
    if thesis:
        # Get the thesis title
        thesis_title = thesis['title']
        # Get the absolute path to the THESIS folder
        thesis_folder = os.path.join(app.root_path, 'THESIS', thesis_id)
        return render_template('thesis.html', thesis=thesis, thesis_folder=thesis_folder, thesis_title=thesis_title)
    else:
        return 'Thesis not found'

if __name__ == '__main__':
    app.run()
