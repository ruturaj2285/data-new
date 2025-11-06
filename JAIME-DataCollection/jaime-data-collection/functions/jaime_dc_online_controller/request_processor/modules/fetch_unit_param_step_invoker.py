import os
import json
import boto3
import logging
from request_processor.utils.constants import (
    STEP_FUNCTIONS_ARN,
    SUCCESS_MESSAGE,
    ERROR_MESSAGE,
    MISSING_STEP_FUNCTIONS_ARN_MESSAGE,
)

class RequestProcessor:
    def __init__(self):
        self.step_functions_arn = os.getenv(STEP_FUNCTIONS_ARN)
        self.sfn = boto3.client('stepfunctions')

    def process_request(self, event) -> str:
        try:
            if not getattr(self, 'step_functions_arn', None):
                logging.error(MISSING_STEP_FUNCTIONS_ARN_MESSAGE)
                return MISSING_STEP_FUNCTIONS_ARN_MESSAGE

            logging.info("Initializing step functions execution")
            input_payload = {
                "detail-type": event.get("detail-type"),
                "source": event.get("source"),
                "event_id": event.get("id"),
                "event_time": event.get("time")
            }
            
            logging.info(f"Starting step functions trigger for execution with input: {input_payload}")
            self.sfn.start_execution(
                stateMachineArn=self.step_functions_arn,
                input=json.dumps(input_payload)
            )
            return SUCCESS_MESSAGE
        except Exception as e:
            logging.error(f"Error starting step functions execution: {e}")
            return ERROR_MESSAGE