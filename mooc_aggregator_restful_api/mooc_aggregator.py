'''
This module aggregates all the course information from different MOOC platforms
and stores them in the database (MongoDB)
'''
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine

from udacity import UdacityAPI
from coursera import CourseraAPI


class MOOCAggregator(object):
    '''
    This class defines the attributes and methods for the MOOC aggregator

    '''
    MOOC_PLATFORMS = {'udacity', 'coursera'}

    def __init__(self):
        self.udacity = UdacityAPI()
        self.coursera = CourseraAPI()
        connect('moocs')

if __name__ == '__main__':
    pass
