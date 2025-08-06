from dotenv import load_dotenv
from flask import request, jsonify, Blueprint

load_dotenv()

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/api/chat')
def chat_to_bot():
    return jsonify({'status':'success', 'data': 'test'}), 200
