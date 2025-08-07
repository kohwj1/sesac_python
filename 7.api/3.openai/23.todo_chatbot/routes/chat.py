from dotenv import load_dotenv
from flask import request, jsonify, Blueprint
import services.chat_service as svc

load_dotenv()
chat_bp = Blueprint('chat', __name__)

@chat_bp.route('', methods=['POST'])
def chat_to_bot():
    data = request.get_json()
    res = svc.request_to_bot(data.get('user_input'))

    return jsonify({'chatbot':res}), 200
