import feedparser

feeds = {
    'Standard Headlines': 'https://www.standardmedia.co.ke/rss/headlines.php',
    'Standard Kenya': 'https://www.standardmedia.co.ke/rss/kenya.php',
    'Standard World': 'https://www.standardmedia.co.ke/rss/world.php',
    'Standard Politics': 'https://www.standardmedia.co.ke/rss/politics.php',
}

for name, url in feeds.items():
    try:
        d = feedparser.parse(url)
        print(f'\n{name}: {len(d.entries)} entries')
        if d.entries:
            for i, e in enumerate(d.entries[:3]):
                title = e.get('title', 'No title')
                link = e.get('link', 'No link')
                pub = e.get('published', 'No date')
                print(f'  {i+1}. {title[:70]}')
                print(f'     Link: {link}')
                print(f'     Published: {pub}')
    except Exception as e:
        print(f'{name}: Error - {e}')
