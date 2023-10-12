import feedparser
import mysql.connector
from passwords import get_password


def get_news(rss):
    # Get the feed data
    feed = feedparser.parse(rss)

    # Extract the titles and links of the top 10 entries
    entries = feed['entries'][:5]
    titles = [entry['title'] for entry in entries]
    num = 1
    print()
    for title in titles:
        print(str(num) + ") "+title)
        num += 1
    print()


def sql_table():
    # CREATE DATABASE CSProject;
    # USE CSProject;
    # CREATE TABLE rssfeed(Category varchar(255) NOT NULL PRIMARY KEY, URL varchar(1000) NOT NULL);
    # INSERT INTO rssfeed(Category, URL) VALUES ("TopStories","https://timesofindia.indiatimes.com/rssfeedstopstories.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("RecentStories","https://timesofindia.indiatimes.com/rssfeedmostrecent.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("World","https://timesofindia.indiatimes.com/rssfeeds/296589292.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("NRI","https://timesofindia.indiatimes.com/rssfeeds/7098551.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("Business","https://timesofindia.indiatimes.com/rssfeeds/1898055.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("Cricket","https://timesofindia.indiatimes.com/rssfeeds/54829575.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("Sports","https://timesofindia.indiatimes.com/rssfeeds/4719148.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("Science","https://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("Environment","https://timesofindia.indiatimes.com/rssfeeds/2647163.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("Tech","https://timesofindia.indiatimes.com/rssfeeds/66949542.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("Education","https://timesofindia.indiatimes.com/rssfeeds/913168846.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("LifeStyle","https://timesofindia.indiatimes.com/rssfeeds/2886704.cms");
    # INSERT INTO rssfeed(Category, URL) VALUES ("Auto","https://timesofindia.indiatimes.com/rssfeeds/74317216.cms");
    pass


def get_rss(category):
    query = "SELECT URL FROM rssfeed WHERE Category = \"" + category+"\""
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    get_news(result)


def main():
    print("Which news would you like from the following categories: ")
    print("""
1. Top Stories 
2. Most Recent Stories
3. Auto
4. World
5. NRI
6. Business
7. Life & Style
8. Cricket	
9. Sports
10. Science
11. Environment
12. Tech
13. Education
14. Exit""")
    num = int(input())
    if num == 1:
        rss = 'TopStories'
    elif num == 2:
        rss = 'RecentStories'
    elif num == 3:
        rss = 'Auto'
    elif num == 4:
        rss = 'World'
    elif num == 5:
        rss = 'NRI'
    elif num == 6:
        rss = 'Business'
    elif num == 7:
        rss = 'LifeStyle'
    elif num == 8:
        rss = 'Cricket'
    elif num == 9:
        rss = 'Sports'
    elif num == 10:
        rss = 'Science'
    elif num == 11:
        rss = 'Environment'
    elif num == 12:
        rss = 'Tech'
    elif num == 13:
        rss = 'Education'
    elif num == 14:
        return True
    else:
        print("Wrong option entered")
        return True
    get_rss(rss)


if __name__ == "__main__":
    host, user, password = get_password()
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = conn.cursor()
    query = "USE CSProject;"
    cursor.execute(query)
    flag = False
    while flag != True:
        flag = main()

    conn.close()
