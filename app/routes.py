from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from .forms import CreateService, UpdateService, SignUpForm, LoginForm, Createaddon, Updateaddon
from .models import Service, User,Addons, Contact
from app import app
from werkzeug.security import check_password_hash
from flask_login import logout_user, login_user, current_user

# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# Home/Login/Register/Logout/

@app.route('/')
def homePage():

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])    
def loginPage():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()
        # SELECT * FROM user WHERE username = <username variable>
            if user:
                if check_password_hash(user.password, password):  # <--NEW
                #user.password == password:  --OLD way
                    flash('YAY, you\'re logged in!', 'success')
                    login_user(user)
                    
                    return redirect(url_for('homePage'))
                    
                else:
                    flash('WRONG password. . .', 'warning')
            else:
                flash('This isn\'t a user!', 'danger')
            return redirect(url_for('loginPage'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def registerPage():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            if User.query.filter_by(username=username).first():
                flash('That username already exists, please try another!', 'warning')
                return redirect(url_for('registerPage'))
            if User.query.filter_by(email=email).first():
                flash('that email has been used previously, try again', 'warning')
                return redirect(url_for('registerPage'))

            user = User(username, email, password)            
            user.saveUser()

            flash(f'Welcome to INSTURBlog {user.username}', 'success')
            return redirect(url_for('loginPage'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logOut():
    logout_user()
    return redirect(url_for('homePage'))

#Services

@app.route('/serv', methods=['GET'])
def shop_home():
    servs = Service.query.all()
    return render_template('serv.html', servs = servs)

@app.route('/serv/create', methods=['GET', 'POST'])
def createProd():
    form = CreateService()
    if request.method == 'POST':
        if form.validate():
            details1 = form.details1.data
            details2 = form.details2.data
            details3 = form.details3.data
            details4 = form.details4.data
            details5 = form.details5.data
            details6 = form.details6.data
            details7 = form.details7.data
            details8 = form.details8.data
            img_url = form.img_url.data
            name = form.name.data
            price = form.price.data
            new = Service( details1, details2, details3,details4,details5,details6,details7,details8,img_url, name, price)
            new.saveService()
            flash('Service created!', category='success')
            return redirect(url_for('shop_home'))
    return render_template('create.html', form=form)

@app.route('/serv/update/<int:serv_id>', methods=['GET', 'POST'])
def updateProd(serv_id):
    form = UpdateService()
    serv = Service.query.get(serv_id)
    if request.method == 'POST':
        details1 = form.details1.data
        details2 = form.details2.data
        details3 = form.details3.data
        details4 = form.details4.data
        details5 = form.details5.data
        details6 = form.details6.data
        details7 = form.details7.data
        details8 = form.details8.data
        img_url = form.img_url.data
        name = form.name.data
        price = form.price.data

        serv.details1 = details1
        serv.details2 = details2
        serv.details3 = details3
        serv.details4 = details4
        serv.details5 = details5
        serv.details6 = details6
        serv.details7 = details7
        serv.details8 = details8
        serv.img_url = img_url
        serv.name = name
        serv.price = price
        serv.saveChanges()
        flash('Product updated!', category='success')
        return redirect(url_for('createAdd', serv_id=serv_id))
    return render_template('update.html', serv=serv, form=form, serv_id=serv_id)

@app.route('/serv/delete/<int:serv_id>', methods=['GET', 'POST'])
def delProd(serv_id):
    service = Service.query.get_or_404(serv_id)
    service.deleteService()
    flash('Service has been deleted. Goodbye!', category='danger')
    return redirect(url_for('shop_home'))

# Addons

@app.route('/serv/createa', methods=['GET', 'POST'])
def createAdd():
    form = Createaddon()
    if request.method == 'POST':
        if form.validate():
            det1 = form.det1.data
            det2 = form.det2.data
            det3= form.det3.data
            det4 = form.det4.data
            new = Addons( det1, det2,det3,det4)
            new.savedet()
            flash('Addon created!', category='success')
            return redirect(url_for('shop_home'))
    return render_template('createa.html', form=form)

@app.route('/addons/delete/<int:addon_id>', methods=['POST'])
def delete_addon(addon_id):
    addon = Addons.query.get_or_404(addon_id)
    addon.delete()  # Call the delete() method from the Addons model
    flash('Addon deleted!', category='success')
    return redirect(url_for('view_addons'))

@app.route('/addons', methods=['GET'])
def view_addons():
    addons = Addons.query.all()  # Retrieve all addons from the database
    return render_template('addons.html', addons=addons)

@app.route('/addons/update/<int:addon_id>', methods=['GET', 'POST'])
def update_addon(addon_id):
    form = Updateaddon()
    addon = Addons.query.get(addon_id)
    if request.method == 'POST':
        addon.det1 = form.det1.data
        addon.det2 = form.det2.data
        addon.det3 = form.det3.data
        addon.det4 = form.det4.data
        addon.saveadd()
        flash('Addon updated!', category='success')
        return redirect(url_for('view_addons'))
    return render_template('update_addon.html', addon=addon, form=form, addon_id=addon_id)

#Customer

@app.route('/customers')
def customers():
    contacts = Contact.query.all()
    return render_template('customers.html', contacts=contacts)

@app.route('/customers/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    contact.deletecontact()
    flash('Contact deleted!', category='success')
    return redirect(url_for('customers'))

@app.route('/api/contact', methods=['POST'])
def create_contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    services = request.form['services']
    message = request.form['message']

    contact = Contact(name=name, phone=phone, email=email, services=services, message=message)
    contact.saveCon()
    
    return jsonify({'message': 'Contact created successfully.'})

# Api

@app.route('/shop')
def productDB():
    y = Service.query.all()
    prodlist = [p.to_dict() for p in y]
    return {
        'status': 'ok',
        'data' : prodlist,
        'item_count' : len(prodlist)
    }

@app.route('/shop/<int:service_id>')
def indPost(service_id):
    product = Service.query.get(service_id)
    if product:
        p = product.to_dict() 
        return {
            'status': 'ok',
            'data': p,
            'item_count': 1 
        }
    else:
        return {
            'status': 'error',
            'message': 'Product not found'
        }, 404 
    
@app.route('/shops')
def addonDB():
    y = Addons.query.all()
    prodlist = [p.to_dict() for p in y]
    return {
        'status': 'ok',
        'data' : prodlist,
        'item_count' : len(prodlist)
    }