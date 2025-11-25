from datetime import datetime
import math


def separator(title: str = "") -> None:
    """Print a formatted section separator."""
    print("\n" + "=" * 20 + f" {title} " + "=" * 20 + "\n")


# Исходные данные
email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": (
        "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and "
        "let me know your feedback.\n\nBest,\nAlice"
    ),
}

# 2. Добавить дату отправки
separator("2. Добавление даты отправки")

send_date = datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

print(f"email с актуальной датой отправки:\n{email}")

# 3. Нормализовать email-адреса
separator("3. Нормализация адресов")

email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

print(
    f"Нормализованные адреса:\nfrom: {email['from']}\n"
    f"to:   {email['to']}"
)

# 4. Извлечение логина и домена
separator("4. Извлечение логина и домена")

login, domain = email["from"].split("@")
print(f"login: {login}, domain: {domain}")

# 5. Сокращённая версия текста
separator("5. Сокращённая версия текста")

email["short_body"] = email["body"][:10] + "..."
print(f"short_body: {email['short_body']}")

# 6. Уникальные списки доменов
separator("6. Списки доменов")

personal_domains = list({
    "gmail.com", "list.ru", "yahoo.com", "outlook.com", "hotmail.com",
    "icloud.com", "yandex.ru", "mail.ru", "bk.ru", "inbox.ru"
})

corporate_domains = list({
    "company.ru", "corporation.com", "university.edu",
    "organization.org", "business.net"
})

print(f"Личные домены:\n{personal_domains}")
print(f"Корпоративные домены:\n{corporate_domains}")

# 7. Проверка пересечений
separator("7. Проверка пересечений доменов")

intersection = set(personal_domains) & set(corporate_domains)
print(f"Пересечения: {intersection}")

# 8. Корпоративность отправителя
separator("8. Корпоративность отправителя")

is_corporate = domain in corporate_domains
print(f"is_corporate: {is_corporate}")

# 9. Чистый текст без табов и переносов
separator("9. Чистый текст сообщения")

email["clean_body"] = (
    email["body"]
    .replace("\t", " ")
    .replace("\n", " ")
)

print(f"clean_body:\n{email['clean_body']}")

# 10. Текст отправленного письма
separator("10. Текст отправленного письма")

email["sent_text"] = (
    f"Кому: {email['to']}, от {email['from']}\n"
    f"Тема: {email['subject']}, дата {email['date']}\n"
    f"{email['clean_body']}"
)

print(email["sent_text"])

# 11. Количество страниц
separator("11. Подсчёт страниц")

pages = math.ceil(len(email["sent_text"]) / 500)
print(f"Количество страниц: {pages}")

# 12. Проверка пустоты темы и тела
separator("12. Проверка пустоты темы и тела")

is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

print(f"is_subject_empty: {is_subject_empty}")
print(f"is_body_empty: {is_body_empty}")

# 13. Маска email отправителя
separator("13. Маска e-mail отправителя")

email["masked_from"] = f"{login[:2]}***@{domain}"
print(f"masked_from: {email['masked_from']}")

# 14. Удаление доменов
separator("14. Удаление доменов из списка")

for removed in ("list.ru", "bk.ru"):
    if removed in personal_domains:
        personal_domains.remove(removed)

print(f"Личные домены после удаления:\n{personal_domains}")

# Финальный вывод
separator("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ")

print("Итоговый словарь email:")
print(email, "\n")

print("Булевы переменные и число страниц:")
print(
    f"is_corporate={is_corporate}, "
    f"is_subject_empty={is_subject_empty}, "
    f"is_body_empty={is_body_empty}, "
    f"pages={pages}"
)
