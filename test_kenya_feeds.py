import requests, re

urls_to_try = [
    'https://www.standardmedia.co.ke/rss/',
    'https://www.citizen.digital/feed/',
    'https://nation.africa/kenya/rss/',
]

for url in urls_to_try:
    try:
        r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        print(f'\n=== {url} ===')
        print(f'Status: {r.status_code}')
        
        if r.status_code == 200:
            text = r.text
            
            # Check for RSS/XML content
            if '<rss' in text.lower() or '<feed' in text.lower():
                print('Contains RSS/Feed markup')
                # Try to extract items
                items = re.findall(r'<item>.*?<title>(.*?)</title>', text, re.DOTALL)
                if items:
                    print(f'Found {len(items)} items')
                    for i, item in enumerate(items[:3]):
                        print(f'  {i+1}. {item[:70]}')
                else:
                    print('No items found with simple regex')
            else:
                print('No RSS markup - likely HTML page')
                # Look for RSS links
                links = re.findall(r'href=["\'](.*?)["\']', text)
                rss_links = [l for l in links if 'rss' in l.lower() or 'feed' in l.lower()]
                print(f'Found {len(rss_links)} potential RSS links:')
                for l in rss_links[:5]:
                    print(f'  {l}')
    except Exception as e:
        print(f'Error: {e}')
