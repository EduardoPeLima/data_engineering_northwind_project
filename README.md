# Northwind Data Engineering Project

*This is a project using data from a fictional company called Northwind, involved in product shipping operations.
  
## Transactional Modeling vs Dimensional Modeling
* The original data is fully normalized, making it ideal for OLTP (Online Transaction Processing) systems where various CRUD operations occur constantly due to the interaction of various users using the application.

  <i>CRUD operations are: Create, Read, Update and Delete</i>
  
<img alt="Northwind normalized schema" src="https://github.com/EduardoPeLima/data_engineering_northwind_project/blob/master/01_northwind_normalized_data/03_northwind_normalized_schema.png">

#### Our goal is to develop an analytical layer for this data, so the transactional data is not the best approach for our case. 
* Normalizing data, besides being more complex for non-technical individuals, presents a poorer performance from an analytical perspective due to the large number of table cross-references (JOINS) needed to obtain answers. For example, for a question like "which product categories have certain customers ordered?" you would need to cross-reference 5 tables: categories, products, order_details, orders and customers, making it a non-performant operation and affecting the transactional database's performance.
* Consequently, we plan to construct a dimensional model based on transactional data. The objective is to create an OLAP (Online Analytical Processing) system, incorporating a "fact" table to record occurrences of specific real-world events and dimension tables that facilitate direct "slicing" of the fact table.
  
<img alt="Northwind dimensional schema" src="https://github.com/EduardoPeLima/data_engineering_northwind_project/blob/master/04_aws/04_rds_mysql_northwind_denormalized/project_northwind_dimensional_model.png">

* Now, to analyze our previous example (which product categories have certain customers ordered?), we only need to cross-reference 3 tables: dim_products, fact_orders and dim_customers. In addition to being more performant due to fewer table cross-references (JOINS), it becomes simpler to understand, even for a non-technical person.
* Even using the same server to store dimensional data, which is our case, we have already benefited from performance. But in scenarios with a larger volume of data and/or big volume of reading operations, creating a new server with the dimensional data may be necessary.

## Defining the Architecture for ETL
<img alt="aws architecture pipeline" src="https://github.com/EduardoPeLima/data_engineering_northwind_project/blob/master/04_aws/aws_architecture.png">

1. Since our data originates from local files, a Python script has been developed to migrate locally stored files to an S3 bucket within AWS.
2. A Lambda function using Python is triggered upon the arrival of new files within S3, where it inserts the data into the RDS MySQL table with the respective name based on the file name. It also inserts logs into CloudWatch.

CloudWatch Logs
<img alt="lambda logs" src="https://github.com/EduardoPeLima/data_engineering_northwind_project/blob/master/04_aws/03_lambda/cloudwatch_lambda_logs.png">
<i>The Lambda Layer's function is to contain the necessary libraries for our triggered Lambda</i>

3. A Python code then executes the list of SQL scripts responsible for creating dimensional tables in a new database.
4. A Power BI Dashboard consumes data from the dimensional database, feeding the charts.
<img alt="Northwind dimensional schema" src="https://github.com/EduardoPeLima/data_engineering_northwind_project/blob/master/05_powerbi/dashboard_img.png">

## Tools used in the project
* **Lucidchart:** web-based diagramming tool that allows you to create flowcharts, diagrams, and visual representations of processes. It is used for designing and documenting the project's database schema and architectural diagrams.
* **Visual Studio Code:** it provides a rich set of features for coding, debugging, and source code version control. VS Code is used for writing and editing code scripts, including Python scripts for data migration and execute SQL scripts inside our database.
* **Pandas:** it provides data structures like data frames for efficient data handling and analysis. Is used in the project for EDA (Exploratory Data Analysis), with the objective to map our columns data types, expected volume of data, null values and outliers. 
* **RDS:** is a managed relational database service provided by AWS. It simplifies database setup, operation, and scaling. In this project, a RDS instance is used with MySQL to host the relational database where transactional and dimensional data is stored.
* **Dbeaver:** is a universal database tool that supports various database management systems. It is used in the project to write and test SQL statements directly in the RDS MySQL database. 
* **S3:** is an object storage service provided by AWS. It is used for storing our local files inside AWS.
* **Lambda:** is a serverless computing service that allows you to run code without provisioning or managing servers. In this project, Lambda functions are used to automate the process of inserting data into the RDS tables based on the arrival of new files in the S3 bucket.
* **IAM:** is an AWS service that helps you securely control access to AWS resources. It is used to define roles and permissions for Lambda functions, such as access to read and write into RDS, S3 and CloudWatch.
* **CloudWatch:** is a monitoring and observability service. It is used in the project to collect and manage logs generated by the Lambda functions.
* **Power BI:** is a business analytics tool by Microsoft that provides interactive visualizations and business intelligence capabilities. It is used to create a dashboard that consumes and displays data from the dimensional database.

