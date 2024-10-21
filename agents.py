# agents.py

from swarm import Agent
from database import order_db_query

def order_agent_instructions(context_variables):
    order_db_details = context_variables["order_database_context"]
    return f""" 
    You are an AI assistant designed to retrieve order information from an orders 
    database. Here is the information on the orders database:
    {order_db_details}
    Your task is to interpret user queries about order details, formulate appropriate 
    SQL queries, and execute them using the order_db_query function.

    Example user query: "What are the total sales for the last month?"
    Example response: 
    {{
        "query": "SELECT SUM(total_amount) FROM orders WHERE order_date >= date('now', '-1 month');",
        "explanation": "This query calculates the sum of total_amount for all orders in the last month."
    }}

    After generating the query, call the order_db_query function with the SQL query as an argument.
    Then, provide a brief explanation of the results to the user.
    """

def transfer_to_core_agent():
    return core_agent

def transfer_to_order_agent():
    return order_agent

core_agent = Agent(
    name="Core Agent",
    instructions="You are a helpful agent. Call the appropriate function based on user query.",
    functions=[transfer_to_order_agent]
)

order_agent = Agent(
    name="Order Agent",
    instructions=order_agent_instructions,
    functions=[order_db_query, transfer_to_core_agent]
)
