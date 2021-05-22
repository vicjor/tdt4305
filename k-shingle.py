def compute_gram(doc_data, k=2):
    """
    In natural language processing a w-shingling is a set of unique "shingles"
    (n-grams, contiguous subsequences of tokens in a document)
    Very much similar to n-grams but here we consider characters
    """
    sh = set()
    if len(doc_data) >= k:
        for pos, token in enumerate(doc_data):
            if pos + k <= len(doc):
                sh.add(doc[pos:pos + k])
        return sh
    else:
        print('Tokens are not available')
    pass


def compute_jaccard_sim(set1, set2):
    """
    Compute the Jaccard similarity between two sets
    Keyword Arguments
    set1 , set2 -- two sets to be compated
    """
    intersection = set1 & set2  # using Python's symbol for intersection
    union = set1 | set2  # using Python's symbol for union

    # Jaccard similarity is the number of elements in the intersection divided by
    # number of elements in the union of two sets
    jaccard_similarity = len(intersection) / len(union)
    return jaccard_similarity


if __name__ == "__main__":

    # Documents
    documents = ["baaa", "accc", "abba", "baac"]

    # Shingling size
    w = 2
    docs = {}
    for index, doc in enumerate(documents):
        docs[doc] = compute_gram(doc, k=w)
        print("Then the set of %s-shingles for doc[%s] : %s" %
              (w, index+1, compute_gram(doc_data=doc, k=w)))
    print()
    print("Jaccard similarities:")
    for key, val in docs.items():
        for key2, val2 in docs.items():
            print(key, " and ",
                  key2, compute_jaccard_sim(val, val2))
