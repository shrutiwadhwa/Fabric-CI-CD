# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "9ee7ff38-e85c-4d0d-a749-6f131dbc583f",
# META       "default_lakehouse_name": "shrulake",
# META       "default_lakehouse_workspace_id": "c48bbed2-cdef-4f1e-9ff6-04461745e6d4",
# META       "known_lakehouses": [
# META         {
# META           "id": "9ee7ff38-e85c-4d0d-a749-6f131dbc583f"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
customers_data = [
    (1, "Amit Sharma", "amit.sharma@email.com", "9876543210", "North", "Delhi", "Gold"),
    (2, "Priya Mehta", "priya.mehta@email.com", "9876543211", "West", "Mumbai", "Silver"),
    (3, "Ravi Kumar", "ravi.kumar@email.com", "9876543212", "South", "Bengaluru", "Gold"),
    (4, "Neha Verma", "neha.verma@email.com", "9876543213", "East", "Kolkata", "Bronze"),
    (5, "Arjun Singh", "arjun.singh@email.com", "9876543214", "North", "Jaipur", "Silver"),
    (6, "Kavita Rao", "kavita.rao@email.com", "9876543215", "South", "Hyderabad", "Gold"),
    (7, "Imran Khan", "imran.khan@email.com", "9876543216", "West", "Pune", "Bronze"),
    (8, "Sunita Das", "sunita.das@email.com", "9876543217", "East", "Bhubaneswar", "Silver")
]

customers_columns = [
    "customer_id",
    "customer_name",
    "email",
    "phone",
    "region",
    "city",
    "customer_segment"
]

df_customers = spark.createDataFrame(customers_data, customers_columns)

df_customers.write.mode("overwrite").format("delta").saveAsTable("customers")

display(df_customers)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_customers.write.mode("overwrite").format("delta").saveAsTable("customers")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

products_data = [
    (101, "Laptop", "Electronics", 65000, "Active"),
    (102, "Mobile Phone", "Electronics", 30000, "Active"),
    (103, "Office Chair", "Furniture", 8500, "Active"),
    (104, "Desk", "Furniture", 15000, "Active"),
    (105, "Printer", "Electronics", 12000, "Inactive"),
    (106, "Notebook Pack", "Stationery", 500, "Active"),
    (107, "Pen Set", "Stationery", 250, "Active"),
    (108, "Monitor", "Electronics", 18000, "Active")
]

products_columns = [
    "product_id",
    "product_name",
    "category",
    "unit_price",
    "product_status"
]

df_products = spark.createDataFrame(products_data, products_columns)

df_products.write.mode("overwrite").format("delta").saveAsTable("products")

display(df_products)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_products.write.mode("overwrite").format("delta").saveAsTable("products")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

sales_data = [
    (1001, 1, 101, "2026-01-05", 1, 65000, "North"),
    (1002, 2, 102, "2026-01-07", 2, 60000, "West"),
    (1003, 3, 103, "2026-01-10", 1, 8500, "South"),
    (1004, 4, 104, "2026-01-12", 1, 15000, "East"),
    (1005, 5, 108, "2026-01-15", 2, 36000, "North"),
    (1006, 6, 101, "2026-01-18", 1, 65000, "South"),
    (1007, 7, 106, "2026-01-20", 10, 5000, "West"),
    (1008, 8, 107, "2026-01-23", 20, 5000, "East"),
    (1009, 1, 102, "2026-02-02", 1, 30000, "North"),
    (1010, 3, 108, "2026-02-05", 1, 18000, "South")
]

sales_columns = [
    "transaction_id",
    "customer_id",
    "product_id",
    "transaction_date",
    "quantity",
    "total_amount",
    "region"
]

df_sales = spark.createDataFrame(sales_data, sales_columns)

df_sales.write.mode("overwrite").format("delta").saveAsTable("sales_transactions")

display(df_sales)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_sales.write.mode("overwrite").format("delta").saveAsTable("sales")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

