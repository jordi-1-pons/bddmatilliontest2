from behave import *
import json
import os

# Define a step to get table name
@given('the table name is "{table_name}"')
def step_given_table_name(context, table_name):
    context.table_name = table_name

# Step to query the database and fetch columns and rep_status values
@when('I query the table {table_name}')
def step_when_query_table(context, table_name):
    context.table_name = table_name
    file_path = '/tmp/table_data/insert_data.txt'
    with open(file_path, 'r') as file:
        data = json.load(file)
        context.rep_status_values = data['rep_status_values']
        print(f"Fetched rep_status values from file: {context.rep_status_values}")

# Step to verify the table is not empty and rep_status column values
@then('the table {table_name} should not be empty')
def step_then_verify_table_not_empty(context, table_name):
    assert context.rep_status_values, f"The table {table_name} is empty."

@then('the column rep_status should only contain "Active" and "Inactive" values without missing values')
def step_then_verify_rep_status_values(context, table_name):
    allowed_values = {"Active", "Inactive"}
    for value in context.rep_status_values:
        assert value in allowed_values, f"Invalid value '{value}' found in column rep_status."
