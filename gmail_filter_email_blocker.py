import pandas as pd
from collections import defaultdict

def group_emails_by_domain(email_list):
    grouped = defaultdict(list)
    for email in email_list:
        if "@" in email:
            local, domain = email.split("@", 1)
            grouped[domain].append(email.strip())
    return grouped

def create_domain_grouped_filter_blocks(csv_path, column='Email', char_limit=1400, separator='--- FILTER BREAK ---'):
    df = pd.read_csv(csv_path)
    emails = df[column].dropna().drop_duplicates().tolist()

    grouped = group_emails_by_domain(emails)
    all_blocks = []

    for domain in sorted(grouped.keys()):
        domain_emails = grouped[domain]
        block = ''
        for email in domain_emails:
            if len(block) + len(email) + 4 > char_limit:
                all_blocks.append(block.strip(' OR '))
                block = ''
            block += f"{email} OR "
        if block:
            all_blocks.append(block.strip(' OR '))

    return f"\n\n{separator}\n\n".join(all_blocks)

# Example usage
if __name__ == "__main__":
    filter_string = create_domain_grouped_filter_blocks('senders.csv')

    with open('gmail_filter_ready_grouped.txt', 'w') as f:
        f.write(filter_string)

    print("✅ Grouped and deduplicated Gmail filter saved to: gmail_filter_ready_grouped.txt")