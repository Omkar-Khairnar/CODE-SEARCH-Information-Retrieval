from myapp.IRMODEL.input import queryProcessing
from myapp.IRMODEL.cosine_similarity import cosine_similarity_queryTodocs

def mainGetRankDocs(Query):
    queryProcessing(Query)
    result_dict, desc_dict = cosine_similarity_queryTodocs()
    return result_dict, desc_dict

