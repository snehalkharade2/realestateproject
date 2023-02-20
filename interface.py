from flask import Flask,render_template,request,jsonify
import config
from utils import Estate
import traceback

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/house_price", methods = ["GET", "POST"])
def house_price():
    try:
        if request.method == "POST":
            data = request.form.get
            print("User Data is ", data)

            X1_transaction_date = eval(data("X1_transaction_date"))
            X2_house_age = eval(data("X2_house_age"))
            X3_distance_to_the_nearest_MRT_station = eval(data("X3_distance_to_the_nearest_MRT_station"))
            X4_number_of_convenience_stores = eval(data("X4_number_of_convenience_stores")) 
            X5_latitude = eval(data("X5_latitude"))
            X6_longitude = eval(data("X6_longitude"))


            pred_price = Estate(X1_transaction_date, X2_house_age, X3_distance_to_the_nearest_MRT_station, X4_number_of_convenience_stores, X5_latitude, X6_longitude)
            price_of_house = pred_price.get_price_prediction()

            
            return render_template("index.html",prediction = price_of_house )
               
        else:
            data = request.args.get
            print("User Data is :",data)
            
            X1_transaction_date = eval(data("X1_transaction_date"))
            X2_house_age = eval(data("X2_house_age"))
            X3_distance_to_the_nearest_MRT_station = eval(data("X3_distance_to_the_nearest_MRT_station"))
            X4_number_of_convenience_stores = eval(data("X4_number_of_convenience_stores")) 
            X5_latitude = eval(data("X5_latitude"))
            X6_longitude = eval(data("X6_longitude"))


            pred_price = Estate(X1_transaction_date, X2_house_age, X3_distance_to_the_nearest_MRT_station, X4_number_of_convenience_stores, X5_latitude, X6_longitude)
            price_of_house = pred_price.get_price_prediction()

            
            return render_template("index.html",prediction =  price_of_house )
    except:
        print(traceback.print_exc())
        return jsonify({"Message" : "Unsuccessful"}) 

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config.PORT_NUMBER, debug = True)

        
            