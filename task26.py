import re


def extract_domains(email_list):
    domain_pattern = r'@([A-Za-z0-9.-]+)'
    domains = []

    for email in email_list:
        match = re.search(domain_pattern, email)
        if match:
            domain = match.group(1)
            domains.append(domain)

    return domains


def extract_vowel_words(text):
    return re.findall(r'\b[aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ][a-zA-Zа-яёА-ЯЁ]*\b', text)


def split_string_by_delimiters(string, *delimiters):
    delimeter_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(delimeter_pattern, string)


if __name__ == '__main__':
    # 1
    print('Task 1\n=====================================')
    email_list = [
        'user1@example.com',
        'user2@gmail.com',
        'user3@yahoo.com',
    ]

    print(*extract_domains(email_list))

    # 2
    print('Task 2\n=====================================')
    print(*extract_vowel_words(
        "Съешь ещё этих мягких французских булок, да выпей же чаю. The quick brown fox jumps over the lazy dog"
    ))

    # 3
    print('Task 3\n=====================================')
    print(split_string_by_delimiters("Hello, World;How|are:you", ',', ';', '|', ':'))
