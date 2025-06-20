from urllib.parse import quote_plus
from langchain_community.llms import CTransformers
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

def get_few_shot_db_chain():
    db_user = "root"
    db_password = quote_plus("@Manya1919")
    db_host = "127.0.0.1"
    db_name = "atliq_tshirts"

    db = SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
        sample_rows_in_table_info=3
    )

    llm = CTransformers(
        model=r"C:\model\llama-2-7b-chat.ggmlv3.q8_0.bin",  # Adjust this path if needed
        model_type="llama",
        config={
            "max_new_tokens": 512,
            "temperature": 0.3,
            "context_length": 2048
        }
    )

    db_chain = SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        verbose=True,
        return_intermediate_steps=True
    )

    return db_chain
