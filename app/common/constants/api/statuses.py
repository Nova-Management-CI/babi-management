

# app/core/constants.py
from fastapi import status
# from app.common import auto_transaction, statuses

CREATED = status.HTTP_201_CREATED
OK = status.HTTP_200_OK
BAD_REQUEST = status.HTTP_400_BAD_REQUEST
NOT_FOUND = status.HTTP_404_NOT_FOUND

# Codes d'erreurs métier standardisés pour tout le SaaS Nova School
AUTH_INVALID_CREDENTIALS = "AUTH_INVALID_CREDENTIALS"
AUTH_ACCOUNT_BLOCKED = "AUTH_ACCOUNT_BLOCKED"
SUBSCRIPTION_EXPIRED = "SUBSCRIPTION_EXPIRED"
FEATURE_NOT_ALLOWED = "FEATURE_NOT_ALLOWED"
RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"