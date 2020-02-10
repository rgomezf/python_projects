from collections import defaultdict

COLLECTION_ONE = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

COLLECTION_TWO = (
    ('Yasoob', 'Brown'),
    ('Ali', 'Purple'),
    ('Ahmed', 'Black'),
    ('Mar', 'Blue'),
    ('Asi', 'Red'),
    ('Nav', 'Pink')
)


def main():
	final_collection = defaultdict(list)

	final_collection = unify_collections(COLLECTION_ONE, COLLECTION_TWO)
    
	print(final_collection)


def unify_collections(first_collection, second_collection):
	result_collection = defaultdict(list)
        
        result_collection.update(List(set([data for data in COLLECTION_ONE if COLLECTION_TWO.count(ele) > 0])))
	for item, value in result_collection.items():
	    yield "{}: {}".format(item, result_collection[item])
	
if __name__ == '__main__':
    main()

