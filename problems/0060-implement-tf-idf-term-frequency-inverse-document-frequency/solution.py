import numpy as np
import math

def compute_tf_idf(corpus, query):
	"""
	Compute TF-IDF scores for a query against a corpus of documents.
    
	:param corpus: List of documents, where each document is a list of words
	:param query: List of words in the query
	:return: List of lists containing TF-IDF scores for the query words in each document
	"""
	result=[]
	m=len(corpus)
	df=sum(1 for doc in corpus if query[0] in doc)
	n=len(query)
	for i in range(m):
		flag=[]
		for j in range(n):
			dj=len(corpus[i])#jisuanzhegeliebiaoyouduoshaociyuan
			tmp=corpus[i].count(query[j])
			tf=tmp/dj
			idf=math.log((m+1)/(df+1))+1
			flag.append(tf*idf)
		result.append(flag)
	return result
