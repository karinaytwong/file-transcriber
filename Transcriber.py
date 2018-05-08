import os

def populate_dict(file_name, BOM, separators, dictionary, key, values):
    with open(os.path.join(os.getcwd(), file_name), mode='r', encoding='utf-8') as file:
        for line in file:
            if BOM:
                line = line.strip('\ufeff')
            line = line.strip()
            line = line.split(separators)
            if values:
                dictionary[line[key]] = line[1:]
            else:
                dictionary[line[key]] = line[1]

def file_to_arpabet(file_name, arpabet_list):
    with open(os.path.join(os.getcwd(), file_name), mode='r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            line = line.split(' ')
            for word in line:
                word = word.upper()
                word = word.strip('.,?!;:"_')
                if len(word)>0:
                    arpabet_list.append(cmudict[word])
                else:
                    arpabet_list.append([''])
            
def transcribe(original, ipa):
    for transcription in original:
        for word in transcription:
            word = word.split(' ')
            ipa_word = list()
            for phoneme in word:
                if phoneme:
                    phoneme = arpabet2ipa[phoneme]
                    ipa_word.append(phoneme)
        ipa.append(''.join(ipa_word))

def ipa_to_file(file_name, transcription):
    with open(os.path.join(os.getcwd(), file_name), mode='w', encoding='utf-8') as output:
        for word in transcription:
            if word == '':
                output.write('\n')
            else:
                output.write(word + ' ')

arpabet2ipa = dict()
cmudict = dict()
threepigs = list()
ipa = list()

populate_dict('arpabet2ipa.txt', True, ',', arpabet2ipa, 0, False)
populate_dict('cmudict.txt', False, '  ', cmudict, 0, True)
file_to_arpabet('three_little_pigs.txt', threepigs) ##input file currently "Three Little Pigs"
transcribe(threepigs, ipa)
ipa_to_file('output.txt', ipa) ##rename output file as desired
