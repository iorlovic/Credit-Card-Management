class Config:
    SECRET_KEY = 'your-generated-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#import os

#class Config:
#    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
#    MYSQL_HOST = 'localhost'
#    MYSQL_USER = 'root'
#    MYSQL_PASSWORD = 'cpsc408!'
#    MYSQL_DB = 'creditapp'
