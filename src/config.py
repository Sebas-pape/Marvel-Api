from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
secret_key = os.getenv("SECRET_KEY")

supabase_client: Client = create_client(supabase_url, supabase_key)