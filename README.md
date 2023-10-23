# Dota2Counters
A simple Python webscrapper to gather information of heroes' counters and items from Dotabuff.

## Instalation
You'll need some dependencies for it to work.
```bash 
pip install -r requirements.txt
```

If you want to use SOCKS proxy (for some network reasons), you'll need to install additional dependency.
```bash 
pip install requests[socks]
```

## How to use
1.After releasing new heroes, needs to update the hero list to ensure that all heroes' data can be obtained. This step will lead to hero_list.txt used for assembling url.
```bash
python dotabuff_hero_scrapper
```

2.Tune parameters in config.py, like request header and sleep_time, to avoid be banned. Then run scrappers. This step will lead to .pkl files which contain all data needed and is easy for debugging.
```bash
python3 dotabuff_counter_scrapper
python3 dotabuff_item_scrapper
```

3.Extract heroes and items set from .pkl file. This will lead to set.txt, which is the template for translation. Manually fill in all translation, then copy and rename it to the specifical directory accoding to config file. If you don't want translation, you can skip this step.
```bash
python3 get_hero_set
python3 get_item_set
```

4.Tune the translation switch. Export data to excel for good searching and reading.
```bash
python3 export_counter_to_excel
python3 export_item_to_excel
```
