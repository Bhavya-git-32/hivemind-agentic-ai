# Claims API Architecture

The Claims API is implemented using FastAPI and AWS Lambda.

The API receives XML claim files uploaded to Amazon S3.

The XML files are validated against predefined schemas before processing.

Validated data is transformed into a structured format and stored in Amazon Redshift.

Amazon CloudWatch provides logging, monitoring, and operational metrics.

API Gateway exposes secure REST endpoints for downstream applications.