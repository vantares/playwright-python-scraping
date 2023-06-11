import os
import json, yaml


from flask import Flask, after_this_request, send_file, abort, render_template, request, redirect, url_for, session
from flask_restx import Resource, Api, fields
from flask_restx.api import Swagger
from werkzeug.utils import safe_join, secure_filename

UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        # upload file flask
        target=os.path.join(UPLOAD_FOLDER,'test_docs')
        if not os.path.isdir(target):
            os.mkdir(target)
        file = request.files['file'] 
        filename = secure_filename(file.filename)
        destination="/".join([target, filename])
        file.save(destination)
        return render_template('index2.html')
    return render_template('index.html')

api = Api(
    app=app,
    doc='/docs',
    version='1.0.0',
    title='TEST APP API',
    description='TEST APP API'
    )


response_fields = api.model('Resource', {
    'value': fields.String(required=True, min_length=1, max_length=200, description='example text')
})


# This class will handle POST
@api.route('/demo/', endpoint='demo')
@api.doc(responses={403: 'Not Authorized'})
class DemoList(Resource):
    @api.expect(response_fields, validate=True)
    @api.marshal_with(response_fields, code=200)
    def post(self):
        api.payload["value"] = 'Im the response ur waiting for'
        return api.payload


@api.route('/swagger')
class HelloSwagger(Resource):
    def get(self):
        data = json.loads(json.dumps(api.__schema__))
        with open('yamldoc.yml', 'w') as yamlf:
            yaml.dump(data, yamlf, allow_unicode=True, default_flow_style=False)
            file = os.path.abspath(os.getcwd())
            try:
                @after_this_request
                def remove_file(resp):
                    try:
                        os.remove(safe_join(file, 'yamldoc.yml'))
                    except Exception as error:
                        log.error("Error removing or closing downloaded file handle", error)
                    return resp

                return send_file(safe_join(file, 'yamldoc.yml'), as_attachment=True, download_name='yamldoc.yml', mimetype='application/x-yaml')
            except FileExistsError:
                abort(404)


# main driver function
if __name__ == '__main__':
    app.run(port=5003, debug=True)
 