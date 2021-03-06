# PYTHONIOENCODING=utf-8 python to_root_form.py

# пол родственников
sex = {'свекровь': 'f', 'свёкор': 'm', 'деверь': 'm', 'золовка': 'f', 'невестка': 'f', 'тёща': 'f', 'тесть': 'm',
       'шурин': 'm', 'свояченица': 'f', 'сноха': 'f', 'мать': 'f', 'отец': 'm', 'сестра': 'f', 'брат': 'm',
       'дочь': 'f', 'сын': 'm', 'бабушка': 'f', 'дедушка': 'm', 'тётя': 'f', 'дядя': 'm', 'зять': 'm', 'муж': 'm',
       'жена': 'f', 'пасынок': 'm', 'падчерица': 'f', 'сват': 'm', 'сваха': 'f', 'племянник': 'm', 'свояк': 'm',
       'племянница': 'f', 'внук': 'm', 'внучка': 'f', 'прабабушка': 'f', 'прадедушка': 'm', 'правнучка': 'f',
       'правнук': 'm', 'кузен': 'm', 'кузина': 'f', 'он': 'm', 'она': 'f', 'я': 'both', 'ты': 'both', 'вы': 'both'}


def get_root_form_string(st: str):
    error = 0
    pronoun = 'я '

    # исключения для первого слова в им. падеже
    exceptions = {'мама': 'мать', 'папа': 'отец', 'тетя': 'тётя', 'свекор': 'свёкор', 'сватья': 'сваха',
                  'дед': 'дедушка', 'бабка': 'бабушка', 'прадед': 'прадудешка', 'прабабка': 'прабабушка'}
    # исключения для местоимений
    pronouns = {'моей': 'я ', 'моего': 'я ', 'его': 'он ', 'её': 'она ', 'мой': 'я ', 'твой': 'ты ', 'ваш': 'вы ',
                'твоего': 'ты ', 'твоей': 'ты ', 'вашего': 'вы ', 'вашей': 'вы ', 'моя': 'я ', 'твоя': 'ты ',
                'ваша': 'вы '}
    k = 0  # для обработки строк, которые начинаются с местоимения
    if st.split()[0] in pronouns:  # проверка, начинается ли строка с местоимения
        pronoun = pronouns[st.split()[0]]
        k = 1  # проверка следующего слова
    if st.split()[k] in exceptions:
        temporary_st = exceptions[st.split()[k]] + ' '
    else:
        temporary_st = st.split()[k] + ' '  # добавляем первое слово в новую строку

    st = st.split()[k + 1:]  # разбиваем строку на слова
    # исключения для слов в родительном падеже
    exceptions = {'дочери': 'дочь ', 'свекрови': 'свекровь ', 'сватьи': 'сваха ', 'матери': 'мать ',
                  'мамы': 'мать ', 'отца': 'отец ', 'папы': 'отец ', 'свёкра': 'свёкор ',
                  'свекра': 'свёкор ', 'пасынка': 'пасынок ', 'тети': 'тётя ', 'тещи': 'тёща ',
                  'деда': 'дедушка ', 'бабки': 'бабушка ', 'прадеда': 'прадедушка ', 'прабабка': 'прабабушка '}
    for word in st:
        if word in exceptions:  # проверяем, есть ли слово в списке исключений
            temporary_st += exceptions[word]
        elif word in pronouns:  # проверяем, является ли слово местоимением
            pronoun = pronouns[word]
        elif word[len(word) - 2:len(word)] == 'ти' or word[
                                                      len(word) - 2:len(word)] == 'ди':  # тёти -> тётя, дяди -> дядя
            temporary_st = temporary_st + word[:len(word) - 1] + 'я '
        elif word[len(word) - 1] == 'а':  # сына -> сын
            temporary_st += word[:len(word) - 1]
            temporary_st += ' '
        elif word[len(word) - 1] == 'ы' or word[len(word) - 1] == 'и':  # сестры -> сестра, дедушки -> дедушка
            temporary_st = temporary_st + word[:len(word) - 1] + 'а '
        elif word[len(word) - 1] == 'я':  # зятя -> зять
            temporary_st = temporary_st + word[:len(word) - 1] + 'ь '
        else:
            error = 1

    new_st = pronoun
    for word in temporary_st.split()[::-1]:  # формирование новой строки в правильном порядке
        new_st = new_st + word + ' '

    # родственники, которые могут быть только у женщины
    for_women = ['свекровь', 'свёкор', 'деверь', 'золовка', 'сноха']
    for_men = ['тёща', 'тесть', 'шурин', 'свояченица', 'невестка',
               'свояк']  # родственники, которые могут быть только у мужчины

    st = new_st.split()
    for i in range(1, len(st)):
        if (st[i - 1] not in sex) or (i == len(st) - 1 and st[i] not in sex):  # есть ли вообще такой термин родства
            error = 1
        elif (st[i] in for_women and sex[st[i - 1]] == 'm') or (
                st[i] in for_men and sex[st[i - 1]] == 'f'):  # может ли существовать эта связь
            error = 2

    if error == 1:  # проверка на ошибки
        raise Exception('Допущена ошибка. Проверьте написание слов.')
    elif error == 2:
        raise Exception('Допущена ошибка. Такой родственной связи не существует.')
    else:
        return new_st  # вывод строки в правильном порядке со словами в именительном падеже
