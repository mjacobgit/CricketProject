import pandas as pd
import time
start=time.time()
# Function to pull the records from each scorecard
def records(name, url, home='Marymoor Park'):
    import pandas as pd
    import regex as re
    d = pd.read_html(url)  # Reading all the tables from the site. Will be read as panda DFs
    # Selecting the individula DFs of interest
    dnb1 = d[3].columns[0]
    dnb2 = d[6].columns[0]
    bat1 = d[2]
    bat2 = d[5]
    bowl1 = d[4]
    bowl2 = d[7]
    info = d[8]
    # Creating an empty DF to store all the records
    totrec = pd.DataFrame(columns=
                          ['Name', 'Runs Scored', 'Balls', 'Fours', 'Sixes', 'Strike Rate',
                           'Game', 'Ground', 'Innings', 'Batting Position', 'Result', 'Overs', 'Maiden',
                           'Runs Given', 'Wickets',
                           'Economy Rate'])
    # getting the ground
    info.index = info['Topic']  # storing first column in index
    test = info.drop(columns="Topic")  # dropping first column since we already have it as index
    v = str(test.loc['Location:'])  # Searchign the location row
    try:
        w = str(test.loc['Points Earned:'])
    except:
        w='empty'
    if re.search(home, v, re.IGNORECASE) != None:
        gr = 'home'
    else:
        gr = 'away'
    #  Checking if the player did not bat
    if re.search(name, dnb1, re.IGNORECASE) != None:
        barun = 'DNB'
        baball = 'DNB'
        bafour = 'DNB'
        basix = 'DNB'
        basr = 'DNB'
        batpos = 'DNB'
        fullname = name
        innings = 1
        # Checking if they bowled

        bo = bowl2[bowl2.columns[1]]
        for i in range(len(bo)):
            h = str(bo[i])
            if re.match(name, h, re.IGNORECASE) != None:
                borec = bowl2.loc[i]
                boover = borec[2]
                bomaid = borec[3]
                borun = borec[4]
                bowicket = borec[5]
                boeco = borec[6]
                break

            borec = 'DNB'
            boover = 'DNB'
            bomaid = 'DNB'
            borun = 'DNB'
            bowicket = 'DNB'
            boeco = 'DNB'
        x = str(bat1.columns[0])
        y = x.split()
        teamname = y[0] + " " + y[1]

        try:
            if re.search(teamname + ': 20', w) != None:
                result = 'win'
            else:
                result = 'loss'
        except:
            if re.search(teamname.split()[0] + ': 20', w) != None:
                result = 'win'
            else:
                result = 'loss'
    elif re.search(name, dnb2, re.IGNORECASE) != None:
        barun = 'DNB'
        baball = 'DNB'
        bafour = 'DNB'
        basix = 'DNB'
        basr = 'DNB'
        batpos = 'DNB'
        fullname = name
        innings = 2

        bo = bowl1[bowl1.columns[1]]
        for i in range(len(bo)):
            h = str(bo[i])
            if re.match(name, h, re.IGNORECASE) != None:
                borec = bowl1.loc[i]
                boover = borec[2]
                bomaid = borec[3]
                borun = borec[4]
                bowicket = borec[5]
                boeco = borec[6]
                break

            borec = 'DNB'
            boover = 'DNB'
            bomaid = 'DNB'
            borun = 'DNB'
            bowicket = 'DNB'
            boeco = 'DNB'

        x = str(bat2.columns[0])
        y = x.split()
        teamname = y[0] + " " + y[1]

        if re.search(teamname + ': 20', w) != None:
            result = 'win'
        else:
            result = 'loss'
    else:

        g = bat1[bat1.columns[0]]
        for i in range(len(g)):
            h = str(g[i])
            if re.match(name, h, re.IGNORECASE) != None:
                k = i
                break
            k = None
        if k != None:
            rec = bat1.loc[k]
            batpos = k + 1
            tem = re.split('\s|\*', rec[0])
            fullname = tem[0] + " " + tem[1]
            barun = rec[2]
            baball = rec[3]
            bafour = rec[4]
            basix = rec[5]
            basr = rec[6]
            innings = 1

            bo = bowl2[bowl2.columns[1]]
            for i in range(len(bo)):
                h = str(bo[i])
                if re.match(name, h, re.IGNORECASE) != None:
                    borec = bowl2.loc[i]
                    boover = borec[2]
                    bomaid = borec[3]
                    borun = borec[4]
                    bowicket = borec[5]
                    boeco = borec[6]
                    break

                borec = 'DNB'
                boover = 'DNB'
                bomaid = 'DNB'
                borun = 'DNB'
                bowicket = 'DNB'
                boeco = 'DNB'
            x = str(bat1.columns[0])
            y = x.split()
            teamname = y[0] + " " + y[1]

            try:
                if re.search(teamname + ': 20', w) != None:
                    result = 'win'
                else:
                    result = 'loss'
            except:
                if re.search(teamname.split()[0] + ': 20', w) != None:
                    result = 'win'
                else:
                    result = 'loss'

        else:

            g = bat2[bat2.columns[0]]
            for i in range(len(g)):
                h = str(g[i])
                if re.match(name, h, re.IGNORECASE) != None:
                    k = i
                    break
            rec = bat2.loc[k]
            batpos = k + 1
            tem = re.split('\s|\*', rec[0])
            fullname = tem[0] + " " + tem[1]
            barun = rec[2]
            baball = rec[3]
            bafour = rec[4]
            basix = rec[5]
            basr = rec[6]

            bo = bowl1[bowl1.columns[1]]
            for i in range(len(bo)):
                h = str(bo[i])
                if re.match(name, h, re.IGNORECASE) != None:
                    borec = bowl1.loc[i]
                    boover = borec[2]
                    bomaid = borec[3]
                    borun = borec[4]
                    bowicket = borec[5]
                    boeco = borec[6]
                    break

                boover = 'DNB'
                bomaid = 'DNB'
                borun = 'DNB'
                bowicket = 'DNB'
                boeco = 'DNB'

            innings = 2
            x = str(bat2.columns[0])
            y = x.split()
            teamname = y[0] + " " + y[1]
            try:
                if re.search(teamname + ': 20', w) != None:
                    result = 'win'
                else:
                    result = 'loss'
            except:
                if re.search(teamname.split()[0] + ': 20', w) != None:
                    result = 'win'
                else:
                    result = 'loss'
    try:
        totrec = totrec.append({'Name': fullname, 'Runs Scored': barun,
                                'Balls': baball, 'Fours': bafour,
                                'Sixes': basix, 'Strike Rate': basr
                                   , 'Game': gr, 'Ground': home, 'Innings': innings, 'Batting Position': batpos
                                   , 'Result': result, 'Overs': boover, 'Maiden': bomaid,
                                'Runs Given': borun, 'Wickets': bowicket,
                                'Economy Rate': boeco}, ignore_index=True)
    except:
        totrec = totrec.append({'Name': fullname, 'Runs Scored': barun,
                                'Balls': baball, 'Fours': bafour,
                                'Sixes': basix, 'Strike Rate': basr
                                   , 'Game': gr, 'Ground': home, 'Innings': innings, 'Batting Position': batpos
                                   , 'Result': result, 'Overs': 'DNB', 'Maiden': 'DNB',
                                'Runs Given': 'DNB', 'Wickets': 'DNB',
                                'Economy Rate': 'DNB'}, ignore_index=True)

    return (totrec)

