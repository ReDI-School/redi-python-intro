import yaml

qa_dict = {}
language = 'English'


def get_dict_from_file( filename ):
    with open(filename, 'r') as dictionary_file:
         qa_dict = yaml.load(dictionary_file)


def main():
    load_dict_from_file('dictionary.yaml')
    print(qa_dict[language])


if __name__ == '__main__':
    main()
