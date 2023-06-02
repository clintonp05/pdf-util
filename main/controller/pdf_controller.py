from flask import request
from flask_restplus import Resource, Namespace
from ..service.pdf_service import mergePDF, imposeImgV2

api = Namespace('pdf')


@api.route('/mergePDF')
class UserList(Resource):
    @api.response(201, 'PDF merged successfully')
    def post(self):
        """PDF merged successfully """
        mergePDF()


@api.route('/imposeSignature')
class User(Resource):
    @api.response(201, 'Signatures imposed successfully')
    def post(self):
        """impose Signature"""
        user = imposeImgV2()
      