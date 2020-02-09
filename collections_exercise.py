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
    
	print(next(final_collection))


def unify_collections(first_collection, second_collection):
	result_collection = defaultdict(list)

	for key, value in first_collection:
		if result_collection.get(key) != value:
			result_collection[key].append(value)

	for key, value in second_collection:
		if result_collection.get(key) != value:
			result_collection[key].append(value)

	for item in result_collection:
	    yield "{}: {}".format(item, result_collection[item])
	
if __name__ == '__main__':
    main()

