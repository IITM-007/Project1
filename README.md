# GitHub Developer Analysis - Delhi 100

## Project Overview
- This project uses the GitHub API to scrape users in Delhi with over 100 followers, fetching their profiles and repository information.
- Analyzing the data revealed that a surprising number of developers don't use wikis or project boards on their repositories.
- Developers should consider utilizing wikis and project boards more effectively to improve project collaboration and documentation.

## A Detailed View

### How the Data was Scraped
I used the GitHub API to query users in the city of Delhi who have more than 100 followers. After identifying these users, I retrieved their public repository information, focusing on up to 500 of their most recent repositories. The data was then exported to two CSV files: `users.csv` and `repositories.csv`.

### Data Collection Process

![alt text](https://github.com/IITM-007/Project1/blob/main/img.png)

1. Start → GitHub API Request: The process starts with a request to the GitHub API.
2. GitHub API Request → Query Users in Delhi with >100 Followers: It queries users based on city and follower count.
3. Query Users → Retrieve Public Repos for Each User: Public repositories are retrieved for each identified user.
4. Retrieve Public Repos → Up to 500 Most Recent Repos per User: Limits to 500 recent repositories per user.
5. Up to 500 Most Recent Repos → Export Data: Data is exported to CSV.
6. Export Data splits into users.csv and repositories.csv as final outputs.


## Most Interesting Findings

#### Wiki Usage Analysis
- Only 23% of repositories have active wikis
- High-star repositories (1000+ stars) show similar low adoption rates
- Documentation quality varies significantly across projects

#### Project Board Statistics
- 27% of repositories utilize project boards
- Larger teams (5+ contributors) show higher board usage (42%)
- Sprint planning tools are underutilized (18% adoption)

## Recommendations for Developers

#### 1. Documentation Enhancement
- Enable wiki features for comprehensive documentation
- Maintain up-to-date API documentation
- Create detailed setup guides
- Document architectural decisions

#### 2. Project Management
- Implement structured project boards
- Use milestone tracking effectively
- Enable automated task assignments
- Regular sprint planning and reviews

#### 3. Collaboration Tools
- Utilize GitHub Discussions for community engagement
- Enable issue templates
- Implement pull request templates
- Set up automated workflow tools

### Project Structure
```
project/
├── gitscrap.py                # Main scraping script
│── [1-16].py                  # Solving answers
└── data/
    ├── users.csv              # User profile data
    └── repositories.csv       # Repository information
```
