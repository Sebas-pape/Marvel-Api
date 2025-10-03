from flask import Blueprint, jsonify
from config import supabase_client as supabase

search = Blueprint("search", __name__)
    
@search.route("/search/<name>", methods=["GET"])

def search_comic(name):
    try:
        #response = supabase.table("comics").select("*").like("name", f"%{name}%").execute()
        response = (
            supabase
            .table("comics")
            .select("*")
            .ilike("name", name)  # tener en cuenta los parametros ya que ilike o eq funcionan igual para este caso
            .limit(20)
            .execute()
        )
        print(response)
        return jsonify({"status": "ok", "data": response.data})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500   
    

    