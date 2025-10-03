from flask import Blueprint, jsonify
from config import supabase_client as supabase

health = Blueprint("health", __name__)

@health.route('/health', methods=['GET'])
def health_check():
    try:
        
        # Solo intentamos hacer una consulta muy simple
        supabase.table("users").select("*").limit(1).execute()
        
        return jsonify({
            "status": "ok",
            "db_connection": True,
            "message": "API funcionando 🚀",
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "db_connection": False,
            "error": str(e)
        }), 500

    

    