employees_data = [
    (1, "Mary", "Young", "Operations", "North", "Operations Analyst", 63392.64, "854-23-9935", "mary.young@company.com"),
    (2, "Jennifer", "White", "Sales", "North", "Sales Manager", 92901.65, "127-81-4257", "jennifer.white@company.com"),
    (3, "Joseph", "Baker", "Marketing", "West", "Brand Manager", 71691.44, "990-10-3615", "joseph.baker@company.com"),
    (4, "Jessica", "Walker", "Finance", "South", "Financial Analyst", 66595.94, "199-55-6635", "jessica.walker@company.com"),
    (5, "Paul", "Davis", "Sales", "West", "Sales Representative", 60910.01, "400-90-6925", "paul.davis@company.com"),
    (6, "Joseph", "Robinson", "Sales", "North", "Account Executive", 119148.38, "987-22-7227", "joseph.robinson@company.com"),
    (7, "Betty", "Hall", "Finance", "South", "Finance Manager", 110263.14, "818-97-2169", "betty.hall@company.com"),
    (8, "Ashley", "King", "HR", "South", "Recruiter", 99476.17, "755-98-4598", "ashley.king@company.com"),
    (9, "John", "Lee", "Sales", "South", "Sales Representative", 75080.57, "316-82-6155", "john.lee@company.com"),
    (10, "Barbara", "Thompson", "Operations", "West", "Operations Analyst", 64797.65, "674-78-5304", "barbara.thompson@company.com"),
    (11, "Betty", "Harris", "Marketing", "West", "Content Strategist", 85571.58, "193-16-2796", "betty.harris@company.com"),
    (12, "Matthew", "Martin", "IT", "West", "Tech Lead", 164670.32, "641-42-1188", "matthew.martin@company.com"),
    (13, "John", "Thomas", "Marketing", "East", "Marketing Analyst", 81085.92, "564-10-5315", "john.thomas@company.com"),
    (14, "Patricia", "Moore", "Finance", "East", "Finance Executive", 93044.74, "265-70-2500", "patricia.moore@company.com"),
    (15, "Robert", "Jackson", "HR", "North", "HR Manager", 121500.40, "742-90-1845", "robert.jackson@company.com"),
    (16, "Linda", "Clark", "IT", "South", "Data Engineer", 145250.90, "602-12-9911", "linda.clark@company.com"),
    (17, "William", "Lewis", "Operations", "East", "Operations Manager", 132750.33, "321-88-7764", "william.lewis@company.com"),
    (18, "Elizabeth", "Allen", "Sales", "East", "Sales Manager", 128000.00, "987-45-1200", "elizabeth.allen@company.com"),
    (19, "David", "Scott", "IT", "North", "Cloud Engineer", 151200.75, "456-72-8871", "david.scott@company.com"),
    (20, "Susan", "Green", "Marketing", "South", "Digital Marketing Lead", 118950.45, "775-21-3345", "susan.green@company.com"),
    (21, "James", "Adams", "Finance", "West", "Accountant", 78900.00, "334-78-9901", "james.adams@company.com"),
    (22, "Karen", "Nelson", "HR", "West", "HR Executive", 72500.25, "112-34-5678", "karen.nelson@company.com"),
    (23, "Michael", "Carter", "Sales", "North", "Regional Sales Head", 158400.80, "661-98-3021", "michael.carter@company.com"),
    (24, "Nancy", "Mitchell", "IT", "East", "Solution Architect", 172300.00, "221-56-7432", "nancy.mitchell@company.com"),
    (25, "Daniel", "Perez", "Operations", "South", "Supply Chain Analyst", 90200.90, "564-44-1290", "daniel.perez@company.com"),
    (26, "Lisa", "Roberts", "Finance", "North", "Senior Financial Analyst", 112500.60, "875-66-9087", "lisa.roberts@company.com"),
    (27, "Mark", "Turner", "IT", "West", "Data Scientist", 160700.10, "932-10-5432", "mark.turner@company.com"),
    (28, "Sandra", "Phillips", "Sales", "South", "Account Manager", 103250.25, "201-76-4598", "sandra.phillips@company.com"),
    (29, "George", "Campbell", "Marketing", "North", "SEO Specialist", 84200.15, "667-19-1205", "george.campbell@company.com"),
    (30, "Donna", "Parker", "HR", "East", "Talent Acquisition Lead", 99000.00, "145-39-8854", "donna.parker@company.com"),
    (31, "Edward", "Evans", "Operations", "North", "Logistics Manager", 126400.40, "490-12-3344", "edward.evans@company.com"),
    (32, "Laura", "Edwards", "Finance", "South", "Payroll Specialist", 87300.50, "777-11-2980", "laura.edwards@company.com"),
    (33, "Brian", "Collins", "IT", "South", "Security Engineer", 154800.35, "563-89-7102", "brian.collins@company.com"),
    (34, "Michelle", "Stewart", "Marketing", "East", "Campaign Manager", 108600.45, "287-90-6311", "michelle.stewart@company.com"),
    (35, "Kevin", "Morris", "Sales", "West", "Sales Executive", 94200.20, "121-34-9088", "kevin.morris@company.com"),
    (36, "Sarah", "Rogers", "HR", "North", "Learning Manager", 116500.00, "442-59-7650", "sarah.rogers@company.com"),
    (37, "Steven", "Reed", "IT", "East", "Platform Engineer", 149900.60, "765-22-8765", "steven.reed@company.com"),
    (38, "Angela", "Cook", "Finance", "West", "Finance Controller", 168000.75, "982-76-1010", "angela.cook@company.com"),
    (39, "Jason", "Morgan", "Operations", "South", "Process Manager", 123450.35, "557-81-4432", "jason.morgan@company.com"),
    (40, "Emily", "Bell", "Sales", "East", "Customer Success Manager", 101300.85, "301-45-7788", "emily.bell@company.com")
]

employees_columns = [
    "employee_id",
    "first_name",
    "last_name",
    "department",
    "region",
    "job_title",
    "salary",
    "ssn",
    "email"
]

df_employees = spark.createDataFrame(employees_data, employees_columns)

df_employees.write.mode("overwrite").format("delta").saveAsTable("employees")

display(df_employees)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_employees.write.mode("overwrite").format("delta").saveAsTable("Employees")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
