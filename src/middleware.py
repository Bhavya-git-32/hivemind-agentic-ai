import time

from fastapi import Request

from src.utils.logger import logger


async def log_requests(request: Request, call_next):
    """
    Logs every incoming request and its processing time.
    """

    start_time = time.time()

    response = await call_next(request)

    process_time = round((time.time() - start_time) * 1000, 2)

    logger.info(
        f"{request.method} {request.url.path} | "
        f"Status: {response.status_code} | "
        f"{process_time} ms"
    )

    return response