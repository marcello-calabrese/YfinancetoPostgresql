## connection string to postgresql database 

import os

CONNECTION_STRING = (
    
    f" Host={os.getenv('DATABASE_HOST')}"
    f" Database={os.getenv('DATABASE_NAME')}"
    f" Username={os.getenv('DATABASE_USER')}"
    f" Password={os.getenv('DATABASE_PASSWORD')}"
    f" Port={os.getenv('DATABASE_PORT')}"

)