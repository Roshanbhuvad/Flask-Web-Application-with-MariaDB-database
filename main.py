from app import app
# from flask_restful import Api, jsonify
from flask import Flask, request, render_template, json, jsonify
import mysql.connector as mariadb

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'b@yC@nl0g!n',
    'port': 3306
}

app = Flask(__name__)
@app.route('/')
def studentlogin():
    return render_template('studentlogin.html')
# create Student
@app.route('/create', methods=['GET', 'POST'])
def create():
    if (request.method == 'POST'):
        try:
            # id = request.form['id']
            roll_no = request.form['roll_no']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            conn = mariadb.connect(
                user='root', password='b@yC@nl0g!n', database='class')
            cursor = conn.cursor()
            sql = "INSERT INTO student (roll_no,first_name, last_name, email) VALUES ('{}','{}','{}','{}')". format(
                roll_no, first_name, last_name, email)
            cursor.execute(sql)
            conn.commit()
            return render_template("output.html", msg="Data has been stored")
            # return res
        except:
            return "database connection error"
        finally:
            '''cursor.close()
            conn.close()'''


@app.route('/student_fetch')
def student_fetch():
    try:
        conn = mariadb.connect(
            user='root', password='b@yC@nl0g!n', database='class')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    '''finally:
        cursor.close()
        conn.close()'''


@app.route('/studentupdate/<int:roll_no>')
def studentUpdate(roll_no):
    try:
        conn = mariadb.connect(
            user='root', password='b@yC@nl0g!n', database='class')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE roll_no=4", roll_no)
        row = cursor.fetchone()
        res = jsonify(row)
        res.status_code = 200
        # return render_template("show.html", row=row)
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update')
def list():
    conn = mariadb.connect(
        user='root', password='b@yC@nl0g!n', database='class')
    cur = conn.cursor()
    cur.execute("Select * from student")
    rows = cur.fetchall()
    return render_template("show.html", rows=rows)


@app.route('/updatestudent', methods=['POST'])
def updatestudent():
    if (request.method == 'POST'):
        try:

            # student_id = _json['id']
            roll_no = request.form['roll_no']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            print(roll_no)
            print(first_name)
            print(last_name)
            print(email)

            conn = mariadb.connect(
                user='root', password='b@yC@nl0g!n', database='class')
            cursor = conn.cursor()
            # update record in database
            cursor.execute("UPDATE student SET first_name='roshan', last_name='bhuvad',email='roshanbhuva15@gmail.com' WHERE roll_no='{}'" .format(
                roll_no, first_name, last_name, email))
            conn.commit()
            return render_template('update.html', msg="Data updated")
        except:
            return "database connection error"

# Delete Studentdata record from database


@app.route('/deletestudent/<int:roll_no>', methods=['DELETE'])
def deletestudent(roll_no):
    try:
        conn = mariadb.connect(
            user='root', password='b@yC@nl0g!n', database='class')
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM student WHERE roll_no=1", (roll_no))
        conn.commit()
        res = jsonify('Student deleted successfully.')
        res.status_code = 200
        return res

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'There is no record: ' + request.url
    }
    res = jsonify(message)
    res.status_code = 404

    return res


if __name__ == "__main__":
    app.run(debug=True)
