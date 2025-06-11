from pydantic import BaseModel, confloat, conint
from datetime import datetime

class SalesRecord(BaseModel):
    transaction_id: str
    product_id: conint(gt=0)
    amount: confloat(gt=0)
    timestamp: datetime
    region: str
