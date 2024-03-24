from utils.functions import load_data, to_create_list_of_categories_with_products

DATA_PATH = "./data/products.json"


def main():
    data = load_data(DATA_PATH)
    categories = to_create_list_of_categories_with_products(data)
    for category in categories:
        print(category)
    print("Done!")


if __name__ == '__main__':
    print("****")
    main()
