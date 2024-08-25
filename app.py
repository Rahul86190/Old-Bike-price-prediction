from flask import Flask,render_template,request
import joblib
import sqlite3

model=joblib.load("./models/bike_by_randomForest_2.lb")
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/predict")
def predict():
    return render_template("predict.html")
@app.route("/rate_us")
def rate_us():
    return render_template("rate_us.html")

@app.route("/data",methods=["GET","POST"])
def data():
    if request.method=="POST":
        brand=int(request.form["bike_type"])
        kms_driven=int(request.form["kilometers_driven"])
        owner=int(request.form["owner"])
        age=int(request.form["years_used"])
        power=int(request.form["power"])
        # return str(brand)

        brand_dict={'Bajaj': 1, 'Royal Enfield': 2, 'Hero': 3, 'Honda': 4, 'Yamaha': 5, 'TVS': 6, 'KTM': 7, 'Suzuki': 8, 'Harley-Davidson': 9, 'Kawasaki': 10, 'Hyosung': 11, 'Mahindra': 12, 'Benelli': 13, 'Triumph': 14, 'Ducati': 15, 'BMW': 16}
        brand_dict2 = {value:key for key ,value in brand_dict.items() }

        unseen_data=[[kms_driven,owner,age,power,brand]]

        PREDICTION=model.predict(unseen_data)[0]  # array  format  , retuen for 0th position

        query_to_insert = """
        Insert into bikedetail values(?,?,?,?,?,?)
        """
        conn = sqlite3.connect("bikedata.db")
        cur=conn.cursor()
        data=(owner,brand_dict2[brand],kms_driven,power,age,int(PREDICTION))
        cur.execute(query_to_insert,data)
        print("record has stored in database")
        cur.close()
        conn.close()
              
        # PREDICTION=int(PREDICTION)
        return render_template('prediction_result.html', 
                           bike_type=brand_dict2[brand], 
                           owner=owner, 
                           kilometers_driven=kms_driven, 
                           years_used=age, 
                           power=power, 
                           prediction=int(PREDICTION))



@app.route("/type_of_bikes")
def type_of_bikes():
    return render_template("type_of_bikes.html")

if __name__=="__main__":
    app.run(debug=True)

