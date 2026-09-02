import text_parsing_functions as tpf


if __name__ == '__main__':
    # Load stopwords from file
    filepath = 'data/train_to_busan_description.txt'
    stopwords = tpf.load_stopwords('data/stopwords.txt')

    # Character names that should be replaced with 'person'
    replace = 'person'
    names = set(
        ['suan', 'seongkyeong', 'yonsuk', 'seokwoo',
         'ingil', 'yonghuk', 'jinhee']
    )

    # Test the pipeline with a sample line
    line_text = (
      "pregnant wife Seong-kyeong, "
      "a high school baseball team, "
      "rich-yet-egotistical"
    )
    cleaned_text = tpf.line_cleaning_pipeline(line_text,
                                              stopwords,
                                              names,
                                              replace)

    print(cleaned_text)

    def print_file_lines(file_name):
        lst =[]
        with open(file_name, 'r') as file:
            for line in file:
                cleaned_line = tpf.line_cleaning_pipeline(line, stopwords, names, replace)
                lst.append(cleaned_line)
        return lst

    finished_list = print_file_lines(filepath)

    def save_to_file(text):
        with open('parsed/train_to_busan.txt', mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(text))
            myfile.write('\n')

    save_to_file(finished_list)

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()