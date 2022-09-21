import logging
import os
from internal.functions import get_text_from_files
from internal.consts import path_dic_data
import uvicorn
from fastapi import FastAPI, UploadFile, Form, File


app = FastAPI()


@app.get("/isalive")
async def root():
    return {"message": "is alive"}


@app.post("/image_path")
async def create_upload_file(file: UploadFile = File(...), language: str = Form(...)):
    """
    get file and the language which are exists in it and return the text from the document in Hebrew

    """
    logging.error("get file path " + file.filename)
    cwd = os.getcwd()
    ex = str(file.filename).split(".")[-1:][0]
    fullpath = os.path.join(cwd + path_dic_data + "doc." + ex)
    test_flag = False
    text = get_text_from_files(fullpath, cwd, file, language, test_flag, ex)
    return text


if __name__ == "__main__":
    # update uvicorn access logger format
    # log_config = uvicorn.config.LOGGING_CONFIG
    # log_config["formatters"]["access"][
    #     "fmt"] = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s] - %(message)s"
    # uvicorn.run(app, host="0.0.0.0", port=EXPOSE_PORT, log_config=log_config)
    uvicorn.run(app, host="0.0.0.0", port=443)
