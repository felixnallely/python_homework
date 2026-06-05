#Task 5: Read Data into a DataFrame
import pandas as pd 
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """
    SELECT 
        line_items.line_item_id, 
        line_items.quantity, 
        line_items.product_id, 
        products.product_name, 
        products.price
    FROM line_items
    JOIN products
        ON line_items.product_id = products.product_id
    """
    df = pd.read_sql_query(sql_statement, conn)

#Print 5 rows: 
print("Inital DataFrame:")
print(df.head(), "\n")

#Part 4: add Total column 
df['total'] = df['quantity'] * df['price']
print("DataFrame with total column:")
print(df.head(), "\n")

#Part 5: add groupby()
result_df = df.groupby('product_id').agg(
    line_item_id_count=('line_item_id', 'count'),
    total_sum=('total', 'sum'),
    product_name=('product_name', 'first')
).reset_index()

print(result_df.head(5))

#Part 6: sort by product_name 
result_df = result_df.sort_values('product_name')
print(result_df.head(), "\n")
print("Grouped column.")

#Part 7: write to csv file 
result_df.to_csv("order_summary.csv")
print("Written order_summary.csv successfully.")