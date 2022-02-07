from http.client import NOT_FOUND
import json
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
        
@app.route('/add', methods=['POST'])
def add_data():
    try:

        _json = request.json
        _name =_json['name']
        _email =_json['email']
        _phone =_json['phone']
        _address =_json['address']		
        if _name and _email and _phone and _address and request.method == 'POST':			
            sqlQuery = "INSERT INTO customer(name, email, phone, address) VALUES(%s, %s, %s, %s, %s)"
            bindData = (_name, _email, _phone, _address)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('customer added successfully!')
            respone.status_code = 200
            return respone
        else:
            return 'not found !'
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/customer')
def customer_view():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, email, phone, address FROM customer")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/customer/<int:id>')
def customer_view(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, email, phone, address FROM customer WHERE id =%s", id)
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['PUT'])
def update_data():
    try:

        _json = request.json
        _id=json['id']
        _name =_json['name']
        _email =_json['email']
        _phone =_json['phone']
        _address =_json['address']		
        if _name and _email and _phone and _address and _id and request.method == 'PUT':			
            sqlQuery = "UPDATE customer SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            bindData = (_name, _email, _phone, _address,_id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('customer updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return 'not found !'
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


if __name__ == "__main__":
    app.run()