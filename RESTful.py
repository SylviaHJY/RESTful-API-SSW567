#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   RESTful.py
@Time    :   2023/02/24 17:29:46
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   Interface with GitHub in order to extract and present useful information to your user. The function will communicate using the RESTful services APIs provided by GitHub.
'''

import requests     
import json

def getUserCommits(userID):
    # GitHub API URL for user repositories
    url = f'https://api.github.com/users/{userID}/repos'

    # Make a GET request to the API URL
    response = requests.get(url)  

    if response.status_code != 200:
        print("User Does not Exist");
    
   # Parse the JSON response
    repos = response.json()
    result = []
    
    # Loop through each repository and get the number of commits
    for repo in repos:
        repo_name = repo["name"]
        commit_url = repo["url"] + "/commits"
        commit_response = requests.get(commit_url)
        commit_data = json.loads(commit_response.content.decode('utf-8'))
        if len(commit_data) == 0:
            commit_count = 0
        else:
            commit_count = len(commit_data);
        result.append(f"Repo: {repo_name} Number of commits: {commit_count}\n");
        
    return result;
        

        
# print(getUserCommits("richkempinski"));
# print(getUserCommits("SylviaHJY"));

        
