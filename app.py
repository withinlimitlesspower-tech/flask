import os
import logging
from flask import Flask, render_template, jsonify, request

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # In-memory counter (for demonstration purposes)
    counter = 0

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/increment', methods=['POST'])
    def increment():
        nonlocal counter
        try:
            counter += 1
            logger.info('Counter incremented to %d', counter)
            return jsonify({'count': counter, 'message': 'Counter updated successfully'}), 200
        except Exception as e:
            logger.error('Error incrementing counter: %s', str(e))
            return jsonify({'error': 'Internal server error'}), 500

    @app.route('/health')
    def health():
        logger.info('Health check requested')
        return jsonify({'status': 'healthy', 'counter': counter}), 200

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        logger.warning('Page not found: %s', request.path)
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.error('Internal server error: %s', str(error))
        return jsonify({'error': 'Internal server error'}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
