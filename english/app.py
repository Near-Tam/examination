#-*- coding:utf-8 -*-
import sys
import yaml
import random
import argparse

reload(sys)
sys.setdefaultencoding('utf-8')

from log import logger

FLAGS = None
TIMES = 3
WORD_EN = 0
WORD_CN = 2
log = logger(__name__).get_logger()

def load_yml(yml_file=None):
    if yml_file == None:
        yml_file = FLAGS.yml_file
    # with open(yml_file, 'r', encoding='utf-8') as f:
    with open(yml_file, 'r') as f:
        res = yaml.load(f)
    return res

def get_groups(content):
    groups = list()
    if FLAGS.is_all:
        for lesson in content:
            groups.extend(content[lesson])
    else:
        lessons = FLAGS.lessons.split(',')
        for lesson in lessons:
            groups.extend(content[lesson])
    random.shuffle(groups)
    return groups

def get_en_or_cn():
    index = random.randint(0, 1)
    if index == 1:
        index = WORD_CN
    # Force index
    index = WORD_CN
    return index

def judge(group, answer, give_index):
    if give_index == WORD_CN:
        if answer == group[WORD_EN]:
            return True
        else:
            return False
    else:
        # using jaccard sim to judge.
        return None

def question(group, time=0):
    give_index = get_en_or_cn()
    log.info('Question: {0}'.format(group[give_index]))
    answer = raw_input('Answer: ')
    is_right = judge(group, answer, give_index)
    if is_right:
        log.info('o {0}, {1}, {2}'.format(group[0], group[1], group[2]))
        return True
    else:
        time += 1
        if time < TIMES:
            question(group, time)
        else:
            log.error('x {0}, {1}, {2}'.format(group[0], group[1], group[2]))
        return False

def testing(groups):
    false_set = list()
    for group in groups:
        is_pass = question(group)
        if is_pass is not True:
            false_set.append(group)
    if len(false_set) == 0:
        return None
    else:
        random.shuffle(false_set)
        testing(false_set)

def run():
    content = load_yml()
    groups = get_groups(content)
    testing(groups)
    log.info('You are finish the task.')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--yml_file',
        type=str,
        default='./lessons.yml',
        help='Directory for storing classify data.')
    parser.add_argument(
        '--is_all',
        type=bool,
        default=False,
        help='Select whether all words are loaded for testing.'
    )
    parser.add_argument(
        '--lessons',
        type=str,
        default='lesson1',
        help='Which lessons would you want.'
    )
    FLAGS, unparsed = parser.parse_known_args()
    run()
