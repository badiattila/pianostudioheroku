import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'piano_studio'
app.config["MONGO_URI"] = 'mongodb://attilabadi:K00nK00n1234@mycodeinstitutecluster-shard-00-00-wpsfr.mongodb.net:27017,mycodeinstitutecluster-shard-00-01-wpsfr.mongodb.net:27017,mycodeinstitutecluster-shard-00-02-wpsfr.mongodb.net:27017/piano_studio?ssl=true&replicaSet=MyCodeInstituteCluster-shard-0&authSource=admin&retryWrites=true&w=majority'
mongo = PyMongo(app)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='mail.pianostudio.hu',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'contact@pianostudio.hu',
	MAIL_PASSWORD = os.environ.get('SMTPPW')
	)
mail = Mail(app)

@app.route('/')
@app.route('/index')
def index():
        return render_template("index.html")

@app.route('/contact')
def contact():
        return render_template("contact.html")

@app.route('/services')
def services():
        return render_template("services.html")

@app.route('/pianos_for_sale')
def pianos_for_sale():
        return render_template("pianos_for_sale.html", pianos=mongo.db.pianos_4_sale.find(), len=mongo.db.pianos_4_sale.find().count())

@app.route('/createadd')
def createadd():
        return render_template("create_add.html")

@app.route('/rent')
def rent():
        return render_template("rent.html")
        
@app.route('/galery')
def galery():
        return render_template("galery.html")

@app.route('/insert_add', methods=['POST'])
def insert_add():
        file_id = mongo.save_file(request.files['picture'].filename, request.files['picture'])
        mongo.db.pianos_4_sale.insert({
            'brand': request.form.get('brand') , 
            'description' : request.form.get('description') , 
            'age' : request.form.get('age') , 
            'price' : request.form.get('price') , 
            'file_name' : request.files['picture'].filename})
        return redirect(url_for('pianos_for_sale'))

@app.route('/file/<file_name>')
def file(file_name):
    return mongo.send_file(file_name)
    
@app.route('/delete_piano/<piano_id>')
def delete_piano(piano_id):
    mongo.db.pianos_4_sale.remove({'_id': ObjectId(piano_id)})
    return redirect(url_for('pianos_for_sale'))    

@app.route('/edit_piano/<piano_id>')
def edit_piano(piano_id):
    return render_template('edit_piano.html', piano=mongo.db.pianos_4_sale.find_one({"_id": ObjectId(piano_id)}))


@app.route('/update_piano/<piano_id>', methods=['POST'])
def update_piano(piano_id):
    file_id = mongo.save_file(request.files['picture'].filename, request.files['picture'])
    mongo.db.pianos_4_sale.update( {'_id': ObjectId(piano_id)},
    {
            'brand': request.form.get('brand') , 
            'description' : request.form.get('description') , 
            'age' : request.form.get('age') , 
            'price' : request.form.get('price') , 
            'file_name' : request.files['picture'].filename
    })
    return redirect(url_for('pianos_for_sale'))

@app.route('/send_mail/', methods=['POST'])
def send_mail():
    try:
        msg = Message("Contact from pianostudio (" + request.form.get('user_fname') +" "+ request.form.get('user_sname') +")", sender=request.form.get('user_email'),recipients=["attila.badi@gmail.com"])
        msg.body = request.form.get('message')
        mail.send(msg)
        return render_template('contact_success.html')
    except:
        return render_template('contact_error.html')
        
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)        