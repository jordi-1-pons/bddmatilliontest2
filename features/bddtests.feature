Feature: Verify fact_test table

Scenario: Check if fact_test table is not empty and rep_status column contains only "Active" and "Inactive" values
    Given the table name is "fact_test"
    When I query the table fact_test
    Then the table fact_test should not be empty
    And the column rep_status should only contain "Active" and "Inactive" values without missing values