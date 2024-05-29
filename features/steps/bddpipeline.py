import json
from behave import *

# Define a step to get table name
@given('the table name is "{table_name}"')
def step_given_table_name(context, table_name):
    context.table_name = table_name
    print(f"Table name set to: {context.table_name}")

# Step to read the file and fetch data
@when('I query the table {table_name}')
def step_when_query_table(context, table_name):
    file_path = '/tmp/table_data/insert_data.txt'
    with open(file_path, 'r') as file:
        data = json.load(file)
        context.rep_status_values = data['rep_status_values']
        print(f"Fetched rep_status values from file: {context.rep_status_values}")

# Step to verify the table is not empty
@then('the table {table_name} should not be empty')
def step_then_verify_not_empty(context, table_name):
    assert len(context.rep_status_values) > 0, f"Table {table_name} is empty"

# Step to verify rep_status column values
@then('the column rep_status should only contain "Active" and "Inactive" values without missing values')
def step_then_verify_rep_status_values(context, table_name):
    valid_values = {"Active", "Inactive"}
    rep_status_set = set(context.rep_status_values)
    print(f"rep_status values in table: {rep_status_set}")
    assert rep_status_set.issubset(valid_values), f"Column rep_status contains invalid values: {rep_status_set - valid_values}"
    assert None not in context.rep_status_values, f"Column rep_status contains missing values"