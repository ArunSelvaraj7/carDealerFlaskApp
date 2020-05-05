from bike import db

class Vehicle(db.Model):
    __tablename__='vehicle'
    id=db.Column(db.Integer,primary_key=True)
    vehicleNumber=db.Column(db.String(15),nullable=False)
    
    make=db.Column(db.String(30),nullable=False)
    model=db.Column(db.String(30),nullable=False)
    year=db.Column(db.Integer,nullable=False)
    # isInsurance=db.Column(db.String(10),nullable=False)
    insuranceEndDate=db.Column(db.String(20))

    salePrice=db.Column(db.Float,nullable=False)
    purchaseDate=db.Column(db.String(20),nullable=False)
    purchaseShop=db.Column(db.String(30),nullable=False)
    isSold=db.Column(db.String(10),nullable=False)

    isDealer=db.Column(db.String(10))
    buyerName=db.Column(db.String(15))
    address=db.Column(db.String(45))
    phoneNo=db.Column(db.String(12))
    idNumber=db.Column(db.String(30))
    url=db.Column(db.String(200))

    purchasePrice=db.Column(db.Float)
    soldPrice=db.Column(db.Float)
    soldDate=db.Column(db.String(20))
    owners=db.Column(db.String(30))
    engine=db.Column(db.String(40))
    chasis=db.Column(db.String(40))
    finance=db.Column(db.String(50))
    colour=db.Column(db.String(20))
    kms=db.Column(db.Integer)
    fuel=db.Column(db.String(20))

    

    def __init__(self,vehicleNumber,insuranceEndDate,purchaseDate,year,
    make,model,purchaseShop,isSold,isDealer,buyerName,address,phoneNo,idNumber,salePrice,url,
    purchasePrice,soldPrice,owners,engine,chasis,finance,colour,kms,fuel,soldDate):
        self.insuranceEndDate=insuranceEndDate
        self.vehicleNumber=vehicleNumber
        self.salePrice=salePrice
        self.purchaseDate=purchaseDate
        self.year=year
        self.purchaseShop=purchaseShop
        self.make=make
        self.model=model
        self.isSold=isSold
        self.isDealer=isDealer
        self.buyerName=buyerName
        self.address=address
        self.phoneNo=phoneNo
        self.idNumber=idNumber
        self.url=url
        self.purchasePrice=purchasePrice
        self.soldPrice=soldPrice
        self.owners=owners
        self.engine=engine
        self.chasis=chasis
        self.finance=finance
        self.colour=colour
        self.kms=kms
        self.fuel=fuel
        self.soldDate=soldDate
    
    def __repr__(self):
        return 'The Vehicle number is {}'.format(self.vehicleNumber)
