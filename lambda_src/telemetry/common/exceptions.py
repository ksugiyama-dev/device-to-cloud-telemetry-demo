class UnprocessedItemsError(RuntimeError):
    """Raised when DynamoDB items remain unprocessed after all retries."""