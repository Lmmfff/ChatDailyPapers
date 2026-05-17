# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import requests
from config import USERNAME, TOKEN, REPO_OWNER, REPO_NAME

def make_github_issue(title, body=None, assignee=USERNAME, closed=False, labels=[]):
    # Create a regular issue on GitHub. The import API requires different
    # permissions and is not a good fit for this project.
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)

    # Headers
    headers = {
        "Authorization": "token %s" % TOKEN,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # Build a normal create-issue payload.
    data = {
        'title': title,
        'body': body or '',
    }
    if assignee:
        data['assignees'] = [assignee]
    if labels:
        data['labels'] = labels

    # Add the issue to our repository
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 201:
        print ('Successfully created Issue "%s"' % title)
    else:
        print ('Could not create Issue "%s"' % title)
        print ('Response:', response.content)

if __name__ == '__main__':
    title = 'Pretty title'
    body = 'Beautiful body'
    assignee = USERNAME
    closed = False
    labels = [
        "imagenet", "image retrieval"
    ]

    make_github_issue(title, body, assignee, closed, labels)
