# AI-Powered Order Database Assistant
This project implements an AI-powered assistant that can query an order database and provide helpful information based on user queries. It uses OpenAI's language model via LangChain, and interacts with a Supabase database for order information.
## Features
- Natural language interface for querying order data
- AI-powered response generation and SQL query formulation
- Integration with Supabase for database operations
- Conversational memory to maintain context across queries
## Prerequisites
- Python 3.7+
- OpenAI API key
- Supabase project with appropriate database setup
## Installation
1. Clone this repository:
git clone https://github.com/yourusername/ai-order-assistant.git
cd ai-order-assistant

2. Install the required packages:
pip install langchain openai supabase

3. Set up your environment variables. You can add these to your `.replit` file or set them in your environment:
OPENAI_API_KEY=your_openai_api_key
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_api_key

## Supabase Setup
Ensure you have a Supabase function named `execute_sql_query` that can safely execute SQL queries. Here's an example of how to create this function:
```sql
CREATE OR REPLACE FUNCTION execute_sql_query(query TEXT)
RETURNS JSONB AS $$
DECLARE
result JSONB;
BEGIN
EXECUTE query INTO result;
RETURN result;
EXCEPTION WHEN OTHERS THEN
RETURN jsonb_build_object('error', SQLERRM);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
Note: Be cautious with this function as it allows arbitrary SQL execution. Implement proper security measures in a production environment.

Usage
Run the script:

python main.py
The AI assistant will greet you and wait for your input. You can ask questions about orders, and the assistant will formulate SQL queries to retrieve the relevant information from the database.

Example interactions:

AI Assistant: Hello! I'm here to help you with order database queries. What would you like to know?
User: What were the total sales last month?
AI: Certainly! I'll query the database to get the total sales for last month. Let me formulate the SQL query and execute it.
[AI formulates and executes the query]
Based on the query results, the total sales for last month were $XXXX.XX. This figure represents the sum of all order amounts from [start date] to [end date]. Is there anything specific about these sales you'd like to know more about?
User: How many unique customers did we have?
AI: Great question! I'll query the database to find out how many unique customers we had last month. 
[AI formulates and executes the query]
According to the database, we had XX unique customers last month. This number represents individual customers who placed at least one order during that period. Would you like to know more about our customer base or their ordering patterns?
User: exit
AI: Goodbye!
Customization
You can modify the context_variables in the script to update the database schema or add more context for the AI assistant. You can also extend the tools list to add more functionalities to the assistant.

License
MIT License

Support
If you encounter any problems or have any questions, please open an issue in this repository.

This README.md provides a comprehensive guide for anyone who wants to use or contribute to your AI-powered order database assistant. It covers:
1. A brief description of the project
2. Features
3. Prerequisites
4. Installation instructions
5. Supabase setup guidance
6. Usage instructions with example interactions
7. Customization possibilities
8. Placeholders for license and contribution information
You can save this content in a file named `README.md` in the same directory as your [main.py](rag://rag_source_0) file. Remember to replace placeholders like `[Specify your license here]` and `[Specify how others can contribute to this project]` with appropriate information for your project.
This README will help users understand what your project does, how to set it up, and how to use it effectively. It also provides a good starting point for any future contributors to your project.
