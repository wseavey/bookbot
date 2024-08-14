def main():
    file_path = 'books/frankenstein.txt'
    with open(file_path) as f:
        file_contents = f.read()
        mkreport(file_contents, file_path)

#counts the number of words in txt       
def word_count(file_contents):
    words = file_contents.split()
    tot_count = len(words)
    return tot_count

#counts the number of repeat characters in txt
def repeat_char(file_contents):
    file_contents = file_contents.lower()
    char_dic = {}
    for char in file_contents:
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic

#make report of word and character data and sort by most common occurances
def mkreport(file_contents, file_path):
    tot_count = word_count(file_contents)
    char_dic = repeat_char(file_contents)
    char_list = [{'name': i, 'num': char_dic[i]} for i in char_dic if i.isalpha()]
    char_list.sort(reverse= True, key = sort_on)
    header = f'--- Begin report of {file_path} ---'
    print(header)
    print(f'{tot_count} words found in the document')
    print()
    for char in char_list:
        print(f'The \'{char["name"]}\' character was found {char["num"]} times')
    print('--- End report ---')

#make sorting filter
def sort_on(dict):
    return dict['num']

main()