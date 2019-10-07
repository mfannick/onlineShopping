from . import db,admin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import func


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255),index =True)
  role=db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True,index = True)
  pass_secure = db.Column(db.String(255))
  product = db.relationship('Product',backref = 'user',lazy = "dynamic")
  orderId = db.relationship('Order',backref = 'user',lazy = "dynamic")
  @property
  def password(self):
      raise AttributeError('You cannot read the password attribute')
  @password.setter
  def password(self,password):
      self.pass_secure = generate_password_hash(password)
  def verify_password(self,password):
      return check_password_hash(self.pass_secure,password)
  def __repr__(self):
      return '<User %r>' % (self.username)


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer,primary_key = True)
    productName = db.Column(db.String)
    productSize=db.Column(db.String(255))
    productCategory=db.Column(db.String)
    productPrice = db.Column(db.String(255))
    productPicPath = db.Column(db.String(120),default='image.jpg')
    productItems=db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    userId = db.Column(db.Integer,db.ForeignKey("users.id"))
    orderId = db.relationship('Order',backref = 'product',lazy = "dynamic")


    def __repr__(self):
        return '<Product %r>' % (self.id) 

    def saveProduct(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def getProduct(cls,id):
        product = product.query.filter_by(userId=id).all()
        return product

class Order(db.Model):
 __tablename__ = 'orders'
 id = db.Column(db.Integer, primary_key=True)
 productName = db.Column(db.String(20))
 productPrice = db.Column(db.Integer)
 productCategory = db.Column(db.String(10))
 productQuantity= db.Column(db.Integer)
 userId = db.Column(db.Integer,db.ForeignKey("users.id"))
 productId = db.Column(db.Integer,db.ForeignKey("products.id"))
 def __repr__(self):
      return '<Order %r>' % (self.id)

class Contact(db.Model):
 __tablename__ = 'contacts'
 id = db.Column(db.Integer, primary_key=True)
 email = db.Column(db.String(20))
 subject = db.Column(db.String(255))
 message = db.Column(db.String(255))
 
 def __repr__(self):
      return '<Contact %r>' % (self.id)

class Subscribe(db.Model):
 __tablename__ = 'subscribes'
 id = db.Column(db.Integer, primary_key=True)
 email = db.Column(db.String(20))
 
 def __repr__(self):
      return '<Subscribe %r>' % (self.id)




class MyModelView(ModelView):
    pass
    # def is_accessible(self):
    #    return current_user.is_authenticated

admin.add_view(MyModelView(Product,db.session))
admin.add_view(MyModelView(Order,db.session))
admin.add_view(MyModelView(User,db.session))























     


 

