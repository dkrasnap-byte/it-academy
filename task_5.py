def calc_word_cnt_distrib(search_queries):
    if not search_queries:
        return {}

    word_count = {}
    for query in search_queries:
        num_words = len(query.split())
        word_count[num_words] = word_count.get(num_words, 0) + 1

    total = len(search_queries)
    distribution = {}
    for num_words, count in sorted(word_count.items()):
        pct = round(count / total * 100)
        distribution[num_words] = pct

    return distribution


def word_form(n):
    if n % 10 == 1 and n % 100 != 11:
        return "слово"
    elif n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return "слова"
    else:
        return "слов"


def print_distrib(distribution):
    for num_words, percent in distribution.items():
        print(f"{num_words} {word_form(num_words)}: {percent}%")


if __name__ == '__main__':
    search_queries = [
        "watch new movies", "coffee near me", "how to find the determinant",
        "python", "data science jobs in UK", "courses for data science",
        "taxi", "google", "yandex", "bing", "foreign exchange rates USD/BYN",
        "Netflix movies watch online free",
        "Statistics courses online from top universities"
    ]
    print_distrib(calc_word_cnt_distrib(search_queries))
