import csv

shortcodes = []
intcodes = []
natdestcodes = []

def updateLists():
    global shortcodes
    global intcodes
    global natdestcodes
    with open('data/short-codes.csv', mode = 'r', encoding='utf-8-sig') as shortCode:
        reader = csv.DictReader(shortCode)
        i=0
        for row in reader:
            shortcodes.append(row['shortcode'])
            i = i+1
            
    with open('data/intnl_codes.csv', mode = 'r', encoding='utf-8-sig') as intCode:
        reader = csv.DictReader(intCode)
        i=0
        for row in reader:
            intcodes.append([row['code'],row['country']])
            i = i+1
    with open('data/national_destination.csv', mode = 'r', encoding='utf-8-sig') as NDC:
        reader = csv.DictReader(NDC)
        i=0
        for row in reader:
            natdestcodes.append(row['NDC'])
            i = i+1
            
if __name__ == "__main__":
    updateLists()
