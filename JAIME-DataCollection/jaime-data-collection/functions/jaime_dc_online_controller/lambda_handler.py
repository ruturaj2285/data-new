# Standard library imports 
import json
import logging
# Third library imports 
# Will be mentioned here if used in the future 
# Local application imports
from request_processor.modules.fetch_unit_param_step_invoker import RequestProcessor
from request_processor.utils.logger_util import configure_logger

def lambda_handler(event, context):
    body = event.get("body") if isinstance(event, dict) else None
    if isinstance(body, str):
        try:
            parsed_data = json.loads(body)
        except Exception:
            parsed_data = body
    else:
        parsed_data = body if body is not None else event
    
    configure_logger(parsed_data.get("id") or "-") # type: ignore
    logging.info(f"Processing request type: {parsed_data.get('detail-type')}") # type: ignore
    
    request_processor = RequestProcessor()
    result = request_processor.process_request(parsed_data)
    logging.info(f"{result}")

