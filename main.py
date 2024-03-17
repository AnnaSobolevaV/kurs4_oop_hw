from utils.functions import load_data

DATA_PATH = "./data/products.json"

def main():
    data = load_data(DATA_PATH)
    print(data)



if __name__ == '__main__':
    main()