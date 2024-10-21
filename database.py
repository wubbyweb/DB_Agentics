# database.py

from supabase import create_client, Client
import os

# Initialize Supabase client
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def order_db_query(query):
    try:
        # Execute the query using Supabase
        result = supabase.rpc('execute_sql_query', {'query': query}).execute()
        
        # Check if there's an error in the response
        if 'error' in result:
            return f"An error occurred: {result['error']}"
        
        # Extract the data from the result
        data = result.data

        # If data is empty, return a message
        if not data:
            return "No results found for the given query."

        # If data is a list of dictionaries, return it as is
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            return data

        # If data is a single dictionary, wrap it in a list
        if isinstance(data, dict):
            return [data]

        # If data is in any other format, return it as a string
        return str(data)

    except Exception as e:
        return f"An error occurred: {str(e)}"
