import boto3
import os


def upload_to_s3(local_dir, bucket, s3_prefix=""):
    """
    Upload all files from local_dir to the S3 bucket,
    preserving the folder structure.

    :param local_dir: Local folder containing the website files
    :param bucket: Name of the S3 bucket
    :param s3_prefix: Optional prefix (folder) inside the bucket
    """
    s3 = boto3.client("s3")

    for root, _, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            # Preserve relative subfolders
            s3_key = os.path.relpath(local_path, local_dir)
            if s3_prefix:
                s3_key = os.path.join(s3_prefix, s3_key)

            # Upload the file
            s3.upload_file(local_path, bucket, s3_key)
            print(f"✅ Transfer completed: {local_path} -> s3://{bucket}/{s3_key}")


if __name__ == "__main__":
    # Get bucket name from environment variable
    bucket_name = os.getenv("AWS_S3_BUCKET")

    if not bucket_name:
        print("Attention: set the AWS_S3_BUCKET environment variable with your bucket name")
    else:
        upload_to_s3("s3-ingestion/website", bucket_name, "")