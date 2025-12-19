

structured and semi structured data
--


 
Structured data has a fixed schema and fits neatly into rows and columns, such as names and phone numbers. Unstructured data has no fixed schema and can have a more complex format, such as audio files and web pages.

Here are key areas where structured and unstructured data differ:

- **Format:** Structured data has a strict, predefined data model. Unstructured data does not have a predefined format.  
      
    
- **Storage:** Structured [data storage](https://www.ibm.com/think/topics/data-storage) systems have rigid schemas, such as those in [relational databases](https://www.ibm.com/think/topics/relational-databases) or [data warehouses](https://www.ibm.com/think/topics/cloud-data-lake-vs-data-warehouse-vs-data-mart). Unstructured data is often stored in its native format in [nonrelational databases](https://www.ibm.com/think/topics/nosql-databases) or [data lakes](https://www.ibm.com/think/topics/data-lake).  
      
    
- **Use cases:** Organizations can use both structured and unstructured data across [artificial intelligence](https://www.ibm.com/think/topics/artificial-intelligence) (AI) and analytics use cases. Structured data is often used in [machine learning](https://www.ibm.com/think/topics/machine-learning) (ML) and drives [ML algorithms](https://www.ibm.com/think/topics/machine-learning-algorithms). Unstructured data is often used in [natural language processing](https://www.ibm.com/think/topics/natural-language-processing) (NLP) and is a rich and diverse data source for [generative AI](https://www.ibm.com/think/topics/generative-ai) (gen AI) models.  
      
    
- **Complexity:** Structured data is easier to manipulate and analyze for general business users with traditional tools. Unstructured data can be more complex and requires specialized skills and tools to parse and analyze.
	## What are the pros and cons of structured data?
	
	The benefits of structured data are tied to its ease of use and access:
	
	- **Works well with machine learning**: Machine learning can process both structured and unstructured data. However, it can be easier for ML applications to analyze and draw insights from structured data due to its specific and organized architecture.  
	      
	    
	- **Accessible and easy to use**: Understanding structured data does not require in-depth data science knowledge. Due to its standard format and high level of organization, most users find it easy to access and interpret structured data.  
	      
	    
	- **Abundance of tools**: Structured data predates unstructured data, so there are more apps and tools available for use and data analysis. For example, [online analytical processing](https://www.ibm.com/think/topics/olap) (OLAP), [SQLite](https://sqlite.org/), [MySQL](https://www.youtube.com/watch?v=UO-yT7Ugnls) and [PostgreSQL](https://www.ibm.com/think/topics/postgresql), among others.
	
	The challenges of structured data revolve around data inflexibility:
	
	- **Limited usage**: Structured data has a predefined data model that can only be used for its intended purpose, which limits its flexibility and usability. Mining more insights requires modifications or additional data.  
	      
	    
	- **Limited storage options**: Structured data storage repositories typically have rigid [schemas](https://www.ibm.com/think/topics/database-schema), such as those within a [relational database](https://www.ibm.com/think/topics/relational-databases) or [data warehouse](https://www.ibm.com/think/topics/data-warehouse). Changes to data requirements need updating all structured data, which is time and resource-intensive.
	## How is unstructured data used?
	
	Because unstructured data does not have a predefined [data model](https://www.ibm.com/think/topics/data-modeling), it is not easily processed and analyzed through conventional data tools and methods.
	
	It is best managed in [nonrelational or NoSQL databases](https://www.ibm.com/think/topics/nosql-databases) or in [data lakes](https://www.ibm.com/think/topics/data-lake), which are designed to handle massive amounts of raw data in any format.
	
	Often, machine learning, [advanced analytics](https://www.ibm.com/think/topics/advanced-analytics) and [natural language processing](https://www.ibm.com/think/topics/natural-language-processing) (NLP) are used to extract valuable insights from unstructured data.
	
	Use cases include:
	
	- [Retrieval augmented generation](https://www.ibm.com/think/topics/retrieval-augmented-generation) (RAG)
	- [Generative AI](https://www.ibm.com/think/insights/unstructured-data-trends) (gen AI)
	- Customer behavior and [sentiment analysis](https://www.ibm.com/think/topics/sentiment-analysis)
	- [Predictive data analytics](https://www.ibm.com/think/topics/predictive-analytics)
	- [Chatbot](https://www.ibm.com/think/topics/chatbots) text analysis
	
	[Learn more about AI and the future of unstructured data](https://www.ibm.com/think/insights/unstructured-data-trends) 
	
	## What are the pros and cons of unstructured data?
	
	The benefits of unstructured data involve advantages in data format, speed and storage:
	
	- **Flexibility**: Unstructured data is stored in its native format and remains undefined until needed. This file format flexibility widens the pool of available data and enables data scientists to use data for multiple use cases.  
	      
	    
	- **Fast accumulation rates**: For most organizations, this type of data is growing at 3x the rate of structured data. Since there is no need to predefine unstructured data, it can be collected quickly and easily, which is helpful for [generative AI](https://www.ibm.com/think/topics/generative-ai) and large language model (LLM) [fine-tuning](https://www.ibm.com/think/topics/fine-tuning).2  
	      
	    
	- **Easy and cheap to store**: Unstructured data has more storage options than structured data. For instance, file systems or data lakes allow for massive storage and pay-as-you-use pricing, which cuts costs and eases scalability.
	
	The challenges of unstructured data center on expertise and available resources:
	
	- **Requires expertise:** Due to its undefined or nonformatted nature, data science expertise is required to prepare and analyze unstructured data. This can alienate business users who might not fully understand specialized data topics or analysis.  
	      
	    
	- **Specialized tools:** Traditional tools such as Excel are not adequate for manipulating unstructured data, and product choices are limited for data managers. Some tools for unstructured data management include: [MongoDB](https://www.ibm.com/think/topics/mongodb), [DynamoDB](https://aws.amazon.com/dynamodb/), [Hadoop](https://www.ibm.com/think/topics/hadoop) and [Azure](https://www.ibm.com/consulting/microsoft).
	
	- **Data cleanliness:** The large volume and nonuniform data structure of unstructured data can introduce inconsistencies, inaccuracies and data quality issues. [Data cleaning](https://www.ibm.com/think/topics/data-cleaning) might be necessary before data processing.
	
	Source:- https://www.ibm.com/think/topics/structured-vs-unstructured-data
	

---
OLTP vs OLAP systems
---
## What’s the difference between OLAP and OLTP?

Online analytical processing (OLAP) and online transaction processing (OLTP) are data processing systems that help you store and analyze business data. You can collect and store data from multiple sources—such as websites, applications, smart meters, and internal systems. OLAP combines and groups the data so you can analyze it from different points of view. Conversely, OLTP stores and updates transactional data reliably and efficiently in high volumes. OLTP databases can be one among several data sources for an OLAP system.

[Read about OLAP »](https://aws.amazon.com/what-is/olap/)

## What are the similarities between OLAP and OLTP?

Both online analytical processing (OLAP) and online transaction processing (OLTP) are database management systems for storing and processing data in large volumes. They require efficient and reliable IT infrastructure to run smoothly. You can use them both to query existing data or store new data. Both support data-driven decision-making in an organization.

Most companies use OLTP and OLAP systems together to meet their business intelligence requirements. However, the approach to and purpose of data management differ significantly between OLAP and OLTP.

## Key differences: OLAP vs. OLTP

The primary purpose of online analytical processing (OLAP) is to **analyze aggregated** data, while the primary purpose of online transaction processing (OLTP) is to **process database transactions.**


***OLAP systems to generate reports, perform complex data analysis, and identify trends***

***OLTP systems to process orders, update inventory, and manage customer accounts.***

Other major differences include data formatting, [data architecture](https://aws.amazon.com/what-is/data-architecture/), performance, and requirements. We’ll also discuss an example of when an organization might use OLAP or OLTP.

### **Data formatting**

OLAP systems use multidimensional data models, so you can view the same data from different angles. OLAP databases store data in a cube format, where each dimension represents a different data attribute. Each cell in the cube represents a value or measure for the intersection of the dimensions.

In contrast, OLTP systems are unidimensional and focus on one data aspect. They use a relational database to organize data into tables. Each row in the table represents an entity instance, and each column represents an entity attribute.

### **Data architecture**

OLAP database architecture prioritizes _data read_ over _data write_ operations. You can quickly and efficiently perform complex queries on large volumes of data. Availability is a low-priority concern as the primary use case is analytics.

On the other hand, OLTP database architecture prioritizes _data write_ operations. It’s optimized for write-heavy workloads and can update high-frequency, high-volume transactional data without compromising data integrity.

For instance, if two customers purchase the same item at the same time, the OLTP system can adjust stock levels accurately. And the system will prioritize the chronological first customer if the item is the last one in stock. Availability is a high priority and is typically achieved through multiple data backups.

### **Performance**

OLAP processing times can vary from minutes to hours depending on the type and volume of data being analyzed. To update an OLAP database, you periodically process data in large batches then upload the batch to the system all at once. Data update frequency also varies between systems, from daily to weekly or even monthly.

In contrast, you measure OLTP processing times in milliseconds or less. OLTP databases manage database updates in real time. Updates are fast, short, and triggered by you or your users. Stream processing is often used over batch processing.

[Read about streaming data »](https://aws.amazon.com/what-is/streaming-data/)

[Read about batch processing »](https://aws.amazon.com/what-is/batch-processing/)

### **Requirements**

OLAP systems act like a centralized data store and pull in data from multiple data warehouses, relational databases, and other systems. Storage requirements measure from terabytes (TB) to petabytes (PB). Data reads can also be compute-intensive, requiring high-performing servers.

On the other hand, you can measure OLTP storage requirements in gigabytes (GB). OLTP databases may also be cleared once the data is loaded into a related OLAP data warehouse or data lake. However, compute requirements for OLTP are also high.

### **Example of OLAP vs. OLTP**

Let's consider a large retail company that operates hundreds of stores across the country. The company has a massive database that tracks sales, inventory, customer data, and other key metrics.

The company uses OLTP to process transactions in real time, update inventory levels, and manage customer accounts. Each store is connected to the central database, which updates the inventory levels in real time as products are sold. The company also uses OLTP to manage customer accounts—for example, to track loyalty points, manage payment information, and process returns.

In addition, the company uses OLAP to analyze the data collected by OLTP. The company’s business analysts can use OLAP to generate reports on sales trends, inventory levels, customer demographics, and other key metrics. They perform complex queries on large volumes of historical data to identify patterns and trends that can inform business decisions. They identify popular products in a given time period and use the information to optimize inventory budgets.

## When to use OLAP vs. OLTP

Online analytical processing (OLAP) and online transaction processing (OLTP) are two different data processing systems designed for different purposes. OLAP is optimized for complex data analysis and reporting, while OLTP is optimized for transactional processing and real-time updates.

Understanding the differences between these systems can help you make informed decisions about which system meets your needs better. In many cases, a combination of both OLAP and OLTP systems may be the best solution for businesses that require both transaction processing and data analysis. Ultimately, choosing the right system depends on the specific needs of your business, including data volume, query complexity, response time, scalability, and cost.

![Example-architecture-using-AWS-Managed-Services](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2021/06/10/Figure-1.-Example-architecture-using-AWS-Managed-Services-1.png)

## Summary of differences: OLAP vs. OLTP

|                      |                                                                                                 |                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Criteria**         | **OLAP**                                                                                        | **OLTP**                                                                              |
| Purpose              | OLAP helps you analyze large volumes of data to support decision-making.                        | OLTP helps you manage and process real-time transactions.                             |
| Data source          | OLAP uses historical and aggregated data from multiple sources.                                 | OLTP uses real-time and transactional data from a single source.                      |
| Data structure       | OLAP uses multidimensional (cubes) or relational databases.                                     | OLTP uses relational databases.                                                       |
| Data model           | OLAP uses star schema, snowflake schema, or other analytical models.                            | OLTP uses normalized or denormalized models.                                          |
| Volume of data       | OLAP has large storage requirements. Think terabytes (TB) and petabytes (PB).                   | OLTP has comparatively smaller storage requirements. Think gigabytes (GB).            |
| Response time        | OLAP has longer response times, typically in seconds or minutes.                                | OLTP has shorter response times, typically in milliseconds                            |
| Example applications | OLAP is good for analyzing trends, predicting customer behavior, and identifying profitability. | OLTP is good for processing payments, customer data management, and order processing. |

## How can AWS support your OLAP and OLTP requirements?

[Analytics on Amazon Web Services (AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/)[)](https://aws.amazon.com/big-data/datalakes-and-analytics/) provides various managed cloud services for online analytical processing (OLAP) and online transaction processing (OLTP) operations. From data movement, data storage, data analytics, and more, AWS offers purpose-built services that provide the best price performance, scalability, and lowest cost.

Here are examples of AWS services that can support your OLAP and OLTP needs:

- [Amazon Redshift](https://aws.amazon.com/redshift/) is a cloud data warehouse designed specifically for OLAP.
- [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) is a relational database with OLAP functionality. You can use it to run OLTP workloads or with Oracle OLAP to perform complex queries on dimensional cubes.
- [Amazon Aurora](https://aws.amazon.com/rds/aurora/) is a MySQL- and PostgreSQL-compatible cloud relational database that can run both OLTP and complex OLAP workloads.



---
Row-Oriented and Column Oriented Databases
--
			Databases are essential for storing, managing, and retrieving data in modern applications. The performance and efficiency of a database system largely depend on how the data is organized and stored. Two primary strategies exist in relational database management systems (RDBMS):

1. ****Row-Oriented Databases:**** store data row by row.
2. ****Column-Oriented Databases:**** store data column by column.

> ****Note:**** Understanding the differences between these two approaches helps in choosing the right database model based on workload and data requirements.

## Row-Oriented Database

In a row-oriented database, data is stored and retrieved row by row, meaning all attributes of a row are stored together in the same physical block.

- Optimized for retrieving entire rows of data.
- Commonly used in traditional RDBMS systems for Online Transaction Processing (OLTP) workloads.

### Example of Row-Oriented Data Storage

|ID|Name|Age|Department|
|---|---|---|---|
|1|John|35|IT|
|2|Jane|28|HR|
|3|Bob|42|Finance|

### Query Behavior

- Retrieving a row fetches all its attributes, even if some are not needed.
- May reduce performance for queries that only need specific columns.

### Advantages

1. ****Effective for OLTP:**** Optimized for frequent inserts, updates, and deletes.
2. ****Full Row Retrieval:**** Efficient when querying all attributes of a single row.
3. ****Easy to Understand and Use:**** Familiar to users of traditional relational databases.

### Disadvantages

1. ****Inefficient for Analytics:**** Queries needing only some columns are slower.
2. ****Higher Storage Requirements:**** Less opportunity for columnar compression.
3. ****Scaling Limitations:**** Performance may degrade as data size grows.

## Column-Oriented Database

In a column-oriented database, data is stored column by column rather than row by row.

- Optimized for retrieving specific columns of data.
- Commonly used in Online Analytical Processing (OLAP) systems and data warehouses.

### Example of Column-Oriented Data Storage

|Column: ID|1|2|3|
|---|---|---|---|
|Column: Name|John|Jane|Bob|
|Column: Age|35|28|42|
|Column: Department|IT|HR|Finance|

### Query Behavior

- Only the columns needed for the query are read.
- Supports columnar compression, reducing storage and improving performance.
- Retrieving full rows is more complex as data is spread across multiple columns.

### Advantages

1. ****Optimized for OLAP:**** Ideal for analytical queries on large datasets.
2. ****Faster Queries on Selected Columns:**** Only relevant data is scanned.
3. ****Storage Efficiency:**** Columnar compression reduces space requirements.

### Disadvantages

1. ****Complex Full Row Retrieval:**** Combining multiple columns may require more processing.
2. ****Less Suitable for OLTP:**** Frequent inserts, updates, or deletes are less efficient.
3. ****Query Complexity:**** May require specialized query languages or optimization techniques.

## Difference Between Row-Oriented Database and Column-Oriented Database

|Feature|Row-Oriented Database|Column-Oriented Database|
|---|---|---|
|Data Storage|Row by row|Column by column|
|Optimized For|OLTP (transactions)|OLAP (analytics)|
|Example|Relational Database (MySQL, PostgreSQL)|HBase, Cassandra, Amazon Redshift|
|Query Performance|Fast for retrieving full rows|Fast for queries on specific columns|
|Storage Efficiency|Less efficient, less compression|High compression, storage-efficient|
|Scaling|Traditional scaling; may become slower as data grows|Designed for horizontal scaling and partitioning|
|Full Row Retrieval|Simple|More complex|
|Schema|Fixed Schema|Flexible/Schema-less (like HBase)|
|Table Type|Thin tables|Wide, sparsely populated tables|

> ****Choosing the Right Database:**** If your system performs many transactions, choose a row-oriented database, but If your system performs analytics or needs to read specific columns from large datasets, choose a column-oriented database.


---
 
# Schema-on-write vs Schema-on-read

Source:- https://www.geeksforgeeks.org/sql/what-is-schema-on-read-and-schema-on-write-in-hadoop/
	**Schema on-Read** is the new data investigation approach in new tools like [Hadoop](https://www.geeksforgeeks.org/data-engineering/hadoop-an-introduction/) and other data-handling technologies. In this schema, the analyst has to identify each set of data which makes it more versatile. This schema is used when the data organization is not the optimal goal but the data collection is a priority. Which makes it easier to create two views on the same data. The use of this Schema made Hadoop technology more popular in today's business scenarios.

**Advantages of using Schema On Read** 

- This approach provides us the benefit of flexibility of the type of data to be consumed.
- It enhances the data generation speed to the availability of data.
- It provides flexibility to store unstructured, semi-structured, loosely or unorganized data.

**Disadvantages of using Schema On Read** 

- It is required to invest time in creating jobs into schema-on-read.
- It does not allow you to look into the schema and identify what data is present in it.
- It is a little expensive in terms of computing resources are utilized.

![Schema on-Read](https://media.geeksforgeeks.org/wp-content/uploads/20201013102054/Hadoop_Schema_on_Read.png)

'
**Schema on write** is a technique for storing data into databases. This has provided a new way to enhance traditional sophisticated systems. It is a newer way of handling data over Schema-on-Read as it provides flexibility to the businesses in big data and analytics. It provides the user to achieve consistency in the data but is very restrictive to the type of data inserted which makes it rejection to many unstructured types of data. With some alterations with hardware and software, it is easily capable to handle a variety of data.

**Advantages of using Schema On Write**

- This approach helps to express the relationship between data points.
- As the schema is being described the user/tool can start its work.
- This approach makes you store dense data.

**Disadvantages of using Schema On Write**

- Schema is to built for specific purposes.
- Schema Requires enough modeling to get it ready for work.
- Semi-structured or unstructured data are not a perfect fit for this approach.

![Schema on write](https://media.geeksforgeeks.org/wp-content/uploads/20201013102211/Hadoop_Schema_on_Write.png)
 
 
 