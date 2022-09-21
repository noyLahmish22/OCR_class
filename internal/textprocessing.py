import csv
import cv2
from autocorrect import Speller
from .consts import path_dic_data


def create_text_file(details, cwd, lang, num, path):
    total_boxes = len(details['text'])
    threshold_img = cv2.imread(path)
    for sequence_number in range(total_boxes):
        if int(details['conf'][sequence_number]) > 30:
            (x, y, w, h) = (
                details['left'][sequence_number], details['top'][sequence_number],
                details['width'][sequence_number],
                details['height'][sequence_number])
            threshold_img = cv2.rectangle(threshold_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    parse_text = []
    word_list = []
    last_word = ''
    line_num = 1
    list_lines = {}
    for word in details['text']:
        if word != '':
            if lang == 'eng':
                spelling = Speller(lang='en')
                word = spelling(word)
            word_list.append(word)
            last_word = word
        if (last_word != '' and word == '') or (word == details['text'][-1]):
            parse_text.append(word_list)
            list_lines[line_num] = word_list
            word_list = []
            line_num += 1
    with open(cwd + path_dic_data + 'result_text' + str(num) + '.txt', 'w', newline="", encoding="utf-8") as file:
        csv.writer(file, delimiter=" ").writerows(parse_text)
    return parse_text


def clear_character(details, bad_chars):
    details['text_clear'] = []
    for data in details['text']:
        if data.isdigit() or data.isalpha() or data in bad_chars:
            if len(data) != 1:
                details['text_clear'].append(data)
    return details


