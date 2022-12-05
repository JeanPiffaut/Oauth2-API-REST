from flask_restful import Api


def response_structure(code_status: int, response=None, message=None):
    if code_status == 200 or code_status == 201:
        status = 'Success'
    else:
        status = 'Error'

    args = dict()
    args['status'] = status
    if message is not None:
        args['message'] = message

    if response is not None:
        args['response'] = response

    return args, code_status


class ExtendAPI(Api):

    def handle_error(self, e):
        return response_structure(e.code, str(e))
