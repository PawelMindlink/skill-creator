
import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path

CLIENT_DIR = Path(r"c:\Users\Paweł\Documents\GitHub\ICP Research\Clients\iiyama")
GA4_FILE = CLIENT_DIR / "GA4_Landing_Pages_Segments.csv"
FEED_FILE = CLIENT_DIR / "feed.xml"

print("--- FEED URLS ---")
tree = ET.parse(FEED_FILE)
root = tree.getroot()
count = 0
for item in root.findall('.//item'):
    link = item.find('link').text
    norm = link.replace('https://iiyama-sklep.pl', '').strip('/')
    print(f"Original: {link}")
    print(f"Normalized: {norm}")
    count += 1
    if count >= 5: break

print("\n--- GA4 URLS ---")
# Skip existing headers logic from main script
col_names = [
    'landing_page', 
    'home_sessions', 'home_arpu', 'home_revenue', 'home_transactions', 'home_first_purchasers', 'home_avg_purchase_revenue',
    'pro_sessions', 'pro_arpu', 'pro_revenue', 'pro_transactions', 'pro_first_purchasers', 'pro_avg_purchase_revenue'
]
df = pd.read_csv(GA4_FILE, skiprows=9, header=None, names=col_names, on_bad_lines='skip')
df = df[df['landing_page'].str.startswith('/', na=False)]

for url in df['landing_page'].head(5):
    norm = url.strip('/').split('?')[0]
    print(f"Original: {url}")
    print(f"Normalized: {norm}")
