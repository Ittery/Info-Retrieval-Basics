import glob
import math as m

def tf(term, doc):  
      
    """ 
    Input: term: Term in the Document, doc: Document 
    Return: Normalized tf: Number of times term occurs 
      in document/Total number of terms in the document 
    """
    # Splitting the document into individual terms 
    normalizeTermFreq = doc.lower().split()  
  
    # Number of times the term occurs in the document 
    term_in_document = normalizeTermFreq.count(term.lower())  
  
    # Total number of terms in the document 
    len_of_document = float(len(normalizeTermFreq ))  
  
    # Normalized Term Frequency 
    normalized_tf = term_in_document / len_of_document  
  
    return normalized_tf

def idf(term, allDocs): 
    num_docs_with_given_term = 0
  
    """ 
    Input: term: Term in the Document, 
           allDocs: Dictionary of all documents 
    Return: Inverse Document Frequency (idf) for term 
            = Logarithm ((Total Number of Documents) /  
            (Number of documents containing the term)) 
    """
    # Iterate through all the documents 
    for doc in allDocs: 
          
        """ 
        Putting a check if a term appears in a document. 
        If term is present in the document, then  
        increment "num_docs_with_given_term" variable 
        """
        if term.lower() in allDocs[doc].lower().split(): 
            num_docs_with_given_term += 1
  
    if num_docs_with_given_term > 0: 
        # Total number of documents 
        total_num_docs = len(allDocs)  
  
        # Calculating the IDF  
        idf_val = m.log(float(total_num_docs) / num_docs_with_given_term) 
        return idf_val 
    else:  
        return 0

def tfidf( t, d ) :
    return tf(t, d)* idf(t, d) 

def norm_file(content) : 
    content = content.replace('\n', ' ')
    content = content.replace('.', ' ')
    content = content.replace(',', ' ')
    content = content.replace('!', ' ')
    content = content.replace('#', ' ')
    content = content.replace('$', ' ')
    content = content.replace('%', ' ')
    content = content.replace('^', ' ')
    content = content.replace('&', ' ')
    content = content.replace('*', ' ')
    content = content.replace('(', ' ')
    content = content.replace(')', ' ')
    content = content.replace('-', ' ')
    content = content.replace('_', ' ')
    content = content.replace('+', ' ')
    content = content.replace('=', ' ')
    content = content.replace(':', ' ')
    content = content.replace(';', ' ')
    content = content.replace('\"', ' ')
    content = content.replace('\'', ' ')
    content = content.replace('|', ' ')
    content = content.replace('<', ' ')
    content = content.replace('>', ' ')
    content = content.replace('?', ' ')
    content = content.replace('~', ' ')
    content = content.replace('`', ' ')
    c=content.split()

    #Making it all lower case
    for i in range(len(c)):
        c[i]=c[i].lower()
    newst=" ".join(c)
    return list(set(c)),newst

tf_idf={}
files = glob.glob("Data/*.txt")
print("The files from which data is being read are :", files)
alldocs={}
newst=''

#To fetch normalized text form of all the files being read in a single list.
for f in files:
    content = open(f).read()
    terms, newst=norm_file(content)
    alldocs[f] = newst

for f in files:
    content = open(f).read()
    print("\n"+f+" contains : \n"+content + "\n")
    tf_idf.update({f : {}})
    for term in terms :
        tf_idf[f].update({term : round(tf(term, newst) * idf(term, alldocs) , 9)})


print ("The tf-idf of the terms in the documents are :\n")
for doc in tf_idf:
    print(doc+" : ")
    print(tf_idf[doc], end="\n\n\n")


