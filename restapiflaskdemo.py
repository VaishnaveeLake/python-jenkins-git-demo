# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:52:23 2021

@author: VaishnaveeLake
app=express()
app.get('',())
app.post('',())

"""

import json
from flask import Flask ,jsonify,request,Response,make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields



app=Flask(__name__)     #flask constructor we pass name of current module,app is object who accepts flask 

#establishin connection toDB
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:admin@localhost:3306/devops'

db= SQLAlchemy(app)

#create table here
class Product(db.Model): #product is a model
    __tablename__="pyproducts"
    productId= db.Column(db.Integer, primary_key=True)
    productName= db.Column(db.String(40))
    description= db.Column(db.String(80))
    productCode= db.Column(db.String(60))
    price  = db.Column(db.Float)
    starRating =db.Column(db.Float)
    imgUrl=db.Column(db.String(50))

    #overriding create method
    def create(self):
        #get connection with db
        db.session.add(self)
        db.session.commit()
        return self
    #start mapping below
    def __init__(self,productName,description,productCode,price,starRating,imgUrl):
        self.productName=productName
        self.description=description
        self.productCode=productCode
        self.price=price
        self.starRating=starRating
        self.imgUrl=imgUrl
    def __repr__(self):         #if wanna give official string representation
        return "% self.productId"
    #perform all above functions
db.create_all()
        
class ProductSchema(ModelSchema):
    #inner class
    class Meta(ModelSchema.Meta):
        model= Product
        sqla_session=db.session
    productId=fields.Number(dump_only=True)
    productName=fields.String(required=True)
    description=fields.String(required=True)
    productCode=fields.String(required=True)
    price=fields.Number(required=True)
    imgUrl=fields.String(required=True)

@app.route('/products',methods=['POST'])       
def createProduct():
    data= request.get_json()        #get json data
    product_schema =ProductSchema()
    product =product_schema.load(data)  #mapping json data to productschema i.e. deserializing
    result= product_schema.dump(product.create())   #here it performs insert
    return make_response(jsonify({"product":result}),201)   #make_response make http response

@app.route('/products',methods=['GET'])
def getAllProducts():
    get_products=Product.query.all()        #it gives rows but we need rows converted into objects
    productSchema=ProductSchema(many=True)
    products=productSchema.dump(get_products)
    return make_response(jsonify({"products":products}))    


@app.route('/products/<int:productId>',methods=['GET']) #we get ele using id
def getProductById(productId):
    get_products=Product.query.get(productId)        #it gives rows but we need rows converted into objects
    productSchema=ProductSchema()
    products=productSchema.dump(get_products)
    return make_response(jsonify({"products":products}),200)    


@app.route('/products/<int:productId>',methods=['DELETE']) #we get ele using id
def deleteProductById(productId):
    get_products=Product.query.get(productId)        #it gives rows but we need rows converted into objects
    
    db.session.delete(get_products)
    db.session.commit()
    return make_response(jsonify({"products":"products deleted"}),204)    

@app.route('/products/<int:productId>',methods=['PUT']) #we get ele using id
def updateProductById(productId):
    data= request.get_json()
    get_products=Product.query.get(productId) 
    if data.get('price'):
        get_products.price=data['price']
    db.session.add(get_products)
    db.session.commit()
           
    product_schema=ProductSchema(only=['productId','price'])
    result=product_schema.dump(get_products)
    return make_response(jsonify({"products":result}),200)    


@app.route('/products/find/<productName>',methods=['GET']) #we get ele using id
def getProductByNmae(productName):
    get_products=Product.query.filter_by(productName=productName)        #it gives rows but we need rows converted into objects
    productSchema=ProductSchema(many=True)
    products=productSchema.dump(get_products)
    return make_response(jsonify({"products":products}),200)    



app.run(port=4004)
    

    
