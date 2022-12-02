from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return handle_structure('Internal server error', {'error': str(e)}), 500

    @app.errorhandler(400)
    def handle_400_error(e):
        return handle_structure('Bad Request'), 400

    @app.errorhandler(401)
    def handle_401_error(e):
        return handle_structure('Unauthorized'), 401

    @app.errorhandler(405)
    def handle_405_error(e):
        return handle_structure('Method not allowed'), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return handle_structure('Forbidden error'), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return handle_structure('Not found error'), 404

    def handle_structure(msj, response: dict = None):
        args = {
            'status': 'error',
            'message': msj,
        }

        if response is not None:
            args['response'] = response

        return jsonify(args)
