# Sales Data Processing Pipeline

A complete ETL pipeline that processes daily sales data from CSV files, validates transactions, calculates metrics, and loads results into a SQL database.

## Project Structure
```
sales_pipeline/
├── data/
│   ├── raw/                 # Input CSV files
│   └── processed/          # Archived processed files
├── pipeline/
│   ├── __init__.py
│   ├── extract.py          # Data ingestion logic
│   ├── transform.py        # Data transformation
│   ├── load.py             # Database loading
│   └── validation.py       # Data quality checks
├── dags/
│   └── sales_pipeline.py   # Airflow orchestration
├── tests/                  # Unit tests
├── Dockerfile              # Containerization
├── requirements.txt        # Dependencies
└── README.md               # Setup/usage instructions
```

## Setup Instructions

```bash
# Clone repository
git clone https://github.com/yourrepo/sales-pipeline.git
cd sales-pipeline

# Build Docker image
docker build -t sales-pipeline .

# Run pipeline
docker-compose up -d

# Execute tests
pytest tests/
```
