## connection string to postgresql database 

import os

CONNECTION_STRING = (
    
    f"host={os.getenv('DATABASE_HOST')}"
    f" port={os.getenv('DATABASE_NAME')}"
    f" dbname={os.getenv('DATABASE_USER')}"
    f" user={os.getenv('DATABASE_PASSWORD')}"
    f" password={os.getenv('DATABASE_PORT')}"

)