from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exceptions import HiveMindException
from src.utils.logger import logger


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(HiveMindException)
    async def hivemind_exception_handler(
        request: Request,
        exc: HiveMindException
    ):

        logger.error(exc.message)

        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "message": exc.message
            }
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception
    ):

        logger.exception(exc)

        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "Internal Server Error"
            }
        )