# Function to find the scorecard URLs
def urlfinder(url):
    import requests
    from bs4 import BeautifulSoup

    urls = []
    # Putting in the GET request
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser') # Using beautiful soup to get the html text file

    temp = soup.find_all('a', text='Scorecard') # Searching for Scorecard URLs
    for i in temp:
        t = 'https://cricclubs.com' + i.get('href') # appending haeder to each url to get complete url
        urls.append(t)
    return (urls)

#Providing team
team={'Aseem Datar':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=277029&clubId=232',
      'Azeem Khan':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=277066&clubId=232',
      'Bhargava Vadapalli':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=461807&clubId=232',
      'Brijesh Singh':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=849520&clubId=232',
        'Damodhar Bhat':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=194337&clubId=232',
        'Karan Rao':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=1211870&clubId=232',
        'Krishna Kannan':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=347873&clubId=232',
        'Manan Ahuja':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=765415&clubId=232',
        'Manoj Panwar':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=1093300&clubId=232',
        'Manu Jacob':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=277610&clubId=232',
        'Naiteek Sangani':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=43336&clubId=232',
        'Naveen Kumar':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=277717&clubId=232',
        'Pradeep Pagadala':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=277818&clubId=232',
        'Raj Subramaniam':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=289310&clubId=232',
        'Rajesh Munshi':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=277919&clubId=232',
        'Sai Prashanth Muttavarapu':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=278050&clubId=232',
        'Samarth Shah':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=278074&clubId=232',
        'Srini Santhanam':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=278257&clubId=232',
        'Ujjawal Patel':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=278372&clubId=232',
        'Vijay Beniwal':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=278428&clubId=232',
        'Vikrant Minhas':'https://cricclubs.com/NWCL/playerAllBattingRecords.do?playerId=278446&clubId=232'
            }
# Getting the names of players
team_names=list(team.keys())
# print(team_names[0])
# Getting all scorecard urls for each player
all=[]
for url in team.values():
    all.append(urlfinder(url))
# print(all[0])
allrec=pd.DataFrame(columns=
                          ['Name', 'Runs Scored', 'Balls', 'Fours', 'Sixes', 'Strike Rate',
                           'Game', 'Ground', 'Innings', 'Batting Position', 'Overs', 'Maiden',
                           'Runs Given', 'Wickets',
                           'Economy Rate'])
# print(allrec)
for i in range(len(all)):
    # allrec = pd.DataFrame(columns=
    #                       ['Name', 'Runs Scored', 'Balls', 'Fours', 'Sixes', 'Strike Rate',
    #                        'Game', 'Ground', 'Innings', 'Batting Position', 'Overs', 'Maiden',
    #                        'Runs Given', 'Wickets',
    #                        'Economy Rate'])
    # name = team_names[i]
    matches=0
    for x in all[i]:
        matches+=1
        # print(records(name=team_names[i],url=x))
        allrec=allrec.append(records(name=team_names[i], url=x), ignore_index=True)

allrec.to_csv('C:\\Users\\mj934a\\Desktop\\Allrecords.csv')
print("Time taken=",time.time()-start)
