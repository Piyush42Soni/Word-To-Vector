from word_to_vector_module.data_processor import DataProcessor
import gensim
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
import math
import logging
def initialize_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main(data):
    initialize_logging()

    wv = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True, limit=1000000)
    wv.load("/word_to_vector_project/w_to_v.model")
    Max=math.inf
    df=pd.read_csv("phrases.csv",encoding="Windows-1252")
    c=0
    ans=""
    for i in df['Phrases']:
        c=wv.wmdistance(data, i)
        if(c<Max):
            ans=i
            Max=c
    processor = DataProcessor(data)
    result = processor.process_data()
    print(f"Given string: {data}")
    print(f"Output string: {ans}")
    print(f"number of words in input: {len(result)}")
if __name__ == '__main__':
    data="Stranger in a Strange Land"
    main(data)