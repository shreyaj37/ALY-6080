import pandas as pd

# Load data from the Excel file into separate DataFrames
milestones_df = pd.read_excel('Fledglings Flight Content v1.2.xlsx', sheet_name='Milestones')
exercises_df = pd.read_excel('Fledglings Flight Content v1.2.xlsx', sheet_name='Exercises')
toys_df = pd.read_excel('Fledglings Flight Content v1.2.xlsx', sheet_name='Toys')
toy_activity_instructions_df = pd.read_excel('Fledglings Flight Content v1.2.xlsx', sheet_name='ToyActivityInstructions')
tasks_df = pd.read_excel('Fledglings Flight Content v1.2.xlsx', sheet_name='Tasks')
new_tasks_df = pd.read_excel('Fledglings Flight Content v1.2.xlsx', sheet_name='New_Tasks')

# Merge Milestones, Exercises, and Toys using age_id as the primary key
merged_age_df = pd.merge(milestones_df, exercises_df, on='age_id', how='inner')
merged_age_df = pd.merge(merged_age_df, toys_df, on='age_id', how='inner')

# Merge Toys and ToyActivityInstructions using toyid as the primary key
merged_toy_df = pd.merge(toys_df, toy_activity_instructions_df, on='toyid', how='inner')

# Merge Tasks and New_Tasks using exerciseid as the primary key
merged_task_df = pd.merge(tasks_df, new_tasks_df, on='exerciseid', how='inner')

# Merge the final DataFrames using the appropriate common columns
final_df = pd.merge(merged_age_df, merged_toy_df, on=['age_id', 'toyid'], how='inner')
final_df = pd.merge(final_df, merged_task_df, on=['age_id', 'exerciseid'], how='inner')

# Save the final merged DataFrame to a CSV file
final_df.to_csv('merged_data.csv', index=False)
