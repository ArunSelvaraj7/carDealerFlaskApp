from flask import render_template,flash,redirect,url_for,request
from bike.garage import main
from bike.garage.models import Vehicle
from flask_login import login_required
from bike.garage.forms import Add_vehicle_form,search_form,Customer_form
from bike import db
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = r'..\bike\bike\static\images'

@main.route('/')
def display_route():
    bikes=Vehicle.query.filter_by(isSold='False').all()
    return render_template('home.html',bikes=bikes)


@main.route('/create',methods=['GET','POST'])
@login_required
def add_vehicle():
    form=Add_vehicle_form()
    if form.validate_on_submit():
        file = request.files.getlist('url')
        img=""
        if not form.isSold.data=='True' and file:
            for f in file:
                if f.filename:
                    filename = secure_filename(f.filename)
                    f.save(os.path.join(UPLOAD_FOLDER, filename))
                    if img=="":
                        img=filename
                    else:
                        img=img+","+filename
        if form.isSold=='False':
            form.soldDate.data='Nil'
            form.isDealer.data='Nil'
        user=Vehicle(
            vehicleNumber=form.vehicleNumber.data,
            insuranceEndDate=form.insuranceEndDate.data,
            purchaseDate=form.purchaseDate.data,
            year=form.year.data,
            make=form.make.data,
            model=form.model.data,
            purchaseShop=form.purchaseShop.data,
            isSold=form.isSold.data,
            soldDate=form.soldDate.data,
            isDealer=form.isDealer.data,
            buyerName=form.buyerName.data,
            address=form.address.data,
            phoneNo=form.phoneNo.data,
            idNumber=form.idNumber.data,
            salePrice=form.salePrice.data,
            url=img,
            purchasePrice=form.purchasePrice.data,
            soldPrice=form.soldPrice.data,
            owners=form.owners.data,
            engine=form.engine.data,
            chasis=form.chasis.data,
            finance=form.finance.data,
            colour=form.colour.data,
            kms=form.kms.data,
            fuel=form.fuel.data
        )
        
        db.session.add(user)
        db.session.commit()
        flash("Added Successfully")
        return redirect(url_for('main.display_route'))
    return render_template('add_vehicle.html',form=form)

@main.route('/view/<id>')
def view(id):
    bike=Vehicle.query.get(id)
    return render_template('view.html',bike=bike)

@main.route('/edit/<id>',methods=['GET','POST'])
@login_required
def edit(id):
    vehicle=Vehicle.query.get(id)
    form=Add_vehicle_form(obj=vehicle)
    
    if form.validate_on_submit():
        vehicle.vehicleNumber=form.vehicleNumber.data
        vehicle.insuranceEndDate=form.insuranceEndDate.data
        vehicle.purchaseDate=form.purchaseDate.data
        vehicle.year=form.year.data
        vehicle.make=form.make.data
        vehicle.model=form.model.data
        vehicle.purchaseShop=form.purchaseDate.data
        vehicle.isSold=form.isSold.data
        vehicle.isDealer=form.isDealer.data
        vehicle.buyerName=form.buyerName.data
        vehicle.address=form.address.data
        vehicle.phoneNo=form.phoneNo.data
        vehicle.idNumber=form.idNumber.data
        vehicle.salePrice=form.salePrice.data
        vehicle.purchasePrice=form.purchasePrice.data
        vehicle.soldPrice=form.soldPrice.data
        vehicle.owners=form.owners.data
        vehicle.engine=form.engine.data
        vehicle.chasis=form.chasis.data
        vehicle.finance=form.finance.data
        vehicle.colour=form.colour.data
        vehicle.kms=form.kms.data
        vehicle.fuel=form.fuel.data
        vehicle.soldDate=form.soldDate.data
        file = request.files.getlist('url')
        if file:
            for f in file:
                if f.filename:
                    filename = secure_filename(f.filename)
                    f.save(os.path.join(UPLOAD_FOLDER, filename))
                    if vehicle.url==None or vehicle.url=="":
                        vehicle.url=filename
                    else:
                        vehicle.url=vehicle.url+","+filename
        
        if form.isSold.data=='True' and vehicle.url != "":
            list=vehicle.url.split(',')
            for l in list:
                if os.path.exists(os.path.join(UPLOAD_FOLDER,l)):
                    os.remove(os.path.join(UPLOAD_FOLDER,l))
            vehicle.url=""

        db.session.commit()
        flash("Edited Successfully!")
        return redirect(url_for('main.display_route'))
    return render_template('edit.html',form=form,flag='edit')
    
@main.route('/delete/<b_id>',methods=['GET','POST'])
@login_required
def delete_vehicle(b_id):
    bike=Vehicle.query.get(b_id)
    if request.method == 'POST':
        if bike.url != "":
            list=bike.url.split(',')
            for l in list:
                if os.path.exists(os.path.join(UPLOAD_FOLDER,l)):
                    os.remove(os.path.join(UPLOAD_FOLDER,l))
        db.session.delete(bike)
        db.session.commit()
        flash('Deleted Successfully!')
        return redirect(url_for('main.display_route'))
    return render_template('delete.html',bike=bike)


@main.route('/search/<flag>',methods=['GET','POST'])
@login_required
def search(flag):
    form=search_form()
    if form.validate_on_submit():
        bike=Vehicle.query.filter_by(vehicleNumber=form.vehicleNumber.data).first()
        if bike and flag == 'search':
            return redirect(url_for('main.view',id=bike.id))
        elif bike and flag=='edit1':
            return redirect(url_for('main.edit',id=bike.id))
        elif bike and flag=='delete':
            return redirect(url_for('main.delete_vehicle',b_id=bike.id))
        flash('No record found!')
    return render_template('edit.html',form=form,flag=flag)


@main.route('/search-cust',methods=['GET','POST'])
@login_required
def searchCustomer():
    cust=Customer_form()
    flag='form'
    if cust.validate_on_submit():
        cust=Vehicle.query.filter_by(phoneNo=cust.phoneNo.data).all()
        flag='display'
        if not cust:
            flash('No record found!')
            return redirect(url_for('main.searchCustomer'))
    return render_template('customer.html',form=cust,flag=flag)
