class HttpErrors:
    """Http errors definition"""

    @staticmethod
    def error_422():
        """HTTP Code: 422 - Unprocessable Entity"""
        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_400():
        """HTTP Code: 400 - Bad Request"""
        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_409():
        """HTTP Code: 409 - Conflict"""
        return {"status_code": 409, "body": {"error": "Conflict"}}
