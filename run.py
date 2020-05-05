from bike import create_app,db
from bike.auth.models import Users


flaskApp=create_app('prod')
with flaskApp.app_context():
    db.create_all()
    if not Users.query.filter_by(user_name='Sri_Ganesh_Cars').first():
        Users.create_user(user='Sri_Ganesh_Cars',email='sriganeshcars@gmail.com',password='secret')
    flaskApp.run(debug=True)