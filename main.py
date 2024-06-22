from flask import Flask, render_template, request, redirect, url_for
from database import create_table, create_student, get_student, get_all_students
from qrcode_generator import generate_qrcode

app = Flask(__name__)

# Create the 'students' table if it doesn't exist
create_table()

@app.route('/')
def index():
    students = get_all_students()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        class_name = request.form['class']
        marks = {
            'subject1': request.form['subject1'],
            'subject2': request.form['subject2'],
            'subject3': request.form['subject3'],
        }

        student_id = create_student(name, class_name, marks)
        generate_qrcode(student_id)

        return redirect(url_for('index'))

    return render_template('add_student.html')

@app.route('/student/<int:student_id>')
def view_student(student_id):
    student = get_student(student_id)
    if student:
        return render_template('view_student.html', student=student)
    else:
        return "Student not found"

if __name__ == '__main__':
    app.run(debug=True)




