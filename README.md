- This project uses a python script and GitHub API to scrape users in Delhi with over 100 followers, fetching their profiles and repository information.
- Analyzing the data revealed that a surprising number of developers don't use wikis or project boards on their repositories.
- Developers should consider utilizing wikis and project boards more effectively to improve project collaboration and documentation.

### How the Data was Scraped
I used the GitHub API to query users in the city of Delhi who have more than 100 followers. After identifying these users, I retrieved their public repository information, focusing on up to 500 of their most recent repositories. The data was then exported to two CSV files: `users.csv` and `repositories.csv`.

### Most Interesting Fact
One interesting finding was that many repositories with high stars and followers lack a wiki or project management features, even though they could benefit from better documentation and task tracking.

### Recommendation for Developers
Based on the analysis, developers can enhance the quality of collaboration by enabling wikis and using project boards. These features help with knowledge sharing and structured development processes, especially for larger teams and open-source projects.

