
## About

This document contains a step-by-step process to deploy a static website on AWS S3. It was developed as part of the **"Creating Resources" module** in the Santander AWS Bootcamp 2025. I built it on my own to **document, consolidate concepts, and demonstrate what I have learned**.

The base structure for this project was inspired by  [alexsandrolechner/awscloudfoundations](https://github.com/alexsandrolechner/awscloudfoundations) and then customized with new ideas, including local automation scripts and CI/CD setup.

### Core Steps

1. Creating the S3 Bucket: Configure the bucket, enable static website hosting, add bucket policy (s3:GetObject), and create an Access Point.
2. Local Ingestion: Use local_ingestion.py with AWS CLI credentials for manual uploads.
3. CI/CD Deployment: main.yaml workflow automates updates whenever changes are pushed.

### Extensions / Custom Features
- Automated the upload process with a custom **local_ingestion.py** script using Boto3, configured with AWS CLI.
- Adapting the workflow to support flexible file organization within the repository.

## Creating the S3 Bucket
* In AWS Console, search for S3 and create the first bucket

  
![](https://github.com/mizhare/aws-santander-2025/blob/main/s3-ingestion/images/s3-view.png)



* For the configuration, I chose **General Purpose** and unchecked the **Block Public Access** settings. This is necessary because we later create an **Access Point** to control public access.

  
 
![](https://github.com/mizhare/aws-santander-2025/blob/main/s3-ingestion/images/creating-bucket-v1.png)


![](https://github.com/mizhare/aws-santander-2025/blob/main/s3-ingestion/images/creating-bucket-v2.png)



* Enable **Static Website Hosting** in the bucket properties to allow the S3 bucket to serve HTML files.



![](https://github.com/mizhare/aws-santander-2025/blob/main/s3-ingestion/images/bucket-properties-step3.png)



* On the **Permissions** page, edit the **Bucket Policy** to add an s3:GetObject permission.
	* This permission is required so that users (through the browser) can fetch and display objects such as HTML, CSS, JavaScript, and images from your bucket. Without this, the website would exist in the bucket but would not be publicly accessible.


![](https://github.com/mizhare/aws-santander-2025/blob/main/s3-ingestion/images/add-policy-step4.png)



* In the **Access Point** page, create an Access Point and configure the network setting as **Internet**. In the Block Public Access options, only leave the last two checked (to avoid overly restrictive settings while still maintaining security).


![](https://github.com/mizhare/aws-santander-2025/blob/main/s3-ingestion/images/create-acesspoint-step5.png)



* Below is the final view of the S3 bucket with the uploaded files:

![](https://github.com/mizhare/aws-santander-2025/blob/main/s3-ingestion/images/s3-final-view.png)




## Setting Up Access and Deployment

- For **local ingestion** (local_ingestion.py), I configured access using the **AWS CLI**, setting up the user and access key. This script automates file uploads from my local machine to the S3 bucket.
    
- For **automation with GitHub Actions** (main.yaml), I created **Secrets** in GitHub (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, and S3_BUCKET) to securely connect GitHub with AWS. This enables a CI/CD pipeline that automatically deploys updates to the S3 bucket whenever I push changes to the main branch.



## Final Result
Here is the final view of the static HTML site hosted directly from S3

![](https://github.com/mizhare/aws-santander-2025/blob/main/s3-ingestion/images/html-s3.png)
