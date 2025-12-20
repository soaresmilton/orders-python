from .http_bad_request import HttpBadRequestError
from .http_unprocessable_entity import HttpUnprocessableEntityError
from .http_not_found import HttpNotFound
from typing import Dict

def handle_errors(error: Exception) -> Dict:
  if isinstance(error, (HttpBadRequestError, HttpUnprocessableEntityError, HttpNotFound)):
    return {
      "status_code": error.status_code,
      "body": {
        "errors": [
          {
            "title": error.name,
            "detail": error.message
          }
        ]
      }
    }
  

  return {
      "status_code": 500,
      "body": {
        "errors": [
          {
            "title": "Server error",
            "detail": str(error)
          }
        ]
      }
    }