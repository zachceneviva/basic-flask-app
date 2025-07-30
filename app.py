import logging

from flask import Flask

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    logger.info("Hello world endpoint was reached.")
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
