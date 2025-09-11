# Managing EC2 Instances on AWS

![](https://github.com/mizhare/aws-santander-2025/blob/main/challenge%201%20-%20managing%20ec2%20instances/images/diagram_s3_ec2.png)

## Data Architecture Overview

This project was developed as the deliverable for the challenge **"Managing EC2 Instances on AWS"**.  
The objective was to design a simple yet realistic data pipeline that demonstrates how **EC2, S3, Lambda, and other AWS services** can be integrated, while applying the concepts covered in the first module: **IAM, EC2 instances, snapshots, and related fundamentals**.

In this project, I aimed to show how we can go from **raw CSV uploads** to **processed data, analytics, and dashboards**, leveraging AWS services in combination with **PySpark for data transformation**.

The focus was not only on processing data, but on building an **end-to-end flow**: from ingestion, processing, and storage, to querying, governance, and visualization. This provides a clear picture of how a **modern data platform** can be implemented in practice.

---
### Step-by-step flow

1. **User Upload (CLI or UI)**  
    Users upload raw CSV files either through the interface or via the AWS CLI (Command Line Interface). IAM ensures that only authorized users can perform this step.
2. **Raw Storage (S3)**  
    The files land in an S3 bucket that acts as our raw data lake. From there, a snapshot copy is made for backup and recovery.
3. **Trigger (Lambda)**  
    Every time a new file arrives, a Lambda function is triggered. It works as an orchestrator, kicking off the processing job on an EC2 instance.
4. **Processing (EC2 with PySpark)**  
    On the EC2 instance, PySpark jobs take care of cleaning, transforming, and enriching the raw data. Logs are streamed to CloudWatch for monitoring, and fail alerts are sent if something goes wrong.
5. **Processed Storage (S3)**  
    Once transformed, the cleaned datasets are stored in a separate S3 bucket, optimized for analytics.
6. **Governance (Glue Catalog + IAM)**  
    Metadata is tracked using the Glue Data Catalog, while IAM and Admin roles enforce governance, permissions, and compliance.
7. **Analytics (Athena + Databricks)**  
    Amazon Athena makes it possible to run SQL queries directly on the processed data in S3. Databricks can also connect to Athena for more advanced analysis and collaborative work.
8. **Visualization (Dashboards / BI)**  
    Finally, analysts can build dashboards in Databricks or BI tools (QuickSight, Tableau, Power BI) to turn the data into insights for decision-making.
    
---

### Insights

- **S3 as a Data Lake**: flexible, cost-efficient, and scalable.
- **Lambda + EC2 with PySpark**: serverless orchestration plus distributed processing power.
- **Snapshots & Monitoring**: keeps data safe and ensures issues are tracked.
- **Athena + Glue**: query-ready data without the need for a dedicated cluster.
- **Databricks + Dashboards**: bridges technical analytics with business insights.
- **IAM Governance**: ensures users only have the right level of access.
    
